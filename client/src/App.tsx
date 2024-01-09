import React from 'react';
import MovieListPage from './Components/MoviesListPage';
import { SearchProvider } from './Components/MoviesListPage/SearchContext/context';

function App() {
  return (
    <div>
      <SearchProvider>
        <MovieListPage />
      </SearchProvider>
    </div>
  );
}

export default App;
