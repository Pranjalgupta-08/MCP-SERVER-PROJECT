from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

value = os.getenv("TAVLIY_API_KEY")

async def main():
    # ✅ No async with — just instantiate and call directly
    client = MultiServerMCPClient(
        {
            "tavily-remote-mcp": 
            {
                "transport": "http",
                "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={value}"
            }
        }
        
    )

    tools = await client.get_tools()
    for tool in tools:
        print("Available tools:", tool.name)
        # if tool.name=='tavily_search':
        #     result=await tool.name.({"query":"What is the capital of france?"})

    tool_search=[tool for tool in tools if tool.name=='tavily_search'][0]

    result=await tool_search.ainvoke({"query":"What is the capital of france?"})
    print("Tool result:",result)

if __name__ == "__main__":
    asyncio.run(main())