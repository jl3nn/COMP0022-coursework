// SearchContext.tsx
import React, { createContext, useState, useContext, ReactNode } from 'react';

interface SearchContextProps {
  searchText: string;
  ratings: [number, number];
  tags: string[];
  genres: string[];
  setSearchFilter: (text: string) => void;
  setRatingFilter: (value: [number, number]) => void;
  setTagsFilter: (selectedTags: string[]) => void;
  setGenresFilter: (selectedGenres: string[]) => void;
  resetFilters: () => void;
}

const SearchContext = createContext<SearchContextProps | undefined>(undefined);

interface SearchProviderProps {
  children: ReactNode;
}

export const SearchProvider: React.FC<SearchProviderProps> = ({ children }) => {
  const [searchText, setSearchText] = useState<string>('');
  const [ratings, setRating] = useState<[number, number]>([0, 10]);
  const [tags, setTags] = useState<string[]>([]);
  const [genres, setGenres] = useState<string[]>([]);

  const setSearchFilter = (text: string) => {
    setSearchText(text);
  };

  const setRatingFilter = (value: [number, number]) => {
    setRating(value);
  };

  const setTagsFilter = (selectedTags: string[]) => {
    setTags(selectedTags);
  };

  const setGenresFilter = (selectedGenres: string[]) => {
    setGenres(selectedGenres);
  };

  const resetFilters = () => {
    setSearchText('');
    setRating([0, 10]);
    setTags([]);
    setGenres([]);
  };

  const contextValue: SearchContextProps = {
    searchText,
    ratings,
    tags,
    genres,
    setSearchFilter,
    setRatingFilter,
    setTagsFilter,
    setGenresFilter,
    resetFilters,
  };

  return <SearchContext.Provider value={contextValue}>{children}</SearchContext.Provider>;
};

export const useSearch = (): SearchContextProps => {
  const context = useContext(SearchContext);
  if (!context) {
    throw new Error('useSearch must be used within a SearchProvider');
  }
  return context;
};
