import React, { useState } from "react";
import StarIcon from "@mui/icons-material/Star";
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
  ListItemText,
} from "@mui/material";
import { Bar } from "react-chartjs-2";
import { Chart, CategoryScale, LinearScale, BarElement } from "chart.js";

Chart.register(CategoryScale, LinearScale, BarElement);

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
};

const MovieCard: React.FC<MovieCardProps> = ({
  imageUrl,
  title,
  year,
  rating,
  movieId,
}) => {
  const [movie, setMovie] = useState<fullMovieInfo | null>(null);
  const [isModalOpen, setModalOpen] = useState(false);

  const handleModalOpen = () => {
    async function fetchMovie() {
      const response = await fetch(
        `http://localhost:5555/movies/get-by-id?movieId=${movieId}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
          mode: "cors",
        }
      );
      const data = await response.json();
      setMovie(data[0]);
    }

    setModalOpen(true);
    fetchMovie();
  };

  const handleModalClose = () => {
    setModalOpen(false);
  };

  const OpenModalButton = (
    <Button variant="outlined" onClick={handleModalOpen}>
      View Details
    </Button>
  );
  const Image = (
    <CardMedia component="img" alt={title} height="140" image={imageUrl} />
  );
  const Title = (
    <Typography variant="h6" component="div">
      {title} - {year}
    </Typography>
  );
  const Genre = (
    <Typography variant="subtitle1" color="textSecondary">
      {movie && movie?.genres && movie?.genres.length > 0
        ? movie.genres.join(" | ")
        : ""}
    </Typography>
  );
  const Rating = (
    <Stack direction="row" spacing={1} paddingLeft={5}>
      <Typography margin="auto" variant="h6" component="div">
        {rating}
      </Typography>
      <StarIcon />
    </Stack>
  );
  const Tags = (
    <Stack
      direction="row"
      spacing={1}
      sx={{ maxWidth: "100%", overflow: "auto" }}
    >
      {movie
        ? movie.tags
            .slice(0, 10)
            .map((tag, index) => <Chip key={index} label={tag} />)
        : ""}
    </Stack>
  );
  const MovieModal = (
    <Modal open={isModalOpen} onClose={handleModalClose}>
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          maxWidth: 600,
          width: "90%",
          bgcolor: "white",
          border: "2px solid #000",
          boxShadow: 24,
          p: 4,
          maxHeight: "80vh",
          overflowY: "auto",
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
            <ListItemText
              primary={"Average Rating: " + rating}
              primaryTypographyProps={{
                variant: "subtitle1",
                fontWeight: "bold",
                color: "text.primary",
              }}
            />
          </ListItem>

          <Box sx={{ marginTop: 2, height: 300 }}>
            <ListItem disablePadding>
              <ListItemText
                primary={"Ratings distribution"}
                primaryTypographyProps={{
                  variant: "subtitle1",
                  fontWeight: "bold",
                  color: "text.primary",
                }}
              />
            </ListItem>
            {movie && (
              <Bar
                data={{
                  labels: ["0", "1", "2", "3", "4", "5"],
                  datasets: [
                    {
                      label: "Number of Ratings",
                      data: [
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 0
                        ).length,
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 1
                        ).length,
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 2
                        ).length,
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 3
                        ).length,
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 4
                        ).length,
                        movie.ratingsList.filter(
                          (rating) => Math.floor(rating) === 5
                        ).length,
                      ],
                      backgroundColor: [
                        "rgba(255, 99, 132, 0.6)",
                        "rgba(255, 159, 64, 0.6)",
                        "rgba(255, 205, 86, 0.6)",
                        "rgba(75, 192, 192, 0.6)",
                        "rgba(54, 162, 235, 0.6)",
                        "rgba(153, 102, 255, 0.6)",
                      ],
                    },
                  ],
                }}
                options={{
                  maintainAspectRatio: false,
                  scales: {
                    y: {
                      title: {
                        display: true,
                        text: "Number of Ratings",
                      },
                      beginAtZero: true,
                      ticks: {
                        callback: (value) =>
                          `${(Number(value) / 1000).toFixed(0)}k`,
                        stepSize: 1000,
                      },
                    },
                    x: {
                      title: {
                        display: true,
                        text: "Rating",
                      },
                    },
                  },
                }}
              />
            )}
          </Box>
        </List>

        <List>
          <ListItem disablePadding>
            <ListItemText
              primary={"Actors"}
              primaryTypographyProps={{
                variant: "subtitle1",
                fontWeight: "bold",
                color: "text.primary",
              }}
            />
          </ListItem>
          {movie
            ? movie.actors.slice(0, 10).map((actor, index) => {
                const capitalizedName = actor
                  .split(" ")
                  .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
                return (
                  <ListItem key={index} disablePadding>
                    <ListItemText primary={capitalizedName} />
                  </ListItem>
                );
              })
            : ""}
        </List>

        <List>
          <ListItem disablePadding>
            <ListItemText
              primary={"Directors"}
              primaryTypographyProps={{
                variant: "subtitle1",
                fontWeight: "bold",
                color: "text.primary",
              }}
            />
          </ListItem>
          {movie
            ? movie.directors.slice(0, 10).map((director, index) => {
                const capitalizedName = director
                  .split(" ")
                  .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
                return (
                  <ListItem key={index} disablePadding>
                    <ListItemText primary={capitalizedName} />
                  </ListItem>
                );
              })
            : ""}
        </List>
      </Box>
    </Modal>
  );

  return (
    <Card sx={{ maxWidth: 600, maxHeight: "100%", display: "flex" }}>
      <Stack direction="row" sx={{ width: "100%" }}>
        {/* Image */}
        <CardMedia
          component="img"
          alt={title}
          width="200"
          height="200"
          image={imageUrl}
          sx={{ objectFit: "cover", flex: "1" }}
        />

        <CardContent sx={{ flex: "2" }}>
          <Stack direction="column" spacing={1}>
            <Stack direction="row" justifyContent="space-between">
              <Stack direction="column">{Title}</Stack>
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
    <Stack spacing={2} key={"movieStack"}>
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
      ))}
    </Stack>
  );
}

export default MovieCards;
