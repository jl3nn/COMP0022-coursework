import React, { useContext, useEffect, useState } from 'react';
import { Paper, InputAdornment, Slider, IconButton, TextField, Stack, Button, Typography, Box } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import FilterIcon from '@mui/icons-material/FilterList';
import Autocomplete from '@mui/material/Autocomplete';
import Drawer from '@mui/material/Drawer';
import { useSearch } from '../SearchContext/context';
import AutocompleteWithFetch from '../../common/AutocompleteSelector';

const SearchComponent = () => {
  const [data, setData] = useState([] as string[]);
  const [searchVal, setSearchVal] = useState('' as string);
  const [isFilterDrawerOpen, setFilterDrawerOpen] = useState(false);

  const handleFilterIconClick = () => {
    setFilterDrawerOpen(true);
  };

  const handleFilterDrawerClose = () => {
    setFilterDrawerOpen(false);
  };


  async function onSearchChange(s: string) {
    setSearchVal(s);
    if (s === '') {
      setData([]);
      return;
    }
    setData(['A', 'B', 'C']);
  }

  return (
    <Paper
      component="form"
      sx={{
        display: 'flex',
        alignItems: 'center',
        borderRadius: 'borderRadius',
        boxShadow: 1,
        width: 600, // Set the width to 600px
        margin: 'auto', // Center the search bar
      }}
    >
      <Autocomplete
        fullWidth
        freeSolo
        options={data}
        inputValue={searchVal}
        onInputChange={(e, newValue) => onSearchChange(newValue)}
        renderInput={(params) => (
          <TextField
            placeholder="Search"
            {...params}
            sx={{ flex: 1 }}
            InputProps={{
              ...params.InputProps,
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton size="small" onClick={() => handleFilterIconClick()}>
                    <FilterIcon />
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
        )}
      />
      <SearchDrawer isFilterDrawerOpen={isFilterDrawerOpen} handleFilterDrawerClose={handleFilterDrawerClose} />
    </Paper>
  );
};

const SearchDrawer = ({ isFilterDrawerOpen, handleFilterDrawerClose }: any) => {
  const { ratings, tags, genres, date, setRatingFilter, setDateFilter, setTagsFilter, setGenresFilter, resetFilters } = useSearch();

  return (
    <Drawer anchor="right" open={isFilterDrawerOpen} onClose={handleFilterDrawerClose}>
      <Box margin={3}>
        <Typography variant="h4" sx={{ 'marginX': 'auto' }}>Search Filters</Typography>
        <Stack spacing={4} sx={{ p: 2, width: 250 }}>
          <Box>
            <Typography>Rating:</Typography>
            <Slider
              value={ratings}
              onChange={(_, val) => setRatingFilter(val as [number, number])}
              valueLabelDisplay="auto"
              min={0}
              max={5}
              step={0.5}
              marks={[{ value: 0, label: '0' }, { value: 10, label: '10' }]}
            />
          </Box>
          <AutocompleteWithFetch value={genres} label="Genres" multiple apiUrl="http://localhost:5555/autocomplete/genre" onChange={(_: any, newValue: any) => setGenresFilter(newValue)} />
          <AutocompleteWithFetch value={tags} label="Tags" multiple apiUrl="http://localhost:5555/autocomplete/tag" onChange={(_: any, newValue: any) => setTagsFilter(newValue)} />
          <Slider
              value={date}
              onChange={(_, val) => setDateFilter(val as [number, number])}
              valueLabelDisplay="auto"
              min={1902}
              max={2018}
              step={1}
              marks={[{ value: 1902, label: '1902' }, { value: 2018, label: '2018' }]}
            />
        </Stack>
        <Button onClick={resetFilters}>Reset Filters</Button>
      </Box>
    </Drawer>
  );
}

export default SearchComponent;
