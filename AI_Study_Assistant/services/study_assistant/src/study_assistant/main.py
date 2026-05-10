#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from study_assistant.crews.study_assistant_crew.study_assistant_crew import StudyAssistantCrew


class StudyAssistantState(BaseModel):
    notes: str = ""
    summary: str = ""
    quiz: str = ""


class StudyAssistantFlow(Flow[StudyAssistantState]):
    @start()
    def summarize_notes(self):
        print("Summarizing notes")
        self.state.summary = StudyAssistantCrew().crew().kickoff(inputs={"notes": self.state.notes})

    @listen(summarize_notes)
    def create_quiz(self):
        print("Creating quiz")
        self.state.quiz = StudyAssistantCrew().crew().kickoff(inputs={"summary": self.state.summary})

    @listen(create_quiz)
    def save_quiz(self):
        print("Saving quiz")
        with open("quiz.txt", "w") as f:
            f.write(self.state.quiz)

    @listen(save_quiz)
    def save_quiz(self):    
        print("Saving quiz")
        with open("quiz.txt", "w") as f:
            f.write(self.state.quiz)
    @listen(save_quiz)
    

#     @listen(generate_poem)
#     def save_poem(self):
#         print("Saving poem")
#         with open("poem.txt", "w") as f:
#             f.write(self.state.poem)


# def kickoff():
#     poem_flow = PoemFlow()
#     poem_flow.kickoff()


# def plot():
#     poem_flow = PoemFlow()
#     poem_flow.plot()


# if __name__ == "__main__":
#     kickoff()
