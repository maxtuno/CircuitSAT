# Generated from C:/Users/oscar/Downloads/Development/TL\CircuitSAT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CircuitSATParser import CircuitSATParser
else:
    from CircuitSATParser import CircuitSATParser

# This class defines a complete generic visitor for a parse tree produced by CircuitSATParser.

class CircuitSATVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CircuitSATParser#circuit.
    def visitCircuit(self, ctx:CircuitSATParser.CircuitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#block.
    def visitBlock(self, ctx:CircuitSATParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#statement.
    def visitStatement(self, ctx:CircuitSATParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#assignment.
    def visitAssignment(self, ctx:CircuitSATParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx:CircuitSATParser.IdentifierFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#printlnFunctionCall.
    def visitPrintlnFunctionCall(self, ctx:CircuitSATParser.PrintlnFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#printFunctionCall.
    def visitPrintFunctionCall(self, ctx:CircuitSATParser.PrintFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#assertFunctionCall.
    def visitAssertFunctionCall(self, ctx:CircuitSATParser.AssertFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#sizeFunctionCall.
    def visitSizeFunctionCall(self, ctx:CircuitSATParser.SizeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#ifStatement.
    def visitIfStatement(self, ctx:CircuitSATParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#ifStat.
    def visitIfStat(self, ctx:CircuitSATParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#elseIfStat.
    def visitElseIfStat(self, ctx:CircuitSATParser.ElseIfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#elseStat.
    def visitElseStat(self, ctx:CircuitSATParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#functionDecl.
    def visitFunctionDecl(self, ctx:CircuitSATParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#forStatement.
    def visitForStatement(self, ctx:CircuitSATParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#whileStatement.
    def visitWhileStatement(self, ctx:CircuitSATParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#assemblerStatement.
    def visitAssemblerStatement(self, ctx:CircuitSATParser.AssemblerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#idList.
    def visitIdList(self, ctx:CircuitSATParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#exprList.
    def visitExprList(self, ctx:CircuitSATParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#boolExpression.
    def visitBoolExpression(self, ctx:CircuitSATParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#numberExpression.
    def visitNumberExpression(self, ctx:CircuitSATParser.NumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:CircuitSATParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#notExpression.
    def visitNotExpression(self, ctx:CircuitSATParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#orExpression.
    def visitOrExpression(self, ctx:CircuitSATParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:CircuitSATParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#powerExpression.
    def visitPowerExpression(self, ctx:CircuitSATParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#eqExpression.
    def visitEqExpression(self, ctx:CircuitSATParser.EqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#andExpression.
    def visitAndExpression(self, ctx:CircuitSATParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#inExpression.
    def visitInExpression(self, ctx:CircuitSATParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#stringExpression.
    def visitStringExpression(self, ctx:CircuitSATParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#expressionExpression.
    def visitExpressionExpression(self, ctx:CircuitSATParser.ExpressionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#addExpression.
    def visitAddExpression(self, ctx:CircuitSATParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#compExpression.
    def visitCompExpression(self, ctx:CircuitSATParser.CompExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#nullExpression.
    def visitNullExpression(self, ctx:CircuitSATParser.NullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CircuitSATParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#multExpression.
    def visitMultExpression(self, ctx:CircuitSATParser.MultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#listExpression.
    def visitListExpression(self, ctx:CircuitSATParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:CircuitSATParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#inputExpression.
    def visitInputExpression(self, ctx:CircuitSATParser.InputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#list.
    def visitList(self, ctx:CircuitSATParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#indexes.
    def visitIndexes(self, ctx:CircuitSATParser.IndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CircuitSATParser#opcode.
    def visitOpcode(self, ctx:CircuitSATParser.OpcodeContext):
        return self.visitChildren(ctx)



del CircuitSATParser