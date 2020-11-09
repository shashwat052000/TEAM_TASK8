import os

def indkr():
	a=1
	b=3
	def clr():
	    os.system('clear')

	clr()
	while True:
	    clr()
	    inp=input('''
		    ________________________________
		    |   press 1: Docker configure  |
		    |   press 2: Launch a container|
		    |   press 3: Docker Images     |
		    |   press 4: Docker container  |
		    |   press 5: Docker logs       |
		    |   press x: exit the program  |
		    """"""""""""""""""""""""""""""""
		Enter the option : ''')


		                     #docker configure block
                                     #"""""""""""""""""""""""
	    if inp=='1':
		clr()
		l=True
		
		while l:
		    
		    inp1 = input('''
		    _________________________________________
		    |   press 1: install docker             |
		    |   press 2: uninstall dokcer           |
		    |   press 3: activate docker services   |
		    |   press 4: deactivate docker services |
		    |   press b: previous menu              | 
		    """""""""""""""""""""""""""""""""""""""""
		    Enter the option:''')
		    clr()
		    if inp1=='b':
		        l=False
		    elif inp1=='1' :
		        if a!=1:
		            a=1
		            os.system('yum install docker-ce')
		        else:
		            print('docker aldready installed!')
		    elif inp1=='2':
		        if a!=2:
		            a=2
		            os.system('yum remove docker-ce')
		        else:
		            print('docker already uninstalled!')
		    elif inp1=='3' :
		        if b!=3:
		            b=3
		            os.system('systemctl start docker')
		            os.system('systemctl status docker')
		        else:
		            print('service already started.....')
		    elif inp1=='4':
		        if b!=4:
		            b=4
		            os.system('systemctl stop docker')
		            os.system('systemctl status docker')
		        else:
		            print('service already stopped.....')
		    else:
		        print('Wrong option! Try Again.')
		    



		                #launch a container block

	    elif inp=='2':
		l = True
		while l:
		    clr()
		    osimg=input('''enter the image:V
		    [some available ones
		    press 1 : centos:latest
		    press 2 : ubuntu:latest]
		    you can download more from prev menu
		    *press b: previous menu*
		    (Enter Here):''')
		    if osimg=='b':
		        l=False
		    else:
		        osname=input('enter your OS name :')
		        use=input('need customisation? yes/no! :')

		        if use=='no' or use=='No' or use=='NO':
		            if osimg=='1':
		                 os.system(f'docker run -it --name {osname} shashwatpp/dmenupy:v2')
		            if osimg=='2':
		                os.system(f'docker run -it --name {osname} ubuntu:latest')
		        else:
		            typ=input('''choose the available customisation
		            1.detached container
		            2.one time container [otc]
		            3.single process container 
		            [press 23 for opt2 + opt3]
		            (Enter here) : ''')
		            if typ=='detached container' or typ=='detached' or type=='detach':
		                os.system(f'docker run -dit --name {osname} {osimg}')
		            elif typ=='otc':
		                os.system(f'docker run -rit --name {osname} {osimg}')
		            elif typ=='23':
		                pro=input('enter one time process :')
		                os.system(f'docker run -rit --name {osname} {osimg} {pro}')
		            elif typ=='3':
		                pro=input('enter the process name :')
		                os.system(f'docker run -it --name {osname} {osimg} {pro}')
		            else:
		                print('Wrong Input!Try Again.')




		                #docker image block
	    elif inp=='3':
		l=True
		clr()
		while l:
		    
		    img=input('''
		        ____________________________________________________
		        |   Press 1: Show all docker images in the system  |
		        |   Press 2: Search for docker images              |
		        |   Press 3: Download a docker image               |
		        |   Press 4: Upload your docker image              |
		        |   Press 5: Remove an image                       |
		        |   Press b: previous menu                         | 
		        """"""""""""""""""""""""""""""""""""""""""""""""""""
		    Enter a option : ''')
		    clr()
		    if img=='b':
		        l=False
		    elif img=='1':
		        os.system('docker images')
		    elif img=='2':
		        iname=input('enter the image name to search')
		        os.system(f'docker search {iname}')
		    elif img=='3':
		        imgd=input('enter the image name to download [latest by default]')
		        os.system(f'docker pull {imgd}')
		    elif img=='4':
		        imgu=input('enter the name of image to upload [should be pressent in the system ]:')
		        os.system(f'docker push {imgu}')
		    elif img=='5':
		        rmi=input('enter the image name/ID to delete')
		        os.system(f'docker rmi {rmi}')
		    else:
		        print('Wrong Input! Try Again.')




		            #docker container block
	    elif inp=='4':
		l=True
		clr()
		while l:
		    
		    dc=input('''
		        ____________________________________________________________    
		        |   press 1: show all running containers                    |
		        |   press 2:show all the container present in the system    |   
		        |   press 3:remove a container                              |
		        |   press 4:remove all containers                           |
		        |   press 5: create an image out of a container             |
		        |   press b: Preevious menu                                 |
		        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
		    Enter the option : ''')
		    clr()
		    if dc=='b':
		        l=False
		    elif dc=='1':
		        os.system('docker ps')
		    elif dc=='2':
		        os.system('docker ps -a')
		    elif dc=='3':
		        cname=input('enter container name to remove :')
		        os.system(f'docker rm {cname}')
		    elif dc=='4':
		        os.system('docker rm `docker ps -a -q`')
		    elif dc=='5':
		        cname=input('enter the container name to clone :')
		        iname=input('enter your clone image name:V [eg-myOS:5.5]')
		        os.system(f'docker commit {cname} {iname}')
		    else:
		        print('Wrong input ! Try Again.')


		                               #docker logs block
	    elif inp=='5':
		l=True
		while l:
		    clr()
		    cn=input('''enter the container name
		      [press b for prev menu]
		      (Enter Here) : ''')
		    if cn=='b':
		        l=False
		    os.system(f'docker logs {cn}')


		                                #exit block
	    elif inp=='x':
		while True:
		    clr()
		    print('HAVE \n\n\n\n\n')
		    print('            Aaa\n\n\n\n\n\n')
		    print('                     NICE\n\n\n\n\n\n')
		    print('                                 DAY!')


		                                #try again block
	    else:
		print('Wrong Input , Try Again!')
		clr()
		
        
