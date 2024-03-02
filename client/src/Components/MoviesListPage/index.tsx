import React, { useEffect, useState, useRef } from "react";
import { useSearch } from "./SearchContext/context";
import { Button, Paper, Stack } from "@mui/material";
import SearchComponent from "./search";
import MovieCards from "../common/MovieCard";
import HourglassBottomIcon from "@mui/icons-material/HourglassBottom";

type Movie = {
  imageUrl: string;
  title: string;
  year: string;
  rating: number;
  movieId: string;
};

function MovieListPage() {
  const { searchText, ratings, tags, genres, date } = useSearch();
  const [data, setData] = useState<Movie[]>([]);
  const [loading, setLoading] = useState(true);
  const [allDataLoaded, setAllDataLoaded] = useState(false);
  const paperRef = useRef<HTMLDivElement>(null);
  const [scrollPosition, setScrollPosition] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(false);
      try {
        const response = await fetch(
          "http://localhost:5555/movies/get-search-results",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              searchText,
              ratings,
              tags,
              genres,
              date,
              numLoaded: 0,
            }),
            mode: "cors",
          }
        );

        if (!response.ok) {
          setData([]);
          console.log("Error fetching data at server");
          return;
        }

        const result = await response.json();
        setAllDataLoaded(result.all_loaded);
        setData(result.results);
      } catch (error: any) {
        setData([]);
        console.log("Server likely down", error);
      }
      setLoading(false);
    };
    fetchData();
  }, [searchText, ratings, tags, genres, date]);

  useEffect(() => {
    // After data changes, restore the scroll position
    if (paperRef.current) {
      const paperElement = paperRef.current;
      requestAnimationFrame(() => {
        paperElement.scrollTop = scrollPosition;
      });
    }
  }, [data, scrollPosition]);

  const loadMore = async () => {
    const currentScrollPosition = paperRef.current?.scrollTop || 0;
    setScrollPosition(currentScrollPosition);

    setLoading(true);
    try {
      const response = await fetch(
        "http://localhost:5555/movies/get-search-results",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            searchText,
            ratings,
            tags,
            genres,
            date,
            numLoaded: data.length,
          }),
          mode: "cors",
        }
      );

      if (!response.ok) {
        console.log("Error fetching data at server");
        return;
      }

      const result = await response.json();
      setAllDataLoaded(result.all_loaded);
      setData((prevData) => [...prevData, ...result.results]);
    } catch (error: any) {
      console.log("Server likely down", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Stack spacing={2} alignItems="center" margin={5}>
      <SearchComponent />
      <Paper
        ref={paperRef}
        sx={{ maxHeight: "calc(100vh - 250px)", overflow: "auto", width: 600 }}
      >
        {loading ? <div data-testid={'loading'}><HourglassBottomIcon /></div> : <MovieCards data={data} />}
        {!loading && !allDataLoaded && (
          <Button onClick={loadMore}>Load More</Button>
        )}
      </Paper>
    </Stack>
  );
}

export default MovieListPage;
