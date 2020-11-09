import os
a=0
b=0
g=0
os.system('tput bold')
def tc(y):
    os.system(f'tput setaf {y}')
def cls():
    os.system('clear')
def zz():
    os.system('sleep 2')
cls()


while True:
    tc(2)
    print('welcome to the docker container')
    tc(1)
    i=input('''        ________________________________________
        |   press 1 : Apache web services       |
        |   press 2 : Install basic protocols   |
        |   press 3 : Python-bash               |
        |   press 4 : services active           |
        |   press 5 : check net-cards           |
        |   Press x : exit from the container   |
        """""""""""""""""""""""""""""""""""""""""
    Enter the option :''' )
    cls()

    if i=='1':
        l=True
        
        while l:
            tc(3)
            i1=input('''                ________________________________________
                |   Press 1 : Install apache services   |
                |   Press 2 : Start web services        |
                |   Press 3 : Uninstall apache services |
                |   Press b : Prev menu                 |
                """""""""""""""""""""""""""""""""""""""""
            Enter the option : ''')
            cls()
            if i1=='1':
                
                if a!=1:
                    a=1
                    b=0
                    tc(2)
                    print('installing httpd protocol....')
                    zz()
                    tc(6)
                    os.system('yum install -y httpd')
                    zz()
                else:
                    tc(1)
                    print('already installed')
                    zz()
            elif i1=='2':
                tc(5)
                if b!=1:
                    b=1
                    print('starting httpd service.....')
                    zz()
                    tc(6)
                    os.system('/usr/sbin/httpd')
                    print()
                    print()
                    tc(3)
                    j=input('want to make it permanent? Y/N : ')
                    if j=='y' or j=='Y':
                        tc(4)
                        os.system('echo "/usr/sbin/httpd" >> /root/.bashrc')
                    else:
                        tc(1)
                        print('service already enabled')
                        zz()
                        l=False
            elif i1=='3':
                if a!=2:
                    a=2
                    tc(2)
                    print('uninstalling httpd services .............')
                    zz()
                    tc(4)
                    os.system('yum remove -y  httpd')
                else: 
                    tc(1)
                    print(' already uninstalled')
                    zz()
            elif i1=='b':
                l=False
            else:
                tc(1)
                print(' wrong input! try again.')
                zz()
    elif i=='2':
        cls
        l=True
        while l:
            if g!=1:
                g=1
                tc(1)
                print('installing ssh protocols........')
                zz()
                tc(6)
                os.system('yum -y install openssh-server openssh-clients')
                tc(1)
                print('ssh protocol installed !')
                zz()
                tc(5)
                print('installing net tools.....')
                zz()
                (6)
                os.system('yum install -y net-tools')
                tc(1)
                print('net-tools installed ')
                zz()
                cls()
                tc(2)
                print('intalling vim........')
                zz()
                tc(3)
                os.system('yum install -y vim')
                tc(1)
                print('vim installed!')
                zz()
                cls()
                tc(5)
                print('installing rpm service.......')
                zz()
                tc(7)
                os.system('yum -y install initscripts && yum clean all')
                tc(1)
                print('rpm services installed successfully!')
                zz()
                cls()
                tc(6)
                print('[*Note-python3 is pre-installed]')
                zz()
                l=False
            
            else:
                tc(1)
                print('all basic services already installed')
                zz()
                l=False
    elif i=='3':
        cls()
        tc(6)
        print('                      python-bash')
        print('                      -----------')
        print()

        l=True
        while l:
            tc(5)
            print('x to exit')
            tc(3)
            m=input('Enter command # ')
            if m=='x':
                l=False
                tc(7)
                print('exiting......')
                zz()
                cls()
            else:
                tc(6)
                os.system(f'{m}')
                zz()
                cls()
                tc(2)
                print('\t\t\t\t\t python-bash')
                print('\t\t\t\t\t"""""""""""\n\n\n')
                
    elif i=='x':
        n=0
        while n<=5:
            print('\n\nHAVE...............\n\n\n\n')
            zz()
            tc(1)
            print('                      A.................\n\n\n\n')
            zz()
            tc(2)
            print('                             NICE..............\n\n\n\n')
            zz()
            tc(3)
            print('                                                 DAY............')
            zz()
            tc(6)
            cls()
            n+=1
            
    elif i=='4':
        cls()
        tc(2)
        print('showing active services......')
        tc(6)
        os.system('netstat -tnlp')
        zz()
        cls()
    elif i=='5':
        cls()
        tc(7)
        print('showing NIC details ')
        tc(6)
        os.system('ifconfig')
        zz()
        cls()
    else:
        tc(1)
        print('wrong input! try again')

