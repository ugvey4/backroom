import subprocess as sp

def getDisplay():
    try:
        fioPerson = input('Введите почту: ')
    except  Exception as e:
        print(f'Ошибка ввода данных: {e}')
        return None
    else:
        print(f"Почта:{fioPerson}")
    
def main():
    getDisplay()

if  __name__ == "__main__":
    main()