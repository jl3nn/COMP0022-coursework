import React, { useEffect, useState } from 'react';
import { Stack, Typography } from '@mui/material';
import BarChartComponent from './BarChartComponent';

interface Results {
    x: string[],
    y: number[]
}

function GenrePersonalityPage() {
    const [data, setData] = useState<Results | null>(null);

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
                setData(data);
            } catch (error: any) {
                console.error('Error calculating skew:', error.message);
            }
        };
        calculateSkew();
    }, []);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <Typography>The following is calculated based off the pearson coefficient between the genre and personality type.</Typography>
            {data? (
                <BarChartComponent data={data as any} />
            ) : (
                <Typography>Calculating...</Typography>
            )}
        </Stack>
    );
}

export default GenrePersonalityPage;
