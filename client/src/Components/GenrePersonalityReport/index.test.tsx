import React from 'react'
import { render, waitFor } from "@testing-library/react";
import GenrePersonalityPage from ".";

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);
jest.mock('./BarChartComponent', () => ({data} : {data: any}) => {
    return <div>Loaded Mock Bar! - {data.x}</div>
});

test('displays mocked bar chart', async () => {
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({ x: ["Genre1", "Genre2"], y: [0.5, 0.8] }),
    });
    
    const { getByText } = await render(<GenrePersonalityPage />);
    const calcText = await waitFor(() => getByText(/Loaded Mock Bar! - /));
    expect(calcText).toBeInTheDocument();
});

test('displays data', async () => {
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({ x: ["Genre1", "Genre2"], y: [0.5, 0.8] }),
    });
    
    const { getByText } = await render(<GenrePersonalityPage />);
    const calcText = await waitFor(() => getByText(/Genre1/));
    expect(calcText).toBeInTheDocument();
});