from mcp.server import FastMCP

# instance the MCP server
mcp = FastMCP("SSE training OpenAI")

@mcp.prompt("Prompt MCP")
def prompt_mcp(input_text: str) -> str:
    """Echoes the input text."""
    return f"You said: {input_text}"