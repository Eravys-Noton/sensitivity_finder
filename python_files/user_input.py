import verification

def get_sensitivities ():
    low_sens = input("Entrez votre sensi faible de départ : ")

    while not verification.verify_sensitivity(low_sens):
        low_sens = input("Entrez votre sensi faible de départ : ")
    high_sens = input("Entrez votre sensi haute de départ : ")

    while not verification.verify_sensitivity(high_sens):
        high_sens = input("Entrez votre sensi haute de départ : ")
    return (float(low_sens), float(high_sens))

def has_pref ():
    pref = input("Avez-vous une préférence pour une des sensis ? (O pour oui, N pour non) : ")

    while not verification.verify_pref(pref):
        pref = input("Avez-vous une préférence pour une des sensis ? (O pour oui, N pour non) : ")
    return str.lower(pref)

def choose_pref ():
    pref_choice = input("Quelle est votre sensi préférée ? (F pour faible, H pour haute) : ")
    while not verification.verify_pref_choice(pref_choice):
        pref_choice = input("Quelle est votre sensi préférée ? (F pour faible, H pour haute) : ")
    return str.lower(pref_choice)