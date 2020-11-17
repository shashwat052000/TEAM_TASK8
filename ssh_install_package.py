import os
import subprocess
def tp(c):
	os.system(f'tput setaf {c}')

def ins_all():
	ip = input("Enter IP")
	os.system('ssh-keygen -t rsa')
	os.system('ssh-copy-id {}'.format(ip))
	while True:
		tp(3)
		print("\n\tPress-1 To download hadoop software \n\tPress-2 To download AWS cli \n\tPress-3 To configure webserver \n\tPress-4 To download Ansible ")
		tp(7)
		i1 = int(input("Enter your choice"))
		if(i1 == 1):
			i = subprocess.getstatusoutput('ssh {} rpm -q hadoop'.format(ip))
			if(i[0] == 0):
				tp(2)
				print("\n\tsoftware is present")
				tp(7)
			else:
				os.system('scp hadoop-1.2.1-1.x86_64.rpm {}:/root'.format(ip))
				os.system('scp jdk-8u171-linux-x64.rpm {}:/root'.format(ip))
				os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ip))
				os.system('ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force'.format(ip))
                
		elif(i1 == 2):
			i = subprocess.getstatusoutput('ssh {} aws --version'.format(ip))
			if(i[0] == 0):
				tp(2)
				print("\n\tSoftware is present")
				tp(7)
			else:
				os.system('ssh {} curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'.format(ip))
				os.system('ssh {} unzip awscliv2.zip'.format(ip))
				os.system('ssh {} sudo ./aws/install'.format(ip))

		elif(i1 == 3):
			i = subprocess.getstatusoutput('ssh {} rpm -q httpd'.format(ip))
			if(i[0] == 0):
				tp(2)
				print("\n\tHttpd software is present")
				tp(7)
			else:
				os.system("ssh {} yum install httpd".format(ip))

		elif(i1 == 4):
			os.system('ssh {} pip3 install ansible'.format(ip))

		else:
			break
        
ins_all()
