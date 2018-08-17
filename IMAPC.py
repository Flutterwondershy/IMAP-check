#!/usr/bin/python

#You can add multiple accounts
accounts = [{"server":"mail.vivaldi.net", "port":993, "login":"me@vivaldi.net", "password":"password"}]

import imaplib
import time

numberOfMails = 0

for account in accounts:
    obj = imaplib.IMAP4_SSL(account["server"], account["port"])
    obj.login(account["login"], account["password"])
    obj.select()
    numberOfMails += len(obj.search(None, 'unseen')[1][0].split())

if numberOfMails != 0:
    print("")
else:
    print("")
