import subprocess as sp

def getDisplay():
    try:
        fioPerson = input('Введите ФИО: ')
    except  Exception as e:
        print(f'Ошибка ввода данных: {e}')
        return None
    else:
        print(f"ФИО:{fioPerson}")
    
def main():
    getDisplay()

if  __name__ == "__main__":
    main()