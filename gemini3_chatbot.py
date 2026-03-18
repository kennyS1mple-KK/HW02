import google.generativeai as genai
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
import time
# 初始化美化控制台（提升Chatbot交互体验）
console = Console()

def configure_gemini_api():
    load_dotenv()  # 加载.env文件中的环境变量
    api_key = os.getenv("AIzaSyDRU45sLIFMWjC3KmFZDDMToqEL_npO_jg") or Prompt.ask("请输入你的Gemini 3 API Key")
    
    # 配置API
    genai.configure(api_key=api_key)
    console.print("[green]✅ Gemini 3 API配置成功！[/green]")
    return api_key

def init_gemini_chatbot():
    generation_config 
= {
        "temperature": 0.3,  # 保证学术分析精准
        "top_p": 0.95,
        "max_output_tokens": 8192,  # 容纳长文本分析
        "response_mime_type": "text/markdown",  # Markdown格式
    }

    # 初始化Gemini 3 flash模型
    model = genai.GenerativeModel(
        model_name="gemini-3-flash",  
        generation_config=generation_config,
        system_instruction=
    """
    你是一名资深分析师，擅长以Markdown格式分析大模型相关论文。
    分析需包含4部分：研究背景与动机、核心方法与创新点、主要实验结果与结论、个人小结与思考
"""
    )

    # 启动Chatbot多轮对话模式（保留上下文）
    chat = model.start_chat(history=[])
    console.print("[blue]💬 Gemini 3 Chatbot已初始化完成，支持多轮对话！[/blue]")
    return chat
def run_gemini_chatbot(chat):
    """运行Chatbot交互逻辑，处理用户输入并生成分析结果"""
    console.print("\n[yellow]📌 输入提示：[/yellow]")
    console.print("  - 输入论文相关内容，Chatbot会自动生成结构化分析；")
    console.print("  - 输入「保存」可将结果写入MD文件；")
    console.print("  - 输入「退出」结束对话。\n")
    default_paper_info = 
"""
论文标题：大模型的框架构建与应用
核心内容：
1. 研究背景：ChatGPT/GPT-4/Med-PaLM潜力大，但算力高、标准化缺失、数据安全问题突出；
2. 核心方法：HAI框架，知识分解原子化模型、网络原生AI、区块链安全体系；
3. 实验结论：理论验证有效，需实证补充；。
"""

    while True:
        user_input = Prompt.ask("[cyan]请输入你的需求/论文内容[/cyan]", default=default_paper_info)
        
        # 退出逻辑
        if user_input.lower() == "退出":
            console.print("[red]👋 对话结束！[/red]")
            break
        
        # 保存结果逻辑
        if user_input.lower() == "保存":
            if not hasattr(run_gemini_chatbot, "last_response"):
                console.print("[red]❌ 暂无可保存的分析结果，请先生成分析！[/red]")
                continue
            # 写入MD文件
            with open("论文分析_Generated_by_Gemini3.md", "w", encoding="utf-8") as f:
                f.write(run_gemini_chatbot.last_response)
            console.print("[green]✅ 分析结果已保存至：论文分析_Generated_by_Gemini3.md[/green]")
            continue
        
        try:
            console.print("[yellow]⏳ Gemini 3正在生成分析结果...[/yellow]")
            response = chat.send_message(user_input)
            run_gemini_chatbot.last_response = response.text  # 缓存最后一次结果
            
            console.print("\n[magenta]=== Gemini 3 生成的论文分析结果 ===[/magenta]\n")
            console.print(response.text)
            console.print("\n" + "-"*80 + "\n")
        
        except Exception as e:
            console.print(f"[red]❌ 生成失败：{str(e)}[/red]")
            time.sleep(1)
            continue

if __name__ == "__main__":
    console.print("[bold purple]🚀 启动Gemini 3 论文分析Chatbot[/bold purple]\n")
    
    configure_gemini_api()
    
    chatbot = init_gemini_chatbot()
    
    run_gemini_chatbot(chatbot)
