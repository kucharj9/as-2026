# SP1 Kroužky

Kód žáka: 9

## Věci, které jsou špatně na původní tabulce

1. Nepravidelné formátování
2. Zbytečné opakování některých ůdajů (např. jméno vedoucího (každý kroužek má vždy stejného); lze to rozdělit do více tabulek)
3. Nejde lehce zjistit některé ůdaje (napŕ. kolik kroužků škola nabízí)

## Co je co

* zaci: PK id_zaka
* krouzky: PK id_krouzku
* prihlasky: PK id_prihlasky, FK id_zaka → zaci, FK id_krouzku → krouzky

## ER diagram

```mermaid
erDiagram
    ZACI ||--o{ PRIHLASKY : "má přihlášky"
    KROUZKY ||--o{ PRIHLASKY : "má přihlášky"

    ZACI {
        int id_zaka PK
        string jmeno
        string prijmeni
        string trida
    }

    KROUZKY {
        int id_krouzku PK
        string nazev
        string vedouci
        string den
        string cas
        string mistnost
        int cena_kc
    }

    PRIHLASKY {
        int id_prihlasky PK
        int id_zaka FK
        int id_krouzku FK
        string zaplaceno
    }
```

## Dotaz SQL

SELECT krouzek, cena FROM krouzky WHERE cena > 500;