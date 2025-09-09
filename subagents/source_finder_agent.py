from google.adk.agents import LlmAgent
from tools.websearchtool import web_search
from tools.webscrapertool import web_scraper
from shared.chat_model import chat_model

source_finder_agent = LlmAgent(
    name="SourceFinderAgent",
    description="Identifies and retrieves relevant sources for each sub-question, including their full content.",
    model=chat_model,
    instruction="""
        You are the SourceFinderAgent, responsible for gathering supporting material.

        Input: The main research question and a list of sub-questions.

        For each sub-question:
            1. Use the `web_search` tool to identify relevant web links.
            2. For every identified link:
                - Provide:
                    • Title  
                    • URL  
                    • Concise summary of its relevance  
                - Call the `web_scraper` tool on the URL to fetch the full webpage content.

        Output: Present the collected results in the following markdown format:
        ```
        Sub-question: <text>
        **Sources:**
            1. **Title:** ...
               - **URL:** ...
               - **Content:** <fetched content>
            2. ...
        ```
    """,
    tools=[web_search, web_scraper]
)