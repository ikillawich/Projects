import bs4 as bs
import urllib.request
import pandas as pd


word1 = "Hola,"
word2 = "Bud."
word3 = "Bud!"
x = 1
ep = 13
length = []

total = 0

url = "http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=bordertown-2016&episode=s01e04"
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
script = soup.find_all("div", {"class":"scrolling-script-container"})[0].text.split()

while x <= ep:
    if x < 10:
        url =   f"http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=bordertown-2016&episode=s01e0{x}"
    else:
        url =   f"http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=bordertown-2016&episode=s01e{x}"
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')

    script = soup.find_all("div", {"class":"scrolling-script-container"})[0].text.split()
    length.append(len(script))
    l = len(script)
    n = 0
    #print(f"episode {x} has {l} words")
    for word in script:
        minutes = int((n/131 - (n/131)%1))
        seconds = int((n/131 % 1) * 60)

        if script[n] == word1 and script[n+1] == word2:
            print("There is an Hola Bud at the " + str(n) + "th word of episode number " + str(x) + ". This is roughly " + str(minutes) + " minutes and " + str(seconds) + " seconds into the episode.")
            n += 1
        elif script[n] == word1 and script[n+1] == word3:
            print("There is an Hola Bud at the " + str(n) + "th word of episode number " + str(x) + ". This is roughly " + str(minutes) + " minutes and " + str(seconds) + " seconds into the episode.")
            n += 1
        else:
            n += 1

    x += 1

# for x in length:
#     total += x
# avg_wpm = total/ep/23
# print(script[691:730])
# print(script[1185:1210])
# print(script[1622:1666])
# print(script[2550:2580])
#print("The average number of words per episode is " + str(total/ep) + "and the average words per minute is " + str(avg_wpm))
