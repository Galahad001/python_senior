import zipfile

class Archive:
    def __init__(self, path, description):
      self.path = path
      self.description = description
      self.password = None
    def getinfo(self):
      print("Path: " + self.path + "\nDesc:" + self.description + "\nPassword:" + str(self.password))


class Bruteforce:
   def __init__(self, dictionary):
      self.dictionary = dictionary
   def hack(self, archive):
        zip_file = zipfile.ZipFile(archive)
        password = None
        f = open(self.dictionary, 'r')
        for line in f.readlines():
         password = line.strip('\n')
         try:
            zip_file.extractall(pwd=password.encode())
            print("-------------------")
            print("RESULT: " + password)
            f.close()
            return (True, password)
         except:
            print(password)
        f.close()
        return (False, None)


class Library:
   def __init__(self, bruteforce):
      self.bruteforce = bruteforce
      self.archives = []
   def showarchives(self):
      for archive in self.archives:
         archive.getinfo()
         print("")
   def hackall(self):
      for archive in self.archives:
         if archive.password == None:
            res = self.bruteforce.hack(archive.path)
            if res[0] == True:
              archive.password = res[1]

library = Library(Bruteforce("dictionary.txt"))
library.archives.append(Archive("test.zip","TEST"))
library.archives.append(Archive("text.zip","TEST2"))

library.showarchives()

library.hackall()
library.showarchives()