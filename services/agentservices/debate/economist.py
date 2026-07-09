from agents import Agent
from env import open_model,SETTINGS
from services.agentservices.prompt import INSTRUCTIONS_ECO
from services.tools.tavily import web_search,economist_search



def eco():

    economist = Agent(
    name="Economist",
    instructions=INSTRUCTIONS_ECO,
    model=open_model,
    tools=[web_search,economist_search],
    model_settings=SETTINGS
    )

    return economist




