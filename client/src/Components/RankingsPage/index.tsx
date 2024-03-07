import React, { useEffect, useState } from "react";
import { Container, Paper, Typography, Box, Stack } from "@mui/material";
import { Bar } from "react-chartjs-2";

function RankingsPage() {
  interface GenreData {
    genre: string;
    statistic: number;
  }

  const [popularGenres, setPopularGenres] = useState([] as GenreData[]);
  const [controversialGenres, setControversialGenres] = useState(
    [] as GenreData[]
  );

  useEffect(() => {
    fetch(`http://localhost:5555/genres/popular`, { mode: "cors" })
      .then((response) => response.json())
      .then((data) => setPopularGenres(data));
  }, []);

  useEffect(() => {
    fetch(`http://localhost:5555/genres/controversial`, { mode: "cors" })
      .then((response) => response.json())
      .then((data) => setControversialGenres(data));
  }, []);

  // Prepare chart data
  const popularChartData = {
    labels: popularGenres.map((g) => g.genre),
    datasets: [
      {
        label: "Average Rating",
        data: popularGenres.map((g) => g.statistic),
        backgroundColor: "rgba(54, 162, 235, 0.5)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
    ],
  };

  const controversialChartData = {
    labels: controversialGenres.map((g) => g.genre),
    datasets: [
      {
        label: "Standard Deviation",
        data: controversialGenres.map((g) => g.statistic),
        backgroundColor: "rgba(255, 99, 132, 0.5)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function (value: any, index: any, values: any) {
            return value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
          }
        }
      }
    }
  };

  return (
    <Container maxWidth="md">
      <Stack spacing={3} alignItems="center" margin={5}>
        <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
          <Typography variant="h4" gutterBottom>
            Most Popular Genres - Average Rating
          </Typography>
          <Box sx={{ minHeight: "350px", overflow: "auto" }}>
            <Bar
              data={popularChartData}
              options={chartOptions}
            />
          </Box>
        </Paper>
        <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
          <Typography variant="h4" gutterBottom>
            Most Controversial Genres - Standard Deviation
          </Typography>
          <Box sx={{ minHeight: "350px", overflow: "auto" }}>
            <Bar
              data={controversialChartData}
              options={chartOptions}
            />
          </Box>
        </Paper>
      </Stack>
    </Container>
  );
}

export default RankingsPage;
