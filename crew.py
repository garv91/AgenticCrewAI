from crewai import Crew,Process,Task
from agents import blog_researcher, blog_writer
from tasks import blog_research_task, blog_write_task


crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[blog_research_task, blog_write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

#start Task Execution


result = crew.kickoff(inputs={
        "youtube_channel_handle": "@CrashCourse",
        "topic": "photosynthesis"
    })
print(result)