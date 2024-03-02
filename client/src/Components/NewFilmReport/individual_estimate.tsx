import React, { useEffect, useState } from "react";
import {
  Button,
  Card,
  CardContent,
  CardActions,
  Collapse,
  List,
  ListItem,
  ListItemText,
  Typography,
  Stack,
} from "@mui/material";
import AutocompleteWithFetch from "../common/AutocompleteSelector";

interface Rating {
  averageRating: number;
  subsetRating: number;
  userBias: number;
  genreBias: number;
  tagBias: number;
  averageBias: number;
  predictedRating: number;
}

function IndividualEstimate() {
  const [rating, setRating] = useState<Rating | null>(null);
  const [movie, setMovie] = useState<String | null>(null);
  const [user, setUser] = useState<String[]>([]);
  const [expanded, setExpanded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  useEffect(() => {
    const calculateRating = async () => {
      setLoading(true);
      try {
        const users_response = await fetch(
          "http://localhost:5555/users/for-prediction",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ movie: movie }),
          }
        );

        const users = await users_response.json();
        setUser(users);

        const response = await fetch(
          "http://localhost:5555/ratings/prediction",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ users: users, movie: movie }),
          }
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const rating = await response.json();
        setRating(rating);
      } catch (error: any) {
        console.error("Error calculating skew:", error.message);
      }
      setLoading(false);
    };

    if (movie) {
      calculateRating();
    } else {
      setRating(null);
    }
  }, [movie]);

  const errorCalculation = rating
    ? Math.abs(rating.averageRating - rating.predictedRating).toFixed(3)
    : 0;

  return (
    <Stack spacing={2} alignItems="center" maxWidth={800} margin="auto">
      <AutocompleteWithFetch
        value={movie}
        label="Movie"
        apiUrl="http://localhost:5555/autocomplete/movie"
        onChange={(_: any, newValue: any) => setMovie(newValue)}
      />
      {rating && !loading && (
        <Card sx={{ width: "100%", bgcolor: "background.paper" }}>
          <CardContent>
            <Typography
              variant="h5"
              component="div"
              sx={{ fontSize: "1.5rem" }}
            >
              {movie}
            </Typography>
            <Typography
              sx={{ mb: 1.5, fontSize: "1.25rem" }}
              color="text.secondary"
            >
              Rating Summary
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
              Analyzed for users: <strong>{user.join(", ")}</strong>
            </Typography>
            <Typography variant="body2" sx={{ fontSize: "1rem" }}>
              Simple Prediction: {rating.subsetRating.toFixed(3)}
              <br />
              Bias-Adjusted Prediction: {rating.predictedRating.toFixed(3)}
              <br />
              <strong>Actual Rating: {rating.averageRating.toFixed(3)}</strong>
              <br />
              </Typography>
              <Typography sx={{ mt: 2, fontSize: "1rem", color: "error.main" }}>
                Prediction Error: {errorCalculation}
              </Typography>
          </CardContent>
          <CardActions disableSpacing>
            <Button
              onClick={handleExpandClick}
              aria-expanded={expanded}
              aria-label="show more"
            >
              Bias Analysis
            </Button>
          </CardActions>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph sx={{ fontSize: "1.25rem" }}>
                Bias Analysis:
              </Typography>
              <List dense>
                <ListItem>
                  <ListItemText
                    primary={`Average Bias: ${rating.averageBias.toFixed(3)}`}
                  />
                </ListItem>
                <ListItem>
                  <ListItemText
                    primary={`User Bias: ${rating.userBias.toFixed(3)}`}
                    sx={{ fontSize: "1.25rem" }}
                  />
                </ListItem>
                <ListItem>
                  <ListItemText
                    primary={`Genre Bias: ${rating.genreBias.toFixed(3)}`}
                    sx={{ fontSize: "1.25rem" }}
                  />
                </ListItem>
                <ListItem>
                  <ListItemText
                    primary={`Tag Bias: ${rating.tagBias.toFixed(3)}`}
                    sx={{ fontSize: "1.25rem" }}
                  />
                </ListItem>
              </List>
              {/* Visualization Component here if applicable */}
            </CardContent>
          </Collapse>
        </Card>
      )}
      {!rating && !loading && (
        <Typography>Please select a movie to see predictions.</Typography>
      )}
      {loading && <Typography>Loading...</Typography>}
    </Stack>
  );
}

export default IndividualEstimate;
