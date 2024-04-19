const fetchServiceStatuses = async () => {
    try {
        const response = await fetch('https://roonee.uk/mon');
        const data = await response.json();

        const statusContainer = document.getElementById('status-container');
        statusContainer.innerHTML = ''; // Clear previous statuses

        for (const [service, status] of Object.entries(data)) {
            const statusElement = document.createElement('div');
            statusElement.textContent = `${service}: ${status}`;
            statusContainer.appendChild(statusElement);
        }
    } catch (error) {
        console.error('Error fetching service statuses:', error);
    }
};

// Fetch and update statuses every 10 seconds
setInterval(fetchServiceStatuses, 10000);

// Initial fetch and update
fetchServiceStatuses();