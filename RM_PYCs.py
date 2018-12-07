import os
import subprocess
import sys

try:
    input = raw_input
except NameError:
    pass



def main():

    pyc_files = []

    for dirpath, _, fnames in os.walk(CWD):
        for fname in fnames:
            if fname.endswith('.pyc'):
                pyc_files.append(os.path.join(dirpath, fname))

    OK_DO_REMOVE = (input('found {} pyc files. press r to remove '.format(len(pyc_files))) == 'r')

    if OK_DO_REMOVE:
        for fp in pyc_files:
            print(fp)
            if not fp.endswith('.pyc'):
                break
            subprocess.call(['rm', fp])
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    CWD = os.getcwd()
    main()
