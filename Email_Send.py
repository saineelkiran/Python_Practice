import smtplib
server_1=smtplib.SMTP("smtp.gmail.com",587)
server_1.starttls()
server_1.ehlo()
#Have to use App Password in GmailAccount-->Security . Instead of original password
server_1.login("saineelkiran@gmail.com",'relojzkchswsjrvi')
server_1.sendmail("saineelkiran@gmail.com","sravani.siri92@gmail.com","Hello Sravani, \nThis Mail is Sent using python code by Sai Neel")
print("Mail Sent Successfully")