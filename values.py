# this script gets names and values from data set
# there must be a file called data.txt in the same directory
# in order for this script to run.


def __items__():
    with open('data.txt', 'r') as ff:
        ff.flush()
        data_in_lines = ff.readlines()

    itemss = []
    for line in data_in_lines:
        if not line.startswith('#'):
            if line == '\n':
                continue
            else:
                itemss.append(line)
    return itemss


def __get_line_number__(phrase, file_name):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if phrase in line:
                j = i - 1
                return j


def __replace_line__(line_num, text):
    lines = open('data.txt', 'r').readlines()
    lines[line_num] = text
    out = open('data.txt', 'w')
    out.writelines(lines)
    out.flush()


class get:
    @staticmethod
    def names():
        names_all = []
        for i in __items__():
            if i.find(' ='):
                name = i.split(' =')
            if i.find('='):
                name = i.split('=')
            names_all.append(name[0])

        return names_all

    @staticmethod
    def names_with_values():
        names_alls = []
        for i in __items__():
            if i.find(' = '):
                name = i.split(' = ')
            names_alls.append(name)

        return names_alls


class modify:
    @staticmethod
    def amount(category, value):
        line_num = int(__get_line_number__(category, 'data.txt'))
        new_line = str(category) + ' = ' + str(value) + '\n'
        lines = open('data.txt', 'r').readlines()
        lines[line_num] = new_line
        out = open('data.txt', 'w')
        out.writelines(lines)

    @staticmethod
    def add_account(account):
        new_line = '\n' + str(account) + ' = 0.00'
        with open("data.txt", "a") as f:
            f.write(new_line)
            f.flush()

    @staticmethod
    def rm_account(account):
        line_num = __get_line_number__(account, 'data.txt')
        __replace_line__(line_num, '')

    @staticmethod
    def reset(account):
        line_num = __get_line_number__(account, 'data.txt')
        new_line = '\n' + account + ' = 0.00'
        __replace_line__(line_num, new_line)

    @staticmethod
    def reset_all():
        with open('data.txt') as f:
            for ihm, line in enumerate(f, 1):
                for name in get.names():
                    if name in line:
                        line_num = ihm - 1
                        new_line = '\n' + name.rstrip() + ' = 0.00'
                        __replace_line__(line_num, new_line)
