import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("未找到环境变量 DEEPSEEK_API_KEY，请确保已设置该环境变量")
os.environ["DEEPSEEK_API_KEY"] = api_key

# 初始化模型
chat = ChatDeepSeek(model="deepseek-chat", temperature=0.7)


def main():
    print("=" * 50)
    print("LangChain + DeepSeek 聊天")
    print("输入内容进行对话，输入 exit 退出")
    print("=" * 50)
    print()

    messages = []

    while True:
        user_input = input("你: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "退出"):
            print("再见！")
            break

        messages.append(HumanMessage(content=user_input))
        messages.append(SystemMessage(content="回答要言简意赅"))
        print("现在的message:",messages)

        response = chat.invoke(messages)
        print(f"AI: {response.content}")
        print()

        messages.append(response)

def test():
    # 他们之间是相互兼容的
    chat_ds=ChatOpenAI(
        model="deepseek-chat",
        temperature=0.7,
        base_url="https://api.deepseek.com",
        api_key=api_key
    )
    response = chat_ds.invoke("你是谁")
    print(f"AI: {response.content}")
if __name__ == "__main__":
    test()
