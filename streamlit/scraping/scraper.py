import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re

def scraping():
    url = 'https://www.wenxuecity.com/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_links = []

    # Regex para pegar apenas links do tipo /news/YYYY/MM/DD/ID.html
    pattern = re.compile(r'^/news/\d{4}/\d{2}/\d{2}/\d+\.html$')

    for li in soup.find_all('li'):
        a_tag = li.find('a')
        if a_tag and a_tag.get('href'):
            href = a_tag['href']
            if pattern.match(href):
                link_text = a_tag.get_text(strip=True)
                #print(link_text, href)
                news_links.append(f'https://www.wenxuecity.com/{href}')
                #news_links.append((link_text, f'https://www.wenxuecity.com/{href}'))

    # Suponha que `news_links` já esteja definido
    resultados = []  # Lista para armazenar os dados

    for link in news_links:
        url = link  # Exemplo
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Pegar o título (H1)
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else 'Sem título'

        # Pegar o conteúdo do artigo
        article_tag = soup.find('article', id='articleContent')
        content = article_tag.get_text(separator='\n', strip=True) if article_tag else 'Sem conteúdo'

        # Mostrar no terminal com estilo
        #print("\033[1m\033[94m标题 Título:\033[0m", title)
        #print("\nConteúdo:\n", content)

        # Adicionar à lista de resultados
        resultados.append({
            "url": url,
            "title": title,
            "content": content
        })
    return resultados