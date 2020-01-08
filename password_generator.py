import random

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

p = PasswordCreator()
print(p.createXKCD())
