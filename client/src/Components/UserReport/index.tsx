import React, { useEffect, useState } from 'react';
import { Paper, Radio, Stack, Typography, RadioGroup, FormControlLabel } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

function UserReportPage() {
    const [genre, setGenres] = useState(null as string | null);
    const [film, setFilms] = useState(null as string | null);
    const [opinion, setOpinion] = useState(null as number | null);
    const [better, setBetter] = useState([] as string[]);
    const [worse, setWorse] = useState([] as string[]);

    useEffect(() => {
        const calculateSkew = async () => {
            try {
                const response = await fetch('http://localhost:5555/user-skew', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ genres: genre, films: film, opinion: opinion }),
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const skewData = await response.json();
                setBetter(skewData.better);
                setWorse(skewData.worse);
            } catch (error: any) {
                console.error('Error calculating skew:', error.message);
            }
        };

        if (opinion && (genre || film)) {
            calculateSkew();
        } else {
            setBetter([]);
            setWorse([]);
        }
    }, [opinion, genre, film]);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <Typography variant="h6">For Users that typically</Typography>
            <RadioGroup
                aria-labelledby="demo-radio-buttons-group-label"
                name="radio-buttons-group"
                value={opinion}
                onChange={(event) => setOpinion(parseInt(event.target.value))}
            >
                <FormControlLabel value="1" control={<Radio />} label="Like" />
                <FormControlLabel value="-1" control={<Radio />} label="Dislike" />
                <FormControlLabel value="0" control={<Radio />} label="Are Neutral On" />
            </RadioGroup>
            <Typography variant="h6">the following</Typography>
            <AutocompleteWithFetch value={genre} disabled={film != null} label="Genres" apiUrl="http://localhost:5555/autocomplete/genre" onChange={(_: any, newValue: any) => setGenres(newValue)} />
            <AutocompleteWithFetch value={film} disabled={genre != null} label="Films" apiUrl="http://localhost:5555/autocomplete/movie" onChange={(_: any, newValue: any) => setFilms(newValue)} />

            <Typography>
                <Typography variant="h6">Those users like:</Typography>
                {better.map((b) => <Typography variant="h6">{b}</Typography>)}
                <Typography variant="h6">Those users dislike:</Typography>
                {worse.map((b) => <Typography variant="h6">{b}</Typography>)}
            </Typography>
        </Stack>
    );
}

export default UserReportPage;
