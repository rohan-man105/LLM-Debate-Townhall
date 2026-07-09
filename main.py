import asyncio
from services.agentservices.run import round_debate
from agents import set_tracing_disabled

set_tracing_disabled(True)


async def main():
    topic = input("\n Enter debate topic: ")
    if not topic:
        return
    rounds = int(input(" Enter number of rounds: "))
    await round_debate(topic, rounds)


if __name__ == "__main__":
    asyncio.run(main())
