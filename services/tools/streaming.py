import sys
from agents import Runner
from agents.stream_events import RawResponsesStreamEvent, RunItemStreamEvent
from agents.items import ToolCallItem, ToolCallOutputItem
from openai.types.responses import ResponseTextDeltaEvent


async def stream_agent(agent, user_input: str) -> str:
    
    full_text = []
    tool_active = False

    result = Runner.run_streamed(agent, user_input)

    async for event in result.stream_events():

        if isinstance(event, RunItemStreamEvent):
            if isinstance(event.item, ToolCallItem) and not tool_active:
                tool_active = True
                sys.stdout.write("\n searching the web...\n\n")
                sys.stdout.flush()
            elif isinstance(event.item, ToolCallOutputItem):
                tool_active = False

        elif isinstance(event, RawResponsesStreamEvent):
            data = event.data
            if isinstance(data, ResponseTextDeltaEvent) and data.delta:
                sys.stdout.write(data.delta)
                sys.stdout.flush()
                full_text.append(data.delta)


    print()
    return "".join(full_text).strip()