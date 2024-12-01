# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append((titre, "À faire"))
    print(f"Todo '{titre}' ajouté avec le statut 'À faire'.")
# Liste pour stocker les todos et leurs statuts
todos = []

# Fonction pour lister les todos
def lister_todos():
    if not todos:
        print("Aucun todo à afficher.")
    else:
        print("\nListe des todos :")
        for i, (titre, statut) in enumerate(todos, 1):
            print(f"{i}. {titre} - {statut}")
