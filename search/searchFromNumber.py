import subprocess as sp

def getDisplay():
    try:
        phoneNumber = input('Введите номер телефона: +7 ')
        checkPhone()
    except Exception as e:
        print(f'Ошибка ввода: {e}')
        return None
    
def checkPhone(phone):
    if len(phone) != 10 or not phone.isdigit():
        return False
    else:
        return True

def bankData():
    pass
        
def main():
    getDisplay()

if  __name__ == "__main__":
    main()
