"""
関数にまとめて再利用しやすくしてみよう
関数を記述する前に使用するときを考える

"""


def warikan(amount, number_of_people):
    return f"1人あたり:{amount // number_of_people}円, 端数:" \
        f" {amount % number_of_people}円"


print(warikan(amount=1500, number_of_people=3))
print(warikan(amount=2000, number_of_people=3))
print(warikan(amount=3647, number_of_people=4))
