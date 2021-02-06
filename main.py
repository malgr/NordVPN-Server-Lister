import requests
import argparse

parser = argparse.ArgumentParser(prog='main.py',
                                 usage='%(prog)s loc [options]',
                                 description='''List Nord VPN servers that
                                 meet the user defined criteria''')

parser.add_argument('country',
                    type=str,
                    help='Country code (eg. AU, US, UK)')

parser.add_argument('-l',
                    '--load',
                    default=20,
                    type=int,
                    help='Maximum server load (default: 20)')

parser.add_argument('-ps',
                    '--pssl',
                    action='store_true',
                    help='Search only for servers with proxy-ssl feature')

parser.add_argument('-s',
                    '--socks',
                    action='store_true',
                    help='Search only for servers with socks feature')

args = parser.parse_args()
country_code = args.country
server_load = args.load
ssl_server = args.pssl
socks_server = args.socks

# TODO: Allow multiple options
if ssl_server and socks_server:
    raise Exception("Sorry, only one feature at a time is allowed")

r = requests.get('https://api.nordvpn.com/server')
response = r.json()
server_list = []


def is_valid(option):
    if ((value["flag"] == country_code) and (value["load"] <= server_load) and
            (value["features"][option])):
        server_list.append((value["domain"], value["load"]))


for value in response:
    if ssl_server:
        is_valid("proxy_ssl")
    if socks_server:
        is_valid("socks")
    else:
        is_valid("proxy")

# print the servers and server load for now
print(sorted(server_list, key=lambda tup: tup[1]))
