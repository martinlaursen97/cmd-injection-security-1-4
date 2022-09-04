import subprocess


def is_valid(cmd: str) -> bool:
    WHITE_LIST = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. '

    for c in cmd:
        if c not in WHITE_LIST:
            return False
    return True

    # return len([i for i in s if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. ']) == 0


domain_name = input('Enter the domain name: ')

command = 'nslookup {}'.format(domain_name)

if is_valid(command):
    response = subprocess.check_output(command, shell=True, encoding='UTF-8')
    print(response)
else:
    print('Something went wrong')
