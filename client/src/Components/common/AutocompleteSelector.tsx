
import React, { useState, useEffect } from 'react';
import { Autocomplete, TextField } from '@mui/material';

type CompleteWithFetchProps = {
    apiUrl: string;
    onChange: any;
    value: any;
    label: string;
    multiple?: boolean;
    disabled?: boolean;
};

const AutocompleteWithFetch = ({ apiUrl, disabled, onChange, label, value, multiple } : CompleteWithFetchProps) => {
  const [fetchOptions, setFetchOptions] = useState([] as string[]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    fetch(`${apiUrl}?prefix=${inputValue}`, { mode: 'cors' })
      .then((response) => response.json())
      .then((data) => setFetchOptions(data));
  }, [apiUrl, inputValue]);

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
