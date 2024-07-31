from crewai import Task
from textwrap import dedent

class ContentTasks:

    def __tip_section(self):
        return """\nRemember to adhere to the content guidelines and maintain a professional tone.\n"""

    def content_planning_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                1. Research the latest trends and key news on the topic: {topic}.
                2. Identify the target audience and their interests.
                3. Create a detailed content outline (introduction, key points, conclusion).
                4. Include SEO keywords and relevant data or sources.
                5. Describe images to be included in the article.
                6. Ensure the plan aligns with content guidelines and professional tone.
                {self.__tip_section()}
            """),
            expected_output=dedent(f"""
                A comprehensive content plan in markdown format.
            """),
            agent=agent
        )

    def researcher_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                1. Conduct thorough web searches on the topic: {topic}.
                2. Provide detailed and referenced domain knowledge.
                3. List relevant open-source images with descriptions and attributions.
                4. Filter out controversial, racial, or harmful content.
                5. Summarize findings in a clear and organized manner.
                6. Maintain adherence to content guidelines and professional tone.
                {self.__tip_section()}
            """),
            expected_output=dedent(f"""
                A comprehensive knowledge document in markdown format.
            """),
            agent=agent
        )

    def writing_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                1. Use the content plan and research to write the article on {topic}.
                2. Incorporate SEO keywords naturally.
                3. Structure the article with engaging sections and a clear narrative flow.
                4. Use images appropriately and provide proper attribution.
                5. Ensure the article is ready for publication with proper references and citations.
                6. Maintain adherence to content guidelines and professional tone.
                {self.__tip_section()}
            """),
            expected_output=dedent(f"""
                A well-written article in markdown format, ready for publication.
            """),
            agent=agent
        )

    def editing_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                1. Proofread the article on {topic} for grammatical accuracy and alignment with the brand’s voice.
                2. Ensure the article follows journalistic best practices.
                3. Provide balanced viewpoints and avoid major controversial topics or opinions.
                4. Confirm images and quotes are properly attributed.
                5. Finalize the article for publication.
                {self.__tip_section()}
            """),
            expected_output=dedent(f"""
                A polished and error-free article in markdown format.
            """),
            agent=agent
        )
    