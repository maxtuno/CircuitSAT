from circuitsat.CircuitSATParser import CircuitSATParser
from circuitsat.CircuitSATVisitor import CircuitSATVisitor


class CicuitSAT(CircuitSATVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.cnf_file = open(self.file_name, 'w+')
        self.current_literal = 0
        self.current_clause = 0
        self.stack = []
        self.register = 0
        self.store = {}

    def add_clauses(self, clauses):
        for cls in clauses:
            self.current_clause += 1
            print(' '.join(list(map(str, cls))) + ' 0', file=self.cnf_file)

    def add_comment(self, comment):
        self.current_clause += 1
        print('c {}'.format(comment), file=self.cnf_file)

    def new(self):
        self.current_literal += 1
        self.register = self.current_literal
        return self.register

    def push(self):
        self.stack.append(self.register)

    def pop(self):
        lit = self.stack[-1]
        del self.stack[-1]
        self.register = lit
        return self.register

    def top(self):
        return self.register

    def apply_true(self):
        x = self.pop()
        self.add_clauses([[x]])
        self.register = x
        self.push()

    def apply_false(self):
        x = self.pop()
        self.add_clauses([[-x]])
        self.register = x
        self.push()

    def apply_not(self):
        x = self.pop()
        y = self.pop()
        self.add_clauses([[x, y],
                          [-x, -y]])
        self.register = y

    def apply_copy(self):
        x = self.pop()
        y = self.pop()
        self.add_clauses([[x, -y],
                          [-x, y]])
        self.register = y

    def apply_and(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, -z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, z]])
        self.register = z

    def apply_nand(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, -z]])
        self.register = z

    def apply_or(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, -z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, z]])
        self.register = z

    def apply_nor(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, -z]])
        self.register = z

    def apply_xor(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, -z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, -z]])
        self.register = z

    def apply_equ(self):
        x = self.pop()
        y = self.pop()
        z = self.pop()
        self.add_clauses([[x, y, z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, z]])
        self.register = z

    def apply_set(self, name):
        self.store[name] = self.register

    def apply_get(self, name):
        self.register = self.store[name]

    def apply_cur(self, name):
        if name in self.store:
            self.current_literal = self.store[name]
        else:
            self.current_literal = int(name) - 1

    def visitOpcode(self, ctx: CircuitSATParser.OpcodeContext):
        opcode = ctx.getText().lower()
        if opcode == 'new':
            self.new()
        elif opcode == 'push':
            self.push()
        elif opcode == 'pop':
            self.pop()
        elif opcode.startswith('set'):
            self.apply_set(opcode[len('set'):].strip())
        elif opcode.startswith('get'):
            self.apply_get(opcode[len('get'):].strip())
        elif opcode.startswith('cur'):
            self.apply_cur(opcode[len('cur'):].strip())
        elif opcode == 'true':
            self.apply_true()
        elif opcode == 'false':
            self.apply_false()
        elif opcode == 'copy':
            self.apply_copy()
        elif opcode == 'not':
            self.apply_not()
        elif opcode == 'and':
            self.apply_and()
        elif opcode == 'or':
            self.apply_or()
        elif opcode == 'xor':
            self.apply_xor()
        elif opcode == 'equ':
            self.apply_equ()
        elif opcode == 'nor':
            self.apply_nor()
        elif opcode == 'nand':
            self.apply_nand()
        return super().visitOpcode(ctx)

    def visitParse(self, ctx: CircuitSATParser.ParseContext):
        ret = super().visitParse(ctx)
        self.cnf_file.close()
        cnf_file = open(self.file_name, 'r+')
        header = 'c CircuitSAT Assembler\n' + 'p cnf {} {}'.format(self.current_literal, self.current_clause)
        content = cnf_file.read()
        cnf_file.seek(0, 0)
        cnf_file.write(header.rstrip('\r\n') + '\n' + content)
        cnf_file.close()
        return ret

    def visitBlock(self, ctx: CircuitSATParser.BlockContext):
        return super().visitBlock(ctx)

    def visitStatement(self, ctx: CircuitSATParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAssignment(self, ctx: CircuitSATParser.AssignmentContext):
        return super().visitAssignment(ctx)

    def visitIdentifierFunctionCall(self, ctx: CircuitSATParser.IdentifierFunctionCallContext):
        return super().visitIdentifierFunctionCall(ctx)

    def visitPrintlnFunctionCall(self, ctx: CircuitSATParser.PrintlnFunctionCallContext):
        return super().visitPrintlnFunctionCall(ctx)

    def visitPrintFunctionCall(self, ctx: CircuitSATParser.PrintFunctionCallContext):
        return super().visitPrintFunctionCall(ctx)

    def visitAssertFunctionCall(self, ctx: CircuitSATParser.AssertFunctionCallContext):
        return super().visitAssertFunctionCall(ctx)

    def visitSizeFunctionCall(self, ctx: CircuitSATParser.SizeFunctionCallContext):
        return super().visitSizeFunctionCall(ctx)

    def visitIfStatement(self, ctx: CircuitSATParser.IfStatementContext):
        return super().visitIfStatement(ctx)

    def visitIfStat(self, ctx: CircuitSATParser.IfStatContext):
        return super().visitIfStat(ctx)

    def visitElseIfStat(self, ctx: CircuitSATParser.ElseIfStatContext):
        return super().visitElseIfStat(ctx)

    def visitElseStat(self, ctx: CircuitSATParser.ElseStatContext):
        return super().visitElseStat(ctx)

    def visitFunctionDecl(self, ctx: CircuitSATParser.FunctionDeclContext):
        return super().visitFunctionDecl(ctx)

    def visitForStatement(self, ctx: CircuitSATParser.ForStatementContext):
        return super().visitForStatement(ctx)

    def visitWhileStatement(self, ctx: CircuitSATParser.WhileStatementContext):
        return super().visitWhileStatement(ctx)

    def visitIdList(self, ctx: CircuitSATParser.IdListContext):
        return super().visitIdList(ctx)

    def visitExprList(self, ctx: CircuitSATParser.ExprListContext):
        return super().visitExprList(ctx)

    def visitBoolExpression(self, ctx: CircuitSATParser.BoolExpressionContext):
        return super().visitBoolExpression(ctx)

    def visitNumberExpression(self, ctx: CircuitSATParser.NumberExpressionContext):
        return super().visitNumberExpression(ctx)

    def visitIdentifierExpression(self, ctx: CircuitSATParser.IdentifierExpressionContext):
        return super().visitIdentifierExpression(ctx)

    def visitNotExpression(self, ctx: CircuitSATParser.NotExpressionContext):
        return super().visitNotExpression(ctx)

    def visitOrExpression(self, ctx: CircuitSATParser.OrExpressionContext):
        return super().visitOrExpression(ctx)

    def visitUnaryMinusExpression(self, ctx: CircuitSATParser.UnaryMinusExpressionContext):
        return super().visitUnaryMinusExpression(ctx)

    def visitPowerExpression(self, ctx: CircuitSATParser.PowerExpressionContext):
        return super().visitPowerExpression(ctx)

    def visitEqExpression(self, ctx: CircuitSATParser.EqExpressionContext):
        return super().visitEqExpression(ctx)

    def visitAndExpression(self, ctx: CircuitSATParser.AndExpressionContext):
        return super().visitAndExpression(ctx)

    def visitInExpression(self, ctx: CircuitSATParser.InExpressionContext):
        return super().visitInExpression(ctx)

    def visitStringExpression(self, ctx: CircuitSATParser.StringExpressionContext):
        return super().visitStringExpression(ctx)

    def visitExpressionExpression(self, ctx: CircuitSATParser.ExpressionExpressionContext):
        return super().visitExpressionExpression(ctx)

    def visitAddExpression(self, ctx: CircuitSATParser.AddExpressionContext):
        return super().visitAddExpression(ctx)

    def visitCompExpression(self, ctx: CircuitSATParser.CompExpressionContext):
        return super().visitCompExpression(ctx)

    def visitNullExpression(self, ctx: CircuitSATParser.NullExpressionContext):
        return super().visitNullExpression(ctx)

    def visitFunctionCallExpression(self, ctx: CircuitSATParser.FunctionCallExpressionContext):
        return super().visitFunctionCallExpression(ctx)

    def visitMultExpression(self, ctx: CircuitSATParser.MultExpressionContext):
        return super().visitMultExpression(ctx)

    def visitListExpression(self, ctx: CircuitSATParser.ListExpressionContext):
        return super().visitListExpression(ctx)

    def visitTernaryExpression(self, ctx: CircuitSATParser.TernaryExpressionContext):
        return super().visitTernaryExpression(ctx)

    def visitInputExpression(self, ctx: CircuitSATParser.InputExpressionContext):
        return super().visitInputExpression(ctx)

    def visitList(self, ctx: CircuitSATParser.ListContext):
        return super().visitList(ctx)

    def visitIndexes(self, ctx: CircuitSATParser.IndexesContext):
        return super().visitIndexes(ctx)

