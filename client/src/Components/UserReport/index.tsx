import React, { useEffect, useState } from "react";
import {
  Paper,
  Radio,
  Stack,
  Typography,
  RadioGroup,
  FormControlLabel,
  Box,
  Container,
  List,
  ListItem,
  ListItemText,
  Divider,
} from "@mui/material";
import AutocompleteWithFetch from "../common/AutocompleteSelector";
import { Bar } from "react-chartjs-2";
// import "chart.js/auto";

interface SkewData {
  id: string;
  avg_rating: number;
}

function UserReportPage() {
  const [genre, setGenres] = useState(null as string | null);
  const [movie, setMovies] = useState(null as string | null);
  const [opinion, setOpinion] = useState(null as number | null);
  const [better, setBetter] = useState([] as SkewData[]);
  const [worse, setWorse] = useState([] as SkewData[]);

  useEffect(() => {
    const calculateSkew = async () => {
      try {
        const apiUrl = `http://localhost:5555/${
          genre ? "genres" : "movies"
        }/user-preferences`;

        const response = await fetch(apiUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            genre,
            movie,
            opinion,
          }),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const skewData = (await response.json()) as SkewData[];
        const skewDataLimit = Math.min(skewData.length, 5);
        setBetter(skewData.slice(0, skewDataLimit));
        setWorse(skewData.slice(-skewDataLimit).reverse());
      } catch (error: any) {
        console.error("Error calculating skew:", error.message);
      }
    };
    if (opinion && (genre || movie)) {
      calculateSkew();
    } else {
      setBetter([]);
      setWorse([]);
    }
  }, [opinion, genre, movie]);

  // Prepare data for the graph
  const chartData = {
    labels: better.map((b) => b.id).concat(worse.map((w) => w.id)),
    datasets: [
      {
        label: "Average Rating",
        data: better
          .map((b) => b.avg_rating)
          .concat(worse.map((w) => w.avg_rating)),
        backgroundColor: [
          ...better.map(() => "rgba(54, 162, 235, 0.5)"),
          ...worse.map(() => "rgba(255, 99, 132, 0.5)"),
        ],
        borderColor: [
          ...better.map(() => "rgba(54, 162, 235, 1)"),
          ...worse.map(() => "rgba(255, 99, 132, 1)"),
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <Container maxWidth="md">
      <Paper elevation={3} sx={{ p: 4, mt: 4, mb: 4 }}>
        <Stack spacing={3} alignItems="center">
          <Typography variant="h4" gutterBottom>
            User Preferences Report
          </Typography>
          <Typography variant="h6">For users that typically</Typography>
          
            <RadioGroup
              row
              aria-labelledby="demo-radio-buttons-group-label"
              name="radio-buttons-group"
              value={opinion}
              onChange={(event) => setOpinion(parseInt(event.target.value))}
            >
              <FormControlLabel value="1" control={<Radio />} label="Like" />
              <FormControlLabel value="2" control={<Radio />} label="Dislike" />
              <FormControlLabel
                value="3"
                control={<Radio />}
                label="Are Neutral On"
              />
            </RadioGroup>
          <Typography variant="h6">the following</Typography>
          <AutocompleteWithFetch
            value={genre}
            disabled={movie != null}
            label="Genres"
            apiUrl="http://localhost:5555/autocomplete/genre"
            onChange={(_: any, newValue: any) => setGenres(newValue)}
          />
          <AutocompleteWithFetch
            value={movie}
            disabled={genre != null}
            label="Movies"
            apiUrl="http://localhost:5555/autocomplete/movie"
            onChange={(_: any, newValue: any) => setMovies(newValue)}
          />

          <Box width="100%">
            <Typography variant="h6" gutterBottom>
              Preferences Analysis
            </Typography>
            <List>
              <Typography variant="subtitle1">Those users like:</Typography>
              {better.length > 0 ? (
                better.map((b, index) => (
                  <ListItem key={index}>
                    <ListItemText
                      primary={b.id}
                      secondary={`Rating: ${b.avg_rating}`}
                    />
                  </ListItem>
                ))
              ) : (
                <ListItem>
                  <ListItemText primary="No data available" />
                </ListItem>
              )}
              <Divider variant="middle" />
              <Typography variant="subtitle1">Those users dislike:</Typography>
              {worse.length > 0 ? (
                worse.map((w, index) => (
                  <ListItem key={index}>
                    <ListItemText
                      primary={w.id}
                      secondary={`Rating: ${w.avg_rating}`}
                    />
                  </ListItem>
                ))
              ) : (
                <ListItem>
                  <ListItemText primary="No data available" />
                </ListItem>
              )}
            </List>
          </Box>
        </Stack>
        <Box width="100%" sx={{ mt: 4 }}>
          <Typography variant="h6" gutterBottom>
            Rating Distribution
          </Typography>
          <Bar
            data={chartData}
            options={{ scales: { y: { beginAtZero: true } } }}
          />
        </Box>
      </Paper>
    </Container>
  );
}

export default UserReportPage;
