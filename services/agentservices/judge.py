from agents import Agent
from env import open_model
from services.agentservices.prompt import INSTRUCTIONS_JUDGE
from pydantic import BaseModel


# Output Format 
class JudgeVerdict(BaseModel):
    econ_score: int
    enviro_score: int
    activist_score: int
    round_winner: str  
    reason: str



def eval():

    judge = Agent(
        name="Judge",
        instructions=INSTRUCTIONS_JUDGE,
        model=open_model,
        output_type=JudgeVerdict
    )


    return judge



