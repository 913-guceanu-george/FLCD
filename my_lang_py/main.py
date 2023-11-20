import re

from hashtable.hash_table import HashTable
from lexer.lexer import Lexer


def test_hashtable():
    htable: HashTable = HashTable(10)
    for i in range(20):
        htable[i] = i
    print(htable)


def playground():
    pass


if __name__ == "__main__":
    # test_hashtable()
    lex1 = Lexer("/home/marianguceanu/Documents/Code/FLCD/Lab1/p1err.marin")
    lex1.scan()
    # lex2 = Lexer("C:\\Users\\maria\\Documents\\Code\\FLCD\\Lab1\\Definitions\\Token.in")
    # lex2.scan()
    # playground()
