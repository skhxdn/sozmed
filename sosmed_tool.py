#!/usr/bin/env python3
"""
SOSMED TOOL - Multi-feature Social Media Toolkit
Untuk keperluan pribadi & belajar
"""

import os
import sys
import json
import random
import time
import subprocess
from datetime import datetime

# ─── COLORS ───────────────────────────────────────────
class C:
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE   = '\033[97m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    RESET   = '\033[0m'

def banner():
    os.system('clear')
    print(f"""
{C.MAGENTA}{C.BOLD}
  ░██████╗░█████╗░░██████╗███╗░░░███╗███████╗██████╗░
  ██╔════╝██╔══██╗██╔════╝████╗░████║██╔════╝██╔══██╗
  ╚█████╗░██║░░██║╚█████╗░██╔████╔██║█████╗░░██║░░██║
  ░╚═══██╗██║░░██║░╚═══██╗██║╚██╔╝██║██╔══╝░░██║░░██║
  ██████╔╝╚█████╔╝██████╔╝██║░╚═╝░██║███████╗██████╔╝
  ╚═════╝░░╚════╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═════╝░
         ████████╗░█████╗░░█████╗░██╗░░░░░
         ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
         ░░░██║░░░██║░░██║██║░░██║██║░░░░░
         ░░░██║░░░██║░░██║██║░░██║██║░░░░░
         ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
         ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
{C.RESET}
{C.DIM}  Social Media Toolkit for Termux  |  For personal use only{C.RESET}
{C.YELLOW}  ══════════════════════════════════════════════════════{C.RESET}
    """)

def menu():
    print(f"""
{C.WHITE}{C.BOLD}  [ MENU UTAMA ]{C.RESET}

  {C.CYAN}[1]{C.RESET} 📥  Downloader Video/Foto
  {C.CYAN}[2]{C.RESET} 🔍  Cek Username di Berbagai Platform
  {C.CYAN}[3]{C.RESET} ✍️   Generator Caption & Hashtag
  {C.CYAN}[4]{C.RESET} 📋  Content Manager (Jadwal Konten)
  {C.CYAN}[5]{C.RESET} 🧹  Clear Screen
  {C.CYAN}[0]{C.RESET} 🚪  Keluar

{C.YELLOW}  ══════════════════════════════════════════════════════{C.RESET}""")

# ════════════════════════════════════════════════════════
# [1] DOWNLOADER
# ════════════════════════════════════════════════════════
def check_ytdlp():
    """Cek apakah yt-dlp terinstall"""
    try:
        subprocess.run(['yt-dlp', '--version'],
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ytdlp():
    print(f"\n  {C.YELLOW}yt-dlp belum terinstall. Install sekarang?{C.RESET}")
    choice = input(f"  {C.WHITE}(y/n): {C.RESET}").lower()
    if choice == 'y':
        print(f"  {C.DIM}Installing yt-dlp...{C.RESET}")
        os.system('pip install yt-dlp --break-system-packages -q')
        print(f"  {C.GREEN}Selesai!{C.RESET}")
        return True
    return False

def downloader():
    print(f"\n{C.CYAN}{C.BOLD}[ 📥 VIDEO/FOTO DOWNLOADER ]{C.RESET}")
    print(f"  {C.DIM}Supported: YouTube, TikTok, Instagram (public), Twitter, dll{C.RESET}\n")

    if not check_ytdlp():
        if not install_ytdlp():
            print(f"  {C.RED}yt-dlp diperlukan untuk fitur ini.{C.RESET}")
            return

    print(f"  {C.DIM}Format pilihan:{C.RESET}")
    print(f"  {C.GREEN}[1]{C.RESET} Video terbaik (default)")
    print(f"  {C.GREEN}[2]{C.RESET} Audio only (MP3)")
    print(f"  {C.GREEN}[3]{C.RESET} Video 720p")
    print(f"  {C.GREEN}[4]{C.RESET} Foto/thumbnail saja")
    fmt_choice = input(f"\n  {C.WHITE}Pilih format [1-4]: {C.RESET}").strip() or '1'

    url = input(f"  {C.WHITE}Masukkan URL: {C.RESET}").strip()
    if not url:
        print(f"  {C.RED}URL tidak boleh kosong!{C.RESET}")
        return

    # Tentukan output folder
    out_dir = os.path.expanduser('~/storage/downloads') if os.path.exists(os.path.expanduser('~/storage')) else os.path.expanduser('~')
    print(f"  {C.DIM}Output: {out_dir}{C.RESET}\n")

    # Build command
    if fmt_choice == '1':
        cmd = f'yt-dlp -o "{out_dir}/%(title)s.%(ext)s" "{url}"'
    elif fmt_choice == '2':
        cmd = f'yt-dlp -x --audio-format mp3 -o "{out_dir}/%(title)s.%(ext)s" "{url}"'
    elif fmt_choice == '3':
        cmd = f'yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" -o "{out_dir}/%(title)s.%(ext)s" "{url}"'
    elif fmt_choice == '4':
        cmd = f'yt-dlp --write-thumbnail --skip-download -o "{out_dir}/%(title)s.%(ext)s" "{url}"'
    else:
        cmd = f'yt-dlp -o "{out_dir}/%(title)s.%(ext)s" "{url}"'

    print(f"  {C.YELLOW}Downloading...{C.RESET}\n")
    os.system(cmd)
    print(f"\n  {C.GREEN}Selesai! File tersimpan di: {out_dir}{C.RESET}")

# ════════════════════════════════════════════════════════
# [2] USERNAME CHECKER
# ════════════════════════════════════════════════════════
def username_checker():
    try:
        import urllib.request
        import urllib.error
    except ImportError:
        pass

    print(f"\n{C.CYAN}{C.BOLD}[ 🔍 USERNAME CHECKER ]{C.RESET}")
    print(f"  {C.DIM}Cek username ada atau tidak di platform publik{C.RESET}\n")

    username = input(f"  {C.WHITE}Masukkan username: {C.RESET}").strip()
    if not username:
        print(f"  {C.RED}Username tidak boleh kosong!{C.RESET}")
        return

    # Platform yang dicek (URL publik saja)
    platforms = {
        "GitHub"      : f"https://github.com/{username}",
        "Twitter/X"   : f"https://twitter.com/{username}",
        "Instagram"   : f"https://www.instagram.com/{username}/",
        "TikTok"      : f"https://www.tiktok.com/@{username}",
        "YouTube"     : f"https://www.youtube.com/@{username}",
        "Reddit"      : f"https://www.reddit.com/user/{username}",
        "Pinterest"   : f"https://www.pinterest.com/{username}/",
        "Twitch"      : f"https://www.twitch.tv/{username}",
        "SoundCloud"  : f"https://soundcloud.com/{username}",
        "Linktree"    : f"https://linktr.ee/{username}",
    }

    import urllib.request
    import urllib.error

    print(f"\n  {C.WHITE}Mengecek username {C.YELLOW}@{username}{C.WHITE} di {len(platforms)} platform...{C.RESET}\n")

    found = []
    not_found = []

    for platform, url in platforms.items():
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'
            })
            response = urllib.request.urlopen(req, timeout=5)
            code = response.getcode()
            if code == 200:
                print(f"  {C.GREEN}[✓] FOUND   {C.RESET}{C.WHITE}{platform:<14}{C.RESET} {C.DIM}{url}{C.RESET}")
                found.append(platform)
            else:
                print(f"  {C.RED}[✗] NOT FOUND{C.RESET} {C.DIM}{platform}{C.RESET}")
                not_found.append(platform)
        except urllib.error.HTTPError as e:
            if e.code in [404, 403]:
                print(f"  {C.RED}[✗] NOT FOUND{C.RESET} {C.DIM}{platform:<14} ({e.code}){C.RESET}")
                not_found.append(platform)
            else:
                print(f"  {C.YELLOW}[?] UNKNOWN {C.RESET} {C.DIM}{platform:<14} ({e.code}){C.RESET}")
        except Exception:
            print(f"  {C.YELLOW}[?] TIMEOUT {C.RESET} {C.DIM}{platform}{C.RESET}")

        time.sleep(0.3)  # biar ga keliatan spam

    print(f"\n  {C.YELLOW}══════════════════════════════════{C.RESET}")
    print(f"  {C.GREEN}Ditemukan : {len(found)} platform{C.RESET}")
    print(f"  {C.RED}Tidak ada  : {len(not_found)} platform{C.RESET}")

# ════════════════════════════════════════════════════════
# [3] CAPTION & HASHTAG GENERATOR
# ════════════════════════════════════════════════════════
def caption_generator():
    print(f"\n{C.CYAN}{C.BOLD}[ ✍️  CAPTION & HASHTAG GENERATOR ]{C.RESET}\n")

    # Template caption per niche
    templates = {
        "1": {
            "nama": "Lifestyle",
            "captions": [
                "Hidup itu tentang menikmati setiap momen kecil yang ada 🌿\nKarena bahagia itu sederhana.",
                "Pagi yang tenang, kopi yang hangat, dan mindset yang positif ☕\nItulah resep hari yang sempurna.",
                "Bukan tentang seberapa jauh kamu pergi,\ntapi seberapa dalam kamu menikmati perjalanannya 🌅",
                "Slow living bukan berarti malas,\ntapi sadar bahwa tidak semua hal perlu terburu-buru 🍃",
            ]
        },
        "2": {
            "nama": "Motivasi",
            "captions": [
                "Mulai dari mana pun tidak masalah,\nyang penting mulai. Jangan tunggu sempurna! 🚀",
                "Setiap hari adalah kesempatan baru untuk menjadi lebih baik dari kemarin 💪",
                "Gagal itu bukan akhir segalanya.\nItu hanya tanda bahwa kamu sedang belajar 🔥",
                "Percaya prosesnya. Percaya dirimu.\nHasil tidak akan mengkhianati usaha 🌟",
            ]
        },
        "3": {
            "nama": "Travel",
            "captions": [
                "Dunia terlalu luas untuk diam di satu tempat saja 🌍\nYuk jelajahi!",
                "Bukan soal destinasinya,\ntapi soal cerita yang kamu bawa pulang ✈️",
                "Traveling taught me that home is wherever I find peace 🏔️",
                "Collect moments, not things.\nKarena kenangan tidak akan muat di koper 🎒",
            ]
        },
        "4": {
            "nama": "Food",
            "captions": [
                "Good food = good mood 🍜\nSederhana tapi nyata.",
                "Makanan terbaik bukan yang paling mahal,\ntapi yang dimakan bareng orang yang tepat 🍽️",
                "Life is short, eat the good stuff first 🤤",
                "Perut kenyang, hati senang.\nFilosofi hidup paling jujur 😄",
            ]
        },
        "5": {
            "nama": "Bisnis/UMKM",
            "captions": [
                "Mimpi besar dimulai dari langkah kecil.\nHari ini kami hadir untuk melayani kamu lebih baik 💼",
                "Kualitas bukan sekadar janji,\ntapi komitmen yang kami pegang setiap hari 🏆",
                "Terima kasih sudah mempercayakan kebutuhan kamu pada kami ❤️\nKepercayaan kamu adalah motivasi terbesar kami.",
                "Promo spesial hari ini hanya untuk kamu!\nJangan sampai kelewatan ya 🎉",
            ]
        },
    }

    # Hashtag bank per niche
    hashtags_bank = {
        "1": ["#lifestyle #lifegoals #dailylife #slowliving #mindfulness #selfcare #blessed #grateful #livingmybestlife #contentcreator"],
        "2": ["#motivasi #motivasiindonesia #semangatpagi #quotes #quotesoftheday #inspirasi #sukses #mindset #growthmindset #nevergiveup"],
        "3": ["#travel #traveling #travelgram #explore #wanderlust #backpacker #holiday #wisata #wisataindonesia #travelphotography"],
        "4": ["#food #foodie #foodphotography #kuliner #kulinerindonesia #makanenak #foodlover #instafood #yummy #foodstagram"],
        "5": ["#bisnis #umkm #umkmindonesia #jualan #onlineshop #produklokal #usaha #entrepreneur #jualanbaju #olshop"],
    }

    print(f"  Pilih niche konten:")
    for key, val in templates.items():
        print(f"  {C.GREEN}[{key}]{C.RESET} {val['nama']}")

    choice = input(f"\n  {C.WHITE}Pilih [1-5]: {C.RESET}").strip()

    if choice not in templates:
        print(f"  {C.RED}Pilihan tidak valid!{C.RESET}")
        return

    niche = templates[choice]
    caption = random.choice(niche['captions'])
    hashtag = hashtags_bank[choice][0]

    # Custom tambahan
    custom = input(f"\n  {C.WHITE}Tambahan info/produk (opsional, Enter untuk skip): {C.RESET}").strip()
    extra = f"\n\n{custom}" if custom else ""

    jumlah = input(f"  {C.WHITE}Generate berapa caption? (default 3): {C.RESET}").strip() or '3'
    try:
        jumlah = min(int(jumlah), len(niche['captions']))
    except:
        jumlah = 3

    print(f"\n  {C.YELLOW}══════════════════════════════════════{C.RESET}")
    print(f"  {C.WHITE}{C.BOLD}HASIL GENERATE - {niche['nama']}{C.RESET}")
    print(f"  {C.YELLOW}══════════════════════════════════════{C.RESET}\n")

    sampled = random.sample(niche['captions'], min(jumlah, len(niche['captions'])))
    for i, cap in enumerate(sampled, 1):
        print(f"  {C.CYAN}── Caption {i} ──────────────────────{C.RESET}")
        print(f"  {cap}{extra}")
        print(f"\n  {C.DIM}{hashtag}{C.RESET}")
        print()

    # Simpan ke file?
    save = input(f"  {C.WHITE}Simpan ke file? (y/n): {C.RESET}").lower()
    if save == 'y':
        filename = f"caption_{niche['nama'].lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for i, cap in enumerate(sampled, 1):
                f.write(f"── Caption {i} ──\n{cap}{extra}\n\n{hashtag}\n\n")
        print(f"  {C.GREEN}Tersimpan: {filename}{C.RESET}")

# ════════════════════════════════════════════════════════
# [4] CONTENT MANAGER
# ════════════════════════════════════════════════════════

CONTENT_FILE = os.path.expanduser('~/.sosmed_content.json')

def load_content():
    if os.path.exists(CONTENT_FILE):
        with open(CONTENT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_content(data):
    with open(CONTENT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def content_manager():
    print(f"\n{C.CYAN}{C.BOLD}[ 📋 CONTENT MANAGER ]{C.RESET}")
    print(f"  {C.DIM}Kelola jadwal & ide konten kamu{C.RESET}\n")

    print(f"  {C.GREEN}[1]{C.RESET} Tambah konten baru")
    print(f"  {C.GREEN}[2]{C.RESET} Lihat semua konten")
    print(f"  {C.GREEN}[3]{C.RESET} Tandai sudah diposting")
    print(f"  {C.GREEN}[4]{C.RESET} Hapus konten")

    choice = input(f"\n  {C.WHITE}Pilih [1-4]: {C.RESET}").strip()

    contents = load_content()

    if choice == '1':
        print(f"\n  {C.WHITE}Platform: {C.RESET}")
        platforms = ["Instagram", "TikTok", "Twitter/X", "YouTube", "Facebook", "Lainnya"]
        for i, p in enumerate(platforms, 1):
            print(f"  {C.GREEN}[{i}]{C.RESET} {p}")
        p_choice = input(f"  Pilih [1-6]: ").strip()
        platform = platforms[int(p_choice)-1] if p_choice.isdigit() and 1 <= int(p_choice) <= 6 else "Lainnya"

        judul = input(f"  {C.WHITE}Judul/Ide konten: {C.RESET}").strip()
        tanggal = input(f"  {C.WHITE}Tanggal posting (misal: 2026-03-01, kosong = hari ini): {C.RESET}").strip()
        if not tanggal:
            tanggal = datetime.now().strftime('%Y-%m-%d')

        catatan = input(f"  {C.WHITE}Catatan tambahan: {C.RESET}").strip()

        item = {
            "id": len(contents) + 1,
            "platform": platform,
            "judul": judul,
            "tanggal": tanggal,
            "catatan": catatan,
            "status": "belum",
            "dibuat": datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        contents.append(item)
        save_content(contents)
        print(f"\n  {C.GREEN}✓ Konten berhasil disimpan!{C.RESET}")

    elif choice == '2':
        if not contents:
            print(f"\n  {C.YELLOW}Belum ada konten tersimpan.{C.RESET}")
            return

        print(f"\n  {C.WHITE}{C.BOLD}DAFTAR KONTEN:{C.RESET}\n")
        for c in contents:
            status_color = C.GREEN if c['status'] == 'posted' else C.YELLOW
            status_icon = "✓" if c['status'] == 'posted' else "○"
            print(f"  {C.DIM}[{c['id']}]{C.RESET} {status_color}{status_icon}{C.RESET} {C.WHITE}{c['judul']}{C.RESET}")
            print(f"       {C.CYAN}{c['platform']}{C.RESET}  |  📅 {c['tanggal']}")
            if c.get('catatan'):
                print(f"       {C.DIM}{c['catatan']}{C.RESET}")
            print()

    elif choice == '3':
        if not contents:
            print(f"\n  {C.YELLOW}Belum ada konten.{C.RESET}")
            return
        id_input = input(f"  {C.WHITE}Masukkan ID konten yang sudah diposting: {C.RESET}").strip()
        for c in contents:
            if str(c['id']) == id_input:
                c['status'] = 'posted'
                c['posted_at'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                save_content(contents)
                print(f"  {C.GREEN}✓ Konten '{c['judul']}' ditandai sudah diposting!{C.RESET}")
                return
        print(f"  {C.RED}ID tidak ditemukan.{C.RESET}")

    elif choice == '4':
        if not contents:
            print(f"\n  {C.YELLOW}Belum ada konten.{C.RESET}")
            return
        id_input = input(f"  {C.WHITE}Masukkan ID konten yang mau dihapus: {C.RESET}").strip()
        before = len(contents)
        contents = [c for c in contents if str(c['id']) != id_input]
        if len(contents) < before:
            save_content(contents)
            print(f"  {C.GREEN}✓ Konten berhasil dihapus.{C.RESET}")
        else:
            print(f"  {C.RED}ID tidak ditemukan.{C.RESET}")

# ════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════
def main():
    banner()
    while True:
        menu()
        choice = input(f"  {C.MAGENTA}Pilih menu{C.RESET} [{C.GREEN}0-5{C.RESET}]: ").strip()

        if choice == '1':
            downloader()
        elif choice == '2':
            username_checker()
        elif choice == '3':
            caption_generator()
        elif choice == '4':
            content_manager()
        elif choice == '5':
            banner()
            continue
        elif choice == '0':
            print(f"\n  {C.CYAN}Bye! 👋{C.RESET}\n")
            sys.exit(0)
        else:
            print(f"\n  {C.RED}Pilihan tidak valid!{C.RESET}")

        input(f"\n  {C.DIM}Tekan Enter untuk kembali ke menu...{C.RESET}")
        banner()

if __name__ == '__main__':
    main()
