import React from 'react';
import { render, screen } from '@testing-library/react';
import NewFilmReport from '.';
import { fireEvent } from '@testing-library/react';

jest.mock('./individual_estimate', () => () => <div>Mock Individual Estimate</div>);
jest.mock('./accuracy_estimate', () => () => <div>Mock Accuracy Estimate</div>);

test('renders with Individual Prediction tab selected by default', () => {
  render(<NewFilmReport />);
  expect(screen.getByText('Mock Individual Estimate')).toBeInTheDocument();
  expect(screen.queryByText('Mock Accuracy Estimate')).toBeNull();
});

test('switches to Accuracy Estimate tab when clicked', async () => {
  render(<NewFilmReport />);
  const accuracyTab = screen.getByRole('tab', { name: 'Accuracy Estimate' });
  fireEvent.click(accuracyTab);

  expect(screen.getByText('Mock Accuracy Estimate')).toBeInTheDocument();
  expect(screen.queryByText('Mock Individual Estimate')).toBeNull();
});
