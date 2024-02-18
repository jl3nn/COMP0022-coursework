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

function UserReportPage() {
  const [genre, setGenres] = useState(null as string | null);
  const [film, setFilms] = useState(null as string | null);
  const [opinion, setOpinion] = useState(null as number | null);
  const [better, setBetter] = useState([] as string[]);
  const [worse, setWorse] = useState([] as string[]);

  useEffect(() => {
    const calculateSkew = async () => {
      try {
        const response = await fetch(
          "http://localhost:5555/genres/user-preferences",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              genre,
              film,
              opinion,
            }),
          }
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const skewData = (await response.json()).map(
          (d: { genre: string; avg_rating: number }) => d.genre
        );

        setBetter(skewData.slice(0, Math.ceil(skewData.length / 2)));
        setWorse(skewData.slice(Math.ceil(skewData.length / 2)).reverse());
      } catch (error: any) {
        console.error("Error calculating skew:", error.message);
      }
    };

    if (opinion && (genre || film)) {
      calculateSkew();
    } else {
      setBetter([]);
      setWorse([]);
    }
  }, [opinion, genre, film]);

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
            disabled={film != null}
            label="Genres"
            apiUrl="http://localhost:5555/autocomplete/genre"
            onChange={(_: any, newValue: any) => setGenres(newValue)}
          />
          <AutocompleteWithFetch
            value={film}
            disabled={genre != null}
            label="Films"
            apiUrl="http://localhost:5555/autocomplete/movie"
            onChange={(_: any, newValue: any) => setFilms(newValue)}
          />

          <Box width="100%">
            <Typography variant="h6" gutterBottom>
              Preferences Analysis
            </Typography>
            <List>
              <Typography variant="subtitle1">Those users like:</Typography>
              {better.map((b, index) => (
                <ListItem key={index}>
                  <ListItemText primary={b} />
                </ListItem>
              ))}
              <Divider variant="middle" />
              <Typography variant="subtitle1">Those users dislike:</Typography>
              {worse.map((w, index) => (
                <ListItem key={index}>
                  <ListItemText primary={w} />
                </ListItem>
              ))}
            </List>
          </Box>
        </Stack>
      </Paper>
    </Container>
  );
}

export default UserReportPage;
