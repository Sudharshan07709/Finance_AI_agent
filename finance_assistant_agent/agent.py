from google.adk.agents import LlmAgent
from typing import Dict
from google.adk.tools.agent_tool import AgentTool
from investment_agent_analyst.agent import investment_plan_agent
def get_user_personal_details() -> Dict:
    """
    Gets users personal finance details like salary, expense and savings capacity.

    """
    return {
        "salary": 50000,
        "expense":{
            "EMI_Expense": 25000,
            "Essentials": 5000,
            "Entertainment": 5000,
            "Shopping and travel": 5000
        },
        "Savings": 10000
        }

finance_assistance_agent= LlmAgent(
    name= "finance_assistance_agent",
    model="gemini-2.5-flash",
    description= " A Simple finanace assistant that helps with user's finance goals.",
    instruction="""You are friendly finance assistant. You can help answer user's generic questions on finance 
    and help plan their finance goals. Be more friendly and positive.
    You have two tools to use to complete your task.
    1. get_user_personal_details - This tool give you the user's current financial information
    2. investment_plan_agent - This tool can perform Google Search to get any latest information from the 
        websites and will be able to ask more details from the user and plan their savings goals.
        
        ALWAYS use the google_search tool when asked about:
    - Stock prices (e.g. "Tesla stock price", "TSLA latest price)
    - Market data, financial news, or company information
    - ANY questions containing words like "latest", "current", "today", "now", "recent"
    """,
tools=[AgentTool(investment_plan_agent) ,get_user_personal_details])

root_agent = finance_assistance_agent