# LLM Debate Townhall

LLM Debate Townhall is an interactive terminal application that stages a structured, evidence-oriented debate between three AI personas:

- **Economist** - evaluates growth, incentives, fiscal realities, and trade-offs.
- **Environmentalist** - evaluates climate, pollution, biodiversity, and ecological limits.
- **Social Activist** - evaluates equity, rights, distributional effects, and community impact.

Given a topic and number of rounds, the application has the agents research and argue their positions, carries their arguments forward through a shared transcript, and asks an independent AI judge to score the final debate.

## What it does

1. Prompts for a debate topic and number of rounds in the terminal.
2. Uses an **Orchestrator** agent to prepare a round-specific briefing for every speaker.
3. Gives each speaker the transcript of all completed rounds so it can respond to specific claims instead of delivering isolated monologues.
4. Provides Tavily-powered web-search tools, including domain-focused search tools for economic, environmental, and social-policy research.
5. Streams each response to the terminal as it is generated.
6. Sends the complete transcript to a **Judge** agent at the end of the debate.
7. Prints 0-10 scores for every speaker, a winner, and a reasoned verdict.

The current implementation runs debates in the terminal and keeps the transcript in memory for the duration of a run. It does **not** yet persist transcripts to disk.

## Debate flow

```text
Topic + round count
        |
        v
Orchestrator creates a briefing for each persona
        |
        v
Economist -> Environmentalist -> Social Activist
        |
        v
Responses are appended to the shared transcript
        |
        +--> next round, if any
        |
        v
Judge scores the complete transcript and declares a winner
```

Round intent is determined by the Orchestrator's instructions:

- **Round 1:** opening positions
- **Middle rounds:** critiques and rebuttals
- **Last round:** final defence and closing argument

For a one-round debate, the agents make opening statements and are then judged. For two rounds, the second round combines rebuttal and closing responsibilities.

## Requirements

- Python 3.10 or newer
- An NVIDIA API key with access to NVIDIA's OpenAI-compatible inference endpoint
- A Tavily API key for web research
- Internet access

The project is currently configured to use the NVIDIA model `nvidia/nemotron-3-super-120b-a12b` through `https://integrate.api.nvidia.com/v1`.

## Installation

From the project directory:

```powershell
cd "C:\New folder (2)\LLM-Debate-Townhall"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run this once for the current terminal session and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Configuration

Create a file named `.env` in the project root:

```env
NVIDIA_API_KEY=your_nvidia_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit `.env`; it is already covered by `.gitignore`.

## Run a debate

With the virtual environment active:

```powershell
python main.py
```

Example session:

```text
Enter debate topic: Should India prioritize rapid economic growth over strict environmental protections and redistribution of wealth?
Enter number of rounds: 3
```

Suggested topics:

- Should India phase out coal power by 2040?
- Should AI regulation prioritize innovation or worker protection?
- Should urban water use be priced more aggressively during droughts?

## Research tools

Every persona can use a general `web_search` tool. It also receives a specialist tool that limits Tavily results to relevant sources:

| Persona | Specialist tool | Examples of targeted sources |
| --- | --- | --- |
| Economist | `economist_search` | RBI, MOSPI, NITI Aayog, World Bank, IMF |
| Environmentalist | `environmentalist_search` | IPCC, UNEP, NASA, CSE, Down To Earth |
| Social Activist | `activist_search` | ILO, UNDP, Oxfam, Census India, NHRC |

Search results are returned to the model with titles, URLs, snippets, and (when available) a Tavily summary. The application displays `searching the web...` when a streamed agent invokes a tool.

## Scoring

The Judge returns a structured verdict with an overall score from 0 to 10 for each persona. Its rubric considers:

- evidence quality and named sources;
- coherent reasoning across rounds;
- effectiveness of critiques and rebuttals; and
- adaptation to opponents' arguments.

The terminal prints the three scores, winner, and explanation after the final round.

## Project structure

```text
LLM-Debate-Townhall/
|-- main.py                              # Interactive terminal entry point
|-- env.py                               # Environment variables, NVIDIA client, Tavily client
|-- requirements.txt                     # Python dependencies
|-- services/
|   |-- agentservices/
|   |   |-- run.py                       # Debate loop and transcript creation
|   |   |-- orchestrator.py              # Orchestrator agent
|   |   |-- judge.py                     # Judge agent and verdict schema
|   |   |-- prompt.py                    # Persona, judge, and orchestration instructions
|   |   `-- debate/
|   |       |-- economist.py             # Economist agent
|   |       |-- environmentalist.py      # Environmentalist agent
|   |       `-- activist.py              # Social Activist agent
|   `-- tools/
|       |-- tavily.py                    # Tavily search tools
|       `-- streaming.py                 # Streaming terminal output
`-- .gitignore
```

## Troubleshooting

### `ModuleNotFoundError`

Activate the project virtual environment and reinstall dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### NVIDIA reports a model is unavailable or end-of-life

Update the `model=` value in `env.py` to a model currently available to your NVIDIA account. NVIDIA retires models over time, so a model name that worked previously may no longer be accepted.

### Authentication or permission error

Check that both values in `.env` are present, valid, and do not include surrounding quotes or extra spaces. Restart the terminal after editing `.env`.

### No search results

Confirm that `TAVILY_API_KEY` is valid and that the machine has network access. Specialist searches intentionally restrict results to selected domains; the agent can fall back to general web search when needed.

## Current limitations

- Debate input is interactive only; command-line flags are not yet implemented.
- Each agent is run sequentially within a round.
- Transcripts and verdicts are not saved after the process exits.
- There are no automated tests yet.
- API usage may incur provider charges and is subject to provider limits.

## Next improvements

- Save each debate as JSON and Markdown, then add list/view/replay commands.
- Add input validation for the number of rounds and clearer API-key validation.
- Add CLI flags such as `--topic`, `--rounds`, and `--output`.
- Add retries and friendly messages for provider and network failures.
- Add automated tests with mocked model and search calls.

## Security

Treat NVIDIA and Tavily API keys as secrets. Keep them in `.env`, do not paste them into issues or screenshots, and rotate them if they are exposed.
