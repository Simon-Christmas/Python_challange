import re

with open('challange_3.txt', 'r') as myfile:
    data = myfile.read()
    # .replace('\n', '')

m = re.findall("[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]", data)
url = ''
for match in m:
    url = url + match[4:5]
print(url)
