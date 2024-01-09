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
    rating: number;
    genre: string;
    tags: string[];
    ratingsList: number[];
}

const MovieCard: React.FC<MovieCardProps> = ({
    imageUrl,
    title,
    rating,
    genre,
    tags,
    ratingsList
}) => {
    const [isModalOpen, setModalOpen] = useState(false);

    const handleModalOpen = () => {
        setModalOpen(true);
    };

    const handleModalClose = () => {
        setModalOpen(false);
    };

    const OpenModalButton = <Button variant="outlined" onClick={handleModalOpen}>
        View Details
    </Button>;
    const Image = <CardMedia component="img" alt={title} height="140" image={imageUrl} />;
    const Title = <Typography variant="h6" component="div">
        {title}
    </Typography>;
    const Genre = <Typography variant="subtitle1" color="textSecondary">
        {genre}
    </Typography>;
    const Rating = <Stack direction='row' spacing={1} paddingLeft={5}><Typography margin='auto' variant="h6" component="div">
        {rating}
    </Typography><StarIcon /></Stack>;
    const Tags = <Stack direction="row" spacing={1}>
        {tags.map((tag, index) => (
            <Chip key={index} label={tag} />
        ))}
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
                    <ListItemText primary={'Average Rating:' + rating} />
                </ListItem>
                <div style={{ overflowY: 'auto', maxHeight: '100px', paddingRight: '16px' }}>
                    {ratingsList.map((rating, index) => (
                        <ListItem key={index} disablePadding>
                            <ListItemText primary={`Rating ${index + 1}: ${rating}`} />
                        </ListItem>
                    ))}
                </div>
            </List>

            <Typography variant="body1" gutterBottom>
                {"TODO put some stuff here"}
            </Typography>
        </Box>
    </Modal>;

  return (
    <Card sx={{ maxWidth: 600, maxHeight: '100%', display: 'flex' }}>
    <Stack direction="row" sx={{ width: '100%' }}>
        {/* Image */}
        <CardMedia
        component="img"
        alt={title}
        width="200" // Adjust the width of the image
        height="200" // Adjust the height to maintain the aspect ratio
        image={imageUrl}
        sx={{ objectFit: 'cover', flex: '1' }} // Set flex: 1 for the image
        />

        {/* Content */}
        <CardContent sx={{ flex: '2' }}> {/* Adjust flex value based on your requirement */}
        <Stack direction="column" spacing={1}>
            <Stack direction="row" justifyContent="space-between">
            <Stack direction="column">
                {Title}
                {Genre}
            </Stack>
            {Rating}
            </Stack>
            {Tags}
            {OpenModalButton}
        </Stack>
        </CardContent>
    </Stack>

    {MovieModal}
    </Card>
    );
};

export default MovieCard;
