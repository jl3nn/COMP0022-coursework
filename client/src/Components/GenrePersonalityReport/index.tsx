import React, { useEffect, useState } from 'react';
import { Box, Slider, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

function GenrePersonalityPage() {
    const [genre, setGenres] = useState(null as string | null);
    const [metric, setMetric] = useState(null as string | null);
    const [metric_degree, setMetricDegree] = useState(null as string | null);
    const [personality_skew, setSkew] = useState<String | null>(null);
    const [openness, setOpenness] = useState([1, 7] as [number, number]);
    const [agreeableness, setAgreeableness] = useState([1, 7] as [number, number]);
    const [emotional_stability, setEmotionalStability] = useState([1, 7] as [number, number]);
    const [conscientiousness, setConscientiousness] = useState([1, 7] as [number, number]);
    const [extraversion, setExtraversion] = useState([1, 7] as [number, number]);

    useEffect(() => {
        const calculateSkew = async () => {
            try {
                const response = await fetch('http://localhost:5555/personality-skew', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ genre, metric, metric_degree, openness, agreeableness, emotional_stability, conscientiousness, extraversion }),
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const skewData = await response.json();
                setSkew(skewData);
            } catch (error: any) {
                console.error('Error calculating skew:', error.message);
            }
        };

        if (genre) {
            calculateSkew();
        } else {
            console.log(':(')
            setSkew(null);
        }
    }, [genre, metric, metric_degree, openness, agreeableness, emotional_stability, conscientiousness, extraversion]);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <AutocompleteWithFetch value={genre} label="Genres" apiUrl="http://localhost:5555/autocomplete/genre"
                onChange={(_: any, newValue: any) => setGenres(newValue)} />
            <AutocompleteWithFetch value={metric} label="Personality Metric" apiUrl="http://localhost:5555/autocomplete/metric"
                onChange={(_: any, newValue: any) => setMetric(newValue)} />
            <AutocompleteWithFetch value={metric_degree} label="Personality Metric Degree" apiUrl="http://localhost:5555/autocomplete/metric-degree"
                onChange={(_: any, newValue: any) => setMetricDegree(newValue)} />

            <SliderForPersonality title="Openness" value={openness} onChange={setOpenness} />
            <SliderForPersonality title="Agreeableness" value={agreeableness} onChange={setAgreeableness} />
            <SliderForPersonality title="Emotional Stability" value={emotional_stability} onChange={setEmotionalStability} />
            <SliderForPersonality title="Conscientiousness" value={conscientiousness} onChange={setConscientiousness} />
            <SliderForPersonality title="Extraversion" value={extraversion} onChange={setExtraversion} />

            <Typography>
                {personality_skew ? (
                    <>This group rates {genre} {personality_skew} compared to other groups.</>
                ) : (
                    <>Please select a genre, to see how this group compares!</>
                )}
            </Typography>
        </Stack>
    );
}

type SliderForPersonalityProps = {
    title: string;
    value: [number, number];
    onChange: (value: [number, number]) => void;
}

function SliderForPersonality({ title, value, onChange }: SliderForPersonalityProps) {
    return (
        <Box>
            <Typography>{title}:</Typography>
            <Slider
                value={value}
                onChange={(_, val) => onChange(val as [number, number])}
                valueLabelDisplay="auto"
                min={1}
                max={7}
                step={0.5}
                sx={{ width: 300 }}
                marks={[{ value: 0, label: '1' }, { value: 10, label: '7' }]}
            />
        </Box>
    );
}

// Openness 1 to 7

// Agreeableness 1 to 7

// Emotional Stability 1 to 7

// Conscientiousness 1 to 7

// Extraversion 1 to 7

// Assigned Metric serendipity, popularity, diversity, default

// Assigned Condition high, medium, low


export default GenrePersonalityPage;
