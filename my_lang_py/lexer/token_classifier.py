import re
from typing import List

from hashtable.hash_table import HashTable


class TokenClassifier:
    def __init__(self, st: HashTable, regexes: dict, keywords) -> None:
        self.__key = 0
        self.__regexes = regexes
        self.__keywords = keywords

    def is_identifier(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["identifier"], token)
        self.__key += 1
        return regex_match is not None

    def is_operator(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["operator"], token)
        return regex_match is not None

    def is_relational_operator(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["relational_operator"], token)
        return regex_match is not None

    def is_number(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["number"], token)
        self.__key += 1
        return regex_match is not None

    def is_string(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["string"], token)
        self.__key += 1
        return regex_match is not None

    def is_char(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["char"], token)
        self.__key += 1
        return regex_match is not None

    def is_separator(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["separator"], token)
        return regex_match is not None

    def is_quotes(self, token: str) -> bool:
        regex_match = re.match(self.__regexes["quotes"], token)
        return regex_match is not None

    def is_keyword(self, token: str) -> bool:
        return token in self.__keywords
