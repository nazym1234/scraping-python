import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'

try:
    # Étape 1 : Télécharger la page
    response = requests.get(url)
    response.raise_for_status()
    print("Page téléchargée avec succès!")

    # Étape 2 : Parser le contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Étape 3 : Trouver les balises <a> avec 'data-testid="internal-link"'
    links = soup.find_all('a', {'data-testid': 'internal-link', 'href': True})

    # Étape 4 : Stocker et construire les liens complets
    article_links = []
    for link in links:
        href = link['href']
        # Vérifier si le lien est relatif (commence par '/')
        if href.startswith('/'):
            full_url = f"https://www.bbc.com{href}"
            article_links.append(full_url)
   
    # Étape 5 : Afficher les liens extraits
    if article_links:
        print(f"{len(article_links)} liens trouvés :")
        for article in article_links:
            print(article)
    else:
        print("Aucun lien trouvé. Vérifie la structure HTML ou la logique du script.")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")
