import sys
from antlr4 import *

from .CircuitSATLexer import CircuitSATLexer
from .CircuitSATParser import CircuitSATParser
from .CircuitSAT import CicuitSAT


def main():
    if len(sys.argv) <= 1:
        print('usage: csat file.csat')
        exit(0)

    file_name = sys.argv[1]
    input_stream = FileStream(file_name)
    lexer = CircuitSATLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    parser = CircuitSATParser(token_stream)
    tree = parser.circuitsat()

    csat = CicuitSAT(file_name.replace('.csat', '.cnf'))
    result = csat.visit(tree)


if __name__ == '__main__':
    main()
