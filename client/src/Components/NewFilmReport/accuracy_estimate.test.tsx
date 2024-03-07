import React from "react";
import AccuracyEstimate from "./accuracy_estimate";
import { fireEvent, render, waitFor } from "@testing-library/react";

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);
jest.mock('../common/AutocompleteSelector', () => () => {
    return <div>Mocked Autocomplete</div>
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
    const { getByText } = await render(<AccuracyEstimate />);
    const calcText = await waitFor(() => getByText('Estimate Accuracy'));
    expect(calcText).toBeInTheDocument();
});

test('displays data when button pressed', async () => {
    mockFetch.mockReturnValueOnce({
        ok: true,
        json: async () => ({'results': [
            {title: 'Movie1'}
        ]})
    }).mockReturnValueOnce({
      ok: true,
      json : async () => ([
        1, 2, 3
      ])  
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

    const { getByRole, getByText } = await render(<AccuracyEstimate />);
    const estimateAccuracyButton = await waitFor(() => getByRole('button', {name: 'Estimate Accuracy'}));
    fireEvent.click(estimateAccuracyButton);
    const averageRating = await waitFor(() => getByText(/Actual Rating: 4.50/));
    expect(averageRating).toBeInTheDocument();
});