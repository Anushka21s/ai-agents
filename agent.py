import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

load_dotenv()

search_tool = SerperDevTool()

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

researcher = Agent(
    role="Research Analyst",
    goal="Research the latest trends in Agentic AI freelancing opportunities",
    backstory="You are an experienced research analyst who finds and analyzes current information from the web.",
    tools=[search_tool],
    llm=llm,
    verbose=True
)
