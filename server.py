from mcp.server.fastmcp import FastMCP
import uvicorn

app = FastMCP("simple-mcp")

@app.tool()
def echo(message: str) -> str:
    return f"You said: {message}"

@app.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    uvicorn.run(app.streamable_http_app, host="0.0.0.0", port=8081)
