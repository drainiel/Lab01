import os


class Player:
    def __init__(self, nickname, score):
        # Force the types to avoid sorting crashes
        self.nickname = str(nickname)
        self.score = int(score)

    def save_score(self, filename):
        scores = []

        # Read existing scores if the file exists
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        try:
                            # Handle nicknames with spaces
                            nick = " ".join(parts[:-1])
                            pts = int(parts[-1])
                            scores.append((nick, pts))
                        except ValueError:
                            # Skip lines that don't have a valid integer score
                            continue

        # Add the current player's score
        scores.append((self.nickname, self.score))

        # Sort scores in descending order based on the integer score
        scores.sort(key=lambda x: x[1], reverse=True)

        # Save the sorted leaderboard back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            for nick, pts in scores:
                file.write(f"{nick} {pts}\n")