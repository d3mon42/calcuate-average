# filepath: average-grades-calculator/src/calculate_average.py
# Calcola la media delle votazioni scolastiche
def main():
    grades = []
    while True:
        try:
            grade_input = input("Inserisci un voto (o 'fine' per terminare): ")
        except (EOFError, KeyboardInterrupt):
            print("\nInterruzione rilevata. Uscita dal programma.")
            return
            if grade_input.lower() == 'fine':  # Exit condition for the loop
                break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 10:  # Assuming grades are between 0 and 10
                grades.append(grade)
            else:
                print("Per favore, inserisci un voto valido tra 0 e 10.")
        except ValueError:
            print("Input non valido. Per favore, inserisci un numero.")

    if grades:
        total_sum = sum(grades)
        import locale
        locale.setlocale(locale.LC_ALL, '')  # Set to the user's locale
        # In the Italian grading system, a grade of 6 or higher is considered sufficient.
        if average >= 6:
            print("Media sufficiente")
        print(f"La media dei voti è: {average:.2f}")
        if average >= 6:
            print("Media sufficiente")
        else:
            print("Media insufficiente")
    else:
        print("Nessun voto inserito.")

if __name__ == "__main__":
    main()