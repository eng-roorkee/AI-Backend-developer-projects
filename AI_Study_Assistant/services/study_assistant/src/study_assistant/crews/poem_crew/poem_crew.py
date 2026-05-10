from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class PoemCrew:
    """Poem Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer"],  # type: ignore[index]
        )

    @agent
    def quiz_master(self) -> Agent:
        return Agent(
            config=self.agents_config["quiz_master"],  # type: ignore[index]
        )

    @task
    def summarize_notes_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarize_notes_task"],  # type: ignore[index]
        )

    @task
    def create_quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_quiz_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    @before_kickoff
    def before_kickoff(self) -> None:
        print("Starting the study assistant crew...")

    @after_kickoff
    def after_kickoff(self) -> None:
        print("Study assistant crew completed.")
