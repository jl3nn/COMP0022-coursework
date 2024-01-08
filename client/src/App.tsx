import React, { useState, useEffect } from 'react';

interface Rating {
  userId: number;
  movieId: number;
  rating: number;
  timestamp: number;
}

interface Tag {
  userId: number;
  movieId: number;
  tag: string;
  timestamp: number;
}

interface Movie {
  movieId: number;
  title: string;
  genres: string;
}

interface Link {
  movieId: number;
  imdbId: string;
  tmdbId: number;
}

function App() {
  const [ratings, setRatings] = useState<Rating[]>([]);
  const [tags, setTags] = useState<Tag[]>([]);
  const [movies, setMovies] = useState<Movie[]>([]);
  const [links, setLinks] = useState<Link[]>([]);

  useEffect(() => {
    // Fetch data from Flask endpoints when the component mounts
    const fetchData = async () => {
      const ratingsResponse = await fetch('http://localhost:5000/ratings');
      const tagsResponse = await fetch('http://localhost:5000/tags');
      const moviesResponse = await fetch('http://localhost:5000/movies');
      const linksResponse = await fetch('http://localhost:5000/links');

      const ratingsData: Rating[] = await ratingsResponse.json();
      const tagsData: Tag[] = await tagsResponse.json();
      const moviesData: Movie[] = await moviesResponse.json();
      const linksData: Link[] = await linksResponse.json();

      setRatings(ratingsData);
      setTags(tagsData);
      setMovies(moviesData);
      setLinks(linksData);
    };

    fetchData();
  }, []);

  const renderTable = (data: any[], headers: string[]) => (
    <table>
      <thead>
        <tr>
          {headers.map(header => (
            <th key={header}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            {headers.map(header => (
              <td key={header}>{row[header]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );

  return (
    <div>
      <h1>Ratings</h1>
      {renderTable(ratings, ['userId', 'movieId', 'rating', 'timestamp'])}

      <h1>Tags</h1>
      {renderTable(tags, ['userId', 'movieId', 'tag', 'timestamp'])}

      <h1>Movies</h1>
      {renderTable(movies, ['movieId', 'title', 'genres'])}

      <h1>Links</h1>
      {renderTable(links, ['movieId', 'imdbId', 'tmdbId'])}
    </div>
  );
}

export default App;
