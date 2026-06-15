import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        hashmap={
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':lambda a,b:int(a/b),
        }
        for element in tokens:
            if element in hashmap:
                b=self.stack.pop()
                a=self.stack.pop()
                self.stack.append(hashmap[element](a,b))
            else: self.stack.append(int(element))
        return self.stack[0]
        