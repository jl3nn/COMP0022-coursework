import { act, fireEvent, render, waitFor } from '@testing-library/react';
import MovieListPage from '.';
import { useSearch } from './SearchContext/context';

// At the top of your test file
jest.mock("./SearchContext/context", () => ({
    useSearch: () => {return {
        searchText: '',
        ratings: [0, 10],
        tags: [],
        genres: [],
        date: [1900, 2020]
    }},
}));

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);

beforeEach(() => {
    mockFetch.mockClear();
});

test('renders component and checks for initial loading state', async () => {
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({ results: [], all_loaded: true }),
    });

    const {findByText} = render(<MovieListPage />);
    const loadMoreText = await waitFor(() => findByText('Load More'));
    expect(loadMoreText).toBeInTheDocument();
});

test('loads movies successfully from API', async () => {
    const mockMovies = [
        { imageUrl: 'url1', title: 'Movie 1', year: '2020', rating: 8, movieId: '1' },
    ];
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({ results: mockMovies, all_loaded: true }),
    });
  
    const { findAllByText } = render(<MovieListPage />);
    const movieTitles = await waitFor(() => findAllByText(/Movie 1/));
    expect(movieTitles.length).toBeGreaterThan(0);
});

test('loads more movies on "Load More" button click', async () => {
    const mockMoviesInitial = [{ imageUrl: 'url1', title: 'Movie 1', year: '2020', rating: 8, movieId: '1' }];
    const mockMoviesAdditional = [{ imageUrl: 'url2', title: 'Movie 2', year: '2021', rating: 9, movieId: '2' }];
    mockFetch.mockReturnValue({
      ok: true,
      json: async () => ({ results: mockMoviesInitial, all_loaded: false }),
    });
  
    const {findByRole, findByText} = render(<MovieListPage />);
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({ results: mockMoviesAdditional, all_loaded: true }),
      });
    const loadMoreButton = await waitFor(() => findByRole('button', { name: 'Load More' }));
    fireEvent.click(loadMoreButton);
    const movieText = await waitFor(() => findByText('Movie 2 - 2021'));
    expect(movieText).toBeInTheDocument();
});
  
  
  