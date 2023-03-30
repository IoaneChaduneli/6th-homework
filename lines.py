import sys

def main(argument):
    define = define_arg(argument)
    count = count_lines(define)
    print(count)


def define_arg(argument):
    if len(argument) < 2:
        sys.exit('To few arguments')
    if len(argument) > 2:
        sys.exit('Too many arguments')
    
    if argument[1].split(".")[1] != 'py':
        sys.exit('it is not python file')

    try:
        file = open(argument[1], 'r')
    except:
        sys.exit('file does not exist')

    return file
    

def count_lines(file):
    lines = 0 
    first_readline = file.readlines()[0]
    list_first_readline = first_readline.split('.')[1]
    for char in list_first_readline:
        if char != '#':
            lines += 1

    return lines
        

if __name__ == '__main__':
    main(sys.argv)