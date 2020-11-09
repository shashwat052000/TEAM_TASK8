import os
import getpass
print("""
Press 1. To integrate hadoop with LVM
Press 2. To resize LVM
Press 3. To setup LVM with out hadoop""")

in1 = int(input("enter your choice"))

if in1 == 1:
	in2 = int(input("Enter total number of nodes including master and client"))
	usr_name = []
	psd = []
	for i in range(0, in2):
		if i == 0:
			in31 = input("Enter name node IP")
			usr_name.append(in31)
			in32 = getpass.getpass("Enter your password")
			psd.append(in32)
		elif i == 1:
			in31 = input("Enter client IP")
			usr_name.append(in31)
			int32 = getpass.getpass("Enter your password")
			psd.append(int32)
		elif i > 1:
			in31 = input("Enter IP of data naode".format(i-1))
			usr_name.append(in31)
			in32 = getpass.getpass("Enter Pass of datanode")
			psd.append(in32)
	
	for i in range(0, in2):
		if i == 0:
			in31 = usr_name[i]
			ps = psd[i]
			m = "ssh {} yum install sshpass -y".format(in31)
			os.system(m)

			a = """sshpass -p {} ssh {} wget -o /root/jdk-8u171-linux-x64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm""".format(ps,in31)
			os.system(a)

			a = """sshpass -p {} ssh {} wget -o /root/hadoop-1.2.1-1.x86_64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/hadoop-1.2.1-1.x86_64.rpm""".format(ps,in31)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(ps,in31)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ps,in31)
			os.system(a)

			a = """sshpass -p {} ssh {} wget -o /etc/hadoop/core-site.xml https://buckettejesh.s3.ap-south-1.amazon.aws.com/code/namenode/core-site.xml""".format(ps, in31) 
			os.system(a)

			a = """sshpass -p {} ssh {} wget -o /etc/hadoop/hdfs-site.xml https://buckettejesh.s3.ap-south-1.amazon.aws.com/code/namenode/hdfs-site.xml""".format(ps, in31) 
			os.system(a)

			a = """sshpass -p {} ssh {} systemctl stop firewalld""".format(ps, in31)
			os.system(a)

			a = 'sshpass -p {} ssh {} systemctl disable firewalld'.format(ps, in31)
			os.system(a)

			a = 'sshpass -p {} ssh {} hadoop namenode -format'.format(ps, in31)
			os.system(a)

			a = 'sshpass -p {} ssh {} hadoop-daemon.sh start namenode'.format(ps, in31)
			os.system(a)


		elif i == 1:
			in32 = usr_name[i]
			ps2 = psd[i]
			m = "ssh {} yum install sshpass -y".format(in32)
			os.system(m)	 

			a = """sshpass -p {} ssh {} wget -o /root/jdk-8u171-linux-x64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm""".format(ps2,in32)
			os.system(a)

			a = """sshpass -p {} ssh {} wget -o /root/hadoop-1.2.1-1.x86_64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/hadoop-1.2.1-1.x86_64.rpm""".format(ps2,in32)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(ps2,in32)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ps2,in32)
			os.system(a)

			a = """wget -0 /core-site.xml https://buckettejesh.s3.ap-south-1.amazon.aws.com/code/namenode/core-site.xml""".format(ps2, in32)
			os.system(a)

			with open('/core-site.xml') as f:
				t = f.read().replace('0.0.0.0', in32)

			with open('/core-site.xml', 'w') as f:
				f.write(t)
			os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(ps2, in32))

		elif (i > 1):
			in33 = usr_name[i]
			ps3 = psd[i]
			m = "ssh {} yum install sshpass -y".format(in31)
			os.system(m)

			print("""Press 1. To show all devices connected
			Press 2. To continue furthur""")
			in4 = int(input("Enter your responce"))
			in5 = int(input("How many devices are connected"))
			h = 'sshpass -p {} ssh {} fdisk -l'.format(ps3, in33)

			if in4 == 1:
				print(os.system(h))
			else:
				pass
			d_name = []
			d = """"""
			for i in range(in5):
				device = input("Enter name of device{}".format(i+1))
				d_name.append(device)
				d = d+' '+d_name[i]

				a = 'sshpass -p {} ssh {} pvcreate {}'.format(ps3, in33, device)
				print(os.system(a))

			vg_name = input("Enter the vg name: ")
			b = 'sshpass -p {} ssh {} vgcreate {} '+d
			b = b.format(ps3, in33, vg_name)
			print(os.system(b))

			parti_name = input("Enter your partition name: ")
			size0 = input("Enter the size of partition: ")
			d = 'sshpass -p {} ssh {} lvcreate {} --size {} --name {} -y'.format(ps3, in33, size0, parti_name)
			print(os.system(d))

			e = 'sshpass -p {} ssh {} mkfs.ext4 /dev/'+vg_name+'/'+parti_name
			e = e.format(ps3, in33)
			f = 'sshpass -p {} ssh {} mount /dev/'+vg_name+'/'+parti_name+' /data'
			f = f.format(ps3, im33)
			print(os.system(e))

			g = 'sshpass -p {} ssh {} mkdir /data'.format(ps3, in33)
			os.system(g)
			os.system(f)
			
			a = """sshpass -p {} ssh {} wget -o /root/jdk-8u171-linux-x64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/jdk-8u171-linux-x64.rpm""".format(ps3, in33)
			os.system(a)

			a = """sshpass -p {} ssh {} wget -o /root/hadoop-1.2.1-1.x86_64.rpm https://buckettejesh.s3.ap-south-1.amazonaws.com/softwares/hadoop-1.2.1-1.x86_64.rpm""".format(ps3,in33)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(ps3,in33)
			os.system(a)

			a = "sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ps3,in33)
			os.system(a)

			
			a = """wget -0 /core-site.xml https://buckettejesh.s3.ap-south-1.amazon.aws.com/code/namenode/core-site.xml""".format(ps3, in33)
			os.system(a)

			with open('/core-site.xml') as f:
				t = f.read().replace('0.0.0.0', in31)

			with open('/core-site.xml', 'w') as f:
				f.write(t)
			os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(ps2, in32))

			a = """sshpass -p {} ssh {} systemctl stop firewalld""".format(ps3, in33)
			os.system(a)

			a = 'sshpass -p {} ssh {} systemctl disable firewalld'.format(ps3, in33)
			os.system(a)

			a = 'sshpass -p {} ssh {} hadoop namenode -format'.format(ps3,  in33)
			os.system(a)

			a = 'sshpass -p {} ssh {} hadoop-daemon.sh start namenode'.format(ps3, in33)
			os.system(a)
			

elif in1 == 2:
	print("""Press 1. To Increase LVM 
Press 2. To Decrease the size of LVM""")
	in10 = int(input("Enter your choice: "))
	if in10 == 1:
		in11 = input("Enter the LVM name which you want to increase")
		in12 = input("Enter the size that you wan to increase")
		a = 'lvextend --resizefs --size +{} {}'.format(in12, in11)
		os.system(a)

	elif in10 == 2:
		in11 = input("Enter the LVM name which you want to decrease")
		in12 = input("Enter the size that you wan to decrease")
		a = 'lvreduce --resizefs --size {} {} -y'.format(in12, in11)
		os.system(a)

elif in1 == 3:
	in50 = int(input("How many devices are connected"))
	d_name = []
	d = """"""
	for i in range(in5):
		print(os.system('fdisk -l'))
		device = input("Enter name of device{}".format(i+1))
		d_name.append(device)
		d = d+' '+d_name[i]

		a = 'pvcreate {}'.format(device)
		print(os.system(a))
		
	vg_name = input("Enter vg name: ")
	c = 'vgcreate {} '+d
	c = c.format(vg_name)
	print(os.system(c))

	parti_name = input("Enter Patition name: ")
	size1 = input("Enter size of partition: ")

	d = 'lvcreate {} --size {} --name {} -y'.format(vg_name, size1, parti_name)
	print(os.system(d))

	e = 'mkfs.ext4 /dev/'+vg_name+'/'+parti_name

	print(os.system(e))

	mo = input("Enter which folder to mount on: ")
	to = 'mkdir '+mo
	os.system(to)
	gg = 'mount /dev/'+vg_name+'/'+parti_name+' '+mo
	os.system(gg)

















