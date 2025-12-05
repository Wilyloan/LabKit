import secrets
from math import log2
from enum import IntEnum

class StrenghtEntropy(IntEnum):
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120


def create_new(lenght: int, characters: str) -> str:
    return ''.join(secrets.choice(characters) for _ in range(lenght))



def get_entropy(lenght: int, characters_number: int) -> float:
    try:
        entropy = lenght * log2(characters_number)
    except ValueError:
        return 0.0
    return round(entropy, 2)                                        