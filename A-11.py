"""
身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリ実装
参考となるWebアプリ https://keisan.casio.jp/exec/system/1161228732
小数点第2位まで表示する

とりあえず
height 168cm
weight 62kg
"""


class BMI:
    def __init__(self, weight, height):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return f'{self.weight / (self.height / 100) ** 2 :.2f}'


personal_bmi = BMI(weight=62, height=168)
print(personal_bmi.calculate_bmi())
