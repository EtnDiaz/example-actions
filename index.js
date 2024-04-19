const express = require('express');
const fetch = require('node-fetch');

const app = express();
const PORT = process.env.PORT || 3000;
const PROMETHEUS_ENDPOINT_URL = 'YOUR_PROMETHEUS_ENDPOINT_URL';

// Function to fetch service statuses from Prometheus endpoint
async function fetchServiceStatuses() {
    try {
        const response = await fetch(PROMETHEUS_ENDPOINT_URL);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching service statuses:', error);
        return {};
    }
}

// Route to get service statuses
app.get('/status', async (req, res) => {
    const serviceStatuses = await fetchServiceStatuses();
    res.json(serviceStatuses);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
