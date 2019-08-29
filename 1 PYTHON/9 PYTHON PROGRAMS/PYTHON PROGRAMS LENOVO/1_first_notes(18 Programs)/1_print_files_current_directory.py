import os
def directory_content(spath):
    for schild in os.listdir(spath):
        schildpath=os.path.join(spath,schild)
    if os.path.isdir(schildpath):
        directory_content(schildpath)
    else:
        print(schildpath)

