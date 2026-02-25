import os
import random
from question import Question
from player import Player


class Game:
    def __init__(self, questions_file, scores_file):
        self.questions_file = questions_file
        self.scores_file = scores_file
        self.questions_by_level = {}
        self.score = 0
        self.current_level = 0

    def load_questions(self):
        if not os.path.exists(self.questions_file):
            print(f"Error: {self.questions_file} not found.")
            return False

        with open(self.questions_file, "r", encoding="utf-8") as f:
            block = []  # Classify the questions as a block of lines

            for line in f:
                clean_line = line.strip()

                if not clean_line:
                    # Process the block when an empty line is found
                    if block:  # Make sure the block isn't empty
                        level = int(block[1])
                        q = Question(
                            question=block[0],
                            level=level,
                            correct=block[2],
                            wrong=block[3:]
                        )

                        # Group questions by difficulty level
                        if level not in self.questions_by_level:
                            self.questions_by_level[level] = []
                        self.questions_by_level[level].append(q)

                        block = []  # Reset block for the next question
                else:
                    # Not a blank line, so add the text to our current block
                    block.append(clean_line)

            # Process the last block if the file doesn't end with an empty line
            if block:
                level = int(block[1])
                q = Question(
                    question=block[0],
                    level=level,
                    correct=block[2],
                    wrong=block[3:]
                )
                if level not in self.questions_by_level:
                    self.questions_by_level[level] = []
                self.questions_by_level[level].append(q)

        return True

    def play(self):
        # Attempt to load questions; stop if it fails
        if not self.load_questions():
            return

        # Main game loop
        while self.current_level in self.questions_by_level:
            # Pick a random question for the current level
            current_question = random.choice(self.questions_by_level[self.current_level])
            answers = current_question.get_shuffled_answers()

            # Print question and shuffled answers
            print(f"Livello {self.current_level}) {current_question.question}")
            for idx, ans in enumerate(answers, 1):
                print(f"        {idx}. {ans}")

            # Get and validate user input
            try:
                user_input = int(input("Inserisci la risposta: "))
            except ValueError:
                user_input = -1

            # Check if the answer is correct
            if 1 <= user_input <= 4 and answers[user_input - 1] == current_question.correct:
                print("Risposta corretta!\n")
                self.score += 1
                self.current_level += 1
            else:
                correct_index = answers.index(current_question.correct) + 1
                print(f"Risposta sbagliata! La risposta corretta era: {correct_index}\n")
                break

                # Game over process
        print(f"Hai totalizzato {self.score} punti!")
        nickname = input("Inserisci il tuo nickname: ")

        # Create a Player object and save the final score
        player = Player(nickname, self.score)
        player.save_score(self.scores_file)