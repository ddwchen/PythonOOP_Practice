class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, *nums):
        self.addNum = 0
        for value in nums:
            self.addNum += value
        self.result += self.addNum
        return self
        
    def subtract(self, *nums):
        self.subtractNum = 0
        for value in nums:
            self.subtractNum -= value
        self.result -= self.subtractNum
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).add(5).result
print(x)
