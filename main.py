import requests
from bs4 import BeautifulSoup

userDrama = ['alice', 'running man', 'flower of evil', 'how do you play']
userAnime = ['jujutsu kaisen', 'maou gakuin', 'major 2nd', 'enen no', 'souma', 'appare', 'ahiru no sora', 'black clover']
kdramaURL = "https://k-vid.co"
animeURL = "https://www6.animeseries.io/"

def main():
    print("0 : KDrama URL")
    print("1 : Anime URL")

    url = ""
    selectionURL = input("Please select which url to scrape? \n")
    if selectionURL == 0:
        url = kdramaURL
    elif selectionURL == 1:
        url = animeURL
    else:
        print("Not Found")
        return        

    page = requests.get(url)
    listDrama = []
    linkVideo = ''

    if page.status_code == 200 :
        soup = BeautifulSoup(page.content, 'html.parser')
        listVideo = soup.find_all(class_='video-block')
        
        if selectionURL == 1:
            listVideo = soup.find(class_='items').find_all('li')
            userDrama = userAnime

        for video in listVideo:
            title = video.find(class_='name').get_text().strip().lower().encode('utf-8')
            linkVideo = video.find('a',href=True)
            for favDrama in userDrama:
                if favDrama in title:
                    listDrama.append(title)
                    print(title)
                    print(url+linkVideo['href'])
        if not listDrama:
            print("Not Found")
            return
    else:
        print("Please check connection!!")

if __name__ == '__main__':
    main()