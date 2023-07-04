class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []
        for token in tokens:
            if token in operations:
                operation = operations[token]
                temp=operation(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack.pop()
#     def evalRPN(self, tokens):
#         stack=[]
#         operations=["-","+","/","*"]
#         for f in tokens:
#             if f in operations:
#                 temp=None
#                 if f=="+":
#                     temp= int(stack[-2])+int(stack[-1])
#                 elif f=="-":
#                     temp= int(stack[-2])-int(stack[-1])
#                 elif f=="*":
#                     temp= int(stack[-2])*int(stack[-1])
#                 elif f=="/":
#                     temp= int(stack[-2])/int(stack[-1])
#                 else:
#                     pass
#                 stack.pop(-1)
#                 stack.pop(-1)
#                 stack.append(int(temp))
                
#             else:
#                 stack.append(f)
#         return stack[0]
                

