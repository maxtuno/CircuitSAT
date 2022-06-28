import copy
from circuitsat.CircuitSATLexer import CircuitSATLexer
from circuitsat.CircuitSATParser import CircuitSATParser
from circuitsat.CircuitSATVisitor import CircuitSATVisitor


class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value


class Function:
    def __init__(self, idx, args, block):
        self.idx = idx
        self.args = args
        self.block = block

    def invoke(self, master, args):
        if master.recursive:
            slave = CicuitSAT(master.file_name)
            slave.store = copy.copy(master.store)
            slave.cnf_file = master.cnf_file
            slave.current_literal = master.current_literal
            slave.current_clause = master.current_clause
        else:
            slave = master
        for arg, value in zip(self.args, args):
            slave.store[arg.getText()] = master.visit(value)
        try:
            ret = slave.visit(self.block)
            master.current_literal = slave.current_literal
            master.current_clause = slave.current_clause
            return ret
        except ReturnValue as ret:
            return ret.value


class CicuitSAT(CircuitSATVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.cnf_file = open(self.file_name, 'w+')
        self.current_literal = 0
        self.current_clause = 0
        self.store = {}
        self.recursive = True

    def visitCircuit(self, ctx: CircuitSATParser.CircuitContext):
        ret = super().visitCircuit(ctx)
        self.cnf_file.close()
        cnf_file = open(self.file_name, 'r+')
        header = 'c CircuitSAT Language\n' + 'p cnf {} {}'.format(self.current_literal, self.current_clause)
        content = cnf_file.read()
        cnf_file.seek(0, 0)
        cnf_file.write(header.rstrip('\r\n') + '\n' + content)
        cnf_file.close()
        return ret

    def visitBlock(self, ctx: CircuitSATParser.BlockContext):
        for fdx in ctx.functionDecl():
            if fdx not in self.store:
                self.visit(fdx)
        for sx in ctx.statement():
            self.visit(sx)
        if ctx.expression():
            value = self.visit(ctx.expression())
            ret = ReturnValue(value)
            raise ret
        return None

    def visitStatement(self, ctx: CircuitSATParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAssignment(self, ctx: CircuitSATParser.AssignmentContext):
        new_val = self.visit(ctx.expression())
        if ctx.indexes():
            val = self.store[ctx.Identifier().getText()]
            for ec in ctx.indexes().expression():
                idx = self.visit(ec)
                val[idx] = new_val
        else:
            idx = ctx.Identifier().getText()
            self.store[idx] = new_val
        return None

    def visitIdentifierFunctionCall(self, ctx: CircuitSATParser.IdentifierFunctionCallContext):
        params = []
        if ctx.exprList():
            params = ctx.exprList().expression()
        idx = ctx.Identifier().getText() + str(len(params))
        return self.store[idx].invoke(self, params)

    def visitPrintlnFunctionCall(self, ctx: CircuitSATParser.PrintlnFunctionCallContext):
        if ctx.expression():
            print(self.visit(ctx.expression()))
        else:
            print()
        return None

    def visitPrintFunctionCall(self, ctx: CircuitSATParser.PrintFunctionCallContext):
        print(self.visit(ctx.expression()), end='')
        return None

    def visitAssertFunctionCall(self, ctx: CircuitSATParser.AssertFunctionCallContext):
        if not self.visit(ctx.expression()):
            raise Exception('Failed Assertion {} at line: {}'.format(ctx.expression().getText(), ctx.start.line))
        return None

    def visitSizeFunctionCall(self, ctx: CircuitSATParser.SizeFunctionCallContext):
        return len(self.visit(ctx.expression()))

    def visitIfStatement(self, ctx: CircuitSATParser.IfStatementContext):
        if self.visit(ctx.ifStat().expression()):
            return self.visit(ctx.ifStat().block())

        for i in range(len(ctx.elseIfStat())):
            if self.visit(ctx.elseIfStat(i).expression()):
                return self.visit(ctx.elseIfStat(i).block())

        if ctx.elseStat():
            return self.visit(ctx.elseStat().block())

    def visitIfStat(self, ctx: CircuitSATParser.IfStatContext):
        if self.visit(ctx.expression()):
            return self.visit(ctx.block())

    def visitElseIfStat(self, ctx: CircuitSATParser.ElseIfStatContext):
        if self.visit(ctx.expression()):
            return self.visit(ctx.block())

    def visitElseStat(self, ctx: CircuitSATParser.ElseStatContext):
        return self.visit(ctx.block())

    def visitFunctionDecl(self, ctx: CircuitSATParser.FunctionDeclContext):
        params = []
        if ctx.idList():
            params = ctx.idList().Identifier()
        idx = ctx.Identifier().getText() + str(len(params))
        block = ctx.block()
        self.store[idx] = Function(idx, params, block)
        return None

    def visitForStatement(self, ctx: CircuitSATParser.ForStatementContext):
        start = int(self.visit(ctx.expression(0)))
        stop = int(self.visit(ctx.expression(1)))
        for i in range(start, stop):
            self.store[ctx.Identifier().getText()] = i
            ret = self.visit(ctx.block())
            if ret:
                return ret
        return None

    def visitWhileStatement(self, ctx: CircuitSATParser.WhileStatementContext):
        while self.visit(ctx.expression()):
            val = self.visit(ctx.block())
            if val:
                return val
        return None

    def visitAssemblerStatement(self, ctx: CircuitSATParser.AssemblerStatementContext):
        return super().visitAssemblerStatement(ctx)

    def visitIdList(self, ctx: CircuitSATParser.IdListContext):
        return super().visitIdList(ctx)

    def visitExprList(self, ctx: CircuitSATParser.ExprListContext):
        return super().visitExprList(ctx)

    def visitBoolExpression(self, ctx: CircuitSATParser.BoolExpressionContext):
        return True if ctx.getText() == 'true' else False

    def visitNumberExpression(self, ctx: CircuitSATParser.NumberExpressionContext):
        return eval(ctx.getText())

    def visitIdentifierExpression(self, ctx: CircuitSATParser.IdentifierExpressionContext):
        idx = ctx.Identifier().getText()
        val = self.store[idx]
        if ctx.indexes():
            for ec in ctx.indexes().expression():
                idx = self.visit(ec)
                if isinstance(val, str):
                    val = list(val)[idx]
                else:
                    val = val[idx]
        return val

    def visitNotExpression(self, ctx: CircuitSATParser.NotExpressionContext):
        a = self.visit(ctx.expression()),
        return not a[0]

    def visitOrExpression(self, ctx: CircuitSATParser.OrExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        return a | b

    def visitUnaryMinusExpression(self, ctx: CircuitSATParser.UnaryMinusExpressionContext):
        a = self.visit(ctx.expression()),
        return -1 * a[0]

    def visitPowerExpression(self, ctx: CircuitSATParser.PowerExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        return a ** b

    def visitEqExpression(self, ctx: CircuitSATParser.EqExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        if ctx.op.type == CircuitSATLexer.Equals:
            return a == b
        if ctx.op.type == CircuitSATLexer.NEquals:
            return a != b

    def visitAndExpression(self, ctx: CircuitSATParser.AndExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        return a & b

    def visitInExpression(self, ctx: CircuitSATParser.InExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        return a in b

    def visitStringExpression(self, ctx: CircuitSATParser.StringExpressionContext):
        return ctx.getText().replace('\'', '').replace('\"', '')

    def visitExpressionExpression(self, ctx: CircuitSATParser.ExpressionExpressionContext):
        val = self.visit(ctx.expression())
        if ctx.indexes():
            for ec in ctx.indexes():
                idx = self.visit(ec)
                val = list(val)[idx]
        return val

    def visitAddExpression(self, ctx: CircuitSATParser.AddExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        if ctx.op.type == CircuitSATLexer.Add:
            if isinstance(a, list):
                a.append(b)
                return a
            return a + b
        if ctx.op.type == CircuitSATLexer.Subtract:
            if isinstance(a, list):
                if b in a:
                    a.remove(b)
                return a
            return a - b

    def visitCompExpression(self, ctx: CircuitSATParser.CompExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        if ctx.op.type == CircuitSATLexer.LT:
            return a < b
        if ctx.op.type == CircuitSATLexer.LTEquals:
            return a <= b
        if ctx.op.type == CircuitSATLexer.GT:
            return a > b
        if ctx.op.type == CircuitSATLexer.GTEquals:
            return a >= b

    def visitNullExpression(self, ctx: CircuitSATParser.NullExpressionContext):
        return None

    def visitFunctionCallExpression(self, ctx: CircuitSATParser.FunctionCallExpressionContext):
        val = self.visit(ctx.functionCall())
        if ctx.indexes():
            for ec in ctx.indexes().expression():
                return val[self.visit(ec)]
        return val

    def visitMultExpression(self, ctx: CircuitSATParser.MultExpressionContext):
        a, b = self.visit(ctx.expression(0)), self.visit(ctx.expression(1))
        if ctx.op.type == CircuitSATLexer.Multiply:
            if isinstance(a, str):
                return a.replace('\'', '').replace('\"', '') * b
            elif isinstance(b, str):
                return a * b.replace('\'', '').replace('\"', '')
            return a * b
        if ctx.op.type == CircuitSATLexer.Divide:
            return a / b
        if ctx.op.type == CircuitSATLexer.Modulus:
            return a % b
        if ctx.op.type == CircuitSATLexer.IDivide:
            return a // b

    def visitListExpression(self, ctx: CircuitSATParser.ListExpressionContext):
        val = self.visit(ctx.list_())
        if ctx.indexes():
            for ec in ctx.indexes():
                idx = self.visit(ec)
                if isinstance(val, str):
                    return list(val)[idx]
                else:
                    return val[idx]
        return val

    def visitTernaryExpression(self, ctx: CircuitSATParser.TernaryExpressionContext):
        return super().visitTernaryExpression(ctx)

    def visitInputExpression(self, ctx: CircuitSATParser.InputExpressionContext):
        raise Exception('TODO: Implement')
        return super().visitInputExpression(ctx)

    def visitList(self, ctx: CircuitSATParser.ListContext):
        ls = []
        if ctx.exprList():
            for ex in ctx.exprList().expression():
                ls.append(self.visit(ex))
        return ls

    def visitIndexes(self, ctx: CircuitSATParser.IndexesContext):
        return super().visitIndexes(ctx)

    def visitOpcode(self, ctx: CircuitSATParser.OpcodeContext):
        opcode = ctx.getText()
        if opcode.startswith('new'):
            x = ctx.Identifier(0).getText()
            if ctx.expression():
                self.apply_new(x + str(self.visit(ctx.expression(0))))
            else:
                self.apply_new(x)
        elif opcode.startswith('copy'):
            x, y = ctx.Identifier(0).getText(), ctx.Identifier(1).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            self.apply_copy(a, b)
        elif opcode.startswith('not'):
            x, y = ctx.Identifier(0).getText(), ctx.Identifier(1).getText()
            a = ctx.expression(0)
            b = ctx.expression(1)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            self.apply_not(a, b)
        elif opcode.startswith('and'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_and(a, b, c)
        elif opcode.startswith('or'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_or(a, b, c)
        elif opcode.startswith('xor'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_xor(a, b, c)
        elif opcode.startswith('equ'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_equ(a, b, c)
        elif opcode.startswith('nor'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_nor(a, b, c)
        elif opcode.startswith('nand'):
            x, y, z = ctx.Identifier(0).getText(), ctx.Identifier(1).getText(), ctx.Identifier(2).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)
            c = ctx.expression(2)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            if c is None:
                c = z
            else:
                c = z + str(self.visit(ctx.expression(2)))

            self.apply_nand(a, b, c)
        elif opcode.startswith('put'):
            x, y = ctx.Identifier(0).getText(), ctx.Identifier(1).getText()

            a = ctx.expression(0)
            b = ctx.expression(1)

            if a is None:
                a = x
            else:
                a = x + str(self.visit(ctx.expression(0)))

            if b is None:
                b = y
            else:
                b = y + str(self.visit(ctx.expression(1)))

            self.apply_put(a, b)
        return super().visitOpcode(ctx)

    def add_clauses(self, clauses):
        for cls in clauses:
            self.current_clause += 1
            print(' '.join(list(map(str, cls))) + ' 0', file=self.cnf_file)

    def add_comment(self, comment):
        self.current_clause += 1
        print('c {}'.format(comment), file=self.cnf_file)

    def apply_new(self, x):
        self.current_literal += 1
        self.store[x] = self.current_literal

    def apply_put(self, x, y):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        x, y = self.store[x], self.store[y]
        if y:
            self.add_clauses([[x]])
        else:
            self.add_clauses([[-1 * x]])

    def apply_not(self, x, y):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        x, y = self.store[x], self.store[y]
        self.add_clauses([[x, y],
                          [-x, -y]])

    def apply_copy(self, x, y):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        x, y = self.store[x], self.store[y]
        self.add_clauses([[x, -y],
                          [-x, y]])

    def apply_and(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, -z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, z]])

    def apply_nand(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, -z]])

    def apply_or(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, -z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, z]])

    def apply_nor(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, -z]])

    def apply_xor(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, -z],
                          [x, -y, z],
                          [-x, y, z],
                          [-x, -y, -z]])

    def apply_equ(self, x, y, z):
        if x not in self.store:
            if '[' in x and x[:x.index('[')] in self.store:
                xl = self.store[x[:x.index('[')]]
                x_ = xl[eval(x[x.index('[') + 1:-1])]
                self.store[x] = x_
        if y not in self.store:
            if '[' in y and y[:y.index('[')] in self.store:
                yl = self.store[y[:y.index('[')]]
                y_ = yl[eval(y[y.index('[') + 1:-1])]
                self.store[y] = y_
        if z not in self.store:
            if '[' in z and z[:z.index('[')] in self.store:
                zl = self.store[z[:z.index('[')]]
                z_ = zl[eval(z[z.index('[') + 1:-1])]
                self.store[z] = z_
        x, y, z = self.store[x], self.store[y], self.store[z]
        self.add_clauses([[x, y, z],
                          [x, -y, -z],
                          [-x, y, -z],
                          [-x, -y, z]])

    def apply_cur(self, name):
        if name in self.store:
            self.current_literal = self.store[name]
        else:
            self.current_literal = int(name) - 1
