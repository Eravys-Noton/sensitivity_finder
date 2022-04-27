import calculation
import user_input

def print_introduction ():
    sentences = [
        "",
        "IMPORTANT A LIRE :",
        "- Pour faire ce test vous aurez besoin de trouver une cible immobile et SURTOUT VOUS NE DEVEZ PAS ETRE ECHAUFFE.",
        "- Pour tester vos préférences de sensibilités, essayez de garder votre viseur sur la cible tout en vous déplaçant.",
        "- La sensibilité avec laquelle vous visez le mieux la cible est votre sensibilité préférée.",
        "- Pour les nombres à virgule, ils doivent être saisis avec des POINTS et non des VIRGULES.",
        "- La sensibilité faible de départ doit être une sensi qui vous semble très lente, genre Papy et tout.",
        "- La sensiblité haute de départ doit être une sensi qui vous semble très rapide, genre Parkinson et tout.",
        "- Lors du test, il est normal de préférer un coup la sensi faible et un coup la sensi haute.",
        ""
    ]
    for sentence in sentences:
        print(sentence)

    start = input("Appuyez sur une touche (si vous avez tout lu) pour commencer.")
    print("")
    print("DEBUT DU TEST : ")


def sens_finder ():
    print_introduction()

    sensitivities = user_input.get_sensitivities()
    low, high = sensitivities[0], sensitivities[1]
    avg = calculation.get_average(low, high)
    user_has_pref = user_input.has_pref()

    while user_has_pref == "o":
        pref = user_input.choose_pref()
        sensitivities = calculation.get_new_sens(pref, low, high, avg)
        low, high = sensitivities[0], sensitivities[1]
        avg = calculation.get_average(low, high)
        user_has_pref = user_input.has_pref()

    print("")
    print("Votre sensibilité finale est : {}".format(avg))
    print("Jouez un certain temps avec pour bien l'essayer (les résultats ne se veront pas tout de suite, puis ajustez-la légèrement si besoin.")
    stop = input("Appuyez sur une touche pour fermer la fenêtre.")
    return 0

sens_finder()