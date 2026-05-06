import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI


async def run_agent():
    # 构建阿里云百炼大模型客户端（新版方式）
    llm = ChatOpenAI(
        model="qwen-plus",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
    )

    # 配置 MCP 服务
    client = MultiServerMCPClient({
        "amap": {
            "url": f"https://mcp.amap.com/sse?key={os.getenv('A_MCP_API_KEY')}",
            "transport": "sse",
            "timeout": 60,
        },
    })

    tools = await client.get_tools()

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "帮我规划一条从长沙梅溪湖到溁湾镇的自驾路线"}]
    })

    print(response)


if __name__ == "__main__":
    asyncio.run(run_agent())