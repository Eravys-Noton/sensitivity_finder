def get_average (low_sens, high_sens):
    return (low_sens + high_sens) / 2

def get_new_sens (pref, sens_f, sens_h, avg):
    if pref == "f":
        print("")
        print("Nouvelle sensi faible : {}".format(sens_f))
        print("Nouvelle sensi haute : {}".format(avg))
        return (sens_f, avg)
    elif pref == "h":
        print("")
        print("Nouvelle sensi faible : {}".format(avg))
        print("Nouvelle sensi haute : {}".format(sens_h))
        return (avg, sens_h)
