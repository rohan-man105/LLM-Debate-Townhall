from agents import function_tool
from env import tavily_client


@function_tool
def web_search(query:str) -> str:
    """Search the web for recent, factual information on a given topic.
    Use this whenever you need real-world data, statistics, or current events
    to support your debate argument.
 
    Args:
        query: query.
 
    Returns:
        A string containing the top search results with titles, URLs, and content snippets.
    """

    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=3,
        include_answer=True
    )

    parts = []
 
    if response.get("answer"):
        parts.append(f"Summary: {response['answer']}\n")
 
    for i, result in enumerate(response.get("results", []), 1):
        title   = result.get("title", "No title")
        url     = result.get("url", "")
        content = result.get("content", "").strip()
        parts.append(f"[{i}] {title}\n    URL: {url}\n    {content}")
 
    return "\n\n".join(parts) if parts else "No results found."


@function_tool
def economist_search(query:str) -> str:
    """Search trusted economic and government sources for data, statistics, and policy information.
    Use this when you need authoritative economic data, RBI reports, government statistics,
    budget information, or macroeconomic indicators specific to India or global institutions.

    Args:
        query: query

    Returns:
        A string containing top results from trusted economic sources with titles, URLs, and content snippets.
    """




    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        include_domains=["rbi.org.in", "mospi.gov.in", "niti.gov.in", "worldbank.org", "imf.org", "economictimes.indiatimes.com", "pib.gov.in", "finmin.nic.in", "livemint.com", "tradingeconomics.com"],
        max_results=3,
        include_answer=True
    )

    parts = []

    if response.get("answer"):
        parts.append(f"Summary: {response['answer']}\n")

    for i, result in enumerate(response.get("results", []), 1):
        title   = result.get("title", "No title")
        url     = result.get("url", "")
        content = result.get("content", "").strip()
        parts.append(f"[{i}] {title}\n    URL: {url}\n    {content}")

    return "\n\n".join(parts) if parts else "No results found."


@function_tool
def environmentalist_search(query:str) -> str:
    """Search trusted environmental sources for data, reports, and policy information.
    Use this when you need authoritative data on climate change, environmental impact,
    biodiversity, pollution, and sustainability initiatives.

    Args:
        query: query.

    Returns:
        A string containing top results from trusted environmental sources with titles, URLs, and content snippets.
    """




    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        include_domains=["ipcc.ch", "moef.gov.in", "cse.org", "downtoearth.org.in", "unep.org", "nasa.gov", "carbonbrief.org", "globalforestwatch.org", "sandrp.in", "theprint.in"],
        max_results=3,
        include_answer=True
    )

    parts = []

    if response.get("answer"):
        parts.append(f"Summary: {response['answer']}\n")

    for i, result in enumerate(response.get("results", []), 1):
        title   = result.get("title", "No title")
        url     = result.get("url", "")
        content = result.get("content", "").strip()
        parts.append(f"[{i}] {title}\n    URL: {url}\n    {content}")

    return "\n\n".join(parts) if parts else "No results found."



@function_tool
def activist_search(query:str) -> str:
    """Search trusted social justice and human rights sources for data, reports, and advocacy information.
    Use this when you need authoritative data on human rights, gender equality, poverty,
    labour rights, discrimination, and grassroots social movements.

    Args:
        query: query.

    Returns:
        A string containing top results from trusted social activism sources with titles, URLs, and content snippets.
    """


    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        include_domains=["censusindia.gov.in", "oxfam.org", "indiaspend.com", "ilo.org", "undp.org", "nhrc.nic.in", "data.gov.in", "scroll.in", "thehindu.com", "reuters.com"],
        max_results=3,
        include_answer=True
    )

    parts = []

    if response.get("answer"):
        parts.append(f"Summary: {response['answer']}\n")

    for i, result in enumerate(response.get("results", []), 1):
        title   = result.get("title", "No title")
        url     = result.get("url", "")
        content = result.get("content", "").strip()
        parts.append(f"[{i}] {title}\n    URL: {url}\n    {content}")

    return "\n\n".join(parts) if parts else "No results found."






