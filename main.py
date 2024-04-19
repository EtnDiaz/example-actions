import os

def generate_index_html(prometheus_endpoint_url):
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Status Page</title>
</head>
<body>
    <h1>Service Status Page</h1>
    <div id="status-container">
        <!-- Here we will dynamically populate service statuses -->
    </div>

    <script src="index.js"></script>
</body>
</html>"""
    return content

def generate_index_js(prometheus_endpoint_url):
    content = f"""const fetchServiceStatuses = async () => {{
    try {{
        const response = await fetch('{prometheus_endpoint_url}');
        const data = await response.json();

        const statusContainer = document.getElementById('status-container');
        statusContainer.innerHTML = ''; // Clear previous statuses

        for (const [service, status] of Object.entries(data)) {{
            const statusElement = document.createElement('div');
            statusElement.textContent = `${{service}}: ${{status}}`;
            statusContainer.appendChild(statusElement);
        }}
    }} catch (error) {{
        console.error('Error fetching service statuses:', error);
    }}
}};

// Fetch and update statuses every 10 seconds
setInterval(fetchServiceStatuses, 10000);

// Initial fetch and update
fetchServiceStatuses();"""
    return content

def generate_dockerfile():
    content = """FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD [ "node", "index.js" ]"""
    return content

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    prometheus_endpoint_url = input("Enter Prometheus endpoint URL: ")
    output_directory = input("Enter output directory path (default: '.'): ") or '.'

    create_directory(output_directory)

    index_html_content = generate_index_html(prometheus_endpoint_url)
    write_to_file(os.path.join(output_directory, 'index.html'), index_html_content)

    index_js_content = generate_index_js(prometheus_endpoint_url)
    write_to_file(os.path.join(output_directory, 'index.js'), index_js_content)

    dockerfile_content = generate_dockerfile()
    write_to_file(os.path.join(output_directory, 'Dockerfile'), dockerfile_content)

    print("Files generated successfully!")

if __name__ == "__main__":
    main()
