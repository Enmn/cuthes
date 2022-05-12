#!/usr/bin/env python3

import json
import os
import itertools
import time
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
from resources.sites import Shorten
from notify import update



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



# First of all, check for updates
update()



# Get the project version by reading a file .version
def get_version():
    with open('.version', 'r') as file:
        version = 'Cuthes ' + f'Version ({file.read()})'
        return version
        


def get_arguments():
    """
    Parses the main command-line arguments
    using argparse
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="url", nargs="+", metavar="Link", action="store", help="This is the link you want to shorten.")
    parser.add_argument("--save", "-s", dest="save", help="If you want to save links to a file .txt")
    parser.add_argument('--version', '-v', action='version', version=get_version(), help="It's me showing the version of the project or script")
    parser.add_argument('--colorless', dest='no_color', action='store_true', help='Disable colors')
    options = parser.parse_args()
    return options



done = False
def loader():
    print("\033[s", end="")
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if done:
            break
        print("\033[u", end="")
        print(f"{darkgreen + '[' + reset + c + darkgreen + ']'} {darkgreen + 'Checking The Link...' + reset}")
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



def sites(args):
    if args.url:
        global allsite
        global done
        cls()
        allsite = []
        url = args.url
        shorten = Shorten(url)
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
        allsite.append(shorten.isgd())
        allsite.append(shorten.linkfox())
        allsite.append(shorten.linkmngr())
        allsite.append(shorten.osdb())
        allsite.append(shorten.ouoio())
        allsite.append(shorten.shortam())
        allsite.append(shorten.shortest())
        allsite.append(shorten.shorturl())
        allsite.append(shorten.snip())
        allsite.append(shorten.tinyurl())
        allsite.append(shorten.trimurl())
        allsite.append(shorten.urlz())
        allsite.append(shorten.v())
        allsite.append(shorten.wiki())
        allsite.append(shorten.y2u())
        allsite.append(shorten.zzb())
        done = True
        cls()
        for sites in allsite:
            parser = json.loads(sites)
            name = parser['name']
            url = parser['url']
            print(f'[{darkgreen + "*" + reset}] ' + darkgreen + name + ': ' + reset + url)



def output(args):
    # Here if the user wants to save to a file 
    if args.save:
        if not os.path.exists('output'):
            os.mkdir('output')
        with open('./output/' + args.save, 'w') as file:
            for loo in allsite:
                JSON = json.loads(loo)
                name = JSON['name']
                url = JSON['url']
                file.write(str(name).lower() + ': ' + url + '\n')



def result(args):
    color(args)
    sites(args)
    output(args)



def run():
    args = get_arguments()
    args = result(args)
    if args is None:
        return



if __name__ == '__main__':
    run()
