# Sols RNG bot macro

A macro for **Sol's RNG Bot** ([@solsrngsimbot](https://t.me/solsrngsimbot) on Telegram) - a bot that recreates the *Sol's RNG* from ROBLOX but on Telegram.

Sol's rng bot macro is a macro for it!

## Functional
| Command | Description |
|---------|-------------|
| `.help` | List all available commands |
| `.about` | Show info about Sol's RNG Bot Macro |
| `.roll` | Toggle the macro on/off |

## Credits
| Role | Credit |
|------|--------|
| **Sol's RNG** (original game) | Sol's Studio |
| **Sol's RNG Bot** | Dimdum111 & Underrosta |
| **Sol's RNG Bot Macro** | Dimdum111 |

## Instructions
1. Download the repository.
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file in the same folder as `main.py`.  
4.Get your `api_id` and `api_hash` from http://my.telegram.org/ and add them to `.env`:  
```example:
api_id=Yourapi_idHere
api_hash="Yourapi_hashHere"
```
5. Run main.py. 
6. Authorize with your Telegram account (you'll be asked for a code, and a password if 2FA is enabled).  
7. type .help for available commands list!

## NOTE
Avoid setting `rollcd` below ~1.75 seconds — going lower increases the risk of 
Telegram flagging/limiting your account. This project is provided as-is (see 
[LICENSE](./LICENSE)); use it at your own risk.

## Licence
MIT License. (See: [LICENSE](./LICENSE))
