import requests

def main():
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=RMB")
    if res.status_code != 200:
        raise Exception("ERROR: API thingy failed")
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()
