from crewai import Crew
from agent import researcher
from task import research_task

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)
