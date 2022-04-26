import input

def verify_sensitivity(sens):
    try:
        float(sens)
        return True
    except ValueError:
        return False

def verify_pref(pref):
    if str.lower(pref) != "o" and str.lower(pref) != "n":
        input.has_pref()

def verify_pref_choice (pref_choice):
    if str.lower(pref_choice) != "f" and str.lower(pref_choice) != "h":
        input.choose_pref()