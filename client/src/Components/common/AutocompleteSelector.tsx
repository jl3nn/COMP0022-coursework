
import React, { useState, useEffect } from 'react';
import { Autocomplete, TextField } from '@mui/material';

type CompleteWithFetchProps = {
    apiUrl: string;
    onChange: any;
    value: any;
    label: string;
    multiple?: boolean;
    disabled?: boolean;
    suffix?: string;
};

const AutocompleteWithFetch = ({ apiUrl, disabled, onChange, label, value, multiple, suffix } : CompleteWithFetchProps) => {
  const [fetchOptions, setFetchOptions] = useState([] as string[]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    async function fetchData() {
      let url = `${apiUrl}?prefix=${inputValue}`
    if (suffix) {
      url += `&${suffix}`;
    }
    const response = await fetch(url, { mode: 'cors' })
    const data = await response.json()
    setFetchOptions(data)
    }
    fetchData();
  }, [apiUrl, inputValue, suffix]);

  return (
    <Autocomplete
        disabled={disabled}
        fullWidth
        multiple={multiple}
        options={fetchOptions}
        inputValue={inputValue}
        value={value}
        onInputChange={(_, val) => setInputValue(val)}
        onChange={onChange}
        renderInput={(params) => <TextField {...params} label={label} />}
    />
  );
};

export default AutocompleteWithFetch;
