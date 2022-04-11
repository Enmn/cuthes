import json
import os
import itertools
import time
import threading
import argparse
from sys import platform
try:
    from bs4 import BeautifulSoup
    from yachalk import chalk
    import requests
    import requests_futures
    import lxml
except ModuleNotFoundError:
    os.system('pip3 install bs4')
    os.system('pip3 install yachalk')
    os.system('pip3 install requests')
    os.system('pip3 install requests-futures')
    os.system('pip3 install lxml')
from resources.sites import Shorten
from notify import update

# Colors Code
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[1;32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
reset = '\033[0;0m'



def close():
    os.system('cls' if os.name == 'nt' else 'clear')



# First of all, check for updates
update()



# Get the project version by reading a file .version
with open('.version', 'r') as file:
        version = 'Cuthes ' + f'Version ({file.read()})'
        


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cut", dest="cut", help="to cut the link")
    parser.add_argument("-o", "--output", dest="output", help="If you want to save links to a file .txt")
    parser.add_argument('-v', '--version', action='version', version=version, help="It's me showing the version of the project or script")
    options = parser.parse_args()
    return options



done = False
def loader():
    print("\033[s", end="")
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if done:
            break
        print("\033[u", end="")
        print(f"{chalk.green.bold('[') + chalk.reset(c) + chalk.green.bold(']')} {chalk.green.bold('Checking The Link...')}")
        time.sleep(0.1)



args = get_arguments()
if args.cut:
    close()
    allsite = []
    url = args.cut
    shorten = Shorten(url)
    t = threading.Thread(target=loader)
    t.start()
    allsite.append(shorten.adfly())
    allsite.append(shorten.binbuck())
    allsite.append(shorten.bitly())
    allsite.append(shorten.chilp())
    allsite.append(shorten.clck())
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
    close()
    for loop in allsite:
        JSON = json.loads(loop)
        name = JSON['name']
        url = JSON['url']
        print(f'[{chalk.green.bold("*")}] ' + chalk.green.bold(name + ': ') + chalk.reset(url))
    if args.output:
        if not os.path.exists('output'):
            os.mkdir('output')
            with open('./output/' + args.output, 'w') as file:
                for loo in allsite:
                    JSON = json.loads(loo)
                    name = JSON['name']
                    url = JSON['url']
                    file.write(str(name).lower() + ': ' + url + '\n')