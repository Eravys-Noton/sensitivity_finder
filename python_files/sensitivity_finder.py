import calculation
import user_input

def print_introduction ():
    print("Pour faire ce test vous aurez besoin de trouver une cible immobile et SURTOUT VOUS NE DEVEZ PAS ETRE ECHAUFFE.")
    print("Pour tester vos préférences de sensibilités, essayez de garder votre viseur sur la cible tout en vous déplaçant.")
    print("La sensibilité avec laquelle vous visez le mieux la cible est votre sensibilité préférée.")
    print("La sensibilité faible de départ doit être une sensi qui vous semble très lente, genre Papy et tout.")
    print("La sensiblité haute de départ doit être une sensi qui vous semble très rapide, genre Parkinson et tout.")
    print("")

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
    print("")
    stop = input("Appuyez sur une touche pour fermer la fenêtre.")
    return 0

sens_finder()