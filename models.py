import sys

def rf():
    print('Ejecutando Random Forest')

def cb():
    print('Ejecutando Catboost')

def xg():
    print('Ejecutando XGBoost')

def main():
    if sys.argv[1] == 'rf':
        rf()
    elif sys.argv[1] == 'cb':
        cb()
    elif sys.argv[1] == 'xg':
        xg()
    else:
        print("Sin modelo")

if __name__ == '__main__':
    main()
