import string

from agents import Agent
from services.agentservices.prompt import INSTRUCTIONS_ORCH
from env import open_model
from pydantic import BaseModel


class OrchestratorOutput(BaseModel):
    round_num: int
    round_brief: str
    round_left: int
    transcript_overview: str



def orch():

    orchestrator = Agent(
        name="Orchestrator",
        instructions=INSTRUCTIONS_ORCH,
        model=open_model,
        output_type=OrchestratorOutput
    )

    return orchestrator
