import random
import bcrypt 

class PasswordCreator:
  
  # Computer dictionary
  word_list = [line.strip() for line in open('/usr/share/dict/words')]

  # Return an XKCD-type password
  def createXKCD(self):
    password = ""
    for i in range(0,4):
      index = random.randint(0, len(self.word_list)-1)
      word = self.word_list[index]
      word = word[0].upper() + word[1:]
      password = password + word
    return password

  # Needs to be of byte type, therefor encode
  def bcrypt_pwd(self, pw):
    return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())


pc = PasswordCreator()
password = pc.createXKCD()
print("password before encryption: " + password)
pencr = pc.bcrypt_pwd(password)
print("password after encryption: " + pencr.decode())
