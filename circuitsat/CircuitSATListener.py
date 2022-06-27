# Generated from C:/Users/oscar/Downloads/Development/TL\CircuitSAT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CircuitSATParser import CircuitSATParser
else:
    from CircuitSATParser import CircuitSATParser

# This class defines a complete listener for a parse tree produced by CircuitSATParser.
class CircuitSATListener(ParseTreeListener):

    # Enter a parse tree produced by CircuitSATParser#circuit.
    def enterCircuit(self, ctx:CircuitSATParser.CircuitContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#circuit.
    def exitCircuit(self, ctx:CircuitSATParser.CircuitContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#block.
    def enterBlock(self, ctx:CircuitSATParser.BlockContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#block.
    def exitBlock(self, ctx:CircuitSATParser.BlockContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#statement.
    def enterStatement(self, ctx:CircuitSATParser.StatementContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#statement.
    def exitStatement(self, ctx:CircuitSATParser.StatementContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#assignment.
    def enterAssignment(self, ctx:CircuitSATParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#assignment.
    def exitAssignment(self, ctx:CircuitSATParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#identifierFunctionCall.
    def enterIdentifierFunctionCall(self, ctx:CircuitSATParser.IdentifierFunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#identifierFunctionCall.
    def exitIdentifierFunctionCall(self, ctx:CircuitSATParser.IdentifierFunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#printlnFunctionCall.
    def enterPrintlnFunctionCall(self, ctx:CircuitSATParser.PrintlnFunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#printlnFunctionCall.
    def exitPrintlnFunctionCall(self, ctx:CircuitSATParser.PrintlnFunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#printFunctionCall.
    def enterPrintFunctionCall(self, ctx:CircuitSATParser.PrintFunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#printFunctionCall.
    def exitPrintFunctionCall(self, ctx:CircuitSATParser.PrintFunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#assertFunctionCall.
    def enterAssertFunctionCall(self, ctx:CircuitSATParser.AssertFunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#assertFunctionCall.
    def exitAssertFunctionCall(self, ctx:CircuitSATParser.AssertFunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#sizeFunctionCall.
    def enterSizeFunctionCall(self, ctx:CircuitSATParser.SizeFunctionCallContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#sizeFunctionCall.
    def exitSizeFunctionCall(self, ctx:CircuitSATParser.SizeFunctionCallContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#ifStatement.
    def enterIfStatement(self, ctx:CircuitSATParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#ifStatement.
    def exitIfStatement(self, ctx:CircuitSATParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#ifStat.
    def enterIfStat(self, ctx:CircuitSATParser.IfStatContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#ifStat.
    def exitIfStat(self, ctx:CircuitSATParser.IfStatContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#elseIfStat.
    def enterElseIfStat(self, ctx:CircuitSATParser.ElseIfStatContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#elseIfStat.
    def exitElseIfStat(self, ctx:CircuitSATParser.ElseIfStatContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#elseStat.
    def enterElseStat(self, ctx:CircuitSATParser.ElseStatContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#elseStat.
    def exitElseStat(self, ctx:CircuitSATParser.ElseStatContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#functionDecl.
    def enterFunctionDecl(self, ctx:CircuitSATParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#functionDecl.
    def exitFunctionDecl(self, ctx:CircuitSATParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#forStatement.
    def enterForStatement(self, ctx:CircuitSATParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#forStatement.
    def exitForStatement(self, ctx:CircuitSATParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#whileStatement.
    def enterWhileStatement(self, ctx:CircuitSATParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#whileStatement.
    def exitWhileStatement(self, ctx:CircuitSATParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#assemblerStatement.
    def enterAssemblerStatement(self, ctx:CircuitSATParser.AssemblerStatementContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#assemblerStatement.
    def exitAssemblerStatement(self, ctx:CircuitSATParser.AssemblerStatementContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#idList.
    def enterIdList(self, ctx:CircuitSATParser.IdListContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#idList.
    def exitIdList(self, ctx:CircuitSATParser.IdListContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#exprList.
    def enterExprList(self, ctx:CircuitSATParser.ExprListContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#exprList.
    def exitExprList(self, ctx:CircuitSATParser.ExprListContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#boolExpression.
    def enterBoolExpression(self, ctx:CircuitSATParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#boolExpression.
    def exitBoolExpression(self, ctx:CircuitSATParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#numberExpression.
    def enterNumberExpression(self, ctx:CircuitSATParser.NumberExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#numberExpression.
    def exitNumberExpression(self, ctx:CircuitSATParser.NumberExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:CircuitSATParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:CircuitSATParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#notExpression.
    def enterNotExpression(self, ctx:CircuitSATParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#notExpression.
    def exitNotExpression(self, ctx:CircuitSATParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#orExpression.
    def enterOrExpression(self, ctx:CircuitSATParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#orExpression.
    def exitOrExpression(self, ctx:CircuitSATParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#unaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:CircuitSATParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#unaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:CircuitSATParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#powerExpression.
    def enterPowerExpression(self, ctx:CircuitSATParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#powerExpression.
    def exitPowerExpression(self, ctx:CircuitSATParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#eqExpression.
    def enterEqExpression(self, ctx:CircuitSATParser.EqExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#eqExpression.
    def exitEqExpression(self, ctx:CircuitSATParser.EqExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#andExpression.
    def enterAndExpression(self, ctx:CircuitSATParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#andExpression.
    def exitAndExpression(self, ctx:CircuitSATParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#inExpression.
    def enterInExpression(self, ctx:CircuitSATParser.InExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#inExpression.
    def exitInExpression(self, ctx:CircuitSATParser.InExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#stringExpression.
    def enterStringExpression(self, ctx:CircuitSATParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#stringExpression.
    def exitStringExpression(self, ctx:CircuitSATParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#expressionExpression.
    def enterExpressionExpression(self, ctx:CircuitSATParser.ExpressionExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#expressionExpression.
    def exitExpressionExpression(self, ctx:CircuitSATParser.ExpressionExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#addExpression.
    def enterAddExpression(self, ctx:CircuitSATParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#addExpression.
    def exitAddExpression(self, ctx:CircuitSATParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#compExpression.
    def enterCompExpression(self, ctx:CircuitSATParser.CompExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#compExpression.
    def exitCompExpression(self, ctx:CircuitSATParser.CompExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#nullExpression.
    def enterNullExpression(self, ctx:CircuitSATParser.NullExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#nullExpression.
    def exitNullExpression(self, ctx:CircuitSATParser.NullExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CircuitSATParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CircuitSATParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#multExpression.
    def enterMultExpression(self, ctx:CircuitSATParser.MultExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#multExpression.
    def exitMultExpression(self, ctx:CircuitSATParser.MultExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#listExpression.
    def enterListExpression(self, ctx:CircuitSATParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#listExpression.
    def exitListExpression(self, ctx:CircuitSATParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:CircuitSATParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:CircuitSATParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#inputExpression.
    def enterInputExpression(self, ctx:CircuitSATParser.InputExpressionContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#inputExpression.
    def exitInputExpression(self, ctx:CircuitSATParser.InputExpressionContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#list.
    def enterList(self, ctx:CircuitSATParser.ListContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#list.
    def exitList(self, ctx:CircuitSATParser.ListContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#indexes.
    def enterIndexes(self, ctx:CircuitSATParser.IndexesContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#indexes.
    def exitIndexes(self, ctx:CircuitSATParser.IndexesContext):
        pass


    # Enter a parse tree produced by CircuitSATParser#opcode.
    def enterOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        pass

    # Exit a parse tree produced by CircuitSATParser#opcode.
    def exitOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        pass



del CircuitSATParser