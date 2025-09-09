# deepresearchagent/shared/chat_model.py

from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

chat_model = LiteLlm(
    model="openai/gpt-4o",
    api_base=os.getenv("LITELLM_URL"),
    api_key=os.getenv("LITELLM_API_KEY", "slkk"),  # Replace with your actual key variable
    headers={
        "agent": "DeepResearchAgent01",
        "appid": os.getenv("AGENT_ID"),
        "userid": "user_113_456",
        "tenantid": os.getenv("TENANT_ID"),
        "sessionid": "session_113_456",
        "teamid": "team_113_456"
    }
)