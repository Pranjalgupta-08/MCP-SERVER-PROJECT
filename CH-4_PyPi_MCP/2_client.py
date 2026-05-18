from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os



async def main():
    # ✅ No async with — just instantiate and call directly
    client = MultiServerMCPClient(
        {
            "agentic_terminal_pranjal": {
                "transport": "stdio",
                "command": 'uvx',
                "args": ["agentic_terminal"]
            }
        }
    )

    tools = await client.get_tools()
    for tool in tools:
        print("Available tools:", tool.name)

    # fetch_tool=tools[0]
    # result=await fetch_tool.ainvoke({"query":"What is the capital of france?"})
    # print("Tool result:",result)

if __name__ == "__main__":
    asyncio.run(main())