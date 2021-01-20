#!/usr/env/bin python3
# sieveOfEratosthenes.py - function that uses the Sieve Of Eratosthenes algorithm to
# return all of the prime numbers up to the given number N as a list.

def sieve_of_eratosthenes(number):
    div_list = []
    prime_list = []
    for i in range(2, number + 1):
        prime_list.append(i)
        div_list.append(i)
    for modulo in div_list:
        for n in prime_list:
            if n % modulo == 0 and n == modulo:
                continue
            if n % modulo == 0:
                prime_list.remove(n)
    return prime_list


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Please enter a positive whole number. \n'))
            if num < 0:
                print('Value entered was not positive.')
            else:
                break
        except ValueError:
            print('Value entered was not an integer.')
    print(sieve_of_eratosthenes(num))
