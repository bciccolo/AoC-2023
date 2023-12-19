processors = {}
units = []

class Processor:
    def __init__(self, line):
        # Line format: {a<2006:qkq,m>2090:A,rfg}

        self.rules = []

        rules = line[1:-1].split(',')
        for rule in rules:
            if ':' not in rule:
                self.default = rule
            else:
                condition, result = rule.split(':')
                if '>' in condition:
                    operator = '>'
                    op_index = condition.index('>')
                else:
                    operator = '<'
                    op_index = condition.index('<')
                component = condition[:op_index]
                threshold = int(condition[op_index + 1:])

                self.rules.append(Rule(component, operator, threshold, result))

    def process(self, unit):
        for rule in self.rules:
            result = rule.check(unit)
            if result:
                return result

        return self.default


class Rule:
    def __init__(self, component, operator, threshold, result):
        self.component = component
        self.operator = operator
        self.threshold = threshold
        self.result = result

    def check(self, unit):
        if self.component == 'x':
            check = unit.x
        elif self.component == 'm':
            check = unit.m
        elif self.component == 'a':
            check = unit.a
        elif self.component == 's':
            check = unit.s

        if (self.operator == '>' and check > self.threshold) or \
           (self.operator == '<' and check < self.threshold):
            return self.result

        return None


class Unit:
    def __init__(self, line):
        # Line format: {x=787,m=2655,a=1222,s=2876}
        parts = [int(kvp.split('=')[1]) for kvp in line[1:-1].split(',')]

        self.x = parts[0]
        self.m = parts[1]
        self.a = parts[2]
        self.s = parts[3]
        self.total = sum(parts)


def load_data(file_name):
    blank_found = False

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        if line == '':
            blank_found = True
            continue

        if blank_found:
            units.append(Unit(line))
        else:
            curly = line.index('{')
            processors[line[:curly]] = Processor(line[curly:])


load_data('day19.dat')

total = 0
for unit in units:
    pid = 'in'
    while True:
        processor = processors[pid]
        # print(pid, end=" ")
        pid = processor.process(unit)
        if pid == 'A':
            # print('accepted')
            total += unit.total
            break
        elif pid == 'R':
            # print('rejected')
            break
    # print()


print('Part 1: ' + str(total))
