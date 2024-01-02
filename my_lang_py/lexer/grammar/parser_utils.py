from enum import Enum

class ParserState(Enum):
    NORMAL = 0
    BACK = 1 
    FINAL = 2
    ERROR = 3

# Stack class, used to store the input and output stacks
class Stack:
    def __init__(self) -> None:
        self.__stack = []
    
    def push(self, element):
        self.__stack.append(element)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        return self.__stack[-1]
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def __str__(self) -> str:
        return str(self.__stack)

class Configuration:
    def __init__(self, state:ParserState, input_stack:Stack, output_stack:Stack, position:int) -> None:
        self.state = state
        self.input_stack = input_stack
        self.output_stack = output_stack
        self.position = position
