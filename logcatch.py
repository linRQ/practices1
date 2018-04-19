import logc
import os
import log_data_basic as ld


def main():
    listd = os.listdir(ld.pathname)
    for i in listd:
        path = os.path.join(ld.pathname, i)
        print(path)
        logc.catchFile(path, ld.savepath)
    pass


main()
