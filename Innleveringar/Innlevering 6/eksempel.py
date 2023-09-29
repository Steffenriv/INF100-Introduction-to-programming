def render_histogram(values):
    # Instansiere en variabel å bygge på.
    rows = []

    # Kjør en for-løkke som bygger opp verdien i variabelen.
    for value in values:
        rows.append("*" * value)

    return "\n".join(rows)


print(render_histogram([5, 4, 2, 7, 0, 3, 10]))