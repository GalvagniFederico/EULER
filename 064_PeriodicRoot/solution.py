import math

def radice_continua(n):
    if int(math.sqrt(n)) ** 2 == n:
        return [int(math.sqrt(n))]  # Se n è un quadrato perfetto, restituisci solo la parte intera

    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0

    period = []

    seen = set()  # per sicurezza, ma non obbligatorio

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)

        # la sequenza inizia a ripetersi quando a == 2*a0
        if a == 2 * a0:
            break

    return [a0, period]  # restituisce: [parte intera, [sequenza periodica]]

# Esempio: √23
n = 23
espansione = radice_continua(n)
print(f"√{n} = [{espansione[0]};", "overline{" + ','.join(map(str, espansione[1])) + "}]")
print(f"Periodo: {len(espansione[1])}")
