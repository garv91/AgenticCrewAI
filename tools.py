from dotenv import load_dotenv
load_dotenv()  

import os
import time
from YoutubeChannelSearchToolWithRetry import YoutubeChannelSearchToolWithRetry

yt_tool = YoutubeChannelSearchToolWithRetry(youtube_channel_handle="@CrashCourse")

