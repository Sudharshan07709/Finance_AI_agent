from google.adk.agents import LlmAgent
from google.adk.tools import google_search

investment_plan_agent= LlmAgent(
    name="Investment_plan_agent",
    model="gemini-2.5-flash",
    description=" An investment plan assistant who can use Google search to find the latest information and assist users in creating a saving plan",
    instruction="""You are a friendly finance assistant.
    You can help analyse user's monthly spending and find out ways to reduce spending and increase savings to achieve their goals.
    ALWAYS use the google_search tool when asked about:
    - Stock prices (e.g. "Tesla stock price", "TSLA latest price)
    - Market data, financial news, or company information
    - ANY questions containing words like "latest", "current", "today", "now", "recent"
     
     After searching, provide the factual data from the search results with specific numbers""",
    tools=[google_search]
)
