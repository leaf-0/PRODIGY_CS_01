def encrypt_text(pt,n):
    ans = ""
    for i in range(len(pt)):
        ch = pt[i]
        
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)  
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97) 
    return ans


def decrypt(pt,k):
    
    letters="abcdefghijklmnopqrstuvwxyz"  
    decrypted_message = ""

    for ch in pt:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("Your decrypted message is:")
    print(decrypted_message)


print("******* CAESAR CIPHER IMPLEMENTATION*******")
print()
while True:
    print("Do you want to Encrypt or Decrypt")
    user=input('Encrypt/Decrypt: ').lower()
    print()
    if user== "encrypt":
        print("***ENCRYPTION***")
        print()
        pt = str(input("PlainText : ").strip())
        n = int(input("Key : "))
        print("Plain Text is : " + pt)
        print("Shift pattern is : " + str(n))
        print("Cipher Text is : " + encrypt_text(pt,n))
    else:
        print("***DECRYPTION***")
        print()
        pt = input("Enter the Cipher Text: ").strip()
        k = int(input("Enter the Key: "))
        decrypt(pt,k)

    a=input("Do you want to continue? (yes/no):  ").lower()
    if a!= 'yes':
        break
    



































