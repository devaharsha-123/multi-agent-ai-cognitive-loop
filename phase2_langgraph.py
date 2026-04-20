import os
import json
from typing import TypedDict
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

load_dotenv()

@tool
def mock_searxng_search(query: str) -> str:
    """Simulates a web search with hardcoded headlines."""
    q = query.lower()
    if "crypto" in q or "bitcoin" in q:
        return "HEADLINE: Bitcoin hits new all-time high amid ETF approvals. HEADLINE: Ethereum reduces gas fees by 90%."
    elif "ai" in q or "openai" in q:
        return "HEADLINE: OpenAI releases GPT-5 with human-level reasoning. HEADLINE: AI replaces 200 junior developers at major firm."
    elif "market" in q or "stock" in q or "fed" in q:
        return "HEADLINE: Fed signals two rate cuts in 2025. HEADLINE: S&P 500 hits record high driven by tech earnings."
    elif "climate" in q or "environment" in q:
        return "HEADLINE: Carbon emissions hit record high despite green pledges. HEADLINE: Big Oil profits surge."
    else:
        return "HEADLINE: Tech giants face antitrust scrutiny. HEADLINE: Automation displaces millions of workers."

def get_llm():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.8)

class PostState(TypedDict):
    bot_id: str
    persona: str
    search_query: str
    search_results: str
    final_post: dict

def decide_search_node(state: PostState) -> PostState:
    llm = get_llm()
    print(f"\n[NODE 1] Deciding search topic for {state['bot_id']}...")
    messages = [
        SystemMessage(content=state["persona"]),
        HumanMessage(content="What ONE topic would you search for today? Reply with ONLY the search query, under 10 words.")
    ]
    response = llm.invoke(messages)
    query = response.content.strip().strip('"').strip("'")
    print(f"[NODE 1] Search query: \"{query}\"")
    return {**state, "search_query": query}

def web_search_node(state: PostState) -> PostState:
    print(f"\n[NODE 2] Searching: \"{state['search_query']}\"...")
    results = mock_searxng_search.invoke({"query": state["search_query"]})
    print(f"[NODE 2] Results: {results[:100]}...")
    return {**state, "search_results": results}

def draft_post_node(state: PostState) -> PostState:
    llm = get_llm()
    print(f"\n[NODE 3] Drafting post for {state['bot_id']}...")
    system_prompt = f"""
{state['persona']}

Respond ONLY with a valid JSON object, no markdown, no explanation:
{{"bot_id": "...", "topic": "...", "post_content": "..."}}

Rules:
- post_content must be under 280 characters
- Be opinionated and in-character
"""
    user_prompt = f"""
Search results:
{state['search_results']}

Bot ID: {state['bot_id']}
Return ONLY the JSON object.
"""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    response = llm.invoke(messages)
    raw = response.content.strip().replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(raw)
        parsed["bot_id"] = state["bot_id"]
        print(f"[NODE 3] ✅ Post drafted:\n{json.dumps(parsed, indent=2)}")
    except json.JSONDecodeError:
        print(f"[NODE 3] ⚠️ JSON parse failed, using raw output")
        parsed = {"bot_id": state["bot_id"], "topic": state["search_query"], "post_content": raw[:280]}

    return {**state, "final_post": parsed}

def build_content_graph():
    graph = StateGraph(PostState)
    graph.add_node("decide_search", decide_search_node)
    graph.add_node("web_search", web_search_node)
    graph.add_node("draft_post", draft_post_node)
    graph.set_entry_point("decide_search")
    graph.add_edge("decide_search", "web_search")
    graph.add_edge("web_search", "draft_post")
    graph.add_edge("draft_post", END)
    return graph.compile()

BOT_PERSONAS = {
    "Bot_A_TechMaximalist": "I believe AI and crypto will solve all human problems. I am highly optimistic about technology, Elon Musk, and space exploration. I dismiss regulatory concerns.",
    "Bot_B_Doomer": "I believe late-stage capitalism and tech monopolies are destroying society. I am highly critical of AI, social media, and billionaires. I value privacy and nature.",
    "Bot_C_FinanceBro": "I strictly care about markets, interest rates, trading algorithms, and making money. I speak in finance jargon and view everything through the lens of ROI.",
}

if __name__ == "__main__":
    graph = build_content_graph()
    for bot_id, persona in BOT_PERSONAS.items():
        print(f"\n{'='*60}\nRunning for: {bot_id}\n{'='*60}")
        result = graph.invoke({
            "bot_id": bot_id,
            "persona": persona,
            "search_query": "",
            "search_results": "",
            "final_post": {}
        })
        print(f"\n✅ FINAL OUTPUT:\n{json.dumps(result['final_post'], indent=2)}")