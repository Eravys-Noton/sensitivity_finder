import calculation
import input

def print_introduction ():
    print("Pour faire ce test vous aurez besoin de trouver une cible immobile.")
    print("Pour tester vos préférences de sensibilités, essayez de garder votre viseur sur la cible tout en vous déplaçant.")
    print("La sensibilité avec laquelle vous visez le mieux la cible est votre sensibilité préférée.")
    print("")

def sens_finder ():
    sensitivities = input.get_sensitivities()
    low, high = sensitivities[0], sensitivities[1]
    avg = calculation.get_average(low, high)
    user_has_pref = input.has_pref()

    while user_has_pref == "o":
        pref = input.choose_pref()
        sensitivities = calculation.get_new_sens(pref, low, high, avg)
        low = sensitivities[0]
        high = sensitivities[1]
        avg = calculation.get_average(low, high)
        user_has_pref = input.has_pref()

    return avg

print_introduction()
print("Votre sensi est {}".format(sens_finder()))