from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
import uvicorn

app = FastMCP("simple-mcp")

@app.tool()
def echo(message: str):
return [TextContent(type="text", text=f"You said: {message}")]

@app.tool()
def add(a: int, b: int):
result = a + b
return [TextContent(type="text", text=str(result))]

@app.tool()
def multiply(a: int, b: int):
result = a * b
return [TextContent(type="text", text=str(result))]

if **name** == "**main**":
uvicorn.run(app.streamable_http_app, host="0.0.0.0", port=8081)
