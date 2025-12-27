import pandas as pd

df = pd.read_csv('inputs.csv', header=None)

df_transposed = df.T
product_ids = df_transposed[0].tolist()


invalid_ids = []

for product_id in product_ids:
    list = product_id.split('-')
    first = int(list[0])
    second = int(list[1])
    for num in range(first,second+1):
        s = str(num)

        for pattern_len in range(1, len(s) // 2 +1):
            pattern = s[:pattern_len]

            if pattern * (len(s) // pattern_len) == s:
                if len(s) // pattern_len >= 2:
                    invalid_ids.append(num)
                    break
print(sum(invalid_ids))
