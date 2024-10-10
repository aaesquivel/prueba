import sys

def rf():
    print('Ejecutando Random Forest')

def main():
    if sys.argv[1] == 'rf':
        rf()
    else:
        print("Sin modelo")

if __name__ == '__main__':
    main()
