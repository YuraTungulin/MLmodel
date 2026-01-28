# Pizza Fairness Simulation

Simulation of fairness in pizza distribution among student groups using Python.

## Description
This project simulates the distribution of pizza among students from different faculties:

- Three groups: Физмат, Гумфак, Медфак
- Each student has a "skill" score (1–100)
- Original pizza distribution rules:
  - Физмат: skill > 40
  - Гумфак: skill > 70
  - Медфак: skill > 60
- Calculates how many students in each group received pizza
- Applies a "fair classifier" with fixed weights per group

Outputs:
- Accuracy of the fair classifier
- Students who deserved pizza but didn’t get it
- New chance to receive pizza per group

## Installation
Requires Python 3 and the following libraries:
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```
