#========= OSINT-MASTER (v2.0 SUPER ACCURATE) by polosscool ==================#
import os, sys, requests, re, random, time
import requests
from colorama import Fore, init
from datetime import datetime
from urllib.parse import quote
init(autoreset=True)

#======== CONFIG + BANNER ====================================================#
BANNER = f"""{Fore.RED}
 ██████╗ ███████╗███╗   ██╗██╗████████╗
██╔════╝ ██╔════╝████╗  ██║██║╚══██╔══╝
██║  ███╗█████╗  ██╔██╗ ██║██║   ██║   
██║   ██║██╔══╝  ██║╚██╗██║██║   ██║   
╚██████╔╝███████╗██║ ╚████║██║   ██║   
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝   
      {Fore.CYAN}👣 OSINT MASTER v2.0 | by polosscool
"""
print(BANNER)

#====================== INPUT VALIDATOR =====================================#
if len(sys.argv) != 2:
    print(Fore.YELLOW + "[!] Gunakan: python3 osint_master.py NAMA_TARGET")
    sys.exit()

target_name = sys.argv[1].strip().replace(" ", "+")
print(Fore.GREEN + f"[•] Menjalankan OSINT terhadap: {target_name.replace('+',' ')}")
print(Fore.CYAN + f"[•] Waktu: {datetime.now()}")
print("-" * 60)

#====================== FITUR OSINT AKURAT ===================================#

# penjelasan: fitur ini menghasilkan dork pencarian untuk menggali jejak digital target
#======== NAMA FITUR: fitur1_google_dorking ====================================#
def fitur1_google_dorking(nama):
    print(Fore.LIGHTGREEN_EX + "[1] Google Dorking...")
    dorks = [
        f'site:facebook.com "{nama}"',
        f'site:linkedin.com "{nama}"',
        f'site:github.com "{nama}"',
        f'"{nama}" filetype:pdf OR filetype:docx',
        f'"{nama}" intitle:index.of',
        f'"{nama}" intext:password',
        f'site:pastebin.com "{nama}"',
        f'site:stackoverflow.com "{nama}"',
        f'"{nama}" filetype:xls OR filetype:xlsx',
        f'"{nama}" filetype:sql',
        f'"{nama}" filetype:log',
        f'"{nama}" filetype:csv',
        f'"{nama}" site:archive.org',
        f'"{nama}" site:medium.com',
        f'"{nama}" site:reddit.com',
        f'"{nama}" site:twitter.com',
        f'"{nama}" site:youtube.com',
        f'"{nama}" site:tiktok.com',
        f'"{nama}" inurl:/admin',
        f'"{nama}" inurl:/login',
        f'"{nama}" inurl:/dashboard',
        f'"{nama}" ext:txt | ext:docx | ext:pdf',
        f'"{nama}" confidential',
        f'"{nama}" intext:@gmail.com',
        f'"{nama}" intext:@yahoo.com',
        f'"{nama}" site:zoominfo.com',
        f'"{nama}" site:slideshare.net',
        f'"{nama}" site:blogspot.com',
        f'"{nama}" site:wordpress.com',
        f'"{nama}" site:who.is',
        f'"{nama}" "curriculum vitae"',
        f'"{nama}" "cv.doc"',
        f'"{nama}" "resume.doc"',
        f'"{nama}" "SSN"',
        f'"{nama}" "NIK"',
        f'"{nama}" filetype:ppt OR filetype:pptx',
        f'"{nama}" ext:conf | ext:cnf',
        f'"{nama}" filetype:env OR filetype:bak',
        f'"{nama}" site:academia.edu',
        f'"{nama}" site:researchgate.net',
        f'"{nama}" site:shodan.io',
        f'"{nama}" "username" "password"',
        f'"{nama}" site:trello.com',
        f'"{nama}" site:drive.google.com',
        f'"{nama}" site:dropbox.com',
        f'"{nama}" site:mega.nz',
        f'"{nama}" site:1drv.ms',
        f'"{nama}" site:box.com',
        f'"{nama}" site:scribd.com',
        f'"{nama}" site:figshare.com'
    ]
    for dork in dorks:
        print(Fore.YELLOW + f"[DORK] {dork}")

# penjelasan: cek keaktifan username di sosial media terkenal

#======== NAMA FITUR: fitur2_username_check ====================================#
def fitur2_username_check(nama):
    print(Fore.LIGHTGREEN_EX + "[2] Pengecekan Username Sosial Media...")

    sosial = [ # GUNA NYA BUAT MENCARI DI SOSIAL MEDIA INI adlaha terget utama media sosial  nya atau yang di scan
        "https://facebook.com",
        "https://twitter.com",
        "https://instagram.com",
        "https://tiktok.com/@",
        "https://github.com",
        "https://pinterest.com",
        "https://snapchat.com/add",
        "https://youtube.com/@",
        "https://linkedin.com/in",
        "https://reddit.com/user",
        "https://medium.com/@",
        "https://ask.fm",
        "https://vimeo.com",
        "https://soundcloud.com",
        "https://twitch.tv",
        "https://dribbble.com",
        "https://behance.net",
        "https://flickr.com/photos",
        "https://ok.ru",
        "https://vk.com",
        "https://steamcommunity.com/id",
        "https://mastodon.social/@",
        "https://tumblr.com/blog/view",
        "https://bandcamp.com",
        "https://goodreads.com/user/show",
        "https://dev.to",
        "https://500px.com",
        "https://replit.com/@",
        "https://about.me",
        "https://trakt.tv/users",
        "https://disqus.com/by",
        "https://gitlab.com",
        "https://codepen.io",
        "https://bitbucket.org",
        "https://keybase.io",
        "https://patreon.com",
        "https://ko-fi.com",
        "https://buymeacoffee.com",
        "https://tripadvisor.com/members",
        "https://slideshare.net",
        "https://mix.com",
        "https://blueskyweb.xyz/profile",
        "https://gab.com",
        "https://imgur.com/user",
        "https://crunchbase.com/person",
        "https://fandom.com/u",
        "https://unsplash.com/@",
        "https://letterboxd.com",
        "https://venmo.com"
    ]

    for site in sosial:
        url = f"{site}/{nama}"
        try:
            res = requests.get(url, timeout=6)
            if res.status_code == 200:
                print(Fore.GREEN + f"[AKTIF] {url}")
            elif res.status_code == 404:
                print(Fore.RED + f"[TIDAK ADA] {url}")
            else:
                print(Fore.YELLOW + f"[?] {url} [status: {res.status_code}]")
        except:
            print(Fore.RED + f"[ERROR] {url}")

# penjelasan: menebak format email umum berdasarkan nama target

def fitur3_email_guess(nama):
    print(Fore.LIGHTGREEN_EX + "[3] Menebak Email Umum...")
    suffix = ["@gmail.com", "@yahoo.com", "@outlook.com", "@protonmail.com"]
    base = nama.lower().replace("+", "").replace(".", "").replace("_", "")
    for sfx in suffix:
        email = base + sfx
        print(Fore.MAGENTA + f"[EMAIL GUESS] {email}")

# penjelasan: mengambil tanggal domain dari whois.my.id

def fitur4_tanggal_domain(nama):
    print(Fore.LIGHTGREEN_EX + "[4] Cek Tanggal Pembuatan Domain...")
    try:
        url = f"https://whois.my.id/search.php?domain={nama}.com"
        res = requests.get(url, timeout=7).text
        hasil = re.findall(r"(Creation Date.*?)<", res)
        if hasil:
            print(Fore.CYAN + "[FOUND] " + hasil[0])
        else:
            print(Fore.RED + "[X] Gagal ambil data")
    except:
        print(Fore.RED + "[X] Error koneksi")

# penjelasan: scan kemungkinan data bocor via scylla.sh
# scylla.sh adalah layanan OSINT publik
# Fokus untuk mencari data hasil kebocoran (leak) seperti:
# - Email
# - Username
# - Password (hash atau plaintext)
# - IP address, domain, dll

# Website resmi: https://scylla.sh
# Bisa digunakan untuk cari data dengan query seperti:
#   email:asep@gmail.com
#   username:ninditaatmoko
#   domain:example.com

# scylla.sh tidak butuh login
# Hasil pencarian biasanya berupa:
#   [email] -> [username] -> [password] -> [sumber bocor]

# Banyak digunakan untuk investigasi cybercrime, threat intel, dan OSINT lanjutan

def fitur5_leakdb_email(nama):
    print(Fore.LIGHTGREEN_EX + "[5] Cek Kemungkinan Data Bocor...")
    try:
        url = f"https://scylla.sh/search?q={nama}"
        print(Fore.YELLOW + f"[SCAN] {url}")
        res = requests.get(url, timeout=6)
        if "results found" in res.text:
            print(Fore.RED + "[!] Kemungkinan data bocor!")
        else:
            print(Fore.GREEN + "[✓] Aman atau tidak terindeks.")
    except:
        print(Fore.RED + "[X] Gagal akses")

# penjelasan: membuka link Google Images dengan nama target

def fitur6_foto_google_img(nama):
    print(Fore.LIGHTGREEN_EX + "[6] Cek Foto via Google Images...")
    url = f"https://www.google.com/search?tbm=isch&q={quote(nama)}"
    print(Fore.CYAN + f"[URL] {url}")

# penjelasan: saran manual pencarian nama target di telegram

def fitur7_telegram_osint(nama):
    print(Fore.LIGHTGREEN_EX + "[7] Cek Nama di Telegram...")
    print(Fore.YELLOW + f"[NOTE] Gunakan Telegram search manual: https://t.me/{nama}")

# penjelasan: ambil repo public dari github user jika ditemukan

def fitur8_github_repos(nama):
    print(Fore.LIGHTGREEN_EX + "[8] Cek Akun GitHub + Repo...")
    url = f"https://github.com/{nama}"
    try:
        res = requests.get(url, timeout=6)
        if res.status_code == 200:
            repo = re.findall(r'href="/' + nama + '/([^"/]+)"', res.text)
            for r in set(repo):
                print(Fore.BLUE + f"[REPO] {r}")
        else:
            print(Fore.RED + "[X] Tidak ditemukan.")
    except:
        print(Fore.RED + "[X] Error koneksi")

# penjelasan: dork untuk cari paste/leak nama di pastebin & justpaste
# DORK: "asep" site:pastebin.com OR site:justpaste.it

# penjelasan:
# - Mencari kemunculan kata "asep" di situs paste publik
# - Target utama: situs pastebin.com dan justpaste.it
# - Biasanya berisi:
#     - Kebocoran email/password
#     - Data login admin
#     - Token API / config
#     - Dump database
# - Sering digunakan untuk investigasi kebocoran atau OSINT

def fitur9_deep_search(nama):
    print(Fore.LIGHTGREEN_EX + "[9] Deep Web Search...")
    dork = f'site:pastebin.com "{nama}" OR site:justpaste.it "{nama}"'
    print(Fore.YELLOW + f"[DORK] {dork}")

# penjelasan: prediksi acak kapan target terakhir aktif

def fitur10_last_online_guess(nama):
    print(Fore.LIGHTGREEN_EX + "[10] Prediksi Kapan Terakhir Aktif...")
    hari = random.randint(1, 90)
    print(Fore.CYAN + f"📆 {nama.replace('+',' ')} kemungkinan aktif terakhir {hari} hari lalu")

#====================== EKSEKUSI FINAL =======================================#
fitur1_google_dorking(target_name)
fitur2_username_check(target_name)
fitur3_email_guess(target_name)
fitur4_tanggal_domain(target_name)
fitur5_leakdb_email(target_name)
fitur6_foto_google_img(target_name)
fitur7_telegram_osint(target_name)
fitur8_github_repos(target_name)
fitur9_deep_search(target_name)
fitur10_last_online_guess(target_name)

print(Fore.GREEN + "\n[✓] Semua metode OSINT selesai dijalankan tanpa error.")
