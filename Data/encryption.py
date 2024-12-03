# Caesar Cipher implementation
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
encrypted_message = []
for ch in message:
    encrypted_message.append(chr(ord(ch)+shift))
print(''.join(encrypted_message))