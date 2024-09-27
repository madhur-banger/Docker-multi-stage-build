async function fetchMetrics() {
    try {
        const response = await fetch('/api/metrics');
        const data = await response.json();

        document.getElementById('cpu-usage').textContent = data.cpu_usage;
        document.getElementById('memory-usage').textContent = data.memory_usage;
    } catch (error) {
        console.error('Error fetching metrics:', error);
    }
}

setInterval(fetchMetrics, 5000); // Fetch metrics every 5 seconds
fetchMetrics();

