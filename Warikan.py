# 関数はなんのためにある?
"""コードを再利用するため
   一連の処理に名前をつけるため
"""


# amount = 1500
# number_of_people = 3

# print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")


def warikan(amount, number_of_people):
    return f"1人あたり:{amount // number_of_people}円, 端数: {amount % number_of_people}円"


# Table1: 1500円で3人
Table1 = warikan(1500, 3)
print(Table1)

# Table2: 2000円で3人
Table2 = warikan(2000, 3)
print(Table2)

# Table3: 3674円で4人
Table3 = warikan(3674, 4)
print(Table3)
