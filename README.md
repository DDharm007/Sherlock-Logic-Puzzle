<!-- Sherlock Puzzle Solver README -->

<div align="center">

# 🕵️ Sherlock Logic Puzzle  

<img src="https://media.tenor.com/QU8XhZbT2D4AAAAM/sherlock-holmes.gif" width="300"/>

### 🔍 One Truth, Two Lies — Can Sherlock deduce the culprit?

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

## ✨ About
This project simulates a **Sherlock Holmes–style deduction puzzle**.  
There are 3 suspects, each giving a statement. Only **one suspect tells the truth**, and the rest lie.  
The program uses logic to determine **who the real culprit is**.

---

## 🛠️ How it Works
- Each suspect makes a statement.  
- The program checks possible truth-tellers.  
- If exactly one statement aligns with the rules, Sherlock deduces the culprit.  

---

## 📂 Code Example

```python
class Sherlock:
    def __init__(self):
        self.suspects = {
            "Suspect A": "Suspect B did it.",
            "Suspect B": "Suspect C is lying.",
            "Suspect C": "I am innocent."
        }

    def deduce_truth(self):
        for suspect, statement in self.suspects.items():
            if self.is_truthful(suspect):
                culprit = self.evaluate_statement(statement)
                print(f"{suspect} is telling the truth. Therefore, the culprit is {culprit}.")
                return

    def is_truthful(self, suspect):
        statements = {
            "Suspect A": self.suspects["Suspect B"] == "I am innocent.",
            "Suspect B": self.suspects["Suspect C"] == "Suspect C is lying.",
            "Suspect C": False,
        }
        return sum(statements.values()) == 1 and statements[suspect]

    def evaluate_statement(self, statement):
        if "did it" in statement:
            return statement.split()[0]
        elif "lying" in statement:
            return "Suspect C"
        elif "innocent" in statement:
            return "Suspect C"
        return "Unknown"


sherlock = Sherlock()
sherlock.deduce_truth()

# Clone the repo
git clone https://github.com/your-username/sherlock-puzzle.git
cd sherlock-puzzle

# Run the script
python sherlock.py
