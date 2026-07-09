from agents import Agent
from services.agentservices.prompt import INSTRUCTIONS_ORCH
from env import open_model





def orch():

    orchestrator = Agent(
        name="Orchestrator",
        instructions=INSTRUCTIONS_ORCH,
        model=open_model,
        #output_type=
    )

    return orchestrator
