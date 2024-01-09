import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography } from '@mui/material';
import AutocompleteWithFetch from '../common/AutocompleteSelector';

function UserReportPage() {
    const [genre, setGenres] = useState(null as string | null);
    const [film, setFilms] = useState(null as string | null);
    const [user, setUsers] = useState(null as string | null);
    const [skew, setSkew] = useState<String | null>(null);

    useEffect(() => {
        const calculateSkew = async () => {
            try {
            const response = await fetch('http://localhost:5555/user-skew', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                },
                body: JSON.stringify({ genres: genre, films: film, users: user }),
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
        
        if (user && (genre || film)) {
            calculateSkew();
        } else {
            setSkew(null);
        }
    }, [user, genre, film]);

    return (
        <Stack spacing={2} alignItems="center" maxWidth={800} margin='auto'>
            <AutocompleteWithFetch value={user} label="User" apiUrl="http://localhost:5555/users-autocomplete" onChange={(_: any, newValue: any) => setUsers(newValue)} />
            <AutocompleteWithFetch value={genre} disabled={film != null} label="Genres" apiUrl="http://localhost:5555/genre-autocomplete" onChange={(_: any, newValue: any) => setGenres(newValue)} />
            <AutocompleteWithFetch value={film} disabled={genre != null} label="Films" apiUrl="http://localhost:5555/films-autocomplete" onChange={(_: any, newValue: any) => setFilms(newValue)} />

            <Typography>
            {skew ? (
                <>{user} rates {film}{genre} {skew} than other films.</>
            ) : (
                <>Please select a user and some genres/films</>
            )}
            </Typography>
        </Stack>
    );
}

export default UserReportPage;
