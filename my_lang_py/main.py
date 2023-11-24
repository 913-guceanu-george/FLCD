import re

from hashtable.hash_table import HashTable
from lexer.finite_automaton.fa import FiniteAutomaton
from lexer.lexer import Lexer


def test_hashtable():
    htable: HashTable = HashTable(10)
    for i in range(20):
        htable[i] = i
    print(htable)


def playground():
    pass


if __name__ == "__main__":
    # lex1 = Lexer("C:\\Users\\maria\\Documents\\Code\\FLCD\\Lab1\\p2.marin")
    # lex1.scan()
    fa = FiniteAutomaton()
    try:
        fa.run()
    except ValueError as e:
        print(e)
