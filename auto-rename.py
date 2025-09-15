import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()


print("""
███▄ ▄███▓ ▄▄▄       ███▄    █ ▒███████▒▒██   ██▒
▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▒ ▒ ▒ ▄▀░▒▒ █ █ ▒░
▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒░ ▒ ▄▀▒░ ░░  █   ░
▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▄▀▒   ░ ░ █ █ ▒ 
▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░▒███████▒▒██▒ ▒██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒▒▒ ░ ░▓ ░
░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒░░   ░▒ ░
░      ░     ░   ▒      ░   ░ ░ ░ ░ ░ ░ ░ ░    ░  
       ░         ░  ░         ░   ░ ░     ░    ░  
                                ░                 
███╗   ██╗ ██████╗ ████████╗    ██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
████╗  ██║██╔═══██╗╚══██╔══╝    ██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║
██╔██╗ ██║██║   ██║   ██║       ███████║██║   ██║██╔████╔██║███████║██╔██╗ ██║
██║╚██╗██║██║   ██║   ██║       ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║ ╚████║╚██████╔╝   ██║       ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
<=============================================================================> 
""")
# Tampilkan ajakan subscribe
print("\033[93mSubscribe ke channel YouTube \033[91m@manzxdigital\033[93m untuk melanjutkan...\033[0m")

# Buka channel YouTube tanpa output
os.system("am start -a android.intent.action.VIEW -d https://www.youtube.com/@manzxdigital > /dev/null 2>&1")

# Tunggu 15 detik biar sempet klik subscribe dulu
time.sleep(15)

# Input folder dan nama dasar
folder = input("Masukin path folder yang isinya foto: ").strip()
nama_dasar = input("Masukin nama dasar file (misal 'foto'): ").strip()

if not os.path.isdir(folder):
    print("Folder nggak ditemukan!")
    exit()

files = sorted(os.listdir(folder))
i = 1

for filename in files:
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        ext = filename.split('.')[-1]
        new_name = f"{nama_dasar}_{i}.{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        i += 1

print("\n\033[92mBerhasil rename semua file!\033[0m")
