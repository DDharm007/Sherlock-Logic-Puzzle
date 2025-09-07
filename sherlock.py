class Sherlock:
    def __init__(self):
        self.suspects = {
            "Suspect A": "Suspect B did it.",
            "Suspect B": "Suspect C is lying.",
            "Suspect C": "I am innocent."
        }

    def deduce_truth(self):
        """
        Determine which suspect is guilty based on the statements.
        Only one suspect tells the truth, and the rest lie.
        """
        for suspect, statement in self.suspects.items():
            if self.is_truthful(suspect):
                culprit = self.evaluate_statement(statement)
                print(f"{suspect} is telling the truth. Therefore, the culprit is {culprit}.")
                return

    def is_truthful(self, suspect):
        """
        Check if a given suspect's statement aligns with the scenario
        where only one tells the truth.
        """
        statements = {
            "Suspect A": self.suspects["Suspect B"] == "I am innocent.",
            "Suspect B": self.suspects["Suspect C"] == "Suspect C is lying.",
            "Suspect C": False,  # Because Suspect C says they're innocent but they're guilty
        }
        return sum(statements.values()) == 1 and statements[suspect]

    def evaluate_statement(self, statement):
        """
        Parse the statement to determine who the culprit is.
        """
        if "did it" in statement:
            return statement.split()[0]  # Extract the name
        elif "lying" in statement:
            return "Suspect C"  # A lying claim implicates the subject
        elif "innocent" in statement:
            return "Suspect C"  # Claiming innocence if guilty
        return "Unknown"


sherlock = Sherlock()
sherlock.deduce_truth()
