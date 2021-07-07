TAMANHO_CPF = 11

def is_cpf_valido(cpf: str) -> bool:
    if len(cpf) != TAMANHO_CPF:
        return False

    if cpf in (c * TAMANHO_CPF for c in "1234567890"):
        return False

    cpf_reverso = cpf[::-1]
    for i in range(2, 0, -1):
        cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
        if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
            return False

    return True


if __name__ == "__main__":
    print(is_cpf_valido("0"))
    print(is_cpf_valido("123456789012345"))
    print(is_cpf_valido("55555555555"))
    print(is_cpf_valido("19627722000"))
    print(is_cpf_valido("19627722091"))
    print(is_cpf_valido("19627722090"))
    print(is_cpf_valido("02927367035"))
    print(is_cpf_valido("64935775009"))
    print(is_cpf_valido("45508834052"))
    print(is_cpf_valido("50406509069"))