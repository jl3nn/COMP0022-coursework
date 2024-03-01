import { fireEvent, getAllByAltText, render, waitFor } from '@testing-library/react';
import UserReportPage from '.';

global.fetch = jest.fn();
jest.mock('../common/AutocompleteSelector', () => ({onChange, label}: any) => {
    return <button aria-label={label} onClick={() => onChange(undefined, 'New Genre')}>CLICK ME</button>
});
jest.mock('react-chartjs-2', () => ({
    Bar: ({data}: any) => <p>{data.labels}</p>
}));

test('initial render shows default UI elements', async () => {
    const {getByText, getAllByText} = await render(<UserReportPage />);
    expect(getByText('User Preferences Report')).toBeInTheDocument();
    expect(getByText('Preferences Analysis')).toBeInTheDocument();
    expect(getAllByText('No data available')).toHaveLength(2);
});
  
test('renders fetched data correctly', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => [
            { id: "Like1", avg_rating: 5.4 },
            { id: "Like2", avg_rating: 6.1 },
            { id: "Like3", avg_rating: 8.5 },
            { id: "Like4", avg_rating: 7.8 },
            { id: "Like5", avg_rating: 6.1 },
        ],
    }).mockResolvedValueOnce({
        ok: true,
        json: async () => [
            { id: "Dislike1", avg_rating: 5.4 },
            { id: "Dislike2", avg_rating: 6.1 },
            { id: "Dislike3", avg_rating: 8.5 },
            { id: "Dislike4", avg_rating: 7.8 },
            { id: "Dislike5", avg_rating: 6.1 },
        ],
    });
    
    const { getByLabelText, getAllByText } = await render(<UserReportPage />);

    const likeButton = await getByLabelText('Like')

    await waitFor(() => fireEvent.click(likeButton));
    
    const genreButton = await getByLabelText('Genres');
    await waitFor(() => fireEvent.click(genreButton));

    await waitFor(() => {
        expect(getAllByText(/Like4/)).toHaveLength(3);
    });
});
  