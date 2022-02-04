# take in commands from user.

import values as vals


def __get_line_number__(phrase, file_name):
    with open(file_name) as f:
        f.flush()
        for i, line in enumerate(f, 1):
            if phrase in line:
                t = i - 1
                return t


def helper():
    print('HELP             User Commands\n')
    print('SYNOPSIS\n   [COMMAND] [OPTION]...[OPTION]\n')
    print('COMMANDS')
    print('   display (disp)')
    print('       displays totals or individual accounts.')
    print('   update')
    print('       update current accounts.')
    print('   add')
    print('       add account.')
    print('   remove (rm)')
    print('       remove account.')
    print('   reset')
    print('       set account to zero.')


def display(choice):
    arg = choice.split()
    names = []
    for i in vals.get.names_with_values():
        names.append(i[0])
    if len(arg) < 2:
        print("display: missing command operand\nTry 'help' for more information.")
    elif len(arg) > 2:
        print("display: too many arguments\nTry 'help' for more information.")
    else:
        if arg[1] == 'total' or arg[1] == 'all' or arg[1] in names or arg[1] == 'help' or arg[1] == 'accounts':
            if arg[1] == 'all':
                print('\n--------------')
                for name in names:
                    line_num = __get_line_number__(name, 'data.txt')
                    with open('data.txt') as f:
                        f.flush()
                        data = f.readlines()
                        dat = data[line_num]
                        dats = dat.split()
                        print(dats[0].capitalize(), '=', '${:0,.2f}'.format(float(dats[2])))

                total = float(0)
                for name in names:
                    line_num = __get_line_number__(name, 'data.txt')
                    with open('data.txt') as f:
                        f.flush()
                        data = f.readlines()
                        dat = data[line_num]
                        dats = dat.split()
                        total += float(dats[2])
                print('\nTotal = ', '${:0,.2f}'.format(total))
                print('--------------\n')
            if arg[1] in names:
                line_num = __get_line_number__(arg[1], 'data.txt')
                with open('data.txt') as f:
                    f.flush()
                    data = f.readlines()
                    dat = data[line_num]
                    dats = dat.split()
                    print('--------------')
                    print(dats[0].capitalize(), '=', '${:0,.2f}'.format(float(dats[2])))
                    print('--------------')
            if arg[1] == 'total':
                total = float(0)
                print('--------------')
                for name in names:
                    line_num = __get_line_number__(name, 'data.txt')
                    with open('data.txt') as f:
                        f.flush()
                        data = f.readlines()
                        dat = data[line_num]
                        dats = dat.split()
                        total += float(dats[2])
                print('Total = ', '${:0,.2f}'.format(total))
                print('--------------')
            if arg[1] == 'help':
                help_msg = 'Usage: display [OPTION]\n' \
                           'Display account information.\n\n' \
                           'Mandatory arguments.\n' \
                           '   help,                  displays this message.\n' \
                           '   all,                   displays every account and total.\n' \
                           '   [ACCOUNT],             displays specific account value.\n' \
                           '   total,                 displays total value of all accounts.\n' \
                           '   accounts               displays all active accounts.'
                print(help_msg)
            if arg[1] == 'accounts':
                print('---------------\nCurrent Accounts:')
                for account in names:
                    print(' ', account.capitalize())
                print('---------------')
        else:
            print("display: invalid command or argument not found")


def update(choice):
    arg = choice.split()
    names = []
    numbers = []
    for i in vals.get.names_with_values():
        names.append(i[0])
        numbers.append(i[1])
    if len(arg) < 2:
        print("update: missing account name and new value\nTry 'help' for more information.")
    elif len(arg) < 3:
        if arg[1] == 'help':
            help_msg = 'Usage: update [OPTION]...[OPTION]\n' \
                       'Update account information.\n\n' \
                       'Mandatory arguments.\n' \
                       '   help,                  displays this message.\n' \
                       '   [ACCOUNT]...[VALUE]    updates account with value given.'
            print(help_msg)
        else:
            print("update: missing new value for account\nTry 'help' for more information.")
    elif len(arg) > 3:
        print("update: too many arguments\nTry 'help' for more information.")
    else:
        if arg[1] in names:
            option = arg[1]
            value = arg[2]
            new_value = ''.join(i for i in value if i.isdigit() or i == '.')
            if new_value.startswith('.') or new_value.endswith('.'):
                print('update: invalid syntax')
            else:
                vals.modify.amount(option, new_value)
                print('updated account')
        else:
            print("update: account not found or invalid command")


def add_account(choice):
    arg = choice.split()
    if len(arg) < 2:
        print("add: missing command operand\nTry 'help' for more information.")
    elif len(arg) > 2:
        print("add: too many arguments\nTry 'help' for more information.")
    else:
        name = arg[1].lower()
        if name == 'help':
            help_msg = 'Usage: add [OPTION]\n' \
                       'Adds new account.\n\n' \
                       'Mandatory arguments.\n' \
                       '   help,                  displays this message.\n' \
                       '   [NEW ACCOUNT NAME]     adds account to list.'
            print(help_msg)
        if arg[1] != 'help':
            vals.modify.add_account(name)
            print('added account: ' + name)


def rm_account(choice):
    arg = choice.split()
    names = []
    for i in vals.get.names_with_values():
        names.append(i[0])
    if len(arg) < 2:
        print("remove: missing command operand\nTry 'help' for more information.")
    elif len(arg) > 2:
        print("remove: too many arguments\nTry 'help' for more information.")
    else:
        name = arg[1].lower()
        if name in names or name == 'help':
            if name in names:
                vals.modify.rm_account(name)
                print('removed account: ' + name)
            if name == 'help':
                help_msg = 'Usage: remove [OPTION]\n' \
                           'Removes account.\n\n' \
                           'Mandatory arguments.\n' \
                           '   help,                  displays this message.\n' \
                           '   [ACCOUNT NAME]         removes account from list.'
                print(help_msg)
        else:
            print("remove: account not found or invalid command")


def reset(choice):
    arg = choice.split()
    names = []
    for i in vals.get.names_with_values():
        names.append(i[0])
    if len(arg) < 2:
        print("reset: missing command operand\nTry 'help' for more information.")
    elif len(arg) > 2:
        print("reset: too many arguments\nTry 'help' for more information.")
    else:
        select = arg[1].lower()
        if select in names or select == 'help' or select == 'all':
            if select in names:
                vals.modify.reset(select)
                print('reset account ' + select + ' to $0.00')
            if select == 'help':
                help_msg = 'Usage: reset [OPTION]\n' \
                           'Resets account to $0.00.\n\n' \
                           'Mandatory arguments.\n' \
                           '   help,                  displays this message.\n' \
                           '   [ACCOUNT NAME],        resets account name specified.\n' \
                           '   all                    resets all accounts.'
                print(help_msg)
            if select == 'all':
                while True:
                    yes_or_no = str(input('You are about to reset all accounts to $0.00.\n'
                                          'Are you sure you wish to do so? '))
                    if yes_or_no == '' or yes_or_no == 'yes':
                        vals.modify.reset_all()
                        print('Reset all accounts to $0.00.')
                        break
                    elif yes_or_no == 'no':
                        print('aborting...')
                        break
                    else:
                        print('reset: command not understood (yes or no)')
