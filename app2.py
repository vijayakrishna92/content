# app.py
import streamlit as st
from crewai import Crew
from textwrap import dedent
from agents import ContentAgents
from tasks import ContentTasks
from dotenv import load_dotenv
import json

load_dotenv()

class ContentCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        agentsa = ContentAgents()
        tasks = ContentTasks()

        planner_agent = agentsa.content_strategist_agent(self.topic)
        researcher_agent = agentsa.content_creator_agent(self.topic)

        planner_task = tasks.content_planning_task(planner_agent, self.topic)
        planner_tasks = tasks.researcher_task(planner_agent, self.topic)
        researcher_task = tasks.writing_task(researcher_agent, self.topic)
        researcher_tasks = tasks.editing_task(researcher_agent, self.topic)


        crew = Crew(
            agents=[planner_agent, researcher_agent],
            tasks=[planner_task, planner_tasks,  researcher_task, researcher_tasks],
            verbose=True
        )

        result = crew.kickoff()
        
        # Debugging: Print the structure and content of the result
        print("DEBUG: Result structure and content")
        print(json.dumps(result, indent=2))
        
        return result

def display_result(result):
    st.write("## Research on Topic")
    st.write('-------------------------------')
    
    # Debugging: Print the result to ensure it has content
    print("DEBUG: Displaying result")
    print(result)
    
    if 'content_plan' in result:
        st.write("### Content Plan")
        st.write(result['content_plan'])
    
    if 'references' in result:
        st.write("### References")
        for ref in result['references']:
            st.markdown(f"- [{ref['title']}]({ref['link']}): {ref['snippet']}")
    
    if 'images' in result:
        st.write("### Images")
        for image in result['images']:
            st.image(image['url'], caption=image['description'])

# Streamlit UI
st.title('Content Creator Chatbot')
st.write('-------------------------------')
    
topic = st.text_input("What topic do you want to write about?")

if st.button('Generate Content'):
    if topic:
        content_crew = ContentCrew(topic)
        result = content_crew.run()
        
        # Debugging: Print the result to ensure it is not empty
        print("DEBUG: Result received")
        print(result)
        
        st.write("## Here is your Content Plan")
        st.write('-------------------------------')
        st.write(result)
    else:
        st.error("Please enter a topic.")

