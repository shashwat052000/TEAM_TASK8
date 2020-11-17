import os
import subprocess
import getpass
import awsmenu

def tp(c):
	os.system(f'tput setaf {c}')

def namenode(p):
	if(p==2):
		ip = input("Enter IP of namenode")
		os.system('ssh-keygen -t rsa')
		os.system('ssh-copy-id {}'.format(ip))
		os.system(f'ssh {ip} wget https://buckettejesh.s3.amazonaws.com/code/namenode/core-site.xml')
		os.system(f'ssh {ip} cp /root/core-site.xml /etc/hadoop/core-site.xml')
		os.system(f'ssh {ip} rm core-site.xml')
		os.system(f'ssh {ip} wget https://buckettejesh.s3.ap-south-1.amazonaws.com/code/namenode/hdfs-site.xml')
		os.system(f'ssh {ip} cp /root/hdfs-site.xml /etc/hadoop/hdfs-site.xml')
		os.system(f'ssh {ip} rm hdfs-site.xml')
		os.system(f'ssh {ip} systemctl stop firewalld')
		os.system(f'ssh {ip} hadoop namenode -format')
		os.system(f'ssh {ip} hadoop-daemon.sh start namenode')

	else:
		print("Entered command is wrong pls retype or restart the process")
		os.system('wget https://buckettejesh.s3.amazonaws.com/code/namenode/core-site.xml')
		os.system('cp /root/core-site.xml /etc/hadoop/core-site.xml')
		os.system('rm core-site.xml')
		os.system('wget https://buckettejesh.s3.ap-south-1.amazonaws.com/code/namenode/hdfs-site.xml')
		os.system('cp /root/hdfs-site.xml /etc/hadoop/hdfs-site.xml')
		os.system('rm hdfs-site.xml')
		os.system('systemctl stop firewalld')
		os.system('hadoop namenode -format')
		os.system('hadoop-daemon.sh start namenode')


def datanode(p):
	ips = []
	pas = []
	tp(3)
	ip = input("\t\t\tEnter IP of namenode: -->")
	tp(7)
	for i in range(p):
		tp(2)
		a = input(f"\t\t\tEnter IP of datanode{i+1}: ")
		pa = getpass.getpass(f'\t\t\tEnter Pass of datanode{i+1}: ')
		tp(7)
		ips.append(a)
		pas.append(pa)
		
	for i in range(p):
		a1 = ips[i]
		b1 = pas[i]
		tp(3)
		print("\n\t\tPrinting available disks")
		os.system('''sshpass -p {} ssh {} fdisk -l'''.format(b1, a1))
		a2 = int(input("\tEnter your number of disks: --> "))
		tp(7)

		d = ''''''
		x = []
		for i in range(a2):
			tp(2)
			a3 = input(f"\t Input your device{i+1} name you like to create lv: -->")
			x.append(a3)
			d = d+' '+x[i]
			os.system(f'sshpass -p {b1} ssh {a1} pvcreate {a3}')
			tp(7)

		tp(5)
		name = input("\t\t Enter your AG name: -->")
		print(os.system(f'sshpass -p {b1} ssh {a1} vgcreate {name}' + d))
		tp(7)

		tp(3)
		parti_name = input("\t\t Enter your partition name: ")
		size0 = input("Enter the size of partition: -->")
		print(os.system('sshpass -p {} ssh {} lvcreate --size {} --name {} {} -y'.format(b1, a1, size0, parti_name, name)))
		tp(7)

		e = 'sshpass -p {} ssh {} mkfs.ext4 /dev/'+name+'/'+parti_name
		e = e.format(b1, a1)
		f = 'sshpass -p {} ssh {} mount /dev/'+name+'/'+parti_name+' /data'
		f = f.format(b1, a1)
		print(os.system(e))

		g = 'sshpass -p {} ssh {} mkdir /data'.format(b1, a1)
		os.system(g)
		os.system(f)

		os.system('wget https://buckettejesh.s3.amazonaws.com/code/namenode/core-site.xml')
		with open('core-site.xml') as f:
			newText = f.read().replace('0.0.0.0', ip)

		with open('/core-site.xml', 'w') as f:
			f.write(newText)

		os.system(f'sshpass -p {b1} scp core-site.xml {a1}:/etc/hadoop/core-site.xml')
		os.system('rm core-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} wget https://buckettejesh.s3.ap-south-1.amazonaws.com/code/namenode/hdfs-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} cp /root/hdfs-site.xml /etc/hadoop/hdfs-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} rm hdfs-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} systemctl stop firewalld')
		os.system(f'sshpass -p {b1} ssh {a1} hadoop-daemon.sh start datanode')
		tp(3)
		os.system(f'sshpass -p {b1} ssh {a1} jps')
		tp(7)
		print("\t\t\tDatanode is created and integrated with LVM")

def client(p):
	ips = []
	pas = []
	ip = input("Enter IP of Namenode")
	for i in range(p):
		a = input(f"Enter IP of datanode{i+1}")
		pa = getpass.getpass(f'Enter Pass of datanode{i+1}')
		ips.append(a)
		pas.append(pa)

	for i in range(p):
		a1 = ips[i]
		b1 = pas[i]
		os.system('wget https://buckettejesh.s3.amazonaws.com/code/namenode/core-site.xml')
		with open('core-site.xml') as f:
			newText = f.read().replace('0.0.0.0', ip)

		with open('/core-site.xml', 'w') as f:
			f.write(newText)

		os.system(f'sshpass -p {b1} scp core-site.xml {a1}:/etc/hadoop/core-site.xml')
		os.system('rm core-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} wget https://buckettejesh.s3.ap-south-1.amazonaws.com/code/client.xml')
		os.system(f'sshpass -p {b1} ssh {a1} cp /root/client.xml /etc/hadoop/hdfs-site.xml')
		os.system(f'sshpass -p {b1} ssh {a1} rm client.xml')
		os.system(f'sshpass -p {b1} ssh {a1} systemctl stop firewalld')
		

def setup():
	while True:
		tp(3)
		print("\n\tPress-1 To setup Hadoop \n\tPress-2 For AWS related \n\tPress-3 To setup Webserver \n\tPress-4 To setup LVM locally \n\tPress-5 To exit \n")
		tp(7)
		i1 = int(input("Enter your option: -->"))
		if(i1 == 1):
			os.system('clear')
			print("\n\tPress-1 To configure namenode \n\tPress-2 To configure datanode \n\tPress-3 To configure client \n")
			tp(3)
			i2 = int(input("Enter your choice: -->"))
			tp(7)
			if(i2 == 1):
				tp(2)
				print("\n\tPress-1 For Local \n\tPress-2 For Remote")
				tp(3)
				i3 = int(input("\t\tEnter your choice"))
				tp(7)
				namenode(i3)
			elif(i2 == 2):
				tp(2)
				i4 = int(input("\n\tEnter number of datanodes: -->"))
				tp(7)				
				datanode(i4)
			else:
				i5 = int(input("\n\tEnter number of clients"))
				client(i5)

		elif(i1 == 2):
			awsmenu.aws()

		elif(i1 == 4):
			tp(3)
			os.system('fdisk -l')
			lin = int(input("\tEnter number of devices to create LV: --> "))
			tp(7)
			x = []
			d = ''''''
			for i in range(lin):
				tp(2)
				lin1 = input('\t\tEnter device name: --> ')
				x.append(lin1)
				d = d+' '+x[i]
				os.system(f'pvcreate {lin1}')
				tp(7)

			tp(3)
			vname = input("\t\tEnter your vg name: -->")
			os.system(f'vgcreate {vname}'+d)
			tp(7)
			
			tp(2)
			parname = input("\tEnter partition name: -->")
			psize = input("\t\tEnter partition size: -->")
			tp(7)

			os.system(f'lvcreate --size {psize} --name {parname} {vname}')

			p1 = input("\t\tEnter dir name to create: -->") 
			i = subprocess.getoutput(f'mkdir /{p1}')
			if(i == 0):
				pass
			else:
				tp(1)
				print(f"\t Directory {p1} is already created give some other dir")
				tp(3)
				p1 = input("\t Enter dir name")
				os.system(f'mkdir /{p1}')
				tp(7)
			os.system('mkfs.ext4 /dev/'+vname+'/'+parname)
			os.system('mount /dev/'+vname+'/'+parname+' /{}'.format(p1))

			os.system('df -h')
			print("\t\t\tLVM is created")
			
			tp(3)
			print("To add some extra space we use lvextent command \n\tPress-1 To perform \n\tPress-2 To not continue")
			i11 = int(input("Enter your responce: -->"))
			tp(7)
		
			if(i11 == 1):
				tp(2)
				le = input("Enter size you want to extent: -->")
				os.system(f'lvextend --size +{le} /dev/'+vname+'/'+parname)
				os.system('resize2fs /dev/'+vname+'/'+parname)
				tp(7)

			else:
				pass

			
		else:
			break


setup()
	
