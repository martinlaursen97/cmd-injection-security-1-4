import subprocess
import shlex

domain_name = input('Enter the domain name: ')

args = shlex.split('nslookup {}'.format(domain_name))

proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

if proc.returncode == 0:
    print(proc.stdout)
else:
    print('Something went wrong')
