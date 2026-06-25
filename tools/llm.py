from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite",
    google_api_key = "Enter you API Key"
)