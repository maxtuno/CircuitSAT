import sys


def satisfy(solver, params='', log=False, file_name=None):
    import subprocess
    key = file_name.replace('.cnf', '')
    with open('{}.mod'.format(key), 'w', encoding="utf8", errors='ignore') as file:
        proc = subprocess.Popen('{0} {1}.cnf {2}'.format(solver, key, params), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for stdout_line in iter(proc.stdout.readline, ''):
            if not stdout_line:
                break
            try:
                line = stdout_line.decode()
                file.write(line)
                if log:
                    print(line, end='')
            except:
                pass
        proc.stdout.close()
    with open('{}.mod'.format(key), 'r') as mod:
        lines = ''
        for line in mod.readlines():
            if line.startswith('v '):
                lines += line.strip('v ').strip('\n') + ' '
        if len(lines) > 0:
            model = list(map(int, lines.strip(' ').split(' ')))
            print([int(lit > 0) for lit in model[:-1]])
            with open(file_name, 'a') as file:
                file.write(' '.join([str(-int(literal)) for literal in model]) + '\n')
            return True
    return False


if __name__ == '__main__':

    while satisfy(solver='./slime', params='', log=False, file_name=sys.argv[1]):
        pass

