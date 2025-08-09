from crewai import Task  
from tools import yt_tool
from agents import blog_researcher, blog_writer 

# Create a task for the blog researcher agent
blog_research_task = Task(
    description=("Identify the videos {topic}."
    "Get detailed information about the video from the channel"
    ),
    expected_output="A comprehensive 3 paragraph summary of the video content based on the {topic} ",
    tools=[yt_tool],
    agent=blog_researcher,  
)

#create a task for the blog writer agent
blog_write_task = Task(
    description=("Write a compelling blog post based on the video content for the topic {topic} from YT Channel."),
    expected_output="A well-structured blog post that narrates the story of the video content in an engaging manner.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog.md"
)