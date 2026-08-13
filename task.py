from crewai import Task
from agent import researcher

research_task = Task(
    description="Research the latest trends in Agentic AI freelancing opportunities.",
    expected_output="A concise report summarizing the latest trends, skills in demand, major freelancing opportunities, and important observations.",
    agent=researcher
)
