import xmlrpc.client

base_url='http://www.pythonchallenge.com/pc/phonebook.php'
proxy=xmlrpc.client.ServerProxy(base_url)
print(proxy.phone('Bert'))