import React from 'react';
import { SearchProvider, useSearch } from './context';
import { fireEvent, render, screen } from '@testing-library/react';

const SearchContextTestComponent = () => {
    const {
        searchText,
        ratings,
        tags,
        genres,
        date,
        setSearchFilter,
        resetFilters,
    } = useSearch();
  
    return (
        <div>
            <div data-testid="searchText">{searchText}</div>
            <div data-testid="ratings">{ratings.join(',')}</div>
            <div data-testid="tags">{tags.join(',')}</div>
            <div data-testid="genres">{genres.join(',')}</div>
            <div data-testid="date">{date.join(',')}</div>
            <button onClick={() => setSearchFilter('Matrix')}>Set Search Text</button>
            <button onClick={resetFilters}>Reset Filters</button>
        </div>
    );
};    
  
const WrappedComponent = () => (
    <SearchProvider>
        <SearchContextTestComponent />
    </SearchProvider>
);


describe('SearchContext functionality', () => {
    it('initializes context with default values', () => {
      render(<WrappedComponent />);
      expect(screen.getByTestId('searchText').textContent).toBe('');
      expect(screen.getByTestId('ratings').textContent).toBe('0,10');
      expect(screen.getByTestId('tags').textContent).toBe('');
      expect(screen.getByTestId('genres').textContent).toBe('');
      expect(screen.getByTestId('date').textContent).toBe('1902,2018');
    });
  
    it('updates search text correctly', () => {
      render(<WrappedComponent />);
      fireEvent.click(screen.getByText('Set Search Text'));
      expect(screen.getByTestId('searchText').textContent).toBe('Matrix');
    });
  
    it('resets filters to default values', () => {
      render(<WrappedComponent />);
      // First, change some values
      fireEvent.click(screen.getByText('Set Search Text'));
      // Then reset
      fireEvent.click(screen.getByText('Reset Filters'));
      expect(screen.getByTestId('searchText').textContent).toBe('');
      expect(screen.getByTestId('ratings').textContent).toBe('0,10');
      expect(screen.getByTestId('tags').textContent).toBe('');
      expect(screen.getByTestId('genres').textContent).toBe('');
      expect(screen.getByTestId('date').textContent).toBe('1902,2018');
    });
  });