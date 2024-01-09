import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography } from '@mui/material';

function RankingsPage() {
    return (
        <Stack spacing={2} alignItems="center" margin={5}>
                <Paper sx={{maxHeight: 'calc(100vh - 200px)', overflow:"auto",  width:600}}>
                    <Typography variant="h4" sx={{'marginX': 'auto'}}>Rankings Page</Typography>
                </Paper>
        </Stack>
    );
}

export default RankingsPage;