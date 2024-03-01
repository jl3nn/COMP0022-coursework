import { render, waitFor } from '@testing-library/react';
import RankingsPage from '.';

jest.mock('react-chartjs-2', () => ({
    Bar: ({data}: any) => <p>{data.labels}</p>
}));

beforeEach(() => {
    global.fetch = jest.fn()
    .mockResolvedValueOnce({
        ok: true,
        json: async () => [
        { genre: "Action", statistic: 8.5 },
        { genre: "Comedy", statistic: 7.8 },
        ],
    })
    .mockResolvedValueOnce({
        ok: true,
        json: async () => [
        { genre: "Thriller", statistic: 5.4 },
        { genre: "Horror", statistic: 6.1 },
        ],
    });
    
  });
  
afterEach(() => {
    jest.restoreAllMocks();
});

test('renders charts with data after successful fetch', async () => {
    const {findByText} = await render(<RankingsPage />);

    const popularTitle = await waitFor(() => findByText('Most Popular Genres - Average Rating'));
    const controversialTitle = await waitFor(() => findByText('Most Controversial Genres - Standard Deviation'));

    expect(popularTitle).toBeInTheDocument();
    expect(controversialTitle).toBeInTheDocument();
});

test('renders charts with genres after fetch', async () => {
    const {findByText} = await render(<RankingsPage />);

    const popularGenre = await findByText(/Action/);
    const conrovertialGenre = await findByText(/Horror/);

    expect(popularGenre).toBeInTheDocument();
    expect(conrovertialGenre).toBeInTheDocument();
});
