def get_average (low_sens, high_sens):
    """
    computes the average between two floats
    :param low_sens: the first float
    :param high_sens: the second float
    :return: float
    """
    return (low_sens + high_sens) / 2

def get_new_sens (pref, sens_f, sens_h, avg):
    """
    computes the new low and high sens
    :param pref: user preference (between high and low)
    :param sens_f: previous low sens
    :param sens_h: previous high sens
    :param avg: previous average
    :return: (float, float)
    """
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
