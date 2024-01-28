import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography, Box } from '@mui/material';
import MovieCards from '../common/MovieCard';

function RankingsPage() {
    const [popularMovies, setPopularMovies] = useState([] as string[])
    const [contrevertialMovies, setContrevertialMovies] = useState([] as string[])

    useEffect(() => {
        fetch(`http://localhost:5555/movies/popular`, { mode: 'cors' })
      .then((response) => response.json())
      .then((data) => setPopularMovies(data));
    }, []);

    useEffect(() => {
        fetch(`http://localhost:5555/movies/contrevertial`, { mode: 'cors' })
      .then((response) => response.json())
      .then((data) => setContrevertialMovies(data));
    }, []);

    return (
        <Stack spacing={2} alignItems="center" margin={5}>
                <Paper sx={{width:600}}>
                    <Typography variant="h4">Most Popular Genres</Typography>
                    <Box sx={{maxHeight: 'calc(50vh - 150px)', overflow:"auto",  width:600}}>
                        {popularMovies.map((m) => <Typography variant="h6">{m}</Typography>)}                    
                    </Box>
                </Paper>
                <Paper sx={{maxHeight: 'calc(50vh - 100px)', overflow:"auto",  width:600}}>
                    <Typography variant="h4">Most Contrevertial Genres</Typography>
                    <Box sx={{maxHeight: 'calc(50vh - 150px)', overflow:"auto",  width:600}}>
                        {contrevertialMovies.map((m) => <Typography variant="h6">{m}</Typography>)}
                    </Box>
                </Paper>
        </Stack>
    );
}

export default RankingsPage;