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

#writes words to file
def get_all_words_from_url(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    gotten_text = re.findall(r'\w+', raw_text)
    f = open("./word_list.txt", "w") 
    f.write(f'{gotten_texst}')
    f.close()



@click.command()
@click.option('--url', '-u', prompt='Enter Url', help='Enter the url of the target.')

def main(url):
    target =  get_html_of(url)
    get_text = get_all_words_from_url(url)
if __name__ == '__main__':
    main()