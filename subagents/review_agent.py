from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from subagents.planner_agent import planner_agent
from subagents.source_finder_agent import source_finder_agent
from subagents.summarizer_agent import summarizer_agent
from subagents.research_writer_agent import research_writer_agent
from shared.chat_model import chat_model

reviewer_agent = LlmAgent(
    name="ReviewerAgent",
    description="Validates and improves sub-questions, sources, and summary before delegating to the ResearchWriterAgent.",
    model=chat_model,
    instruction="""
    You are the ReviewerAgent responsible for evaluating the quality of the research pipeline outputs.

    Workflow:
    1. You will receive the following inputs:
         - Main research question
         - Sub-questions
         - Sources with content
         - Consolidated summary

    2. Review each component for completeness and quality:
         - **Sub-questions**: Check if they adequately address the main question. 
             • If gaps exist, regenerate improved sub-questions using the `PlannerAgent` tool, then pass them to `SourceFinderAgent` and `SummarizerAgent` to refresh sources and summary.
         - **Sources**: Evaluate relevance and reliability. 
             • If weak or irrelevant, re-run `SourceFinderAgent` with existing sub-questions, then re-run `SummarizerAgent` to update the summary.
         - **Summary**: Assess clarity, coverage, and coherence. 
             • If inadequate, re-run the `SummarizerAgent` with the same sub-questions and sources.

    3. Iterate as needed until the outputs are consistent, relevant, and comprehensive.

    4. Once validated and improved, delegate the Report writing task to `ResearchWriterAgent` agent with the finalized:
         - Main research question
         - Sub-questions
         - Sources
         - Final summary
    """,
    tools=[
        AgentTool(agent=planner_agent),
        AgentTool(agent=source_finder_agent),
        AgentTool(agent=summarizer_agent)
    ],
    sub_agents=[research_writer_agent]
)
