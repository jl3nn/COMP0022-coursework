
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
    let url = `${apiUrl}?prefix=${inputValue}`
    if (suffix) {
      url += `&${suffix}`;
    }
    fetch(url, { mode: 'cors' })
      .then((response) => response.json())
      .then((data) => {setFetchOptions(data)});
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
