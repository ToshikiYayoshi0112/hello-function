"""
関数にまとめて再利用しやすくしてみよう
関数を記述する前に使用するときを考える

"""


def caluclate_warikan(amount, number_of_people):
    quotinet = amount // number_of_people
    remainder = amount % number_of_people
    return f'1人あたり:{quotinet}円, 端数: {remainder}円'

# print(warikan(amount=1500, number_of_people=3))
# print(warikan(amount=2000, number_of_people=3))
# print(warikan(amount=3647, number_of_people=4))
