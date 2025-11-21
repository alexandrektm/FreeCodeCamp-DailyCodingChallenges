def infected(days):

    infected = 1

    for day in range (days):

        infected *= 2

        if (day+1) % 3 == 0:

            loss = (0.2 * infected)

            if loss % 1 != 0:
                loss = ((loss // 1) + 1)

            infected = infected - loss

    return infected

print(infected(17))