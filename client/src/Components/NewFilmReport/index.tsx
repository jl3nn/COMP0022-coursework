import React, { useEffect, useState } from 'react';
import { Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

function NewFilmPage() {
  const [users, setUsers] = useState([] as string[]);
  const [rating, setRating] = useState<String | null>(null);
  const [movie, setMovie] = useState<String | null>(null);

  useEffect(() => {
    const calculateRating = async () => {
      try {
        const response = await fetch('http://localhost:5555/movie-pred', {
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

    if (movie && users.length > 0) {
      calculateRating();
    } else {
      setRating(null);
    }
  }, [users, movie]);

  return (
    <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
      <AutocompleteWithFetch label="User" 
        apiUrl={`http://localhost:5555/autocomplete/user`}
        suffix={`movie=${encodeURIComponent(movie as string || "")}`} 
        onChange={(_: any, newValue: any) => setUsers(newValue)} value={users} multiple disabled={!movie} />

      <AutocompleteWithFetch
        value={movie}
        label="Movie"
        apiUrl="http://localhost:5555/autocomplete/movie"
        onChange={(_: any, newValue: any) => {if (newValue == '' || newValue == null) setUsers([]); setMovie(newValue);}}
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
