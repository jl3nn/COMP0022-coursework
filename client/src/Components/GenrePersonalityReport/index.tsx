import React, { useEffect, useState } from 'react';
import { Box, Slider, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

interface Results {
    genre: string,
    trait: string
}

function GenrePersonalityPage() {
    const [positives, setPositives] = useState<Results[]>([])
    const [negatives, setNegatives] = useState<Results[]>([])

    useEffect(() => {
        const calculateSkew = async () => {
            try {
                const response = await fetch('http://localhost:5555/personality-skew', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                setPositives(data.positive_correlations);
                setNegatives(data.negative_correlations);
            } catch (error: any) {
                console.error('Error calculating skew:', error.message);
            }
        };
        calculateSkew();
    }, []);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <Typography>The following is calculated based off the pearson coefficient between the genre and personality type.</Typography>
            {positives && negatives ? (
                <Box>
                    {positives.map((x) => {
                        return <Typography>Users with high {x.trait} tend to rate {x.genre} highly.</Typography>
                    })}
                    {negatives.map((x) => {
                        return <Typography>Users with high {x.trait} tend to rate {x.genre} poorly.</Typography>
                    })}
                </Box>
            ) : (
                <Typography>Calculating...</Typography>
            )}
        </Stack>
    );
}

export default GenrePersonalityPage;
