import os
from dotenv import load_dotenv
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from agents import ModelSettings
from tavily import TavilyClient

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

open_client = AsyncOpenAI(
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

open_model = OpenAIChatCompletionsModel(
    model="nvidia/llama-3.3-nemotron-super-49b-v1.5",
    openai_client=open_client
)

tavily_client = TavilyClient(
    api_key=TAVILY_API_KEY,
)


SETTINGS = ModelSettings()
