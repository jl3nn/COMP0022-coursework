import React from 'react';
import { Box, Tab, Tabs } from '@mui/material';
import MovieListPage from '../MoviesListPage';
import RankingsPage from '../RankingsPage';
import UserReportPage from '../UserReport';
import NewFilmPage from '../NewFilmReport';
import GenrePersonalityPage from '../GenrePersonalityReport';
import { SearchProvider } from '../MoviesListPage/SearchContext/context';

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function CustomTabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
            {children}
        </Box>
      )}
    </div>
  );
}

export default function BasicTabs() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Tabs value={value} onChange={handleChange} aria-label="basic tabs example" centered>
            <Tab label="Movie Overview (1, 2)" />
            <Tab label="Rankings (3)" />
            <Tab label="User Report (4)" />
            <Tab label="New Film Report (5)" />
            <Tab label="Genre Personality Report (6)" />
            </Tabs>
        </Box>
        <CustomTabPanel value={value} index={0}>
            <SearchProvider>
                <MovieListPage />
            </SearchProvider>
        </CustomTabPanel>
        <CustomTabPanel value={value} index={1}>
            <RankingsPage />
        </CustomTabPanel>
        <CustomTabPanel value={value} index={2}>
            <UserReportPage />
        </CustomTabPanel>
        <CustomTabPanel value={value} index={3}>
            <NewFilmPage />
        </CustomTabPanel>
        <CustomTabPanel value={value} index={4}>
            <GenrePersonalityPage />
        </CustomTabPanel>
    </Box>
  );
}
