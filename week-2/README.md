# Nädal 2 – SQL Data Cleaning

## Projekti eesmärk

Selle nädala eesmärk oli õppida SQL abil andmeid puhastama ja ette valmistama usaldusväärseks analüüsiks. Keskendusin duplikaatide kontrollimisele, puuduvate väärtuste analüüsimisele ning andmete vormindamisele.

## Äriküsimus

Kas UrbanStyle andmed on piisavalt kvaliteetsed, et nende põhjal koostada usaldusväärseid aruandeid ja teha ärilisi otsuseid?

## Minu ülesanne

Kasutasin SQL päringuid, et hinnata andmete kvaliteeti ning harjutada andmete puhastamise meetodeid testtabelis.

Teostasin järgmised tegevused:

- lõin testtabeli (`sales_test`) andmete turvaliseks töötlemiseks;
- kontrollisin duplikaatkirjeid;
- kontrollisin puuduvaid (`NULL`) väärtusi;
- kasutasin `COALESCE()` funktsiooni puuduvate väärtuste käsitlemiseks;
- kasutasin `TRIM()`, `UPPER()` ja `LOWER()` funktsioone tekstiväljade korrastamiseks;
- kontrollisin kuupäevade ja arvväärtuste korrektsust;
- analüüsisin müüke aastate, kuude, müügikanalite ja kaupluste lõikes.

## Tulemused

Analüüsi käigus selgus, et:

- testtabel võimaldas andmete puhastamise võtteid turvaliselt katsetada;
- **988** müügikirjel puudus `customer_id`;
- väljadel `sale_date`, `unit_price` ja `total_price` puuduvad väärtused puudusid;
- müügiandmed jagunesid aastate ja kuude lõikes ootuspäraselt;
- füüsiliste kaupluste suurim käive oli Tallinna kaupluses.

## Minu soovitused

Analüüsi põhjal soovitan:

- selgitada välja, miks osadel müügikirjetel puudub `customer_id`;
- rakendada kontrollid, mis vähendavad duplikaatkirjete tekkimise võimalust;
- standardiseerida tekstiväljade sisestamine;
- kontrollida andmete kvaliteeti enne regulaarsete aruannete koostamist;
- kasutada enne andmete muutmist alati testtabelit.

## Mida õppisin

Õppisin kasutama SQL-i andmete kvaliteedi kontrollimiseks ja puhastamiseks. Sain praktilise kogemuse duplikaatide kontrollimisel, puuduvate väärtuste analüüsimisel ning teksti- ja arvuväljade korrastamisel. Mõistsin, et usaldusväärne andmeanalüüs algab kvaliteetsetest andmetest.

## Kasutatud tööriistad

- PostgreSQL (Supabase)
- SQL
- GitHub
- NotebookLM
- ChatGPT
