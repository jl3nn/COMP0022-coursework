import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BasicTabs from './App';

jest.mock('./Components/MoviesListPage', () => ({
    __esModule: true,
    default: () => <div>MovieListPage Mock Loaded</div>,
    SearchProvider: ({ children }: any) => <div>{children}</div> // Mock context provider if necessary
}));

jest.mock('./Components/RankingsPage', () => () => <div>RankingsPage Mock Loaded!</div>);
jest.mock('./Components/UserReport', () => () => <div>UserReportPage Mock Loaded!</div>);
jest.mock('./Components/NewFilmReport', () => () => <div>NewFilmPage Mock Loaded!</div>);
jest.mock('./Components/GenrePersonalityReport', () => () => <div>GenrePersonalityPage Mock Loaded!</div>);
  

describe('BasicTabs Component', () => {
  test('renders without crashing', () => {
    render(<BasicTabs />);
    expect(screen.getByText('Movie Overview (1, 2)')).toBeInTheDocument();
  });

  test('switching tabs changes displayed content', async () => {
    render(<BasicTabs />);
    expect(screen.getByText('MovieListPage Mock Loaded')).toBeInTheDocument();
    const rankingsTab = screen.getByRole('tab', { name: 'Rankings (3)' });
    fireEvent.click(rankingsTab);
    expect(screen.getByText('RankingsPage Mock Loaded!')).toBeInTheDocument();
  });

  test('old content is hidden when switching tabs', async () => {
    render(<BasicTabs />);
    const loadedText = screen.getByText('MovieListPage Mock Loaded');
    expect(loadedText).toBeInTheDocument();
    const rankingsTab = screen.getByRole('tab', { name: 'Rankings (3)' });
    fireEvent.click(rankingsTab);
    expect(loadedText).not.toBeInTheDocument();
  });
});
