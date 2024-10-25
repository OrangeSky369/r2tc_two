import gradio as gr
from utils.test_case_generator import generate_test_cases

def build_interface(llm):
    """
    构建Gradio用户界面。
    """
    # 定义输入组件
    requirements_input = gr.Textbox(
        label="需求文本",
        lines=5,
        placeholder="请输入您的需求文本..."
    )
    
    methods_checkbox = gr.CheckboxGroup(
        label="选择生成测试用例的方法",
        choices=["等价类划分", "边界值分析", "决策表测试"],
        value=["等价类划分"]  # 默认选中
    )
    
    creativity_slider = gr.Slider(
        label="生成用例的创造性",
        minimum=0,
        maximum=100,
        step=1,
        value=50,
        info="0: 严格遵循需求文本，100: 高度发挥想象"
    )
    
    generate_button = gr.Button("生成测试用例")
    
    output_box = gr.Textbox(
        label="生成的测试用例",
        lines=10,
        readonly=True
    )
    
    # 定义界面布局
    with gr.Blocks() as interface:
        gr.Markdown("# 测试用例生成器")
        with gr.Row():
            with gr.Column():
                requirements_input
                methods_checkbox
                creativity_slider
                generate_button
            with gr.Column():
                output_box
        
        # 定义按钮点击事件
        generate_button.click(
            fn=lambda req, methods, creativity: generate_test_cases(llm, req, methods, creativity),
            inputs=[requirements_input, methods_checkbox, creativity_slider],
            outputs=output_box
        )
    
    return interface
