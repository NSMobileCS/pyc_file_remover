import subprocess

pyc_files = subprocess.check_output(['find', '.', '-name', "'*.pyc'"]).split('\n')

ok = (input('found {} pyc files. press r to remove '.format(len(pyc_files))) == 'r')

if ok:
    for fp in pyc_files:
        if not fp.endswith('.pyc'):
            print(fp)
            break
        subprocess.call(['rm', fp])
