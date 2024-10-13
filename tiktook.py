import os, time, requests, random
try:from user_agent import generate_user_agent
except ModuleNotFoundError:
    os.system('pip install user_agent')
    os.system('clear')
    from user_agent import generate_user_agent
from user_agent import generate_user_agent
user_agent = generate_user_agent()
g = '\x1b[1;32m'
r = '\x1b[1;31m'
b = '\x1b[1;34m'
c = '\x1b[1;36m'
w = '\x1b[1;37m'
def wait():
    for i in range(100):
        print(f'\n\n{g}[ + ] Wait 2 Menite For Next Submit : {i>
        time.sleep(1)
        os.system('clear')
class TikDemoVeiw:
    def __init__(self):print("𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔 : ᏔᏫᏫᎠᎬ")
    def boost_video(self, user: str, link: str) -> dict:
        response = requests.post('https://api.likesjet.com/free>
        return response
def main():
    print ('____________________')
    print (w+'𝑺𝑶𝑴𝑬 𝑯𝑨𝑪𝑲𝑬𝑹𝑺 𖠔')
    print ('ᏔᏫᏫᎠᎬ')
    print ('V249V <|> C249c')
    print ('SUDAN')
    print ('____________________')
    user = input(f'{c}[?]TikTok UserName:{w} ')
    print ('____________________')
    link = input(f'{b}[?]Video Link: {w}')
    booster = TikDemoVeiw()
    response = booster.boost_video(user, link)
    if response.get('status'):