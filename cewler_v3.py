import click
import requests
import re
from bs4 import BeautifulSoup

#This confirms the website is up
def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'HTTP status code = {rep.status_code}, but was expecting hoping for 200. exiting...')
        exit(1)

    return resp.content.decode()


#grabs urls
def get_links(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

#captures words
def get_all_words_from_url(url, length):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    grepped = re.findall(r'\w+', raw_text)
    gotten_text = []
    for word in grepped:
        if len(word) <= length:
            continue
        else:
            gotten_text.append(word)
    return gotten_text

 #removes common words
def Compare_Words_common(gotten_text, common_words):
    with open(common_words, 'r') as common_words_file:
        content1 = common_words_file.read()
    compared_words_file = [word for word in gotten_text if word not in content1]
    f = open("word_list.txt", "w") 
    f.write(f'{compared_words_file}')
    f.close()



@click.command()
@click.option('--url', '-u',prompt='Enter Url', help='Enter the url of the target.')
@click.option('--common_words', '-w', default='./common_words.txt',prompt='File with common words', help='Point to file with words to remove from cewled words.')
@click.option('--length', '-l', default=0, prompt='Specify the word minimum word length', help='Specify the word minimum word length.')

def main(url, common_words, length):
    get_html_of(url)
    get_links(url)
    retrieved_words = get_all_words_from_url(url, length)
    Compare_Words_common(retrieved_words, common_words)
if __name__ == '__main__':
    main()