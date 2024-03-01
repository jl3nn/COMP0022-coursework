import React, { useEffect, useState } from 'react';
import { Box, List, ListItem, ListItemText, Paper, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

interface Rating {
  averageBias: number;
  averageRating: number;
  genreBias: number;
  predictedRating: number;
  subsetRating: number;
  tagBias: number;
  userBias: number;
}

function IndividualEstimate() {
  const [rating, setRating] = useState<Rating | null>(null);
  const [movie, setMovie] = useState<String | null>(null);
  const [user, setUser] = useState<String[]>([]);

  useEffect(() => {
    const calculateRating = async () => {
      try {
        const users_response = await fetch('http://localhost:5555/users/for-prediction', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ movie: movie }),
        });

        const users = await users_response.json();
        setUser(users);

        const response = await fetch('http://localhost:5555/ratings/prediction', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ users: users, movie: movie }),
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const rating = await response.json();
        setRating(rating);
      } catch (error: any) {
        console.error('Error calculating skew:', error.message);
      }
    };

    if (movie) {
      console.log(":)")
      calculateRating();
    } else {
      console.log(":(")
      setRating(null);
    }
  }, [movie]);

  return (
    <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
      <AutocompleteWithFetch
        value={movie}
        label="Movie"
        apiUrl="http://localhost:5555/autocomplete/movie"
        onChange={(_: any, newValue: any) => setMovie(newValue)}
      />

      <Typography>
        {rating ? (
          <Box sx={{ p: 2, bgcolor: 'background.default', borderRadius: 2 }}>
            <Typography variant="h6" component="h2" gutterBottom>
              Movie Analysis
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
              For the movie: <strong>{movie}</strong>
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
              Analyzed for users: <strong>{user.join(', ')}</strong>
            </Typography>
            <Paper elevation={3} sx={{ mt: 2, mb: 2, p: 2 }}>
              <Typography variant="body1" component="div">
                The following estimates have been produced:
              </Typography>
              <List dense>
                <ListItem>
                  <ListItemText primary={`Average Bias: ${rating.averageBias}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`Average Rating: ${rating.averageRating}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`Genre Bias: ${rating.genreBias}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`Predicted Rating: ${rating.predictedRating}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`Subset Rating: ${rating.subsetRating}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`Tag Bias: ${rating.tagBias}`} />
                </ListItem>
                <ListItem>
                  <ListItemText primary={`User Bias: ${rating.userBias}`} />
                </ListItem>
              </List>
            </Paper>
            <Typography variant="body2" color="textSecondary" align="right">
              Data provided is based on current analysis metrics.
            </Typography>
          </Box>          
        ) : (
          <Typography>Please select some ratings or tags</Typography>
        )}
      </Typography>
    </Stack>
  );
}

export default IndividualEstimate;
