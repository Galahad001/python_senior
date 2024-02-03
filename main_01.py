import zipfile

zipname = 'python_senior.zip'
dictionary = 'key.txt'

zip_file = zipfile.ZipFile(zipname)
print(zip_file)

password = None

f = open(dictionary, 'r')
for line in f.readlines():
    password = line.strip('\n')
    try:
        zip_file.extractall(pwd=password.encode())
        print("-------------------")
        print("RESULT: " + password)
        f.close()
        break
    except:
        print(password)
f.close()