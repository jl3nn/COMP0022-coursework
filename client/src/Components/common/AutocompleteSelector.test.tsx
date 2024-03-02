import React from 'react';
import { render, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import AutocompleteWithFetch from './AutocompleteSelector';

global.fetch = jest.fn() as jest.Mock;
const mockFetch = (fetch as unknown as jest.Mock);

test('renders with initial props', async () => {
    mockFetch.mockReturnValue({
        ok: true,
        json: async () => ({
            options: ['Option1', 'Option2']
        })
    });

    const { getByLabelText } = await render(<AutocompleteWithFetch apiUrl="/test-api" onChange={jest.fn()} label="Test Label" value="" />);
    const testLable = await waitFor(() => getByLabelText(/Test Label/i));
    expect(testLable).toBeInTheDocument();
});
