Bardzo stabilny i bezpieczny bot wymieniający Bitcoina.
Tworzy tylko krótkoterminowe transakcje.
Korzysta z aktualnych kursów coinBase.com

Działa na dwóch głównych wątkach:
-Czeka na zebranie 16-stu ostatnich kursów, zanim zacznie działać
-Pobieranie i aktualizowanie listy z kursami
-Tworzenie transakcji, obsługiwanie sprzedaży i kupna, analizowanie sytuacji

###Zasady kupowania:
-Jesli uniwersalnaSrednia > aktualnyKurs, kupuje kryptowalutę za kwotę 10000zł
-Nie prowadzi w jednym momencie więcej niż 6 transakcji
-Brak turbulencji na rynku (wyjaśnienie niżej)

###Zasady sprzedawania:
-Gdy kurs dolara wzrośnie o min 0.5 dolara
-Jeśli transakcja jest starsza niż 120s (zabezpieczenie przed dużymi stratami)

Bajery i zabezpieczenia:
-Współczynnik turbulencji:
  Jeśli rozstęp ostatnich sześciu kursów jest większy niż 50 dolarów, wstrzymuje kupowanie. Zabezpiecza przed kupowaniem waluty podczas dużych zmian ceny (z reguły bot tracił w takich przypadkach)
-Współczynnik desperacji:
  -im starsza jest transakcja, tym na mniejszy zysk zgadza się bot (niewprowadzone, ale duży potencjał na zysk).
-Wykrywanie trendu rosnącego/malejącego/nijakiego 

Zapisuje zakończone transakcje do pliku .txt.

Projekt stworzony na potrzeby hackathonu CryptoBrawl. Pobiera kursy ze strony coinBase i wykonuje transakcje na platformie the-brawl.eu
Dane między dwoma platformami zbyt różniły się w czasie, żeby bot mógł rozwinąć skrzydła :C
(ta platforma, na której się wykonywało transakcje nie posiadała udostępnionego API do pobierania cen. coinBase był polecony przez organizatora)
Natomiast uważam że ma bardzo dobry model, dobrze jest zabezpieczony, myślę że z kilkoma modyfikacjami mógłby faktycznie działać (największym problemem są prowizje).
Na spokojnie go zostawiałem żeby działał w tle bez nadzoru i bez obaw że mi sprzeda cały portfel.


![image](https://github.com/Zajac2003/Trading-Bot/assets/110545626/100a7d8d-50c9-453f-b7c7-df7e62e560bd)


