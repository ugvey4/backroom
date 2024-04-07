import subprocess as sp
from search import searchForNumber as sn
from search import searchForFIO as fio
from search import searchForEmail as mail
from search import searchForNIckname as nick

def getDisplay():
    print('''
[1] По номеру телефона
[2] По ФИО
[3] По электроной почте
[4] По никнейму
[5] Выйти из программы
 ''')

def checkPython():
    print('У вас установлен python?', end=' ')
    yORn = input('Y/N: ').lower()
    if yORn == 'y':
        try:
            version = sp.run(['python3 --version'], shell = True)
            print(version)
        except Exception as e:
            print("Нет")
    elif  yORn == "n":
        print("Для продолжения необходим Python.")
        downPy = sp.run(['sudo apt install python3'], shell = True)
    else:
        exit(0)

def yuorChoice():
    choice  = input('Выбкрете способ поиска:\n')
    if choice == '1':
        sn.getDisplay()
    elif choice == '2':
        fio.getDisplay()
    elif choice == '3': 
        mail.getDisplay()
    elif choice == '4':
        nick.main()
    elif choice == '5':
        exit(0)
    else: 
        return None

def main():
    checkPython()
    getDisplay()
    yuorChoice()

if  __name__ == "__main__":
    main()