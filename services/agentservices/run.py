import asyncio
from services.tools.streaming import stream_agent
from services.agentservices.debate.economist import eco
from services.agentservices.debate.environmentalist import enviro
from services.agentservices.debate.activist import socio
from services.agentservices.orchestrator import orch
from services.agentservices.judge import JudgeVerdict,eval
from services.agentservices.prompt import INSTRUCTIONS_ORCH
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


async def build_briefing_with_orchestrator(topic, agent_name, round_num, total_rounds, transcript):

    prompt = f"""
    Create the debate briefing for this agent.
    
    Agent: {agent_name}
    Debate topic: {topic}
    Round: {round_num}
    Total rounds: {total_rounds}
    
    Transcript so far:
    {transcript if transcript else "No previous rounds. This is the opening round."}
    
    Return only the briefing that should be sent to the agent.
    """
    
    result = await Runner.run(orch_agent, prompt)
    return result.final_output
  


async def run_round(agents, topic, round_num, total_rounds, transcript):
    results = {}
    for name, agent in agents.items():
        briefing = await build_briefing_with_orchestrator(
            topic,
            name,
            round_num,
            total_rounds,
            transcript
        )
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




    

    
















