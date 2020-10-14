#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return - number
    else:
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixes = "JKLMNOPQ", "ack"
    word_list = []

    for c in prefixes:
        word_list.append(c + suffixes)
    return word_list


def is_prime(number):
    for i in (2, number ** 0.5):
        if number % i == 0:
            return False
    return True


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number = 6
    while len(prime) < 100:
        if is_prime(number):
            prime.append(number)
        number += 1
    return sum(prime)


def factorial(number: int) -> int:
    for i in range(1, number):
        number *= i
    return number


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for small_groups in groups:

        if len(small_groups) <= 3 or len(small_groups) > 10:
            acceptance.append(False)
            continue

        if 25 in small_groups:
            acceptance.append(True)
            continue

        if 50 in small_groups:
            is_50 = True
        else:
            is_50 = False

        is_accepted = True
        for age in small_groups:
            if age < 18:
                is_accepted = False
                break
            elif age > 70 and is_50:
                is_accepted = False
                break
        acceptance.append(is_accepted)
    
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
