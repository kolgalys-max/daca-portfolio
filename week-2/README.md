# Nädal 2 – SQL Data Cleaning

## Projekti eesmärk

Selle nädala eesmärk oli õppida SQL abil andmeid puhastama ja ette valmistama usaldusväärseks analüüsiks. Keskendusin duplikaatide leidmisele ja eemaldamisele, puuduvate väärtuste kontrollimisele ning andmete vormindamisele.

## Äriküsimus

Kas UrbanStyle andmed on piisavalt kvaliteetsed, et nende põhjal koostada usaldusväärseid aruandeid ja teha ärilisi otsuseid?

## Minu ülesanne

Kasutasin SQL päringuid, et hinnata ja parandada andmete kvaliteeti.

Tegin järgmised tegevused:

- lõin testtabeli (`sales_test`) andmete turvaliseks töötlemiseks;
- leidsin ja eemaldasin duplikaatkirjed;
- kontrollisin puuduvaid (`NULL`) väärtusi;
- kasutasin `COALESCE()` puuduvate väärtuste käsitlemiseks;
- kasutasin `TRIM()`, `UPPER()` ja `LOWER()` tekstiväljade korrastamiseks;
- vormindasin kuupäevi ja arvväärtusi;
- analüüsisin müüke aastate, kuude, müügikanalite ja kaupluste lõikes.

## Tulemused

Analüüsi käigus selgus, et:

- duplikaadid eemaldati edukalt testtabelist;
- 988 müügikirjel puudus `customer_id`;
- `sale_date`, `unit_price` ja `total_price` puuduvad väärtused puudusid;
- müügiandmed jagunesid aastate ja kuude lõikes ootuspäraselt;
- füüsiliste kaupluste suurim käive oli Tallinnas.

## Minu soovitused

Analüüsi põhjal soovitan:

1. selgitada välja, miks osadel müügikirjetel puudub `customer_id`;
2. rakendada kontrollid, mis takistavad duplikaatkirjete tekkimist;
3. standardiseerida tekstiväljade sisestamine;
4. kontrollida andmete kvaliteeti enne regulaarsete aruannete koostamist;
5. kasutada enne andmete muutmist alati testtabelit.

## Mida õppisin

Õppisin kasutama SQL-i andmete puhastamiseks ning sain praktilise kogemuse duplikaatide eemaldamisel, puuduvate väärtuste kontrollimisel ja andmete vormindamisel. Mõistsin, et kvaliteetne andmeanalüüs algab alati kvaliteetsetest andmetest.

## Kasutatud tööriistad

- Supabase (PostgreSQL)
- SQL
- GitHub
- NotebookLM
- Chat GPT
