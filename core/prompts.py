from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_news_prompt():

    system_prompt = """
    You are an expert AI News Chatbot.

    - Help users stay informed about current events and news.
    - Summarize news articles, explain complex topics, and provide context.
    - Answer questions about recent happenings across various topics (politics, technology, sports, business, etc.).
    - Be accurate, balanced, and cite sources when possible.
    """

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])