import streamlit as st
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI

st.set_page_config(layout="wide")
st.title("Zotero AI Research Dashboard")

# ======================
# CONFIG
# ======================

API_KEY = st.secrets["ZOTERO_API_KEY"]
USER_ID = st.secrets["ZOTERO_USER_ID"]
OPENAI_KEY = st.secrets["OPENAI_API_KEY"]

BASE_URL = f"https://api.zotero.org/users/{USER_ID}"
HEADERS = {"Zotero-API-Key": API_KEY}

# ======================
# CARICA ITEM
# ======================

@st.cache_data
def get_items():
    items = []
    start = 0
    while True:
        url = f"{BASE_URL}/items?v=3&limit=100&start={start}"
        r = requests.get(url, headers=HEADERS)
        data = r.json()
        if not data:
            break
        items.extend(data)
        start += 100
    return items

items = get_items()

st.subheader("Numero articoli:")
st.write(len(items))

# ======================
# RAG
# ======================

st.subheader("Chat sui tuoi articoli")

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [item["data"].get("abstractNote","") for item in items if item["data"].get("abstractNote")]

embeddings = model.encode(texts)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search(query, k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k)
    return [texts[i] for i in I[0]]

client = OpenAI(api_key=OPENAI_KEY)

question = st.text_input("Fai una domanda")

if question:
    context_docs = search(question)
    context = "\n\n".join(context_docs)

    prompt = f"""
    Usa solo questo contesto:
    {context}
    
    Domanda: {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    st.write(response.choices[0].message.content)
