import tarfile
names = []
for i in range(9):
    names.append("images_"+str(0)+str(i+1)+(".tar.gz"))
for i in [10,11,12]:
    names.append("images_"+str(i)+(".tar.gz"))
for file in names:
    tar = tarfile.open(file, "r:gz")
    if tar:
        tar.extractall()
