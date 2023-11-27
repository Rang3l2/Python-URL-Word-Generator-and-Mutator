import click
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

#This confirms the website is up
def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'HTTP status code = {rep.status_code}, but was expecting hoping for 200. exiting...')
        exit(1)
    return resp.content.decode()


#Grabs urls
def get_links(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    link_list = [link.get('href') for link in links]
    full_links = [urljoin(url, link) for link in link_list]
    #print (full_links)


#captures words, lowered, unquied and set length
def get_all_words_from_url(url, length):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    grepped = re.findall(r'\w+', raw_text)
    lowered = [GW.lower() for GW in grepped ]
    unquied = []
    for words in lowered:
        if words not in unquied:
            unquied.append(words)
        else:
            continue
    gotten_text = []
    for word in unquied:
        if len(word) <= length:
            continue
        else:
            gotten_text.append(word)
    return gotten_text

 #removes common words and write to wordlist
def Compare_Words_common(gotten_text, common_words):
    with open(common_words, 'r') as common_words_file:
        content1 = common_words_file.read()
    compared_words_file = [word for word in gotten_text if word not in content1]
    with open("word_list.txt", 'w') as WL:
        for word in compared_words_file:
            WL.write(str(word) + '\n')


# mutates the wordlist with leet speak, caps first letter
def Mutate_Wordlist(mutation):
    if mutation:
        leets = {'o': '0', 'i': '1', 'e': '3'}
        if os.path.exists("mutated_word_list.txt"):
            os.remove("mutated_word_list.txt")
        WL = open("word_list.txt", 'r')
        for word in WL:
            elite = (''.join(leets.get(char, char) for char in word))
            word =word.strip()
            with open("mutated_word_list.txt", 'a') as elited:
                elited.write(str(word).capitalize()+'\n')
                elited.write(word.strip() + '\n')
                elited.write(word[::-1] + '\n')
                elited.write(word.upper() + '\n')
                elited.write(elite)
                elited.write(word + "0" +'\n')
                elited.write(word + "1" +'\n')
                elited.write(word + "2" +'\n')
                elited.write(word + "3" +'\n')
                elited.write(word + "4" +'\n')
                elited.write(word + "5" +'\n')
                elited.write(word + "6" +'\n')
                elited.write(word + "7" +'\n')
                elited.write(word + "8" +'\n')
                elited.write(word + "9" +'\n')
                elited.write(word + "00" +'\n')
                elited.write(word + "01" +'\n')
                elited.write(word + "02" +'\n')
                elited.write(word + "11" +'\n')
                elited.write(word + "12" +'\n')
                elited.write(word + "13" +'\n')
                elited.write(word + "21" +'\n')
                elited.write(word + "22" +'\n')
                elited.write(word + "23" +'\n')
                elited.write(word + "69" +'\n')
                elited.write(word + "77" +'\n')
                elited.write(word + "88" +'\n')
                elited.write(word + "99" +'\n')
                elited.write(word + "123" + '\n')
                elited.write(word + "e" +'\n')
                elited.write(word + "s" +'\n')
                elited.write(word(-1))
    else:
        quit(1)

@click.command()
@click.option('--url', '-u',prompt='Enter Url', help='Enter the url of the target.')
@click.option('--common_words', '-w', default='./common_words.txt',prompt='File with common words', help='Point to file with words to remove from cewled words.')
@click.option('--length', '-l', default=0, prompt='Specify the word minimum word length.', help='Specify the word minimum word length.')
#change default to false
@click.option('--mutation', '-m', is_flag=False, default=True, prompt='Would you like to mutate the generated wordlist?', help='To mutate the wordlist.')

def main(url, common_words, length, mutation):
    get_html_of(url)
    get_links(url)
    retrieved_words = get_all_words_from_url(url, length)
    Compare_Words_common(retrieved_words, common_words)
    Mutate_Wordlist(mutation)

if __name__ == '__main__':
    main()


'''
def Mutate_Wordlist():
    leets = {'o': '0', 'i': '1', 'e': '3'}
    if os.path.exists("mutated_word_list.txt"):
        os.remove("mutated_word_list.txt")
    WL = open("word_list.txt", 'r')
    for word in WL:
        elite = (''.join(leets.get(char, char) for char in word))
        with open("mutated_word_list.txt", 'a') as elited:
            elited.write(str(word))
            elited.write(str(elite))


                    for word in WL:
            elite = (''.join(leets.get(char, char) for char in word))
            with open("mutated_word_list.txt", 'a') as elited:
                word = word.strip()
                elited.write(str(word).capitalize())
                elited.write(word.strip())
                elited.write(word[::-1]+'\n')
                elited.write(word + "1")
                elited.write(elite)

                
'''
