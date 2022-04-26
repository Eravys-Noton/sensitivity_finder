import input

def verify_sensitivity(sens):
    try:
        float(sens)
        return True
    except ValueError:
        return False

def verify_pref(pref):
    if str.lower(pref) == "o" or str.lower(pref) == "n":
        return True
    else:
        return False

def verify_pref_choice (pref_choice):
    if str.lower(pref_choice) == "f" or str.lower(pref_choice) == "h":
        return True
    else:
        return False