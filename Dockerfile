# Use Python 3.12 base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy your MCP server code
COPY . /app

# Install dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install mcp fastmcp

# Use the venv python as default
ENV PATH="/opt/venv/bin:$PATH"

# Expose MCP port
EXPOSE 8081

# Run the MCP server
CMD ["python3", "server.py"]
