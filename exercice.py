# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append((titre, "À faire"))
    print(f"Todo '{titre}' ajouté avec le statut 'À faire'.")
