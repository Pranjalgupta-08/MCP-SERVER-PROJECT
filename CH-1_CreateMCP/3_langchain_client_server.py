from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

mcp_server_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "1_first_mcp_server.py")
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".venv")

async def main():
    # ✅ No async with — just instantiate and call directly
    client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": os.path.join(venv_path, "bin", "python3"),
                "args": [str(mcp_server_script)]
            }
        }
    )
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))

    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())