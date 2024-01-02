class NotCFG(Exception):
    "This grammar is not an exception"

class ParserError(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(message)
