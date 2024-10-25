from langchain import LLMChain, PromptTemplate
from langchain_ollama.llms import OllamaLLM


def initialize_llm(model_name):
    """
    初始化本地部署的Ollama大语言模型，并配置Langchain的LLMChain。
    """
    # 初始化Ollama模型
    model = OllamaLLM(model=model_name)

    # 定义提示模板
    prompt = "你好"

    # 创建Langchain的LLMChain
    llm_chain = LLMChain(prompt=prompt, llm=model)

    return llm_chain
