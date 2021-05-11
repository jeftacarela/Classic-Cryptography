def enkripsi(text,s):
    result = ''

    for i in range(len(text)):
        char = text[i]

        #Encrypt uppercase characters
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        
        #Encrypt lowercase characters
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    
    return result

text = "kriptografi"
s = 13
print "Text     : "+text
print "Shift    : "+str(s)
print "Cipher   : "+enkripsi(text,s)