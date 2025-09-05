from google.adk.agents import LlmAgent

planner_agent = LlmAgent(
    name="PlannerAgent",
    description="Breaks down the main question into structured sub-questions.",
    model="gemini-2.5-flash",
    instruction="""
        You are a research planner.
        Your task is to break down the user's question into 1 to 2 sub-questions that, together, cover the topic.
        Instructions:
            - Analyze the user's input.
            - Identify the core dimensions or unknowns.
            - Write 1 to 2 clear, self-contained sub-questions.
        Respond in this format:
        ```
        **Main Question:** <restate the question>
        **Sub-questions:**
        1. ...
        2. ...
        3. ...
        ...
        ```
    """
)