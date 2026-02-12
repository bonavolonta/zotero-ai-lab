# 📚 Zotero AI Research Intelligence Platform

AI-powered bibliometric analysis, semantic clustering, topic evolution,
and RAG assistant built on top of Zotero.

------------------------------------------------------------------------

## 🚀 Overview

**Zotero AI Lab** transforms your Zotero library into:

-   📊 Topic modeling system (LDA + Dynamic Topic Modeling)
-   🤖 Semantic clustering engine (Embeddings NLP)
-   🌍 3D thematic knowledge map (UMAP)
-   🌐 Tag network analysis (Louvain community detection)
-   📈 Topic evolution over time
-   🤖 AI-powered RAG assistant (chat over your articles)
-   📊 Professional interactive dashboard (Streamlit)

Designed for:

-   Digital Humanities
-   Bibliometrics & Scientometrics
-   Academic research labs
-   Knowledge mapping
-   Advanced literature analysis

------------------------------------------------------------------------

## 🏗 Architecture

Zotero API\
↓\
Metadata + Abstracts\
↓\
SentenceTransformer Embeddings\
↓\
Clustering + Topic Modeling + Network Analysis\
↓\
FAISS Vector Store\
↓\
RAG (OpenAI API)\
↓\
Streamlit Dashboard

------------------------------------------------------------------------

## 📦 Features

### 📚 Topic Modeling

Extract latent themes from abstracts using LDA and dynamic topic
modeling.

### 🧠 Semantic Embeddings

Detect semantic similarity and conceptual overlap between research
areas.

### 🌍 3D Thematic Map

Interactive 3D visualization of research domains using UMAP.

### 🌐 Tag Network Analysis

-   Co-occurrence graph\
-   Community detection (Louvain)\
-   Centrality analysis

### 📊 Topic Evolution

Track how research themes change over time.

### 🤖 RAG Assistant

Chat with your research corpus using retrieval-augmented generation.

------------------------------------------------------------------------

## 🛠 Local Installation

``` bash
git clone https://github.com/YOUR_USERNAME/zotero-ai-lab.git
cd zotero-ai-lab
pip install -r requirements.txt
streamlit run app.py
```

Create `.streamlit/secrets.toml`:

    ZOTERO_API_KEY = "your_zotero_api_key"
    ZOTERO_USER_ID = "your_user_id"
    OPENAI_API_KEY = "your_openai_key"

------------------------------------------------------------------------

## ☁ Deploy to Streamlit Cloud

1.  Push repository to GitHub\
2.  Go to https://streamlit.io/cloud\
3.  Connect your GitHub account\
4.  Select repository\
5.  Set main file: `app.py`\
6.  Add Secrets in Advanced Settings

Deploy and enjoy your live dashboard.

------------------------------------------------------------------------

## 🔑 Required API Keys

### Zotero API Key

Create at:\
https://www.zotero.org/settings/keys

### OpenAI API Key

Create at:\
https://platform.openai.com

------------------------------------------------------------------------

## 📊 Research Applications

-   Knowledge domain mapping\
-   Emerging theme detection\
-   Interdisciplinary drift analysis\
-   AI-assisted literature review\
-   Research intelligence dashboards

------------------------------------------------------------------------

## ⚠️ Data Privacy

-   No external storage\
-   Secrets handled securely via Streamlit\
-   Only RAG queries are sent to OpenAI

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------

## 👤 Author

Developed as an advanced academic AI knowledge mapping system.
