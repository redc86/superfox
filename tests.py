import superfox as fox

req = fox.get('https://pakkan.com.tr/')

print(req.text)  