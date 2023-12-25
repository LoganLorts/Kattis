import re
from sys import stdin

if __name__ == '__main__':
    on_string = False
    for line in stdin:
        #print(line)
        if on_string == False:
            pattern = line.rstrip()
            on_string = True
        else:
            string = line.rstrip()
            on_string = False
            try:
                a = [m.start() for m in re.finditer('(?={0})'.format(re.escape(pattern)), string)]
                for i in a:
                    print(i, end = " ")
                print('\n')
            except:
                continue