from mcp.server.fastmcp import FastMCP
import datetime
import json
import os
import random

# instance the MCP server
mcp = FastMCP("SSE training OpenAI")

@mcp.tool()
def hello_world(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to MCP SSE Training."

@mcp.tool()
def get_current_time() -> str:
    """Returns the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def calculate_sum(a: float, b: float) -> float:
    """Calculates the sum of two numbers."""
    return a + b

@mcp.tool()
def generate_random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generates a random number between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

@mcp.tool()
def get_system_info() -> dict:
    """Returns basic system information."""
    return {
        "platform": os.name,
        "current_directory": os.getcwd(),
        "environment_variables_count": len(os.environ),
        "server_name": "MCP SSE Training Server"
    }

@mcp.tool()
def create_todo_item(title: str, description: str = "", priority: str = "medium") -> dict:
    """Creates a todo item with title, description and priority."""
    todo = {
        "id": random.randint(1000, 9999),
        "title": title,
        "description": description,
        "priority": priority,
        "created_at": datetime.datetime.now().isoformat(),
        "completed": False
    }
    return todo

@mcp.tool()
def format_json(data: str) -> str:
    """Formats a JSON string with proper indentation."""
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=2, ensure_ascii=False)
    except json.JSONDecodeError as e:
        return f"Error formatting JSON: {str(e)}"

@mcp.tool()
def word_count(text: str) -> dict:
    """Counts words, characters, and lines in the given text."""
    lines = text.split('\n')
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(' ', ''))
    
    return {
        "words": len(words),
        "characters": characters,
        "characters_no_spaces": characters_no_spaces,
        "lines": len(lines),
        "paragraphs": len([line for line in lines if line.strip()])
    }