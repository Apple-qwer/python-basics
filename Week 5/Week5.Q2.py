# Write your code
class FultiFuncs2(MultiFuncs):
    def Maxima(self, x):
        print(f'주어진 리스트의 최대값은 {max(x)}입니다.')
    def Mean(self, x):
        mean = sum(x) / len(x)
        print(f'주어진 리스트의 평균은 {mean}입니다.')


# Validate your class

obj2 = FultiFuncs2(30, 4)
obj2.FourCal()
obj2.Maxima([10, 90, 65, 25, 40])
obj2.Mean([70, 10, 25, 5, 44, 1.5])