import pandas as pd

position = 50
counter = 0

inputs = pd.read_csv('inputs.csv')

inputs['direction'] = [i[:1] for i in inputs['input'].tolist()]
inputs['clicks'] = [int(i[1:]) for i in inputs['input'].tolist()]

for _, row in inputs.iterrows():

    direction = row['direction']
    click = row['clicks']


    for _ in range(click):
        if direction == 'L':
            position = (position - 1) % 100
        elif direction == 'R':
            position = (position + 1) % 100
    
        if position == 0:
            counter += 1

print(counter)