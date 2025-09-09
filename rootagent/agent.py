from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from shared.chat_model import chat_model
from subagents.planner_agent import planner_agent
from subagents.source_finder_agent import source_finder_agent
from subagents.summarizer_agent import summarizer_agent
from subagents.review_agent import reviewer_agent

root_agent = LlmAgent(
    name="DeepResearchAgent",
    description="Agent that orchestrates the research.",
    model=chat_model,
    instruction="""
    You are the RootAgent responsible for orchestrating the initial research process.

    Workflow:
    1. Receive the user's main research question.
    2. Call the `PlannerAgent` tool with the main question to generate structured sub-questions.
    3. Provide the generated sub-questions to the `SourceFinderAgent` tool to identify relevant sources and retrieve their content.
    4. Provide the main question, sub-questions, and all gathered sources (including full content) to the `SummarizerAgent` tool.
    5. The `SummarizerAgent` must produce a consolidated summary that integrates insights from all sub-questions and their sources.
    6. Pass the following outputs to the `ReviewerAgent`:
         - Main question
         - Sub-questions
         - Sources
         - Consolidated summary
    """,
    tools=[
        AgentTool(agent=planner_agent),
        AgentTool(agent=source_finder_agent),
        AgentTool(agent=summarizer_agent)
    ],
    sub_agents=[reviewer_agent]
)



# from google.adk.agents import LlmAgent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai.types import Content, Part
# import asyncio

# try:
#     from dotenv import load_dotenv
#     load_dotenv()
#     print("Loaded environment variables from .env file.")
# except ImportError:
#     # If python-dotenv is not installed, skip loading .env
#     print("python-dotenv not installed; skipping .env loading.")
#     pass

# APP_NAME = "generic_tools"
# USER_ID = "user123"
# SESSION_ID = "abcd1234"

# async def main():

#     async def run_agent():
#         session_service = InMemorySessionService()

#         print("Creating session...")
#         session = await session_service.create_session(
#             app_name=APP_NAME,
#             user_id=USER_ID,
#             session_id=SESSION_ID
#         )

#         runner = Runner(
#             agent=root_agent,
#             app_name=APP_NAME,
#             session_service=session_service
#         )
#         print("Runner initialized.")

#         message = Content(parts=[Part(text="I need information about pahalgram attack on india")], role="user")
        
#         events = runner.run_async(user_id=USER_ID,session_id=SESSION_ID, new_message=message)

#         response_text = ""
#         async for event in events:  
#             if event.is_final_response() and event.content and event.content.parts:
#                 response_text = event.content.parts[0].text
#                 print(event.author)
#                 print(response_text)
#                 print("session_state:",session.state)
#                 print("-------------------")

#         await runner.close()

#     await run_agent()

# if __name__ == "__main__":
#     asyncio.run(main())