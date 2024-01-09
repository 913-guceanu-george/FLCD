from hashtable.hash_table import HashTable
from lexer.finite_automaton.fa import FiniteAutomaton
from lexer.grammar.grammar import Grammar
from lexer.grammar.parser import Parser

def test_hashtable():
    htable: HashTable = HashTable(10)
    for i in range(20):
        htable[i] = i
    print(htable)


def test_lexer():
    #lex1 = Lexer("C:\\Users\\maria\\Documents\\Code\\FLCD\\Lab1\\p2.marin")
    #lex1.scan()
    pass

def test_fa():
    fa = FiniteAutomaton()
    try:
        fa.run()
    except ValueError as e:
        print(e)

def test_firsts():
    parser:Parser = Parser() 
    print(parser.follow("S"))
    print(parser.follow("A"))
    print(parser.follow("B"))


def test_parser():
    parser = Parser()
    
    # print(parser.first("S"))
    # print(parser.first("A"))
    # print(parser.first("B"))

    parser.print_table()
    parser.parse_input("adb")

def test_grammar():
    grammar = Grammar()
    grammar.print_grammar()
    #print(f"Is grammar CFG? -> {grammar.cfg_check()}")
    #grammar.check_productions_for_terminal()

