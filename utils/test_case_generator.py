from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import config

template = """Question: {question}

Answer: Let's think step by step."""


def generate_test_cases(selected_llm, template):
    """
    Generate test cases using the specified LLM model.
    
    Arguments:
        - selected_llm: text of model name to use for generating test cases
        - template: text of prompt to use for generating test cases
    
    Returns:
        - text of generated test cases
    """

    model = OllamaLLM(model=selected_llm)

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    test_cases = chain.invoke({"question": "What is LangChain?"})

    return test_cases
