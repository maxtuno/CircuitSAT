# Generated from C:/Users/oscar/Documents/GitHub/circuitsat\CircuitSAT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CircuitSATParser import CircuitSATParser
else:
    from CircuitSATParser import CircuitSATParser

# This class defines a complete listener for a parse tree produced by CircuitSATParser.
class CircuitSATListener(ParseTreeListener):

    # Enter a parse tree produced by CircuitSATParser#circuitsat.
    def enterCircuitsat(self, ctx:CircuitSATParser.CircuitsatContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#circuitsat.
    def exitCircuitsat(self, ctx:CircuitSATParser.CircuitsatContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#end.
    def enterEnd(self, ctx:CircuitSATParser.EndContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#end.
    def exitEnd(self, ctx:CircuitSATParser.EndContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#line.
    def enterLine(self, ctx:CircuitSATParser.LineContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#line.
    def exitLine(self, ctx:CircuitSATParser.LineContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#opcode.
    def enterOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#opcode.
    def exitOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        pass



del CircuitSATParser