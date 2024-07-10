class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    CBLUE = '\33[36m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'    
    CREDBG = '\33[41m'

import os
import subprocess
import sys

try:
    __import__('requests')
except ImportError:
    print(f"{bcolors.CREDBG}requests not found.{bcolors.ENDC}  {bcolors.OKCYAN} Installing...{bcolors.ENDC} ", end='')
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    print(f"{bcolors.CREDBG}requests installed successfully.{bcolors.ENDC}")
finally:
    import requests

try:
    __import__('bs4')
except ImportError:
    print(f"{bcolors.CREDBG}BeautifulSoup not found.{bcolors.ENDC} {bcolors.OKCYAN} Installing...{bcolors.ENDC} ", end='')
    subprocess.check_call([sys.executable, "-m", "pip",
                          "install", 'beautifulsoup4'])
    print(f"{bcolors.CREDBG}BeautifulSoup installed successfully.{bcolors.ENDC}")
finally:
    from bs4 import BeautifulSoup


try:
    __import__('bs4')
except ImportError:
    print(f"{bcolors.CREDBG}tqdm not found.{bcolors.ENDC} {bcolors.OKCYAN} Installing...{bcolors.ENDC} ", end='')
    subprocess.check_call([sys.executable, "-m", "pip",
                          "install", 'tqdm'])
    print(f"{bcolors.CREDBG}tqdm installed successfully.{bcolors.ENDC}")
finally:
    from tqdm import tqdm
from urllib.parse import urljoin
import argparse


# saved file at MUSIC/DEV/ 
def download_Songs_from(url, base_folder = './../Telugu Songs/'):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{bcolors.WARNING}Failed to retrieve webpage: {response.status_code}{bcolors.ENDC}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    h2_tag = soup.find('h2')
    if not h2_tag:
        print(f"{bcolors.FAIL}No Title found, saving everything into Songs Folder{bcolors.ENDC}")
        folder_name = base_folder + 'Songs'
    else:
        folder_name = h2_tag.get_text(strip=True)
        movie_name = folder_name.split('Audio')[0].strip().replace('Movie', '').replace('Free', '').replace(
            'Songs Download', '').replace('Download', '').replace('Mp3', '').replace(
            'songs', '').replace('download', '').replace('mp3', '').replace('movie', '').replace('free', '').replace(
            '  ', ' ').replace('  ', ' ').replace('-.', '.').replace('- .', '.').replace(' .', '.').replace('  ', ' ').replace('  ', ' ').replace(' - ', ' ').replace('  ', ' ').replace(' .', '.').strip()
        print(f'{bcolors.HEADER}\n> Downloading {bcolors.ENDC}{bcolors.WARNING}{bcolors.BOLD}{movie_name}{bcolors.ENDC}{bcolors.HEADER} Movie Songs :{bcolors.ENDC}')

        folder_name = base_folder + movie_name.strip()

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    audio_links = soup.find_all('a', href=True)
    audio_sources = [link['href']
                     for link in audio_links if link['href'].endswith('.mp3')]

    download_links = []
    
    for i,audio_url in enumerate(audio_sources):
        song_url = urljoin(url, audio_url)

        song_name = os.path.basename(song_url).replace('%20', ' ').replace('SenSongsMp3.Co', '').replace(
            'SenSongsMp3', '').replace('NaaSongsMp3', '').replace('SenSongs', '').replace('NaaSongs', '').replace('.-', '').replace(
                '-.', '.').replace('.com', '').replace('.Com', '').replace('.COM', '').replace('.Co', '').replace('.co', '').replace(
                    '  ', ' ').replace('  ', ' ').replace('-.', '.').replace('- .', '.').replace(' .', '.').replace('  ', ' ').replace('  ', ' ').replace(' - ', ' ').replace('  ', ' ').replace(' .', '.').strip().replace(
                        '.Co', '').replace('.co', '').strip()

        song_path = folder_name.strip() + '/' + song_name.strip()
        
        download_links.append((song_url,song_path, song_name))
        
        print( f'{bcolors.OKCYAN}\t{i}{bcolors.ENDC}: {bcolors.CBLUE}{song_name}{bcolors.ENDC}')
    
    print()
    failed_Songs = {}
    
    for song_url, song_path, song_name in tqdm(download_links, desc="Downloading", colour="blue", ascii=False, unit="Song"):
        with requests.get(song_url, stream=True) as r:
            if r.status_code == 200:
                with open(song_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                failed_Songs[(song_url, song_path, song_name)] = r.status_code
    if failed_Songs:
        print(f'{bcolors.FAIL}\nDownload Failed Songs list{bcolors.ENDC}')
        for (song_url, song_path, song_name),Status_Code in failed_Songs.items():
            print(f'{song_name=}\n{song_path=}\n{song_url=}\n{Status_Code=}\n\n')
    else:
        print(f'{bcolors.OKGREEN}\nDownloaded All {len(download_links)} songs to {folder_name}{bcolors.ENDC}')
        
def main_mine():
    parser = argparse.ArgumentParser(description="Download audio files from  : naasongs.com.co")
    parser.add_argument('url', type=str, nargs='?', help='The URL of the webpage to download audio files from')

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        return
    
    download_Songs_from(args.url)


def main_cli():
    parser = argparse.ArgumentParser(
        description="""Download audio files from a 'naasongs.com.co' webpage only (version 1.0).
        Note: if the Audio is Available in 2 quality versions, it might download both or override one other which ever is last (HQ generally)""")
    parser.add_argument('url', type=str, nargs='?',
                        help='The URL of the webpage to download audio files from')
    parser.add_argument('-d', '--directory', type=str, default='./',
                        help='The base folder to save the downloaded audio files (default: current directory)')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        return

    download_Songs_from(args.url, args.directory)


if __name__ == '__main__':
    # main_mine()
    main_cli()
