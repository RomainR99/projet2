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
# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    if not todos:
        print("Aucun todo à modifier.")
        return
lister_todos()
    try:
        choix = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if 0 <= choix < len(todos):
            titre, statut = todos[choix]
            if statut == "À faire":
                todos[choix] = (titre, "Fait")
                print(f"Le statut du todo '{titre}' a été mis à jour à 'Fait'.")
            elif statut == "Fait":
                todos[choix] = (titre, "À fair")  # Erreur volontaire
                print(f"Le statut du todo '{titre}' a été mis à jour à 'À fair'.")
            else:
                print(f"Statut inconnu pour le todo '{titre}'. Aucune modification effectuée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')
    
    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
	case 'q': print('Au revoir')
	case _: print('Choix invalide')
