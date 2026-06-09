from mcp.server.fastmcp import FastMCP
from agent import agent_loop

# Create MCP Server
mcp = FastMCP("OutageCommsDrafter")

@mcp.tool()
def generate_outage_message(
    technical_text: str,
    tone: str = "empathetic",
    severity: str = None
) -> dict:
    """
    Generate 3 customer-facing outage messages from technical details.
    
    Args:
        technical_text: The technical description of the outage
        tone: Message tone - empathetic, calm, or concise
        severity: Severity level - low, medium, high (optional, auto-detected if not provided)
    
    Returns:
        Dictionary with initial, in_progress, and resolved messages
    """
    results, detected_severity = agent_loop(
        technical_text,
        tone,
        severity
    )
    
    return {
        "initial": results.get("initial", ""),
        "in_progress": results.get("in-progress", ""),
        "resolved": results.get("resolved", ""),
        "detected_severity": detected_severity,
        "tone_used": tone
    }

@mcp.tool()
def get_tone_options() -> dict:
    """
    Returns available tone options with descriptions.
    """
    return {
        "tones": [
            {
                "name": "empathetic",
                "description": "Warm and caring tone, shows understanding"
            },
            {
                "name": "calm",
                "description": "Professional and neutral tone"
            },
            {
                "name": "concise",
                "description": "Short and direct, minimal words"
            }
        ]
    }

@mcp.tool()
def get_severity_levels() -> dict:
    """
    Returns available severity levels with descriptions.
    """
    return {
        "levels": [
            {
                "name": "low",
                "description": "Minor issue, minimal customer impact"
            },
            {
                "name": "medium", 
                "description": "Moderate issue, some customers affected"
            },
            {
                "name": "high",
                "description": "Critical issue, all customers affected"
            }
        ]
    }

if __name__ == "__main__":
    print("Starting MCP Server...")
    print("Tools available:")
    print("  - generate_outage_message")
    print("  - get_tone_options")
    print("  - get_severity_levels")
    mcp.run(transport="stdio")
