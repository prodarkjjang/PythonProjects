#13 learn a little about xmlrpc i guess
# no idea at all - check hints directly, turns out its xmlrpc module (installed in py3)
# RPC stands for remote procedure call, we use xmlrpc.client
# get the method and phone Bert (we found that Bert is evil in previous stages)
# got '555-ITALY' after calling bert
# got 'He is not the evil' after calling '555-ITALY'('555-48259')
# got 'He is not the evil' after calling '555-44482555999'
# just realised that it will return 'He is not the evil' when we don't call bert
# '555-ITALY' is still the clue
# at the evil stage, one of the picture of has 'ity' slashed
# italy is the answer
# just realised 555 phone numbers are fake in the US
import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
conn.system.listMethods()

conn.phone('Bert')

conn.phone('555-48259')

conn.phone('555-44482555999')

