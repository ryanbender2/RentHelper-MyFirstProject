import cli

print("=============\nRent Helper\nType help for list of commands\nexit with 'exit'\n=============\n")

while True:
    choice = str(input('RH |-__-|$ '))
    c = choice.startswith
    if c('help') or c('exit') or c('clear') or c('disp') or c('update') \
            or c('add') or c('remove') or c('reset')or c('rm'):
        if c('help'):
            cli.helper()
        if c('exit'):
            break
        if c('clear'):
            print('\n' * 150)
        if c('disp'):
            cli.display(choice)
        if c('update'):
            cli.update(choice)
        if c('add'):
            cli.add_account(choice)
        if c('remove'):
            cli.rm_account(choice)
        if c('rm'):
            cli.rm_account(choice)
        if c('reset'):
            cli.reset(choice)
    else:
        if choice == '':
            continue
        else:
            print(choice.rstrip() + ': command not found')
