import { Box, Tab, Tabs } from "@mui/material";
import React, { useState } from "react";
import IndividualEstimate from "./individual_estimate";
import AccuracyEstimate from "./accuracy_estimate";

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
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

const NewFilmReport = () => {
  const [value, setValue] = useState(0);

  function handleChange(event: React.SyntheticEvent, newValue: number) {
    setValue(newValue);
  }

  return (
    <Box>
      <Tabs
        value={value}
        onChange={handleChange}
        aria-label="simple tabs example"
      >
        <Tab label="Individual Prediction" {...a11yProps(0)} />
        <Tab label="Accuracy Estimate" {...a11yProps(1)} />
      </Tabs>

      <CustomTabPanel value={value} index={0}>
        <IndividualEstimate />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <AccuracyEstimate />
      </CustomTabPanel>
    </Box>
  );
};

export default NewFilmReport;
