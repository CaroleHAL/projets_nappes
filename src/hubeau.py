import requests

def recuperer_toutes_les_pages(url, parametres):
    """Récupère toutes les pages d'une requête Hub'Eau.
    Reçoit l'adresse de l'API et le dictionnaire de paramètres.
    Demande les pages une par une, jusqu'à la dernière.
    Renvoie la liste de toutes les lignes (une liste de dictionnaires).
    """
    lignes=[]
    parametres_recus=dict(parametres)
    for page in range (1,3000) :
        parametres["page"]=page
        r=requests.get(url, params=parametres_recus, timeout=30)
        reponse=r.json()
        lignes.extend(reponse["data"])
        if reponse["next"] is None:
            break
    return lignes