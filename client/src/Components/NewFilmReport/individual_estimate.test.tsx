import React from "react";
import IndividualEstimate from "./individual_estimate";
import { fireEvent, render, waitFor } from "@testing-library/react";

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);
jest.mock('../common/AutocompleteSelector', () => ({onChange}: any) => {
    return <button data-testid={'testButton'} onClick={() => onChange(undefined, 'New Movie')}>CLICK ME</button>
});

interface Rating {
    averageRating: number;
    subsetRating: number;
    userBias: number;
    genreBias: number;
    tagBias: number;
    averageBias: number;
    predictedRating: number;
}

test('displays accuracy button', async () => {
    const { getByText } = await render(<IndividualEstimate />);
    const ratingHeader = await waitFor(() => getByText('Please select a movie to see predictions.'));
    expect(ratingHeader).toBeInTheDocument();
});

test('displays info when movie selected', async () => {
    mockFetch.mockReturnValueOnce({
        ok: true,
        json: async () => ([1,2,3])
    }).mockReturnValueOnce({
        ok: true,
        json: async () => ({ 
            averageRating: 4.5,
            subsetRating: 4.5,
            userBias: 0.5,
            genreBias: 0.5,
            tagBias: 0.5,
            averageBias: 0.5,
            predictedRating: 4.5,
         } as Rating),
    });
    
    const { getByRole, getByText } = await render(<IndividualEstimate />);
    const button = await waitFor(() => getByRole('button', {name: 'CLICK ME'}));
    await fireEvent.click(button);
    const averageRating = await waitFor(() => getByText(/Actual Rating: 4.50/));
    const movieName = await waitFor(() => getByText(/New Movie/));
    expect(movieName).toBeInTheDocument();
    expect(averageRating).toBeInTheDocument();
});