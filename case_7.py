import os


def main():
    while True:
        print(os.getcwd())
        print("MENU")
        command = acceptCommand()
        if command == "QUIT":
            print("Работа программы завершена.")
            break

main()
