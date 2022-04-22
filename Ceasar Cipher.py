class Ceasar_Cipher:

    import string
    from time import sleep

    def execution(self): 
        

        self.alphabet = self.string.ascii_lowercase

        print("Welcome to Caesar Cipher Encryption.\n")
        self.message = input("Type a message you would like to encrypt: ").lower()
        print()
        self.key = int(input("Enter your key: "))

        self.encrypted_message = ""

        for self.c in self.message:

            if self.c in self.alphabet:
                self.position = self.alphabet.find(self.c)
                self.new_position = (self.position + self.key) % 26
                self.new_character = self.alphabet[self.new_position]
                self.encrypted_message += self.new_character
            else:
                self.encrypted_message += self.c

        print("\nEncrypting your message...\n")
        self.sleep(2) # give an appearance of doing something complicated
        print("Stand by, almost finished...\n")
        self.sleep(2) # more of the same
        print("Your encrypted message is:", self.encrypted_message)
        self.finalized = self.encrypted_message.count('') - 2
        return self.finalized, 'char in the message +', self.key, '=', self.finalized + self.key, 'messages'

test = Ceasar_Cipher()
result = test.execution()
print(result)