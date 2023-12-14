from hashtable.hash_table import HashTable
from lexer.finite_automaton.fa import FiniteAutomaton
from lexer.grammar.grammar import Grammar


def test_hashtable():
    htable: HashTable = HashTable(10)
    for i in range(20):
        htable[i] = i
    print(htable)


def test_lexer():
#    lex1 = Lexer("C:\\Users\\maria\\Documents\\Code\\FLCD\\Lab1\\p2.marin")
#    lex1.scan()
    pass

def test_fa():
    fa = FiniteAutomaton()
    try:
        fa.run()
    except ValueError as e:
        print(e)


def test_grammar():
    grammar = Grammar()
    grammar.print_grammar()
    print(grammar.cfg_check())
    grammar.check_productions_for_terminal()

if __name__ == "__main__":
    # test_hashtable()
    # test_lexer()
    # test_fa()
    test_grammar()
