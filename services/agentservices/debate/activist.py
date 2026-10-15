from agents import Agent
from env import open_model,SETTINGS
from services.agentservices.prompt import INSTRUCTIONS_SOCIO
from services.tools.tavily import web_search,activist_search


def socio():
    
    activist = Agent(
        name="Social Activist",
        instructions=INSTRUCTIONS_SOCIO,
        model=open_model,
        tools=[web_search,activist_search],
        model_settings=SETTINGS
    )

    return activist

