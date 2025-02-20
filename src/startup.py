import sys
import time
import random
from colorama import Fore, Style, init
from art import text2art

init(autoreset=True)

def animated_loading():
    animation = ["|", "/", "-", "\\"]
    for i in range(30):
        sys.stdout.write(f"\r{Fore.YELLOW}🚀 Starting bot... {animation[i % len(animation)]} {Fore.CYAN}{'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\r{Fore.GREEN}✅ Bot started successfully!       ")

def progress_bar():
    print(Fore.CYAN + "🔹 Initializing...")
    for i in range(1, 21):
        time.sleep(0.1)
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r[{Fore.GREEN}{bar}{Fore.RESET}] {i*5}%")
        sys.stdout.flush()
    print("\n" + Fore.GREEN + "✅ Initialization Complete!")

def startup_banner():
    banner = text2art("OCTOMOD")
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for line in banner.split("\n"):
        print(random.choice(colors) + line)
        time.sleep(0.1)
