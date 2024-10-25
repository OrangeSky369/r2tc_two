import json


def get_methods_prompt(selected_methods):
    """
    Create a prompt for generation methods.
    :param selected_methods: list of selected methods for generating test cases
    :return: text of the prompt
    """

    methods_prompt = "、".join(selected_methods)

    return methods_prompt


def get_creativity_level_prompt(creativity_level):
    """
    Create a prompt for creativity level.
    :param creativity_level:integer indicating the creativity level
    :return: text of the prompt
    """

    if creativity_level < 30:
        creativity_instruction = "严格遵循需求文本。"
    elif creativity_level < 70:
        creativity_instruction = "在遵循需求文本的基础上适当发挥。"
    else:
        creativity_instruction = "高度发挥想象，较少受需求文本限制。"

    return creativity_instruction


def load_few_shots(filepath):
    """
    Load few shots from a JSON file.
    :param filepath: path to the JSON file
    :return: few shots in dictionary format
    """

    with open(filepath, "r", encoding="utf-8") as f:
        dict_few_shots = json.load(f)

    return dict_few_shots


def get_few_shots_prompt(selected_methods, dict_few_shots):
    """
    :param selected_methods: list of selected_methods
    :param dict_few_shots:
    :return: text of few shots prompt for all the generation methods
    """

    few_shots_prompt = ""

    for method in selected_methods:
        if method in dict_few_shots:
            few_shots_prompt += f"{method}方法：\n"
            examples = dict_few_shots[method]
            for example in examples:
                few_shots_prompt += f"需求：\n{example['example_name']}\n"
                few_shots_prompt += f"测试用例：\n{example['example_description']}\n\n"

    return few_shots_prompt


def get_final_prompt(requirements, selected_methods, few_shots_json_filepath, creativity_level):
    """
    Create a prompt for generating test cases, combining with different input parameters.

    Arguments:
        - requirements: text of input requirements to generate test cases
        - methods_prompt: text of methods name to generate test cases
        - few_shots_prompt: text of the examples of each generation method
        - creativity_level_prompt: text of description indicating the creativity level

    Returns:
        - text of the final prompt
    """

    # get each part of the prompt
    methods_prompt = get_methods_prompt(selected_methods)
    dict_few_shots = load_few_shots(few_shots_json_filepath)
    few_shots_prompt = get_few_shots_prompt(selected_methods, dict_few_shots)
    creativity_level_prompt = get_creativity_level_prompt(creativity_level)

    final_prompt = f"""
根据以下需求生成测试用例：
{requirements}

使用以下方法：{methods_prompt}生成测试用例。

举例说明：
{few_shots_prompt}

生成用例的创造性程度：{creativity_level_prompt}
"""

    return final_prompt


