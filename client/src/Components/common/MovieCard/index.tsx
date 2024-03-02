import React, { useState } from 'react';
import StarIcon from '@mui/icons-material/Star';
import {
    Card,
    CardContent,
    CardMedia,
    Chip,
    Typography,
    Stack,
    Modal,
    Button,
    Box,
    Divider,
    List,
    ListItem,
    ListItemText
} from '@mui/material'; 

interface MovieCardProps {
    imageUrl: string;
    title: string;
    year: string;
    rating: number;
    movieId: string;
}

type fullMovieInfo = {
    imageUrl: string;
    title: string;
    year: string;
    rating: number;
    genres: string[];
    tags: string[];
    ratingsList: number[];
    actors: string[];
    directors: string[];
}

const MovieCard: React.FC<MovieCardProps> = ({
    imageUrl,
    title,
    year,
    rating,
    movieId
}) => {
    const [movie, setMovie] = useState<fullMovieInfo | null>(null);
    const [isModalOpen, setModalOpen] = useState(false);

    const handleModalOpen = () => {
        async function fetchMovie() {
            const response = await fetch(`http://localhost:5555/movies/get-by-id?movieId=${movieId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors'
            });
            const data = await response.json();
            setMovie(data[0]);
        }

        setModalOpen(true);
        fetchMovie();
    };

    const handleModalClose = () => {
        setModalOpen(false);
    };

    const OpenModalButton = <Button variant="outlined" onClick={handleModalOpen}>
        View Details
    </Button>;
    const Image = <CardMedia component="img" alt={title} height="140" image={imageUrl} />;
    const Title = <Typography variant="h6" component="div">
        {title} - {year}
    </Typography>;
    const Genre = <Typography variant="subtitle1" color="textSecondary">
        {movie && movie?.genres && movie?.genres.length > 0 ? movie.genres.join(' | ') : ''}
    </Typography>;
    const Rating = <Stack direction='row' spacing={1} paddingLeft={5}><Typography margin='auto' variant="h6" component="div">
        {rating}
    </Typography><StarIcon /></Stack>;
    const Tags = <Stack direction="row" spacing={1} sx={{ maxWidth: "100%", overflow: "auto" }}>
        {movie ? movie.tags.slice(0, 10).map((tag, index) => (
            <Chip key={index} label={tag} />
        )) : ''}
    </Stack>;
    const MovieModal = <Modal open={isModalOpen} onClose={handleModalClose}>
        <Box
            sx={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                maxWidth: 600,
                width: '90%',
                bgcolor: 'white',
                border: '2px solid #000',
                boxShadow: 24,
                p: 4,
                borderRadius: 8,
                marginY: 3,
                overflow: "auto"
            }}
        >
            {Title}
            <Divider />
            {Image}

            <Stack direction="column" spacing={1}>
                <Stack direction="row" justifyContent="space-between">
                    {Genre}
                </Stack>
                {Tags}
            </Stack>

            <List>
                <ListItem disablePadding>
                    <ListItemText primary={'Average Rating: ' + rating} />
                </ListItem>
                <div style={{ overflowY: 'auto', maxHeight: '100px', paddingRight: '16px' }}>
                    {movie ? movie.ratingsList.slice(0, 10).map((rating, index) => (
                        <ListItem key={index} disablePadding>
                            <ListItemText primary={`Rating ${index + 1}: ${rating}`} />
                        </ListItem>
                    )) : ''}
                </div>
            </List>

            <List>
                <ListItem disablePadding>
                    <ListItemText primary={'Actors'} />
                </ListItem>
                {movie ? movie.actors.slice(0, 10).map((actor, index) => (
                    <ListItem key={index} disablePadding>
                        <ListItemText primary={actor} />
                    </ListItem>
                )) : ''}
            </List>

            <List>
                <ListItem disablePadding>
                    <ListItemText primary={'Directors'} />
                </ListItem>
                {movie ? movie.directors.slice(0, 10).map((director, index) => (
                    <ListItem key={index} disablePadding>
                        <ListItemText primary={director} />
                    </ListItem>
                )) : movie}
            </List>
        </Box>
    </Modal>;

    return (
        <Card sx={{ maxWidth: 600, maxHeight: '100%', display: 'flex' }}>
            <Stack direction="row" sx={{ width: '100%' }}>
                {/* Image */}
                <CardMedia
                    component="img"
                    alt={title}
                    width="200"
                    height="200"
                    image={imageUrl}
                    sx={{ objectFit: 'cover', flex: '1' }}
                />

                <CardContent sx={{ flex: '2' }}>
                    <Stack direction="column" spacing={1}>
                        <Stack direction="row" justifyContent="space-between">
                            <Stack direction="column">
                                {Title}
                            </Stack>
                            {Rating}
                        </Stack>
                        {OpenModalButton}
                    </Stack>
                </CardContent>
            </Stack>

            {MovieModal}
        </Card>
    );
};

function MovieCards({ data }: { data: MovieCardProps[] }) {
    return (
        <Stack spacing={2} key={'movieStack'}>
            {data.map((movie) => (
                <Box key={movie.movieId}>
                    <MovieCard
                        imageUrl={movie.imageUrl}
                        title={movie.title}
                        year={movie.year}
                        rating={movie.rating}
                        movieId={movie.movieId}
                    />
                </Box>
            )
            )}
        </Stack>
    )
}

export default MovieCards;
