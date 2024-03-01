import { cleanup, render, fireEvent, screen, waitFor } from '@testing-library/react';
import BarChartComponent from './BarChartComponent';

afterEach(cleanup);

interface BarChartProps {
    data: any;
}

jest.mock('react-chartjs-2', () => ({
    Bar: ({data}: BarChartProps) => <p>{data.labels}</p>
}));

test('renders with initial data', () => {
    const data = {
      "Extrovert": { x: ["Genre1", "Genre2"], y: [0.5, 0.8] },
      "Introvert": { x: ["Genre3", "Genre4"], y: [0.2, 0.4] }
    };
  
    render(<BarChartComponent data={data} />);
  
    expect(screen.getByLabelText('Personality Type')).toBeInTheDocument();
});

test('displays extrovert by default', () => {
    const data = {
        "Extrovert": { x: ["Genre1", "Genre2"], y: [0.5, 0.8] },
        "Introvert": { x: ["Genre3", "Genre4"], y: [0.2, 0.4] }
      };
    
      render(<BarChartComponent data={data} />);
    
      expect(screen.getByText(/Genre1/i)).toBeInTheDocument();
})
  
test('updates on select change', async () => {
    const data = {
      "Extrovert": { x: ["Genre1", "Genre2"], y: [0.5, 0.8] },
      "Introvert": { x: ["Genre3", "Genre4"], y: [0.2, 0.4] }
    };
  
    render(<BarChartComponent data={data} />);

    const select = screen.getByRole('combobox', { name: 'Personality Type' });
    fireEvent.mouseDown(select);

    const introvertOption = await screen.findByText('Introvert'); // Use findByText for async operations
    fireEvent.click(introvertOption);
  
    await waitFor(() => {
        expect(screen.queryAllByText(/Genre1/i)).toHaveLength(0);
        expect(screen.getByText(/Genre3/i)).toBeInTheDocument();
    });
});
  