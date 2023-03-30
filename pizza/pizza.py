import sys, csv
from tabulate import tabulate

def main(argument):
    define = define_argumen(argument)
    print(define)




def define_argumen(argument):
    if len(argument) > 2:
        sys.exit('Too many argument')
    if len(argument) < 2:
        sys.exit('Too few argument')
    
    if not argument[1].endswith('.csv'):
        sys.exit('This is not the csv file')

    try: 
        with open('sicilian.csv', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = [row for row in reader]

        with open ('regular.csv', 'w', newline='') as fwrite:
            writer = csv.writer(fwrite)
            writer.writerow(header)
            writer.writerows(data)
            if argument[1]:
                table = tabulate(data, headers=header, tablefmt='grid')
                return table
    except FileNotFoundError:
        sys.exit(f'{argument[1]} file is not found')
    except csv.Error as e:
        sys.exit(f'Error during reading {e} file')



if __name__ == '__main__':
    main(sys.argv)