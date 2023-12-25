from sys import stdin
def string_match(pattern, string):
    char = 0
    length = len(pattern)
    #print(length)
    while char < (len(string)):
        try:
            if(length == 1):
                location = string.index(pattern, char)
            else:
                location = string.index(pattern, char, -(length - 1))
            print(location, end = " ")
            char = location + 1
            #print(char)
        except:
            break

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
            if pattern in string:
                string_match(pattern, string)
                print('\n')
            else:
                print('\n')
                continue