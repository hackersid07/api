import requests
import colorama
import os
colorama.init(autoreset=True)
def main():
     print(colorama.Fore.RED+'hii')
     data=requests.get("https://raw.githubusercontent.com/hackersid07/demo/master/db.json")
     print(os.getcwd(),data.json())

if __name__=="__main__":
    main()
