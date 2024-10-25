from llm.prompts import get_final_prompt

def main():
    user_input_req = "这是一个示例需求"
    selected_methods = ["等价类划分"]
    final_prompt = get_final_prompt(user_input_req, selected_methods, "llm/few_shots.json", 29)
    print(final_prompt)

if __name__ == "__main__":
    main()
