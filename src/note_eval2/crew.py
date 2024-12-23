from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, SerperDevTool
import logging

logging.basicConfig(level=logging.DEBUG)

@CrewBase
class NoteEval2():
    """NoteEval2 crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def note_summarizer(self) -> Agent:
        logging.debug("Creating note_summarizer agent")
        return Agent(
            config=self.agents_config['note_summarizer'],
            verbose=True,
            tools=[FileReadTool('note.txt')]  
        )

    @agent
    def note_complementer(self) -> Agent:
        logging.debug("Creating note_complementer agent")
        return Agent(
            config=self.agents_config['note_complementer'],
            verbose=True,
            tools=[SerperDevTool()] 
        )

    @agent
    def learning_advisor(self) -> Agent:
        logging.debug("Creating learning_advisor agent")
        return Agent(
            config=self.agents_config['learning_advisor'],
            verbose=True,
        )

    @task
    def note_summary_task(self) -> Task:
        logging.debug("Executing note_summary_task")
        return Task(
            config=self.tasks_config['note_summary_task'],
            output_file='note_summary_output.md'
        )

    @task
    def note_complement_task(self) -> Task:
        logging.debug("Executing note_complement_task")
        return Task(
            config=self.tasks_config['note_complement_task'],
            output_file='note_complement_output.md'
        )

    @task
    def learning_advice_task(self) -> Task:
        logging.debug("Executing learning_advice_task")
        return Task(
            config=self.tasks_config['learning_advice_task'],
            output_file='learning_advice_output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NoteEval2 crew"""
        logging.debug("Creating the NoteEval2 crew")
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True,
        )
