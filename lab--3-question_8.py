def checkPrime(number):
    index = 2
    while (index < number):
        if number % index == 0:
            return False
        index += 1
    return True


print(checkPrime(12))