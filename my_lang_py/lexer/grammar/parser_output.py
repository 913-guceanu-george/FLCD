from typing import List, Dict

class ParserOutput:
    def __init__(self) -> None:
        self.__filename = "parser.out"
        with open(self.__filename, "a") as f:
            f.write("----STACK----\n") 

    def write_stack(self, stack:List[str]):
        string = ""
        for elem in stack:
            string += elem + " "
        with open(self.__filename, "a") as f:
            f.write(string + "\n") 

    def write_parsing_table(self, parsing_table:Dict[str, Dict[str,List[str]]]):
        string:List[str] = list()
        string.append("\t\t")
        for nt in parsing_table.keys():
            current:str = nt
            for term in parsing_table[nt].keys():
                string[0] += term +  "\t\t"
                current += "\t\t" + str(parsing_table[nt][term])
            current += "\n"
            string.append(current)
        final = ""
        for s in string:
            final += s

        with open(self.__filename, "a") as f:
            f.write("----PARSING TABLE----\n")
            f.write(final) 
