import base64

# paste the code you want to uncover here and remove the last line that says 
# eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))


with open('output.txt','wb') as output:
  output.write(base64.b64decode(trust))
