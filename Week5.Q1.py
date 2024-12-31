class MultiFuncs():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def FourCal(self):
        print (f'덧셈의 결과는 {self.x + self.y}입니다.')
        print (f'뺄셈의 결과는 {self.x - self.y}입니다.')
        print (f'곱셈의 결과는 {self.x * self.y}입니다.')
        print (f'나눗셈의 결과는 {self.x / self.y}입니다.')
        

# Check if your code has no problem at all

obj = MultiFuncs(50, 10)
obj.FourCal()
#obj = MultiFuncs(20, 80)
#obj.FourCal()