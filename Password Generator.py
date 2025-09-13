import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def menu():
    print("===== 🔑 Password Generator =====")
    while True:
        try:
            length = int(input("Enter password length (min 6): "))
            if length < 6:
                print(" Password length too short! Try again.")
                continue

            password = generate_password(length)
            print(f" Generated Password: {password}")

            again = input("Generate another? (y/n): ").lower()
            if again != "y":
                print(" Exiting Password Generator. Stay secure!")
                break
        except ValueError:
            print(" Please enter a valid number.")

if __name__ == "__main__":
    menu()