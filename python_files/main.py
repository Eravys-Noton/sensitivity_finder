import calculation
import input
import verification


def sens_finder ():
    sensitivities = input.get_sensitivities()
    low = sensitivities[0]
    high = sensitivities[1]
    return calculation.get_average(low, high)

print("Votre sensi est {}".format(sens_finder()))