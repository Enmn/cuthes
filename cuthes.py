#!/usr/bin/env python3

import json
import os
import itertools
import time
import csv
import threading
import argparse
try:
    from bs4 import BeautifulSoup
    import requests
    import requests_futures
    import lxml
except ModuleNotFoundError:
    os.system('pip3 install bs4')
    os.system('pip3 install requests')
    os.system('pip3 install requests-futures')
    os.system('pip3 install lxml')
from resources.sites import Shorten, request
from notify import update

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



# First of all, check for updates
update()



# Get the project version by reading a file .version
def get_version():
    with open('.version', 'r') as file:
        version = 'cuthes: ' + file.read()
        return version
        


def get_arguments():
    """
    Parses the main command-line arguments
    using argparse
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="url", nargs="+", metavar="LINK", action="store", help="This is the link you want to shorten.")
    parser.add_argument("--save", "-s", dest="save", help="If you use this command, you can save the results according to the file type.")
    parser.add_argument('--version', '-v', action='version', version=get_version(), help="It's me showing the version of the project or script.")
    parser.add_argument('--tor', '-t', dest='tor', action='store_true', help='Connecting with Tor to make requests from Tor.')
    parser.add_argument('--proxy', '-p', dest='proxy', action="store", default=None, help='Make requests through proxy link. socks5://127.0.0.1:1080')
    parser.add_argument('--browser', '-b', dest="browser", action="store", default=None, help='It changes the browser for requests. You can choose several browsers. (chrome or firefox or another)')
    parser.add_argument('--colorless', dest='no_color', action='store_true', help='Disables colors terminal output.')
    options = parser.parse_args()
    return options



def loader():
    global Done
    Done = False
    print("\033[s", end="")
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if Done:
            break
        print("\033[u", end="")
        print(f"{darkgreen + '[' + reset + c + darkgreen + ']'} {darkgreen + 'Checking The URL...' + reset}")
        time.sleep(0.1)



def color(args):
    global red
    global darkred
    global underline
    global green
    global darkgreen
    global reset
    global white
    global darkwhite
    if args.no_color:
        # Disable color output.
        red = "\033[0;0m"
        darkred = "\033[0;0m"
        underline = "\033[0;0m"
        green = "\033[0;0m"
        darkgreen = "\033[0;0m"
        reset = "\033[0;0m"
        white = "\033[0;0m"
        darkwhite = "\033[0;0m"
    else:
        # Enable color output.
        red = "\033[0;31m"
        darkred = "\033[1;31m"
        underline = "\033[4m"
        green = "\033[0;32m"
        darkgreen = "\033[1;32m"
        reset = "\033[0;0m"
        white = "\033[0;37m"
        darkwhite = "\033[1;37m"



def sites(args=None):
    # Here is 
    if args.url:
        global allsite
        global Done
        allsite = []
        url = args.url
        shorten = Shorten(url)
        time.sleep(1)
        t = threading.Thread(target=loader)
        t.start()
        allsite.append(shorten.adfly())
        allsite.append(shorten.binbuck())
        allsite.append(shorten.bitly())
        allsite.append(shorten.chilp())
        allsite.append(shorten.cleanuri())
        allsite.append(shorten.cpmlink())
        allsite.append(shorten.cuttus())
        allsite.append(shorten.cuttly())
        allsite.append(shorten.gcc())
        allsite.append(shorten.gg())
        allsite.append(shorten.intip())
        allsite.append(shorten.isgd())
        allsite.append(shorten.linkfox())
        allsite.append(shorten.linkmngr())
        allsite.append(shorten.linkshortner())
        allsite.append(shorten.n9())
        allsite.append(shorten.osdb())
        allsite.append(shorten.ouoio())
        allsite.append(shorten.shortam())
        allsite.append(shorten.shortest())
        allsite.append(shorten.shortmy())
        allsite.append(shorten.shorturl())
        allsite.append(shorten.snip())
        allsite.append(shorten.tinyurl())
        allsite.append(shorten.trimurl())
        allsite.append(shorten.u())
        allsite.append(shorten.urlz())
        allsite.append(shorten.vgd())
        allsite.append(shorten.vht())
        allsite.append(shorten.vu())
        allsite.append(shorten.youtube())
        allsite.append(shorten.zzb())
        Done = True
        for sites in allsite:
            parser = json.loads(sites)
            name = parser['name']
            url = parser['url']
            status = parser['status']
            if status == 'true':
               print(f'[{darkgreen + "+" + reset}] ' + darkgreen + name + ': ' + reset + url)
            if status == 'false':
               print(f'[{darkred + "-" + reset}] ' + darkgreen + name + ': ' + reset + url)



def contextTypes(file, status, site, url, path):
    # In this function, he selects the file type in order to save it correctly without problems
    filename = os.path.basename(file)
    dot = str(filename).split('.')[1]
    if dot == "csv":
        writer = csv.writer(path)
        if status == 'true':
            writer.writerow([site, url]) 
        if status == 'false':
            pass
    else:
        if status == 'true':
            path.write(url + '\n')
        if status == 'false':
            path.write('')
        


def output(args):
    # Here if the user wants to save to a file 
    if args.save:
        os.makedirs(os.path.dirname(args.save), exist_ok=True)
        with open(args.save, "w", newline='', encoding="utf-8") as file:
            for sites in allsite:
                parser = json.loads(sites)
                site = parser['name']
                status = parser['status']
                url = parser['url']
                contextTypes(args.save, status, site, url, file)



def result(args):
    request(args)
    color(args)
    sites(args)
    output(args)
    


def run():
    # Here is Running 
    args = get_arguments()
    args = result(args)
    if args is None:
        return



if __name__ == '__main__':
    run()
