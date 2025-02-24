#pour envoyer des requêtes HTTP et récupérer le contenu d'une page web:
import requests
#extraire des informations spécifiques dans une page web:
from bs4 import BeautifulSoup
#declarer le lien qu'on veut utiliser :
url = 'https://www.bbc.com/news'

try:
    # Envoie une requête HTTP GET pour télécharger le contenu de la page:
    response = requests.get(url)
    #Vérifie si la requête a réussi (code 200). 
    # Si la page renvoie une erreur (comme 404 ou 500),
    #  une exception est levée, et ton programme s'arrête ici:
    response.raise_for_status()  
    print("Page téléchargée avec succès!")
    
    # reponse.content : contient le code complet de la page html
    #BeautifulSoup(...... , 'html.parser'){
    # Transforme ce code HTML en un objet manipulable (comme un arbre d'éléments HTML).
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # soup.find_all() : Permet de rechercher tous les éléments HTML correspondant à un critère.
    # 'h2' : Recherche les balises <h2> (utilisées pour les titres dans cette page).
    # {'data-testid': 'card-headline'} : Ajoute un filtre pour trouver uniquement 
    # les <h2> avec l'attribut data-testid="card-headline"
    titles = soup.find_all('h2', {'data-testid': 'card-headline'})
    
    if titles:
        print(f"{len(titles)} titres trouvés :")
        for title in titles:
            #title.get_text(strip=True) : Extrait uniquement le texte contenu dans la balise
            #  <h2> (par exemple, le titre de l'actualité), et enlève les espaces inutiles.
            print(title.get_text(strip=True))
    else:
        print("Aucun titre trouvé. Vérifie la structure HTML ou la logique du script.")


except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")



