import requests
from bs4 import BeautifulSoup

def scraping():
    url = 'https://www.wenxuecity.com/news/2025/06/22/126216987.html'  # Exemplo
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Pegar o título (H1)
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else 'Sem título'

    # Pegar o conteúdo do artigo
    article_tag = soup.find('article', id='articleContent')
    content = article_tag.get_text(separator='\n', strip=True) if article_tag else 'Sem conteúdo'
    return content
#print("Título:", title)
#print("\nConteúdo:\n", content)
