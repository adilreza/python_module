import email
import imaplib
username='xuetianhc@gmail.com'
password='2226223326sparkbrain'

mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select("inbox")

type, data = mail.search(None, 'ALL',)
mail_ids =data[0]

id_list=mail_ids.split()
fmid=int(id_list[0])
lmid=int(id_list[-1])
print(fmid)
print(lmid)


print(mail_ids)

