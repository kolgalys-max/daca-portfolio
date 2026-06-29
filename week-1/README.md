# Nädal 1 – SQL Basics

## Projekti eesmärk

Selle nädala eesmärk oli õppida SQL-i põhikäsklusi ning analüüsida UrbanStyle müügiandmeid.

## Äriküsimus

Kas müügiandmed on usaldusväärsed ja valmis edasiseks analüüsiks?

## Minu ülesanne

Minu roll oli analüüsida müügiandmete kvaliteeti SQL päringute abil.

Teostasin järgmised kontrollid:

- kontrollisin müügikirjete koguarvu;
- leidsin suurima ja väikseima müügitehingu;
- kontrollisin puuduvaid `customer_id` väärtusi;
- hindasin andmete kvaliteeti.

## Tulemused

Analüüsi käigus selgus, et:

- tabel sisaldas 15 234 müügikirjet;
- suurim müügitehing oli 2170,40 €;
- väikseim müügitehing oli −1405,32 €;
- 1487 kirjel puudus `customer_id`;
- andmestik sisaldas kirjeid, mis vajavad enne edasist analüüsi täiendavat kontrolli.

## Õppisin

Selle nädala jooksul õppisin:

- SQL SELECT päringuid;
- WHERE tingimusi;
- ORDER BY kasutamist;
- andmete kvaliteedi kontrollimist;
- SQL abil andmete analüüsimise põhimõtteid.

## Kasutatud tööriistad

- PostgreSQL (Supabase)
- SQL
- GitHub
- NotebookLM
