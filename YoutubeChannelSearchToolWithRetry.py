from crewai_tools import YoutubeChannelSearchTool
import time

class YoutubeChannelSearchToolWithRetry(YoutubeChannelSearchTool):
    def run(self, *args, retries=5, delay=10, **kwargs):
        for attempt in range(retries):
            try:
                return super().run(*args, **kwargs)
            except Exception as e:
                if '429' in str(e) and attempt < retries - 1:
                    wait = delay * (2 ** attempt)  # Exponential backoff
                    print(f"Rate limited. Retrying in {wait} seconds (attempt {attempt+1}/{retries})...")
                    time.sleep(wait)
                elif 'TranscriptsDisabled' in str(type(e)):
                    print("Transcript disabled for this video. Skipping.")
                    return None
                else:
                    print(f"Failed to fetch YouTube data: {e}")
                    return None