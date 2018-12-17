import os
import subprocess
import sys

try:
    input = raw_input
except NameError:
    pass



def main(DONT_ASK=False):

    pyc_files = []

    for dirpath, _, fnames in os.walk(CWD):
        for fname in fnames:
            if fname.endswith('.pyc'):
                pyc_files.append(os.path.join(dirpath, fname))
    if DONT_ASK or input('found {} pyc files. press r to remove '.format(len(pyc_files))) == 'r':
        for fp in pyc_files:
            assert fp.endswith('.pyc')
            subprocess.call(['rm', '-f', fp])
    print('found and removed {} *.pyc files.'.format(len(pyc_files)))
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    CWD = os.getcwd()
    main(DONT_ASK=(sys.argv[-1] in ('--yes', '-F', '-y'))) #support several flags. why not
