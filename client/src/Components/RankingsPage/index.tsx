import React, { useEffect, useState } from "react";
import {
  Container,
  Paper,
  Typography,
  Box,
  Stack,
  List,
  ListItem,
  ListItemText,
} from "@mui/material";

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

  return (
    <Container maxWidth="md">
      <Stack spacing={3} alignItems="center" margin={5}>
        <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
          <Typography variant="h4" gutterBottom>
            Most Popular Genres
          </Typography>
          <Box sx={{ maxHeight: "calc(50vh - 150px)", overflow: "auto" }}>
            <List>
              {popularGenres.map((popGen, index) => (
                <ListItem key={index}>
                  <ListItemText
                    primary={popGen.genre}
                    secondary={`Average: ${popGen.statistic}`}
                  />
                </ListItem>
              ))}
            </List>
          </Box>
        </Paper>
        <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
          <Typography variant="h4" gutterBottom>
            Most Controversial Genres
          </Typography>
          <Box sx={{ maxHeight: "calc(50vh - 150px)", overflow: "auto" }}>
            <List>
              {controversialGenres.map((conGen, index) => (
                <ListItem key={index}>
                  <ListItemText
                    primary={conGen.genre}
                    secondary={`Standard Deviation: ${conGen.statistic}`}
                  />
                </ListItem>
              ))}
            </List>
          </Box>
        </Paper>
      </Stack>
    </Container>
  );
}

export default RankingsPage;
