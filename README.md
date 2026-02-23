# 📰 AI News Chatbot

A conversational AI chatbot that helps users stay informed about current events and news. Built with LangChain, Groq (Llama 3.3 70B), and Streamlit. Deployed on AWS EC2.
---

## 🎯 Features

- **Conversational Interface** – Chat naturally about news and current events
- **Multi-topic Coverage** – Politics, technology, sports, business, and more
- **Contextual Responses** – Summaries, explanations, and balanced answers
- **Conversation Memory** – Maintains chat history for coherent follow-up questions
- **Session Monitoring** – Token usage tracking in the sidebar
- **Cloud Deployment** – Runs on AWS EC2 for public access

---

## 🏗️ Architecture

```
news_chatbot/
├── app.py                 # Streamlit frontend
├── config/
│   └── settings.py       # Configuration
├── core/
│   ├── chain.py          # LangChain pipeline (prompt → LLM → output)
│   ├── llm.py            # Groq LLM initialization
│   └── prompts.py       # System prompts for news chatbot
├── services/
│   └── news_service.py   # Chat logic & conversation handling
├── utils/
│   └── logger.py         # Logging configuration
├── requirements.txt
├── .env                  # API keys
└── README.md
```

### Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM** | Groq (Llama 3.3 70B Versatile) |
| **Framework** | LangChain |
| **UI** | Streamlit |
| **Deployment** | AWS EC2 |
| **Language** | Python 3.10+ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Vivek-Nemani/news_chatbot.git
   cd news_chatbot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Get your API key from [Groq Console](https://console.groq.com/).

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ AWS EC2 Deployment

### Quick Deploy Steps

1. **Launch an EC2 instance** (Ubuntu 22.04, t2.micro or t3.micro)
2. **Security group** – Allow inbound: SSH (22), Custom TCP (8501)
3. **SSH into instance**

   ```bash
   ssh -i your-key.pem ubuntu@<PUBLIC_IP>
   ```

4. **Clone and setup**

   ```bash
   git clone https://github.com/Vivek-Nemani/news_chatbot.git
   cd news_chatbot
   sudo apt update && sudo apt install -y python3.12-venv python3-pip
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Create `.env`** with your `GROQ_API_KEY`

6. **Run Streamlit (bind to all interfaces)**

   ```bash
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

7. **Access** at `http://<PUBLIC_IP>:8501`

### Run as a Background Service (Optional)

Create `/etc/systemd/system/news-chatbot.service`:

```ini
[Unit]
Description=News Chatbot Streamlit App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/news_chatbot
Environment="PATH=/home/ubuntu/news_chatbot/.venv/bin"
ExecStart=/home/ubuntu/news_chatbot/.venv/bin/streamlit run app.py --server.address 0.0.0.0 --server.port 8501
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable news-chatbot
sudo systemctl start news-chatbot
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| langchain | LLM orchestration & chains |
| langchain-community | Community integrations |
| langchain-groq | Groq chat model |
| streamlit | Web UI |
| python-dotenv | Environment variables |
| boto3 | AWS SDK (optional, for future use) |

---

## 🔧 Configuration

- **LLM Model**: `llama-3.3-70b-versatile` (configurable in `core/llm.py`)
- **Temperature**: 0.5 (controls response randomness)
- **Port**: 8501 (Streamlit default)

