import requests
import instaloader
import json



def search_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Найден пользователь GitHub с именем {data['login']}:")
        print(f"Имя: {data['name']}")
        print(f"Биография: {data['bio']}")
        print(f"Последний визит: {data['updated_at']}")
    elif response.status_code == 404:
        print("Пользователь не найден на GitHub.")
    else:
        print("Произошла ошибка при выполнении запроса.")

def main():
    username = input('Введите никнейм: ')
    search_github_user(username)
    

if __name__ == "__main__":
    main()