'''
To do:
    Fix add
    Fix remove
    Fix color palets
'''


import paramiko
import sys
import os
import time

#Setup bot class
class Bot():
    def __init__(self, host, port, user, passw):
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw
        
        try:
            ssh.connect(host, port=port, username=user, password=passw)
            print('   \033[92m[+]\033[0m Connected to {}@{}!'.format(user, host))
        except Exception:
            print('   \033[91m[!]\033[0m Connection error. Couldnt connect to host!')

    def send_comm(self, comm):
        print('   Command: {}'.format(comm))
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comm)
        return ssh_stdout.readlines()


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    
bots = []

def load_bots():
    bots = []

    fr = open('bots.txt', 'r+')
    fw = open('bots.txt', 'a')
    lines = fr.readlines()

    for l in lines:
        p = l.split()
        bots.append(Bot(p[0], int(p[1]), p[2], p[3]))
    
    return bots

os.system('clear')

print('''
   \033[91m _____ \033[0m _   _      _   
   \033[91m|  ___|\033[0m| \ | | ___| |_ 
   \033[91m| |_   \033[0m|  \| |/ _ \ __|
   \033[91m|  _|  \033[0m| |\  |  __/ |_ 
   \033[91m|_|    \033[0m|_| \_|\___|\__|
                      \033[94mv1.0\033[0m
''')

command = ''

while command != 'quit':
    command = input('\033[91mF\033[0mNet\033[94m~#\033[0m ')
    parametar = command.split()

    if command == 'help':
        print('\n')
        print('     help .............. Show commands')
        print('    clear .............. Clear terminal')
        print('     quit .............. Quit FNet')
        print('      add .............. Add bot')
        print('   delete .............. Remove bot')
        print('     send .............. Send command to bots')
        print('     list .............. List bots')
        print('     load .............. Load saved bots')
        print('\n')
    
    elif command == 'clear':
        os.system('clear')
    
    elif 'add' in command:
        if ' ' in command:
            if len(parametar) == 5:
                host = parametar[1]
                port = parametar[2]
                user = parametar[3]
                passw = parametar[4]

                bot = Bot(host, int(port), user, passw)
                if bot not in bots:
                    try: 
                        ssh.connect(host, port=port, username=user, password=passw)
                        for_db = host + ' ' + port + ' ' + user + ' ' + passw
                        if for_db not in lines:
                            bots.append(bot)
                            fw.write(for_db + '\n')
                            print('   \033[92m[+]\033[0m Bot added to list!')
                        else:
                            print('   \033[91m[!]\033[0m Bot is already added!')
                    except:
                        pass
                else:
                    print('   \033[91m[!]\033[0m Bot is already added!')
            else:
                print('   \033[91m[!]\033[0m Insufficient number of arguments!')
        else:
            print('   \033[91m[!]\033[0m Incorrect syntax\n   Example: add 1.2.3.4 22 username password')
    
    elif command == 'delete':
        deleteBot()

    elif 'send' in command:
        if ' ' in command:
            comm = str(parametar[1])
            comm = comm.replace('_', ' ')

            confirm = input('   \033[93m[?]\033[0m Are yoo sure you want to send "{}" to {} bots? [y/n]> '.format(comm, len(bots)))
            if confirm == 'y':
                if len(bots) != 0:
                    for b in bots:
                        b.send_comm(comm)
                    print('   \033[92m[+]\033[0m Command "{}" successfully sent to {} bots!'.format(comm, len(bots)))
                else:
                    print('   \033[91m[!]\033[0m You dont have bots yet!')
        else:
            print('   \033[91m[!]\033[0m Incorrect syntax\n   Example: send ls _-a\n   Important!: Use _ instead of Space!')

    elif command == 'quit':
        pass
    elif command == 'list':
        if len(bots) != 0:
            print('   Number of bots: {}'.format(len(bots)))
            time.sleep(1)

            count = 1
            for b in bots:
                print('   Bot ID: {}'.format(count))
                print('   Host: {}'.format(b.host))
                print('   Port: {}'.format(b.port))
                print('   User: {}'.format(b.user))
                print('   Pass: {}'.format(b.passw))
                print('   ------------------------')
                count += 1
        else:
            print('   \033[91m[!]\033[0m You dont have any bots yet!')
    elif command == 'load':
        bots = load_bots()

    else:
        print('   \033[91m[!]\033[0m Command {} does not exist!'.format(command))
