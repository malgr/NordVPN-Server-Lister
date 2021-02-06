# NordVPN-Server-Lister
List NordVPN servers from https://api.nordvpn.com/server that meet the criteria. For use with software that accepts HTTP/HTTPS or SOCKS5 proxy like Firefox or Chrome with SwitchyOmega extension.

## Usage Example
    python main.py US -ps -l 5

results in

    [('us5802.nordvpn.com', 4),  ('us5842.nordvpn.com', 5), ('us6699.nordvpn.com', 5) ...]


## Arguments
### required
    loc
server country code as used by NordVPN (e.g AU, NL, SG, US, UK)
    

## optional
    -l or --load
server load, any value from 1 - 100 (defaults to 20)

Default is HTTP Proxy

    -ps or --pssl
list servers with SSL proxy. Note that NordVPN user port 89

    -s or --socks
list servers with SOCK5.