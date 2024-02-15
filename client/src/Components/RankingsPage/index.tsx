import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography, Box } from '@mui/material';

function RankingsPage() {
    const [popularGenres, setPopularGenres] = useState([] as string[])
    const [controversialGenres, setControversialGenres] = useState([] as string[])

    useEffect(() => {
        fetch(`http://localhost:5555/genres/popular`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setPopularGenres(data));
    }, []);

    useEffect(() => {
        fetch(`http://localhost:5555/genres/controversial`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setControversialGenres(data));
    }, []);

    return (
        <Stack spacing={2} alignItems="center" margin={5}>
            <Paper sx={{ width: 600 }}>
                <Typography variant="h4">Most Popular Genres</Typography>
                <Box sx={{ maxHeight: 'calc(50vh - 150px)', overflow: "auto", width: 600 }}>
                    {popularGenres.map((m) => <Typography variant="h6">{m}</Typography>)}
                </Box>
            </Paper>
            <Paper sx={{ maxHeight: 'calc(50vh - 100px)', overflow: "auto", width: 600 }}>
                <Typography variant="h4">Most Controversial Genres</Typography>
                <Box sx={{ maxHeight: 'calc(50vh - 150px)', overflow: "auto", width: 600 }}>
                    {controversialGenres.map((m) => <Typography variant="h6">{m}</Typography>)}
                </Box>
            </Paper>
        </Stack>
    );
}

export default RankingsPage;
