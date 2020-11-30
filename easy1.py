x = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
y = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

shift= (int(input("Enter the shift:")))
text= (str(input("Enter the text:")))

ciphertext = ""
for c in text.upper():
    if c.isalpha(): ciphertext += y[ (x[c] + shift)%26 ]
    else: ciphertext += c

text2 = ""
for c in ciphertext.upper():
    if c.isalpha(): text2 += y[ (x[c] - shift)%26 ]
    else: text2 += c

print (text)
print (ciphertext)
print (text2)
