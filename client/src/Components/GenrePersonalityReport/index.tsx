import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

function GenrePersonalityPage() {
    const [genre, setGenres] = useState(null as string | null);
    const [personality, setPersonality] = useState(null as string | null);
    const [personality_skew, setSkew] = useState<String | null>(null);

    useEffect(() => {
        const calculateSkew = async () => {
            try {
            const response = await fetch('http://localhost:5555/personality-skew', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify({ genre, personality }),
            });
        
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
        
            const skewData = await response.json();
            setSkew(skewData);
            } catch (error : any) {
            console.error('Error calculating skew:', error.message);
            }
        };
        
        if (genre && personality) {
            calculateSkew();
        } else {
            console.log(':(')
            setSkew(null);
        }
    }, [genre, personality]);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <AutocompleteWithFetch value={genre} label="Genres" apiUrl="http://localhost:5555/genre-autocomplete" 
                onChange={(_: any, newValue: any) => setGenres(newValue)} />
            <AutocompleteWithFetch value={personality} label="Personality" apiUrl="http://localhost:5555/personalities-autocomplete" 
                onChange={(_: any, newValue: any) => setPersonality(newValue)} />

            <Typography>
            {personality_skew ? (
                <>{personality}s rate {genre} {personality_skew} compared to other groups.</>
            ) : (
                <>Please select a user and some genres/films</>
            )}
            </Typography>
        </Stack>
    );
}

export default GenrePersonalityPage;