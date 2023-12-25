from sys import stdin

if __name__ == '__main__':
    on_string = False
    for line in stdin:
        if not on_string:
            pattern = line.rstrip()
            on_string = True
        else:
            string = line.rstrip()
            on_string = False

            for index, char in enumerate(string):

                if len(string) - index < len(pattern):
                    break
                if string[index:index+len(pattern)] == pattern:
                    print(index, end=" ")

            print('\n')