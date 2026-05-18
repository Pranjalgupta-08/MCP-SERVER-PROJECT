from fastmcp import FastMCP

mcp=FastMCP()

# Mount the tools to the MCP instance
mcp.mount(
    FastMCP.as_proxy({
        "mcpServers" : {
            "ddg_mcp": {"command":"uvx", "args": ["duckduckgo-mcp-server"]}        }
    }
    )
)

mcp.mount(
    FastMCP.as_proxy({
        "mcpServers" : {
            "agentic_terminal": {"command":"uvx", "args": ["agentic_terminal"]}        }
    }
    )
)

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)