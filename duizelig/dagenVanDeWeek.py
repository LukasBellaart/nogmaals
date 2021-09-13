dagen = {
    "ma": 1,
    "di": 2,
    "wo": 3,
    'do': 4,
    'vr': 5,
    'za': 6,
    'zo': 7
}


dagenlijst = [
    "maandag",
    'dinsdag',
    'woensdag',
    'donderdag',
    'vrijdag',
    'zaterdag',
    'zondag'
]

dag = input("welke dag? ")
x = dagen[dag]
i = 1
while i <= x:
    print(str(dagenlijst[i-1]))
    i = i + 1
