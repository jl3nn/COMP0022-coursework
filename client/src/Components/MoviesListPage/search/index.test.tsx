import { act, render, waitFor } from "@testing-library/react";
import SearchComponent from ".";
import userEvent from "@testing-library/user-event";

jest.mock('../SearchContext/context', () => {
  return {
    useSearch: () => {
      return {
        setSearchFilter: jest.fn(),
      };
    },
  };
});

interface AutocompleteProps {
    label: string;
    value: string;
    onChange: (e: any) => void;
}

jest.mock('../../common/AutocompleteSelector', () => {
  return ({label, value, onChange}: AutocompleteProps) => <div>{label}-input: <input type={'text'} value={value} onChange={onChange} /></div>;
});

describe('SearchComponent', () => {
    test('renders without crashing', () => {
        render(<SearchComponent />);
    });

    test('Drawer is hidden by default', () => {
        const { queryByText } = render(<SearchComponent />);
        expect(queryByText('Search Filters')).toBeNull();
    });

    test('Renders search bar', () => {
        const { getByPlaceholderText } = render(<SearchComponent />);
        expect(getByPlaceholderText('Search')).toBeInTheDocument();
    });

    test('can open drawer', async () => {
        const {getByTestId, getByText} = render(<SearchComponent />);
        act(() => userEvent.click(getByTestId('filter-icon')));
        await waitFor(() => {
            expect(getByText('Search Filters')).toBeInTheDocument();
        });
    });
});