import os

print("\033[33mОбновление python3-pip...\033[0m")
os.system("pip3 install --upgrade pip")
print("")
bib = ["html5lib", "pystyle", "phonenumbers", "requests", "whois",  "random", "colorama", "threading", "faker", "bs4"]
for i in range(len(bib)):
    print("\033[33mУстановка "+bib[i]+"...\033[0m")
    os.system("pip3 install "+bib[i])
print('\033[32mУстановка модулей успешно завершена!\033[0m')
