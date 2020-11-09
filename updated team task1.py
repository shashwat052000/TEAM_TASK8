import getpass
def send_email():
	# smtplib module send mail
    import smtplib
    print("To whom you want this email: \n")
    TO = input("")
    SUBJECT = 'TEST MAIL'
    TEXT = 'Here is a message from python.'

	# Gmail Sign In
    print("Enter Your Email: \n")
    gmail_sender = input("")
    print("Password: \n")
    gmail_passwd = getpass.getpass('')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    BODY = '\r\n'.join(['To: %s' % TO,
                    	'From: %s' % gmail_sender,
                    	'Subject: %s' % SUBJECT,
                    	'', TEXT])
    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')
        
    server.quit()

def run_ml_code():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

	# Importing the dataset
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    X = X.reshape(-1,1)
    Y = dataset.iloc[:, 1].values # Dependent Variable/Target Values
    Y = Y.reshape (-1,1)

	# Splitting the Dataset into Training Set and Test Set
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)
    
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)

	# Predicting the Test Set Results
    y_pred = regressor.predict(X_test)
    print("Enter Years Experience")
    rr = regressor.predict([[int(input())]])
    print (rr)

def send_whatsapp_message():
    import webbrowser
    new = 2 
    url = "add of html file"
    webbrowser.open(url,new=new)


def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print( "1. Press 1 to sent an email")
    print ("2. Press 2 to run ML code")
    print( "3. Press 3 to sent a whatsapp  messgae")
    print ("4. Exit")
    print( 67 * "-")
loop=True      
  
#while loop:          ## While loop which will keep going until loop = False
 #   print_menu()    ## Displays menu
  #  choice = input("Enter your choice [1-5]: ")
print_menu()
print("Enter your choice [1-5]: \n")
v1 = int(input())

if v1 == 1:
    send_email()

elif v1 == 2:
    run_ml_code()

elif v1 == 3:
    send_whatsapp_message()