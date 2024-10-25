
# 调用LLM生成测试用例
try:
    test_cases = llm.run(prompt_inputs)
    print(test_cases)
except Exception as e:
    test_cases = f"生成测试用例时发生错误：{str(e)}"

return test_cases
