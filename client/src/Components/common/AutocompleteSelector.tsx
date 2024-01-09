
import React, { useState, useEffect } from 'react';
import { Autocomplete, TextField } from '@mui/material';

type CompleteWithFetchProps = {
    apiUrl: string;
    onChange: (event: React.ChangeEvent<{}>, value: string[]) => void;
    label: string;
};

const AutocompleteWithFetch = ({ apiUrl, onChange, label } : CompleteWithFetchProps) => {
  const [fetchOptions, setFetchOptions] = useState([] as string[]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    fetch(`${apiUrl}?prefix=${inputValue}`, { mode: 'cors' })
      .then((response) => response.json())
      .then((data) => setFetchOptions(data));
  }, [apiUrl, inputValue]);

  return (
    <Autocomplete
      multiple
      options={fetchOptions}
      inputValue={inputValue}
      onInputChange={(_, val) => setInputValue(val)}
      onChange={onChange}
      renderInput={(params) => <TextField {...params} label={label} />}
    />
  );
};

export default AutocompleteWithFetch;
