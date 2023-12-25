from sys import stdin

if __name__ == '__main__':
    on_string = False
    for line in stdin:
        if on_string == False:
            pattern = line.rstrip()
            on_string = True
        else:
            string = line.rstrip()
            on_string = False
            index = 0
            while index < len(string):
                if len(pattern) > len(string[index:]):
                    break
                index = string.find(pattern, index)
                if index == -1:
                    break
                print(index, end=" ")
                index += 1
            print('\n')