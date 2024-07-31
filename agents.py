from crewai import Agent
from langchain.llms import OpenAI
from langchain.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
#from tools.browser_tools import BrowserTools
#from tools.search_tools import SearchTools
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
mistral = HuggingFaceEndpoint(repo_id=repo_id,max_new_tokens=28000,temperature=0.3,repetition_penalty=1.1, huggingfacehub_api_token=OPENAI_API_KEY)

class ContentAgents:

  def content_strategist_agent(self, topic):
    return Agent(
        role = "Senior Content Strategist",
        goal = "Plan and gather comprehensive and engaging content for the given topic.",
        backstory = "You are a seasoned strategist responsible for developing content plans, conducting research, and ensuring the foundation for high-quality articles.",
        #tools=[
        #    SearchTools.search_internet,
        #    BrowserTools.scrape_and_summarize_website,
        #],
        llm = mistral,
        allow_delegation=False,
        verbose=True)


  def content_creator_agent(self, topic):
    return Agent(
        role = "Senior Content Writer and Editor",
        goal = "Write and edit compelling, factually accurate, and engaging articles based on provided content plans and research.",
        backstory = "You are a skilled writer and editor responsible for creating well-structured content and ensuring it meets quality standards.",
        #tools=[
         #   SearchTools.search_internet,
         #   BrowserTools.scrape_and_summarize_website,
        #],
        llm = mistral,
        allow_delegation=False,
        verbose=True)

