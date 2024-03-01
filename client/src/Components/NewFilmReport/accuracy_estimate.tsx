import React, { useState } from "react";
import { Box, Button, Paper, Typography } from "@mui/material";
import { getAllJSDocTagsOfKind } from "typescript";

interface EstimatedAccuracyType {
  name: string;
  rating: number;
  estimated_rating: number;
}

const AccuracyEstimate = () => {
  const [estimated_accuracy, setEstimatedAccuracy] = useState<
    EstimatedAccuracyType[] | null
  >(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [average_difference, setAverageDifference] = useState<number>(0);

  async function getMoviePrediction(name: string) {
    const users_response = await fetch(
      "http://localhost:5555/users/for-prediction",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ movie: name }),
      }
    );

    const users = await users_response.json();

    const response = await fetch("http://localhost:5555/ratings/prediction", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ users: users, movie: name }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    return await response.json();
  }

  async function handleSubmit() {
    setLoading(true);
    const response = await fetch(
      "http://localhost:5555/movies/get-search-results",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          searchText: "",
          ratings: [0, 10],
          tags: [],
          genres: [],
          date: [1902, 2018],
          numLoaded: 0,
        }),
        mode: "cors",
      }
    );
    const bestMovies = (await response.json()).results;
    const movie_names = bestMovies.map((movie: any) => movie.title);
    const movie_ratings = bestMovies.map((movie: any) => movie.rating);

    const estimated_ratings_promises = movie_names.map((name: string) =>
      getMoviePrediction(name)
    );
    const estimated_ratings = await Promise.all(estimated_ratings_promises);

    const estimated_accuracy = movie_names.map(
      (name: string, index: number) => ({
        name: name,
        rating: movie_ratings[index],
        estimated_rating: estimated_ratings[index].predictedRating,
      })
    );

    const total_difference = estimated_accuracy.reduce(
      (acc: any, movie: any) =>
        acc + Math.abs(movie.rating - movie.estimated_rating),
      0
    );
    const average_difference = total_difference / estimated_accuracy.length;

    setAverageDifference(average_difference);
    setEstimatedAccuracy(estimated_accuracy);
    setLoading(false);
  }

  return (
    <Box>
      <Button
        type="submit"
        variant="contained"
        color="primary"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Estimating..." : "Estimate Accuracy"}
      </Button>
      {estimated_accuracy && (
        <Box>
          <Typography variant="h4">
            <strong>Estimated Accuracy</strong>
            <br />
            Average Difference: {average_difference}
          </Typography>
          <p></p>
          <Box>
            {estimated_accuracy.map((movie: EstimatedAccuracyType) => (
              <Paper elevation={3} sx={{ padding: 2 }}>
                <Typography variant="h6" component="p" gutterBottom>
                  {movie.name}
                </Typography>
                <Typography variant="body1" component="p">
                  Actual Rating: {movie.rating}
                </Typography>
                <Typography variant="body1" component="p">
                  Estimated Rating: {movie.estimated_rating}
                </Typography>
              </Paper>
            ))}
          </Box>
        </Box>
      )}
    </Box>
  );
};

export default AccuracyEstimate;
