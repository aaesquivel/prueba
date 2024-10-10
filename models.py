import sys

def rf():
    print('Ejecutando Random Forest')

def cb():
    print('Ejecutando Catboost')

def main():
    if sys.argv[1] == 'rf':
        rf()
    elif sys.argv[1] == 'cb':
        cb()
    else:
        print("Sin modelo")

if __name__ == '__main__':
    main()
