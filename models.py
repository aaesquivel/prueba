import sys

def xg():
    print('Ejecutando XGBoost')

def cb():
    print('Ejecutando Catboost')

def rf():
    print('Ejecutando Random forest')

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
