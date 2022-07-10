import sqlite3

def dodaj():
    conn = sqlite3.connect("Przepisy.db")
    c = conn.cursor()
    nazwa = input("Podaj nazwę:\n")
    p_trud = input("Poziom trudności (w skali 1-5):\n")
    skl = input("Składniki (oddziel je przecinkami):\n")
    instr = input("Instrukcje:\n")
    c.execute("INSERT INTO przepisy VALUES (?,?,?,?)",(nazwa, p_trud, skl, instr))
    conn.commit()
    conn.close()
def usun():
    conn = sqlite3.connect("Przepisy.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM przepisy")
    przepisy = c.fetchall()
    for przepis in przepisy:
        print(przepis[0], przepis[1])
    ktory = input("Który przepis chciałbyś usunąć? (Podaj liczbę) \n")
    c.execute("DELETE FROM przepisy WHERE rowid = ?", ktory)
    c.execute("SELECT rowid, * FROM przepisy")
    conn.commit()
    conn.close()
def czytaj():
    conn = sqlite3.connect("Przepisy.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM przepisy")
    przepisy = c.fetchall()
    for przepis in przepisy:
        print(przepis[0], przepis[1])
    ktory = int(input("Który przepis chciałbyś przeczytać? (podaj numer)\n"))
    c.execute("SELECT * FROM przepisy")
    przepis = c.fetchall()[ktory - 1]
    print(przepis[0].upper())
    print("Poziom trudności: " + przepis[1] + "\n")
    skl = przepis[2].replace(", ","\n")
    print("Składniki:\n" + skl + "\n")
    instr = przepis[3].replace(", ", "\n-->")
    print("Instrukcje:\n" + "-->" + instr + "\n")
def edytuj():
    conn = sqlite3.connect("Przepisy.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM przepisy")
    przepisy = c.fetchall()
    for przepis in przepisy:
        print(przepis[0], przepis[1])
    ktory = int(input("Który przepis chciałbyś edytować? (podaj numer)\n"))
    c.execute("SELECT * FROM przepisy")
    print(c.fetchall()[ktory - 1])
    while True:
        ktory_el = input("Który element chcesz edytować?\n"
                         "1.Nazwa\n"
                         "2.Poziom Trudności\n"
                         "3.Składniki\n"
                         "4.Instrukcje\n")
        if ktory_el == "1":
            nowa_nazwa = input("Podaj nową nazwę:\n")
            c.execute("UPDATE przepisy SET nazwa = ? WHERE rowid = ?", (nowa_nazwa, ktory))
            dalej = input("Czy chciałbyś zedytować więcej wartości w tym przepisie? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                break
        elif ktory_el == "2":
            nowy_poziom = input("Podaj nowy poziom trudności:\n")
            c.execute("UPDATE przepisy SET poziom_trudnosci = ? WHERE rowid = ?", (nowy_poziom, ktory))
            dalej = input("Czy chciałbyś zedytować więcej wartości w tym przepisie? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                break
        elif ktory_el == "3":
            nowe_skladniki = input("Podaj nową listę składników:\n")
            c.execute("UPDATE przepisy SET skladniki = ? WHERE rowid = ?", (nowe_skladniki, ktory))
            dalej = input("Czy chciałbyś zedytować więcej wartości w tym przepisie? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                break
        elif ktory_el == "4":
            nowe_instrukcje = input("Podaj nowe instrukcje:\n")
            c.execute("UPDATE przepisy SET instrukcje = ? WHERE rowid = ?", (nowe_instrukcje, ktory))
            dalej = input("Czy chciałbyś zedytować więcej wartości w tym przepisie? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                break
        else:
            print("Niepoprawny input, upewnij się, że wpisujesz odpowiednią wartość (1/2/3/4)")
            continue

if __name__=="__main__":
    while True:
        akcja = input("Witaj Wiktor, co chciałbyś zrobić?\n1.Dodaj przepis\n2.Odczytaj przepis\n3.Edytuj przepis\n4.Usuń przepis\n")
        if akcja == "1":
            dodaj()
            dalej = input("Czy chcesz zrobić coś jeszcze? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                print("Do Zobaczenia!")
                break
        elif akcja == "2":
            czytaj()
            dalej = input("Czy chcesz zrobić coś jeszcze? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                print("Do Zobaczenia!")
                break
        elif akcja == "3":
            edytuj()
            dalej = input("Czy chcesz zrobić coś jeszcze? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                print("Do Zobaczenia!")
                break
        elif akcja == "4":
            usun()
            dalej = input("Czy chcesz zrobić coś jeszcze? (y/n)\n").lower()
            if dalej == "y":
                continue
            elif dalej == "n":
                print("Do Zobaczenia!")
                break
        else:
            print("Upewnij się, że podajesz prawidłową wartość (1/2/3/4)\n")
            continue