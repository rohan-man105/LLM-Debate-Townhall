from agents import Agent
from services.agentservices.prompt import INSTRUCTIONS_ENVI
from env import open_model,SETTINGS
from services.tools.tavily import web_search,environmentalist_search



def enviro():

    environmentalist = Agent(
        name="Environmentalist",
        instructions=INSTRUCTIONS_ENVI,
        model=open_model,
        tools=[web_search,environmentalist_search],
        model_settings=SETTINGS
    )

    return environmentalist
