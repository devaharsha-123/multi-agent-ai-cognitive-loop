from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

BOT_PERSONAS = {
    "Bot_A_TechMaximalist": (
        "I believe AI and crypto will solve all human problems. I am highly optimistic "
        "about technology, Elon Musk, and space exploration. I dismiss regulatory concerns."
    ),
    "Bot_B_Doomer": (
        "I believe late-stage capitalism and tech monopolies are destroying society. "
        "I am highly critical of AI, social media, and billionaires. I value privacy and nature."
    ),
    "Bot_C_FinanceBro": (
        "I strictly care about markets, interest rates, trading algorithms, and making money. "
        "I speak in finance jargon and view everything through the lens of ROI."
    ),
}

def get_embeddings():
    print("[INFO] Using local HuggingFace embeddings")
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_persona_vectorstore(embeddings):
    docs = []
    for bot_id, persona_text in BOT_PERSONAS.items():
        doc = Document(page_content=persona_text, metadata={"bot_id": bot_id})
        docs.append(doc)
    vectorstore = FAISS.from_documents(docs, embeddings)
    print("[INFO] Persona vector store built successfully.")
    return vectorstore

def route_post_to_bots(post_content: str, threshold: float = 0.30):
    embeddings = get_embeddings()
    vectorstore = build_persona_vectorstore(embeddings)
    results = vectorstore.similarity_search_with_score(post_content, k=3)

    matched_bots = []
    print(f"\n[ROUTING] Post: \"{post_content}\"")
    print(f"[ROUTING] Threshold: {threshold}")
    print("-" * 60)

    for doc, raw_score in results:
        similarity = 1 / (1 + raw_score)
        bot_id = doc.metadata["bot_id"]
        print(f"  {bot_id}: similarity={similarity:.4f}")
        if similarity >= threshold:
            matched_bots.append((bot_id, round(similarity, 4)))

    print("-" * 60)
    if matched_bots:
        print(f"[RESULT] Matched bots: {[b[0] for b in matched_bots]}")
    else:
        print("[RESULT] No bots matched above threshold.")

    return matched_bots

if __name__ == "__main__":
    test_posts = [
        "OpenAI just released a new model that might replace junior developers.",
        "The S&P 500 just dropped 3% due to rising interest rates.",
        "Big Tech companies are collecting your data without consent.",
    ]
    for post in test_posts:
        route_post_to_bots(post, threshold=0.30)
        print()