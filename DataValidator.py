# -*- coding: utf-8 -*-


def validate_sex(sex: int) -> bool:
    return (sex == 1) or (sex == 2)


def validate_age(age: int) -> bool:
    return age in range(18, 101)


def validate_name(name: str) -> bool:
    if len(name) < 2:
        return False
    name = name.lower()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    for sym in name:
        if sym not in alphabet:
            return False
    return True
