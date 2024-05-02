from abc import ABC
from datetime import datetime


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def jellemzok(self):
        pass


class EgyagyasSzoba(Szoba):
    def jellemzok(self):
        return "Egyágyas szoba"


class KetagyasSzoba(Szoba):
    def jellemzok(self):
        return "Kétágyas szoba"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"{foglalas.szoba.jellemzok()} - {foglalas.szoba.szobaszam}: {foglalas.datum}")


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


def main():
    # Szalloda és szobák létrehozása
    szalloda = Szalloda("Hotel Carpentum")
    szobak = [EgyagyasSzoba(101, 5000), EgyagyasSzoba(102, 6000), KetagyasSzoba(201, 8000)]
    for szoba in szobak:
        szalloda.szoba_hozzaadasa(szoba)

    # Példa foglalások
    foglalasok = [(101, "2024-05-15"), (102, "2024-05-20"), (201, "2024-06-01"),
                  (101, "2024-06-10"), (102, "2024-07-01")]
    for foglalas in foglalasok:
        szalloda.foglalas(foglalas[0], foglalas[1])

    # Felhasználói interfész
    print("Üdvözöljük a szálloda foglalási rendszerében!")
    while True:
        print("\nKérem válasszon a következő műveletek közül:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Válasszon egy számot a kívánt művelet végrehajtásához: ")

        if valasztas == "1":
            print("Szobák száma: 101, 102, 201")
            szobaszam = int(input("Kérem adja meg a foglalni kívánt szoba számát: "))
            datum = input("Kérem adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")

            try:
                foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
                if foglalas_datum < datetime.now():
                    print("A foglalás dátuma nem lehet múltbeli.")
                    continue
            except ValueError:
                print("Hibás dátum formátum!")
                continue

            foglalas_ar = szalloda.foglalas(szobaszam, datum)
            if foglalas_ar:
                print(f"A foglalás sikeres! A foglalás ára: {foglalas_ar} Ft")
            else:
                print("Nincs ilyen szobaszám a szállodában.")
        elif valasztas == "2":
            print("Jelenlegi foglalások:")
            szalloda.foglalasok_listazasa()
            szobaszam = int(input("Kérem adja meg a lemondani kívánt foglalás szobaszámát: "))
            datum = input("Kérem adja meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")

            lemondando_foglalas = None
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    lemondando_foglalas = foglalas
                    break

            if lemondando_foglalas:
                szalloda.lemondas(lemondando_foglalas)
                print("A foglalás sikeresen lemondva.")
            else:
                print("Nincs ilyen foglalás a rendszerben.")
        elif valasztas == "3":
            print("Foglalások listája:")
            szalloda.foglalasok_listazasa()
        elif valasztas == "0":
            print("Kilépés a programból.")
            break
        else:
            print("Hibás választás. Kérem válasszon a megadott lehetőségek közül.")


if __name__ == "__main__":
    main()
