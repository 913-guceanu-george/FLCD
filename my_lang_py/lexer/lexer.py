from operator import eq
from typing import List

from hashtable.hash_table import HashTable
from lexer.token_classifier import TokenClassifier


class Lexer:
    def __init__(self, input_file: str) -> None:
        self.__regexes: dict = {
            "identifier": r"[a-zA-Z][a-zA-Z0-9]*",
            "operator": r"[+\-*/=%]",
            "relational_operator": r"[<=>]",
            "number": r"^[+\-]?[0-9]+$",
            "string": r"\".*?\"",
            "char": r"'.'",
            "separator": r"^[;:,()\[\]\{\}]{1}$",
            "quotes": r"['\"]"
        }
        self.__keywords: List[str] = (
            "BEGIN END ConsoleRead ConsoleWrite int char string var while if else"
        ).split()
        self.__symbols_output_file: str = "ST.out"
        self.__pif: str = "PIF.out"
        self.__symbol_table: HashTable = HashTable(10)
        self.__key: int = 0
        self.__input_file: str = input_file
        self.__token_classifier = TokenClassifier(
            self.__symbol_table, self.__regexes, self.__keywords
        )
        self.__program: List[str] = self.__split_program()

    def __read_file(self) -> str:
        with open(self.__input_file, "r") as file:
            return file.read()

    def __split_program(self) -> List[str]:
        result: List[str] = list()
        prg = self.__read_file()
        for w in prg.split():
            result.append(w)
        return result

    def __add_token_to_pif(self, token: str) -> None:
        is_str = self.__token_classifier.is_string(token)
        is_char = self.__token_classifier.is_char(token)
        is_quotes = self.__token_classifier.is_quotes(token)
        with open(self.__pif, "a") as file:
            if is_str:
                file.write(f"{token.split("\"")[1]} -> {self.__symbol_table.search(token)}\n")
                return
            if is_char:
                file.write(f"{token.split("\"")[1]} -> {self.__symbol_table.search(token)}\n")
                return
            if is_quotes:
                file.write(f'{token} -> {self.__symbol_table.search(token)}\n')
                return
            file.write(f"{token} -> {self.__symbol_table.search(token)}\n")

    def __add_token_to_st(self, token: str) -> None:
        exists: int = self.__symbol_table.search(token)
        if exists == -1:
            self.__symbol_table.insert(token, self.__key)
            self.__key += 1
            with open(self.__symbols_output_file, "a") as file:
                file.write(f"{self.__symbol_table.search(token)} -> {token}\n")

    def __categorize(self, word: str) -> bool:
        if self.__token_classifier.is_keyword(word):
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_separator(word):
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_operator(word):
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_relational_operator(word):
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_number(word):
            self.__add_token_to_st(word)
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_string(word):
            self.__add_token_to_st(word)
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_char(word):
            self.__add_token_to_st(word)
            self.__add_token_to_pif(word)
            return True
        if self.__token_classifier.is_quotes(word):
            self.__add_token_to_pif(word)
            return True
        return False

    def __add_errors(self, errors: List[str], curr_tok) -> None:
        with open(self.__input_file, "r") as file:
            lines = file.readlines()
            line_no = 0
            for line in lines:
                line_no += 1
                if line.find(curr_tok) != -1:
                    err_msg = f"Lexical error: invalid token {curr_tok} at line {line_no}"
                    if err_msg not in errors:
                        errors.append(err_msg)

    def scan(self):
        print(self.__program)
        errors: List[str] = list()
        for word in self.__program:
            if self.__categorize(word):
                continue
            curr_char = word[0]
            curr_tok = ""
            for i in range(1, len(word) + 1):
                # Classifying the current character, because it may be separator, operator or relational operator
                is_sep = self.__token_classifier.is_separator(curr_char)
                is_op = self.__token_classifier.is_operator(curr_char)
                is_rel_op = False
                is_quotes = self.__token_classifier.is_quotes(curr_char)
                if is_quotes:
                    self.__add_token_to_pif(curr_char)
                if is_op and i < len(word):
                    is_rel_op = self.__token_classifier.is_relational_operator(
                        curr_char + word[i + 1]
                    )
                if not (is_sep or is_op or is_rel_op or i == len(word)):
                    curr_tok += curr_char
                    curr_char = word[i]
                    continue
                if (is_sep or is_op or is_rel_op) and curr_tok == "":
                    self.__add_token_to_pif(curr_char)
                    if i != len(word):
                        curr_char = word[i]
                    curr_tok = ""
                    continue
                if i == len(word) and not (is_sep or is_op or is_rel_op):
                    curr_tok += curr_char
                is_id = self.__token_classifier.is_identifier(curr_tok)
                is_const = (
                    self.__token_classifier.is_char(curr_tok)
                    or self.__token_classifier.is_number(curr_tok)
                    or self.__token_classifier.is_string(curr_tok)
                )
                is_keyword = self.__token_classifier.is_keyword(curr_tok)

                if is_keyword:
                    self.__add_token_to_pif(curr_tok)
                    curr_tok = ""
                    self.__add_token_to_pif(curr_char)
                    if i != len(word):
                        curr_char = word[i]
                    continue
                if is_const or is_id:
                    self.__add_token_to_st(curr_tok)
                    self.__add_token_to_pif(curr_tok)
                    curr_tok = ""
                    if is_sep or is_op or is_rel_op:
                        self.__add_token_to_pif(curr_char)
                    if i != len(word):
                        curr_char = word[i]
                    continue
                self.__add_errors(errors, curr_tok)
        for err in errors:
            print(err)
