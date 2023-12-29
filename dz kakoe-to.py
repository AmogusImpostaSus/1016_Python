import colorama
from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Це текст з червоним кольором" + Style.RESET_ALL)
print(Back.GREEN + "Це текст зеленого фону" + Style.RESET_ALL)
print(Fore.CYAN + Back.YELLOW + "Це текст із синім кольором та жовтим фоном" + Style.RESET_ALL)
print(Fore.MAGENTA + Style.BRIGHT + "Це яскравий текст" + Style.RESET_ALL)

init_color = lambda: init(autoreset=True, convert=True)

colorama.deinit()
