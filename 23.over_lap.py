#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import random

def is_prime(number):
    for i in range(2, number/2 +1):
        if number % i == 0:
            return False;
    return True;

def gen_prime_number(maxNumber):
    primes = [1]

    for number in range(2, maxNumber + 1):
        if is_prime(number):
            primes.append(number);

    random.shuffle(primes)

    return primes;

def gen_samples(maxNumber):
    return random.sample(range(100), maxNumber);

def overlap(primes, samples):
    overlaps = []
    for i in primes:
        if i in samples:
            overlaps.append(i)

    return overlaps;

maxNumber = int(raw_input("Input max length of array: "))

primes = gen_prime_number(maxNumber)
samples = gen_samples(maxNumber)

print "Primes number: ", primes
print "Samples number: ", samples

print "Overlap numbers: ", overlap(primes, samples)
