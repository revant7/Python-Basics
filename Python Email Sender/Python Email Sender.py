##############  PYTHON - E-MAIL SENDER   #################
#importing the required modules
import smtplib as sl

def email_sender(s_email_id,s_email_pass,r_email_id,message):
  s = sl.SMTP('smtp.gmail.com',587) #create smtp session to send email
  s.starttls() #starts tls security to ensure privacy
  s.login(s_email_id,s_email_pass) # login with sender's orignal email id and password
  s.sendmail(s_email_id,r_email_id,message) #sending email: final step
  s.quit() #quit the server
  print("\nEmail Sent Successfully.\n")
  print("\nThank You For Choosing My App. Please Visit Again Soon!\n")

a = input("Enter Sender's Email Address: ")
b = input("Enter Sender's Email Address Password: ")#2-step verification should be turned on
################generate app password from 'manage your google account page'
################enter the 16 digit gmail app password here
################you can also use your google account password if 2-step verification is turned off.
c = input("Enter Reciever's Email Address: ")
d = input("Enter Your Message: ")


email_sender(a,b,c,d) #calling the function
