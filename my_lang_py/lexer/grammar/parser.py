from typing import Dict, List
from lexer.grammar.grammar import Grammar
from exceptions.customs import ParserError

class Parser:

    def __init__(self) -> None:
        # Grammar structure
        self.__grammar = Grammar().get_grammar()
        self.__productions:dict = self.__grammar["productions"]
        self.__terminals:list = self.__grammar["terminals"]
        self.__non_terminals:list = self.__grammar["non_terminals"]
        self.__starting_symbol:str = self.__grammar["start_symbol"]
        self.__epsilon:str = self.__grammar["epsilon"]

        # Parser structure
        self.__parsing_table:Dict[str, Dict] = dict()
        self.__stack:List[str] = list()

        self.__construct_table()

    def first(self, non_terminal:str, checked_non_terms:List[str] = list()) -> List[str]:
        # First check if the given non-terminal is in our grammar
        if non_terminal not in self.__non_terminals:
           raise ParserError(f"Non-terminal {non_terminal} is not in the grammar")

        # List of first non-terminals
        first_elems:List[str] = list()
        for productions in self.__productions[non_terminal]:
            first_elem = productions[0]
            # Is first elem a terminal?
            if first_elem in self.__terminals and first_elem not in first_elems:
                first_elems.append(first_elem)
                continue
            # Or a non-terminal?
            if first_elem in self.__non_terminals and first_elem not in checked_non_terms:
                checked_non_terms.append(first_elem)
                # We have to keep a list of checked non-terminals in case of recursion
                firsts:List[str] = self.first(first_elem, checked_non_terms)
                for el in firsts:
                    if el not in first_elems:
                        first_elems.append(el)
        return first_elems

    def follow(self, non_terminal:str) -> List[str]:
        # First check if the given non-terminal is in our grammar
        if non_terminal not in self.__non_terminals:
           raise ParserError(f"Non-terminal {non_terminal} is not in the grammar")

        follow_elems:List[str] = list()
        checked_non_terms:List[str] = list()

        # Going through all the productions
        for nt in self.__productions:
            for productions in self.__productions[nt]:
                for i in range(len(productions)):
                    # Check if we have found our non-terminal in a production
                    if i != len(productions)-1 and productions[i] == non_terminal:
                        for j in range(i+1, len(productions)):
                            elem = productions[j]
                            # Is it a terminal?
                            if elem in self.__terminals and elem not in follow_elems and elem != self.__epsilon:
                                follow_elems.append(elem)
                                continue
                            # Or a non-terminal?
                            if elem in self.__non_terminals and elem not in checked_non_terms:
                                checked_non_terms.append(elem)
                                """
                                In case of a non-terminal all we have to do is
                                 append the firsts of that non-terminal to our list
                                """
                                firsts:List[str] = self.first(elem)
                                for el in firsts:
                                    if el not in follow_elems:
                                        follow_elems.append(el)
        if non_terminal == self.__starting_symbol:
            follow_elems.append("$")
        # Now we check if the productions of our starting symbol are ending in our non-terminal
        for p in self.__productions[self.__starting_symbol]:
            if p[-1] == non_terminal:
                follow_elems.append("$")
                break
        return follow_elems


    def __construct_table(self) -> None:
        for nt in self.__productions:
            firsts:List[str] = self.first(nt)
            follows:List[str] = self.follow(nt)
            self.__parsing_table[nt] = dict()

            # All eps-productions are placed under the follow sets
            # Everything else is placed under the first sets

            for prod in self.__productions[nt]:
                if prod[0] == self.__epsilon:
                    for term in follows:
                        self.__parsing_table[nt][term] = prod
                    continue
                for term in firsts:
                    self.__parsing_table[nt][term] = prod

    def parse_input(self, input:str) -> None:
        # First terminal in the input must be in the first of the starting symbol
        if input[0] not in self.first(self.__starting_symbol):
            raise ParserError(f"Input {input} is not in the grammar")

        # Now we can begin the parsing
        self.__stack.append("$")
        prod:List[str] = self.__parsing_table[self.__starting_symbol][input[0]]
        prod.reverse()
        # We add the elements of the corresponding production
        for t in prod:
            self.__stack.append(t)
        
        input_index = 0
        while self.__stack[-1] != "$":
            print(f"Stack: {self.__stack}")
            current_in_stack = self.__stack[-1]
            # If we have reached a terminal corresponding to the current input's terminal, we move along
            if current_in_stack  == input[input_index]:
                input_index += 1
                self.__stack.pop()
                continue
            # If we reached epsilon, we just pop it and move along
            if current_in_stack  == self.__epsilon:
                self.__stack.pop()
                continue
            
            # If we reach a terminal, we have to check the table for it's productions
            if current_in_stack in self.__non_terminals:
                self.__stack.pop()
                prod = self.__parsing_table[current_in_stack][input[input_index]]
                prod.reverse()
                for t in prod:
                    self.__stack.append(t)
                continue

            # If we reach an unparsable case, the input doesn't fit
            if self.__stack[-1] != "$":
                raise ParserError(f"Input {input} cannot be parsed.")

        # One last print
        print(f"Stack: {self.__stack}")
        print(f"Input {input} accepted!")

    def print_table(self) -> None:
        for nt in self.__parsing_table:
            for term in self.__parsing_table[nt]:
                print(f"({nt},{term}) -> {self.__parsing_table[nt][term]}")
