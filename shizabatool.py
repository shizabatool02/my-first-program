from collections import  deque
open = ["[", "{", "("]
close = ["]", "}", ")"]
class valid_equation:
    def __init__(self):
        self.stack = deque()
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            False
    def size(self):
        return len(self.stack)


    def check(self,checkequation):
        for brackets in checkequation:
            if brackets in open:
                self.push(brackets)
            elif brackets in close:
                pos = close.index(brackets)
                if ((self.size() > 0) and (open[pos] == self.stack[self.size() - 1])):
                    self.pop()
                else:
                    return " InValid Equation"
        if self.size() == 0:
            return "Valid Equation"
        else:
            return "InValid Equation"

s = valid_equation()
equation1 = '(“({a+b})”)'
equation2 = '(“)))((a+b){“}'
equation3 = '(“((a+b))”)'
equation4 = '(“))”)'
equation5 = '(“[a+b]*(x+2y)*{gg+kk}”) '
print("This ",equation1 ,"equation is ",s.check(equation1))
print("This ",equation2 ,"equation is ",s.check(equation2))
print("This ",equation3 ,"equation is ",s.check(equation3))
print("This ",equation4 ,"equation is ",s.check(equation4))
print("This ",equation5 ,"equation is ",s.check(equation5))


