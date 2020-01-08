import random
import bcrypt 
import hashlib

class PasswordCreator:
  
  # Computer dictionary
  word_list = [line.strip() for line in open('/usr/share/dict/words')]

  # Return an XKCD-type password
  def createXKCD(self, word_list=word_list, num_of_words=4):
    password = ""
    for i in range(0,num_of_words):
      index = random.randint(0, len(word_list)-1)
      word = word_list[index]
      word = word[0].upper() + word[1:]
      password = password + word
    return password


  # User can now choose the length of the words to be used
  def createXKCD_short(self, word_len=4):
    word_list_new = list(filter(lambda k: len(k)==word_len, self.word_list))
    return self.createXKCD(word_list_new)

  # Needs to be of byte type, therefor encode
  def bcrypt_pwd(self, pw):
    return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())

  def md5_pwd(self, pw):
    return hashlib.md5(pw.encode())


  def decrypt(self):
    str = self.md5_pwd("LampFootball").hexdigest() # Just a way to represent that we have the password
    wd = self.word_list
    num_of_guesses = 0
    
    # Will run until it finds something, else for eternity
    while True:
      password = self.createXKCD(word_list=wd, num_of_words=2)
      num_of_guesses = num_of_guesses + 1
      if(str == self.md5_pwd(password).hexdigest()):
        print(password)
        print(num_of_guesses)  
        return password
 



# ------------------------------------------------------------------------------------------------------------------------------------------------------    

# Just testing 
pc = PasswordCreator()

# pc.decrypt()
# md5_pw =pc.md5_pwd("jonathan")
#print(md5_pw.hexdigest())

password = pc.createXKCD()
print(password)

# print("password before encryption: " + password)
# pencr = pc.bcrypt_pwd(password)
# print("password after encryption: " + pencr.decode())
