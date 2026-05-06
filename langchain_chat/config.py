"""
API密钥管理模块

用于安全存储和管理大模型API密钥，避免在代码中硬编码敏感信息。
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# 获取当前模块所在目录
_CURRENT_DIR = Path(__file__).parent

# 加载.env文件到环境变量
_env_file = _CURRENT_DIR / ".env"
load_dotenv(dotenv_path=_env_file)


def get_api_key(key_name: str) -> str:
    """
    获取指定名称的 API 密钥

    参数:
        key_name: 密钥的环境变量名称，如 "DEEPSEEK_API_KEY"

    返回:
        str: 对应的密钥值

    异常:
        ValueError: 当密钥不存在或未配置时抛出
    """
    api_key = os.getenv(key_name)
    print("api_key:"+api_key)

    if not api_key:
        raise ValueError(f"未找到API密钥: {key_name}，请在.env文件中配置")
    return api_key
# 便捷函数：获取DeepSeek API密钥
def get_deepseek_key() -> str:
    """获取DeepSeek API密钥"""
    return get_api_key("DEEPSEEK_API_KEY")


# 便捷函数：获取OpenAI API密钥
def get_openai_key() -> str:
    """获取OpenAI API密钥"""
    return get_api_key("OPENAI_API_KEY")
if __name__ == '__main__':
    get_deepseek_key()
