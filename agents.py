from dotenv import load_dotenv    
import os 
from tools import yt_tool  
from crewai import Agent
from langchain_openai import ChatOpenAI  


# Load env vars
load_dotenv()

# Check API key
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Set model name
model_name = "gpt-4-0125-preview"

# Initialize LLM
llm = ChatOpenAI(
    model=model_name,
    temperature=0.7,
    api_key=os.environ['OPENAI_API_KEY']
)

# Define Agents
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get relevant video content for the topic YT Channel",
    verbose=True,
    memory=True,
    backstory="Expert in understanding videos on AI, Data Science, Machine Learning, and GenAI, providing suggestions.",
    llm=llm,
    tools=[yt_tool],
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT Channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex concepts, you craft engaging narratives that resonate with readers. "
        "Your expertise lies in transforming technical content into relatable stories, making it accessible and enjoyable."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
)
