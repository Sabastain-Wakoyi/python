def main():
    name = input("What's your name")
    print(hello(name))

    #output = hello(name)
    #print(output)


def hello(to="world"):
    return f"hello {to}"


if __name__ == "_manin_":
    main()
