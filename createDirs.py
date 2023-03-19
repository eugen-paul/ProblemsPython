import os

path = "Problems"

for th in range(0, 5):
    f = path + "/" + str(th * 1000) + "_" + str(th * 1000 + 999)
    isExist = os.path.exists(f)
    if not isExist:
        os.mkdir(f)
    for h in range(10):
        sub = f + "/" + str(th * 1000 + h * 100) + "_" + str(th * 1000 + h * 100 + 99)
        isExist = os.path.exists(sub)
        if not isExist:
            os.mkdir(sub)
