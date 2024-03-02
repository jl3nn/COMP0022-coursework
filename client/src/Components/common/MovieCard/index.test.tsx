import React from "react";
import { render, waitFor, fireEvent, act } from "@testing-library/react";
import MovieCards from ".";

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);

const movieData = {
    imageUrl: 'poster.jpg',
    title: 'Movie1',
    year: 2020,
    rating: 5.0,
    genres: ['genre1', 'genre2'],
    tags: ['tag1', 'tag2'],
    ratingsList: [5.0, 4.0, 3.0, 2.0, 1.0],
    actors: ['actor1', 'actor2'],
    director: ['director1'],
}

const movieListData = [
    {
        title: 'Movie1',
        year: '2020',
        imageUrl: 'poster.jpg',
        rating: 5.0,
        movieId: '123'
    },
    {
        title: 'Movie2',
        year: '2022',
        imageUrl: 'poster.jpg',
        rating: 5.0,
        movieId: '124'
    }
]

test('displays movie card', async () => {
    const { getByText } = await render(<MovieCards data={movieListData} />);
    const movieTitle = await waitFor(() => getByText(/Movie1/));
    expect(movieTitle).toBeInTheDocument();
});

test('displays second movie', async () => {
    const { getByText } = await render(<MovieCards data={movieListData} />);
    const movieTitle = await waitFor(() => getByText(/Movie2/));
    const movieYear2 = await waitFor(() => getByText(/2022/));
    expect(movieYear2).toBeInTheDocument();
    expect(movieTitle).toBeInTheDocument();
});
