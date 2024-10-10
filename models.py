import sys

def xg():
    print('Ejecutando XGBoost')

def main():
    if sys.argv[1] == 'xg':
        xg()
    else:
        print("Sin modelo")

if __name__ == '__main__':
    main()
