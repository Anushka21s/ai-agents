from crewai import Task
from agent import researcher

research_task = Task(
    description="Research the latest opportunities in remote sensing and gis",
    expected_output="A concise report summarizing the latest research paper, skills in demand, major freelancing and work opportunities, and important observations.",
    agent=researcher
)
