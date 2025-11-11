def nth_prime(n):

    number = 1
    number_list = []
    counter = -1
    prime_list = []

    while True:

        skip = False
        number += 1

        for divisor in number_list:
            if number % divisor == 0:
                skip = True
                break
        
        if skip == False:
            prime_list.append(number)
            counter += 1
                
        if counter == n:
            result = prime_list[counter-1]
            break

        number_list.append(number)

    return result

print(nth_prime(5))