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

    def visitEnd(self, ctx: CircuitSATParser.EndContext):
        self.cnf_file.close()
        cnf_file = open(self.file_name, 'r+')
        header = 'c CircuitSAT Assembler\n' + 'p cnf {} {}'.format(self.current_literal, self.current_clause)
        content = cnf_file.read()
        cnf_file.seek(0, 0)
        cnf_file.write(header.rstrip('\r\n') + '\n' + content)
        cnf_file.close()
        return super().visitEnd(ctx)

    def visitLine(self, ctx: CircuitSATParser.LineContext):
        return super().visitLine(ctx)

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
