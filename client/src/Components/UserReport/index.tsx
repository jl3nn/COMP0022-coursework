import React, { useEffect, useState } from 'react';
import { Paper, Stack, Typography } from '@mui/material';

function UserReportPage() {
    return (
        <Stack spacing={2} alignItems="center" margin={5}>
                <Paper sx={{maxHeight: 'calc(100vh - 200px)', overflow:"auto",  width:600}}>
                    <Typography variant="h4" sx={{'marginX': 'auto'}}>User Report</Typography>
                </Paper>
        </Stack>
    );
}

export default UserReportPage;