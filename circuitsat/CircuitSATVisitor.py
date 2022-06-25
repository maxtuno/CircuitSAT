# Generated from C:/Users/oscar/Documents/GitHub/circuitsat\CircuitSAT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CircuitSATParser import CircuitSATParser
else:
    from CircuitSATParser import CircuitSATParser

# This class defines a complete generic visitor for a parse tree produced by CircuitSATParser.

class CircuitSATVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CircuitSATParser#circuitsat.
    def visitCircuitsat(self, ctx:CircuitSATParser.CircuitsatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#end.
    def visitEnd(self, ctx:CircuitSATParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#line.
    def visitLine(self, ctx:CircuitSATParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#opcode.
    def visitOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        return self.visitChildren(ctx)



del CircuitSATParser