import React, { useEffect, useState } from 'react';
import { Button, IconButton, Paper, Slider, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';
import CloseIcon from '@mui/icons-material/Close';

type RatingInputProps = {
  users: string[];
  ratings: number[];
  setUsers: any;
  setRatings: any;
};

const RatingInput = ({ users, ratings, setUsers, setRatings }: RatingInputProps) => {
  const addUserRating = () => {
    setUsers([...users, '']); // Add a new user
    setRatings([...ratings, 0]); // Add a new rating
  };

  const removeUserRating = (index: number) => {
    const updatedUsers = [...users];
    const updatedRatings = [...ratings];
    updatedUsers.splice(index, 1);
    updatedRatings.splice(index, 1);
    setUsers(updatedUsers);
    setRatings(updatedRatings);
  };

  const handleUserChange = (index: number, newValue: string) => {
    const updatedUsers = [...users];
    updatedUsers[index] = newValue;
    setUsers(updatedUsers);
  };

  const handleRatingChange = (index: number, newValue: number) => {
    const updatedRatings = [...ratings];
    updatedRatings[index] = newValue;
    setRatings(updatedRatings);
  };

  return (
    <Paper sx={{ padding: 2, marginBottom: 2, width: '100%' }}>
      <Typography variant="h6">User Ratings</Typography>
      <Stack spacing={3}>
        {users.map((user, index) => (
          <Stack direction="row" alignItems="center" spacing={2} key={index} sx={{ width: '100%' }}>
            <AutocompleteWithFetch
              value={user}
              label="User"
              apiUrl="http://localhost:5555/autocomplete/user"
              onChange={(_: any, newValue: any) => handleUserChange(index, newValue)}
            />
            <Slider
              value={ratings[index]}
              step={0.5}
              marks
              min={0}
              max={5}
              valueLabelDisplay="auto"
              onChange={(_, newValue: any) => handleRatingChange(index, newValue)}
            />
            <Stack direction="row" alignItems="center" spacing={1}>
              <IconButton onClick={() => removeUserRating(index)}>
                <CloseIcon />
              </IconButton>
              <Stack sx={{ width: '80px' }}>
                <Typography variant="caption">Rating</Typography>
                <Typography>{ratings[index]}</Typography>
              </Stack>
            </Stack>
          </Stack>
        ))}
      </Stack>
      <Button variant="outlined" onClick={addUserRating} fullWidth>
        Add User Rating
      </Button>
    </Paper>
  );
};

function NewFilmPage() {
  const [tags, setTags] = useState([] as string[]);
  const [ratings, setRatings] = useState([] as number[]);
  const [users, setUsers] = useState([] as string[]);
  const [rating, setRating] = useState<String | null>(null);

  useEffect(() => {
    const calculateRating = async () => {
      try {
        const response = await fetch('http://localhost:5555/movie-pred', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ tags: tags, ratings: ratings, users: users }),
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const skewData = await response.json();
        setRating(skewData);
      } catch (error: any) {
        console.error('Error calculating skew:', error.message);
      }
    };

    if (tags && users && ratings && (tags.length != 0 || users.length != 0 || ratings.length != 0)) {
      calculateRating();
    } else {
      setRating(null);
    }
  }, [users, tags, ratings]);

  return (
    <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
      <RatingInput
        users={users}
        ratings={ratings}
        setUsers={setUsers}
        setRatings={setRatings}
      />

      <AutocompleteWithFetch
        value={tags}
        multiple
        label="Tags"
        apiUrl="http://localhost:5555/autocomplete/tag"
        onChange={(_: any, newValue: any) => setTags(newValue)}
      />

      <Typography>
        {rating ? (
          <>The estimated rating is {rating}</>
        ) : (
          <>Please select some ratings or tags</>
        )}
      </Typography>
    </Stack>
  );
}

export default NewFilmPage;
