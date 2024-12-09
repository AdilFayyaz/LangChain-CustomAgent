from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from .tools import venue_tool, catering_tool, entertainment_tool
import os

def initialize_main_agent(memory):
    # Load the OpenAI API key from environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        raise ValueError("OpenAI API key not set in environment variables.")

    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key, temperature=0.7)

    # Define tools
    tools = [venue_tool, catering_tool, entertainment_tool]

    # Initialize the main agent
    main_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory
    )
    return main_agent