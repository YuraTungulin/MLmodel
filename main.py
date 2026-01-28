import pandas as pd
import random
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
random.seed(42)

print("=== Исследование справедливости: Пицца для студентов ===\n")

groups = ["Физмат", "Гумфак", "Медфак"]
students = []

for i in range(150):
    skill = random.randint(1, 100)
    group = random.choices(groups, weights=[0.4, 0.3, 0.3])[0]
    if group == "Физмат":
        got_pizza = skill > 40
    elif group == "Гумфак":
        got_pizza = skill > 70
    else:
        got_pizza = skill > 60
    students.append({
        "Name": f"Студент_{i+1}",
        "Group": group,
        "Skill": skill,
        "GotPizza": got_pizza
    })

df = pd.DataFrame(students)

# Старые шансы
frequencies = {}
for g in groups:
    subgroup = df[df['Group'] == g]
    got = subgroup[subgroup['GotPizza']]
    chance = len(got) / len(subgroup)
    frequencies[g] = chance
    print(f"{g}: {len(got)}/{len(subgroup)} = {chance*100:.1f}% получили пиццу")

# Фиксированные коэффициенты
weights = {
    "Физмат": 1.17,
    "Гумфак": 1.95,
    "Медфак": 1.21
}

print("\nФиксированные коэффициенты:")
for g, w in weights.items():
    print(f"{g}: вес = {w}")

def fair_classifier(skill, group, weights):
    base_threshold = 60
    adjusted_threshold = base_threshold / weights[group]
    return skill > adjusted_threshold

df['FairDecision'] = df.apply(lambda row: fair_classifier(row['Skill'], row['Group'], weights), axis=1)
df['TrulyDeserving'] = df['Skill'] > 60

TP = sum(df['FairDecision'] & df['TrulyDeserving'])
TN = sum(~df['FairDecision'] & ~df['TrulyDeserving'])
FP = sum(df['FairDecision'] & ~df['TrulyDeserving'])
FN = sum(~df['FairDecision'] & df['TrulyDeserving'])

accuracy = (TP + TN) / len(df)
left_out = FN

print(f"\nОбщая точность справедливого классификатора: {accuracy*100:.2f}%")
print(f"Студентов, которые должны были получить пиццу, но не получили: {left_out}")

print("\nНовый шанс получить пиццу по группам:")
for g in groups:
    subgroup = df[df['Group'] == g]
    got = subgroup[subgroup['FairDecision']]
    chance = len(got) / len(subgroup)
    print(f"{g}: {chance*100:.1f}% получили пиццу")
