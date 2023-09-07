import os


if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by Yash Somani")
    while True:
        x=input("Enter what you want to speak: ")
        if( x == 'q'):
            break
        command =f"say {x}"
        os.system(command)

