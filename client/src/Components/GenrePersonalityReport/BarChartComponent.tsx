import React, { useState } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import {
  Paper,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from "@mui/material";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

type FullDataType = {
  [personality: string]: DataType;
};

type DataType = {
  x: string[];
  y: number[];
};

type BarChartComponentProps = {
  data: FullDataType;
};

const BarChartComponent: React.FC<BarChartComponentProps> = ({ data }) => {
  const [selectedPersonality, setSelectedPersonality] = useState(
    Object.keys(data)[0]
  );

  const handleChange = (event: React.ChangeEvent<{ value: unknown }>) => {
    setSelectedPersonality(event.target.value as string);
  };

  const chartData = {
    labels: data[selectedPersonality].x,
    datasets: [
      {
        label: `Pearson Coefficient of Genre and ${selectedPersonality}`,
        data: data[selectedPersonality].y,
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: "Pearson Coefficient",
        },
        ticks: {
          callback: function (value: any, index: any, values: any) {
            return value.toLocaleString(undefined, {
              minimumFractionDigits: 2,
              maximumFractionDigits: 2,
            });
          },
        },
      },
      x: {
        title: {
          display: true,
          text: "Genre",
        },
        ticks: {
          autoSkip: false, // Optional: Prevents the automatic skipping of labels to improve readability
        },
      },
    },
  };

  return (
    <Paper
      elevation={3}
      style={{
        padding: "20px",
        marginBottom: "20px",
        width: "100%",
        height: "auto",
      }}
    >
      <FormControl fullWidth>
        <InputLabel id="personality-select-label">Personality Type</InputLabel>
        <Select
          labelId="personality-select-label"
          id="personality-select"
          value={selectedPersonality}
          label="Personality Type"
          onChange={handleChange as any}
        >
          {Object.keys(data).map((personality) => (
            <MenuItem key={personality} value={personality}>
              {personality}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Bar data={chartData} options={chartOptions} />
    </Paper>
  );
};

export default BarChartComponent;
