import requests


def main():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response)


if __name__ == "__main__":
    main()
    # e4f461af9bc04ba38f31829d071fb25c
