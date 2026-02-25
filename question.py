import random

class Question:
    def __init__(self, question, level, correct, wrong):
        self.question = question
        self.level = level
        self.correct = correct
        self.wrong = wrong # may be a list but do not need to declare anything thanks to duck typing
        # i.e. wrong: list[str] in the __init__ is not mandatory

    def __str__(self):
        """ pretty print used to debug """
        return f"[Level {self.level}] {self.question} -> Correct: {self.correct}, Wrong: {self.wrong}"

    def get_shuffled_answers(self):
        """ combine and shuffle the answer """
        all_answer = [self.correct] + self.wrong
        random.shuffle(all_answer)
        return all_answer