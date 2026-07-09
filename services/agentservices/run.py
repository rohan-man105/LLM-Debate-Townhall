import asyncio
from services.tools.streaming import stream_agent
from services.agentservices.debate.economist import eco
from services.agentservices.debate.evironmentalist import enviro
from services.agentservices.debate.activist import socio
from services.agentservices.orchestrator import orch
from services.agentservices.judge import JudgeVerdict,eval
from agents import Runner

eco_agent = eco()
envi_agent = enviro()
socio_agent = socio()
orch_agent = orch()


def build_transcript(topic, all_rounds):

    lines = [f"Topic: {topic}\n"]
    for round_num, results in all_rounds.items():
        lines.append(f"=== ROUND {round_num} ===")
        for agent_name, response in results.items():
            lines.append(f"{agent_name}: {response}")
    return "\n\n".join(lines)


def build_briefing(topic, agent_name, round_num, total_rounds, transcript):
    
    if round_num == 1:
        round_type = "OPENING STANCE"
        instructions = "Present your opening position backed by data..."
    elif round_num == total_rounds:
        round_type = "FINAL DEFENCE & CLOSING"
        instructions = "Deliver your closing argument, address the strongest critique against you..."
    else:
        round_type = "CRITIQUE & REBUTTAL"
        instructions = "Critique the other agents' arguments, defend against attacks on yours..."
    
    briefing = f"""
DEBATE TOPIC: {topic}

ROUND {round_num} OF {total_rounds} — {round_type}

INSTRUCTIONS FOR THIS ROUND:
{instructions}

FULL DEBATE TRANSCRIPT SO FAR:
{transcript if transcript else "No previous rounds — this is the opening round."}
"""
    return briefing


async def run_round(agents, topic, round_num, total_rounds, transcript):
    results = {}
    for name, agent in agents.items():
        briefing = build_briefing(topic, name, round_num, total_rounds, transcript)
        print(f"\n{name} —\n")
        response = await stream_agent(agent, briefing)
        results[name] = response
    return results


async def round_debate(topic, num_rounds):
    agents = {"Economist": eco_agent, "Environmentalist": envi_agent, "Social Activist": socio_agent}
    
    all_rounds = {}
    transcript = ""
    
    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num} of {num_rounds}")
        
        results = await run_round(agents, topic, round_num, num_rounds, transcript)
        all_rounds[round_num] = results
        transcript = build_transcript(topic, all_rounds) 
    
    result = await Runner.run(eval(), transcript)
    verdict: JudgeVerdict = result.final_output
    print("JUDGE: FINAL VERDICT")
    print(f"  Economist        : {verdict.econ_score}/10")
    print(f"  Environmentalist : {verdict.enviro_score}/10")
    print(f"  Social Activist  : {verdict.activist_score}/10")
    print(f"\n  Winner : {verdict.round_winner}")
    print(f"  Reason : {verdict.reason}\n")




    

    
















