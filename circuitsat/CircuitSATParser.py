# Generated from C:/Users/oscar/Documents/GitHub/circuitsat\CircuitSAT.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,3,2,22,8,2,1,2,3,2,25,8,2,1,
        3,1,3,1,3,0,0,4,0,2,4,6,0,0,27,0,13,1,0,0,0,2,18,1,0,0,0,4,21,1,
        0,0,0,6,26,1,0,0,0,8,9,3,4,2,0,9,10,5,7,0,0,10,12,1,0,0,0,11,8,1,
        0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,
        13,1,0,0,0,16,17,3,2,1,0,17,1,1,0,0,0,18,19,5,2,0,0,19,3,1,0,0,0,
        20,22,3,6,3,0,21,20,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,25,5,
        5,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,5,1,0,0,0,26,27,5,1,0,0,27,
        7,1,0,0,0,3,13,21,24
    ]

class CircuitSATParser ( Parser ):

    grammarFileName = "CircuitSAT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "OPCODE", "END", "NAME", "NUMBER", "COMMENT", 
                      "WS", "EOL" ]

    RULE_circuitsat = 0
    RULE_end = 1
    RULE_line = 2
    RULE_opcode = 3

    ruleNames =  [ "circuitsat", "end", "line", "opcode" ]

    EOF = Token.EOF
    OPCODE=1
    END=2
    NAME=3
    NUMBER=4
    COMMENT=5
    WS=6
    EOL=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CircuitsatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end(self):
            return self.getTypedRuleContext(CircuitSATParser.EndContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitSATParser.LineContext)
            else:
                return self.getTypedRuleContext(CircuitSATParser.LineContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitSATParser.EOL)
            else:
                return self.getToken(CircuitSATParser.EOL, i)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_circuitsat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircuitsat" ):
                listener.enterCircuitsat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircuitsat" ):
                listener.exitCircuitsat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircuitsat" ):
                return visitor.visitCircuitsat(self)
            else:
                return visitor.visitChildren(self)




    def circuitsat(self):

        localctx = CircuitSATParser.CircuitsatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_circuitsat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircuitSATParser.OPCODE) | (1 << CircuitSATParser.COMMENT) | (1 << CircuitSATParser.EOL))) != 0):
                self.state = 8
                self.line()
                self.state = 9
                self.match(CircuitSATParser.EOL)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(CircuitSATParser.END, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd" ):
                return visitor.visitEnd(self)
            else:
                return visitor.visitChildren(self)




    def end(self):

        localctx = CircuitSATParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(CircuitSATParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opcode(self):
            return self.getTypedRuleContext(CircuitSATParser.OpcodeContext,0)


        def COMMENT(self):
            return self.getToken(CircuitSATParser.COMMENT, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = CircuitSATParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.OPCODE:
                self.state = 20
                self.opcode()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircuitSATParser.COMMENT:
                self.state = 23
                self.match(CircuitSATParser.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPCODE(self):
            return self.getToken(CircuitSATParser.OPCODE, 0)

        def getRuleIndex(self):
            return CircuitSATParser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcode" ):
                return visitor.visitOpcode(self)
            else:
                return visitor.visitChildren(self)




    def opcode(self):

        localctx = CircuitSATParser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_opcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CircuitSATParser.OPCODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





