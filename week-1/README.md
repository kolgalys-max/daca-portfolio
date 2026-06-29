# Nädal 1 – SQL Basics

## Projekti eesmärk

Selle nädala eesmärk oli õppida SQL-i põhikäskusid ning uurida UrbanStyle müügiandmeid. Minu ülesanne oli hinnata müügiandmete kvaliteeti ja leida võimalikud probleemid enne edasist analüüsi.

## Minu ülesanne

Minu roll oli **Roll A – Sales**.

Kasutasin SQL päringuid, et:

- uurida `sales` tabelit;
- kontrollida müügikirjete koguarvu;
- leida suurimad ja väikseimad müügitehingud;
- kontrollida puuduvaid `customer_id` väärtusi;
- hinnata müügiandmete kvaliteeti.

## Tulemused

Minu analüüsi tulemusena selgus, et:

- `sales` tabelis oli **15 234** müügikirjet;
- suurim müügitehing oli **2170,40 €**;
- väikseim müügitehing oli **−1405,32 €**;
- **1487** müügikirjel puudus `customer_id`;
- andmestikus esines negatiivseid müügisummasid, mis vajavad täiendavat kontrolli.

## Minu soovitused

Analüüsi põhjal soovitan enne põhjalikumat ärianalüüsi:

1. kontrollida puuduvaid `customer_id` väärtusi;
2. uurida negatiivseid müügisummasid ja selgitada nende põhjus;
3. kontrollida võimalikke duplikaate;
4. täiendada andmestiku dokumentatsiooni;
5. rakendada andmete kvaliteedi kontroll enne regulaarset aruandlust.

## Mida õppisin

Õppisin kasutama SQL-i põhikäskusid (`SELECT`, `WHERE`, `ORDER BY`, `COUNT`, `MIN`, `MAX`) ning sain praktilise kogemuse müügiandmete uurimisel. Mõistsin, et enne analüüsi tegemist tuleb alati kontrollida andmete kvaliteeti, sest see mõjutab otseselt analüüsi usaldusväärsust.

## Kasutatud tööriistad

- Supabase (PostgreSQL)
- SQL
- GitHub
- NotebookLM
- Chat GPT
