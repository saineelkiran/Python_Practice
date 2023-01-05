import smtplib
server_1=smtplib.SMTP("smtp.gmail.com",587)
server_1.starttls()
server_1.ehlo()
#Have to use App Password in GmailAccount-->Security . Instead of original password
server_1.login("<Sender Email>",'<Gmail's App Password>')
server_1.sendmail("<Sender Email>","<Reeiver's Email>","Hello <Receiver Name>, \nThis Mail is Sent using python code by <Sender>")
print("Mail Sent Successfully ")
