from zipfile import ZipFile
import os

test,train=[],[]
for file in os.listdir('test/'):
    test.append(file)

for file in os.listdir('train/'):
    train.append(file)

with ZipFile('test.zip','w') as zip:
    for file in test:
        zip.write('test/'+file)
print(len(test),len(train))

with ZipFile('train.zip', 'w') as zip:
    for file in train:
        if os.path.isfile('train/'+file):
            zip.write('train/'+file)
        else:
            print("{} file not found".format(file))
