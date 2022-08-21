<p align="center">
  <img src="./assets/banner.png"  alt="logo" height="100">
</p>

<h3 align="center">Cuthes</h3>

<p align="center">
Now you can shorten the link you want simply and with all kinds<br>
shortened sites

## Getting Started
You have to follow the steps in order for everything to be fine
### Requirements
All you have to do is install the libraries in a file <code>requirements.txt</code>

### Installation
Now you need to install these commands
```console
# Of course it is important to install Git
$ sudo apt install git

# Now you need install Python3
$ sudo apt install python3
```
Then that we run cuthes
```console
# Now lets go to the track
$ cd cuthes

# And then we run it
$ python3 cuthes.py -a <URL>
```
## Usage
```console
$ python3 cuthes.py -h

usage: cuthes.py [-h] [--save SAVE] [--version] [--tor] [--proxy PROXY] [--browser BROWSER] [--colorless] LINK [LINK ...]

positional arguments:
  LINK                  This is the link you want to shorten.

optional arguments:
  -h, --help            show this help message and exit
  --save SAVE, -s SAVE  If you use this command, you can save the results according to the file type.
  --version, -v         It's me showing the version of the project or script.
  --tor, -t             Connecting with Tor to make requests from Tor.
  --proxy PROXY, -p PROXY
                        Make requests through proxy link. socks5://127.0.0.1:1080
  --browser BROWSER, -b BROWSER
                        It changes the browser for requests. You can choose several browsers. (chrome or firefox or another)
  --colorless           Disables colors terminal output.

```
## Errors
Sometimes some sites within this project may sometimes not work, not all of them, but one site. If you have this problem, try again and if it does not work for you,<br/> perhaps the site has been closed or changed the data on it, so be careful,<br/> We hope to avoid these mistakes and try it without any problems problems
## Benefit
The project has a great benefit, such as shortening large and long links, as well as decoding or cutting links. This project was created so that the user does not get confused in choosing the appropriate sites,<br/>We are not responsible for your misuse of it
## License
The source code for the site is licensed under the MIT license<br/>
Find a file called 'LICENSE'<br/>
Developr - [Emnm](https://github.com/Enmn)
