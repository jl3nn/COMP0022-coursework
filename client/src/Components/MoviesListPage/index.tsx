// App.js
import React, { useEffect, useState } from 'react';
import { useSearch } from './SearchContext/context';
import { Paper, Stack } from '@mui/material';
import SearchComponent from './search';
import MovieCards from '../common/MovieCard';

type Movie = {
    imageUrl: string;
    title: string;
    rating: number;
    genre: string;
    tags: string[];
    ratingsList: number[];
}

function MovieListPage() {
    const {searchText, ratings, tags, genres, date} = useSearch();
    const [data, setData] = useState<Movie[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:5555/get-search-results', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    searchText,
                    ratings,
                    tags,
                    genres,
                    date
                }),
                mode: 'cors'
                });

                if (!response.ok) {
                    // throw new Error('Failed to fetch data');
                    setData([{
                        imageUrl: '',
                        title: 'Server Is Broken',
                        rating: 1   ,
                        genre: 'Bar',
                        tags: ['bla'],
                        ratingsList: [1, 2, 3, 4, 5]
                    }])
                    return;
                }

                const result = await response.json();
                setData(result);
            } catch (error: any) {
                // console.error('Error fetching data:', error.message);
                setData([{
                    imageUrl: '',
                    title: 'Server is down',
                    rating: 1,
                    genre: 'Bar',
                    tags: ['bla'],
                    ratingsList: [1, 2, 3, 4, 5]
                }])
            }
        };

        fetchData();
    }, [searchText, ratings, tags, genres]);

    return (
        <Stack spacing={2} alignItems="center" margin={5}>
                <SearchComponent/>
                <Paper sx={{maxHeight: 'calc(100vh - 250px)', overflow:"auto",  width:600}}>
                    <MovieCards data={data} />
                </Paper>
        </Stack>
    );
}

export default MovieListPage;