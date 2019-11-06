"""
身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリ実装
参考となるWebアプリ https://keisan.casio.jp/exec/system/1161228732
小数点第2位まで表示する

"""


class BMI:

    def calculate(self):
        return f'{self.weight / (self.height ** 2):.2f}'


bmi = BMI()
bmi.height = int(input("身長を入力(cm):")) / 100
bmi.weight = int(input("体重を入力(kg):"))

print('あなたのBMIは' + str(bmi.calculate()) + 'です。')
