def main():
    #write your code below this line
    age = int(input("How old are you?"))

    if age >= 0 and age <= 120:
        print("OK")
    else:
        print("Impossible!")

if __name__ == '__main__':
    main()
