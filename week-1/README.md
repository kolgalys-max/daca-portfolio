# Nädal 1 – SQL Basics: UrbanStyle Data Landscape

## Projekti eesmärk

Selle nädala eesmärk oli tutvuda SQL-i põhikäskudega ning õppida uurima UrbanStyle ettevõtte andmeid. Fookuses oli müügiandmete kvaliteedi hindamine ja esmaste tähelepanekute tegemine enne põhjalikuma ärianalüüsi alustamist.

## Äriküsimus

Kas UrbanStyle müügiandmed on piisavalt kvaliteetsed, et nende põhjal teha usaldusväärseid äriotsuseid?

## Minu roll

Minu roll meeskonnas oli **Roll A – Sales**.

Kasutasin SQL päringuid, et analüüsida `sales` tabelit ning hinnata müügiandmete kvaliteeti.

## Mida ma tegin

- uurisin `sales` tabelit SQL päringutega;
- kontrollisin müügikirjete koguarvu;
- leidsin suurimad ja väikseimad müügitehingud;
- kontrollisin puuduvaid `customer_id` väärtusi;
- analüüsisin müügiandmete kvaliteeti;
- osalesin meeskonna ühise Data Landscape kokkuvõtte koostamisel ja esitlusmaterjalide ettevalmistamisel.

## Tulemused

Analüüsi käigus selgus, et:

- müügitabelis oli **15 234** müügikirjet;
- suurim müügitehing oli **2170,40 €**;
- väikseim müügitehing oli **−1405,32 €**;
- **1487** müügikirjel puudus `customer_id`;
- andmestikus leidus negatiivseid müügisummasid, mis vajavad täiendavat kontrolli.

## Mida tulemused näitavad

Andmestik sobib edasiseks analüüsiks, kuid enne äriliste otsuste tegemist tuleb parandada andmete kvaliteeti. Puuduvad kliendiandmed ja negatiivsed müügisummad võivad mõjutada aruannete täpsust ning seeläbi ka juhtimisotsuseid.

## Soovitused Toomasele

Pärast UrbanStyle andmestiku analüüsi soovitame:

1. Kontrollida puuduvaid `customer_id` väärtusi ning selgitada nende põhjus.
2. Uurida negatiivseid müügisummasid ja teha kindlaks, kas tegemist on tagastuste või andmevigadega.
3. Kontrollida võimalikke duplikaate kliendiandmetes.
4. Täiendada andmestiku dokumentatsiooni, et tabelite ja veergude tähendus oleks üheselt mõistetav.
5. Standardiseerida andmete sisestamise põhimõtted, et parandada andmekvaliteeti ja suurendada aruandluse usaldusväärsust.

## Mida õppisin

Õppisin kasutama SQL-i põhikäskusid (`SELECT`, `WHERE`, `ORDER BY`, `COUNT`, `MIN`, `MAX`) ning sain praktilise kogemuse andmete kvaliteedi hindamisel. Samuti mõistsin, et enne analüüsi või aruannete koostamist tuleb alati kontrollida andmete korrektsust.

## Kasutatud tööriistad

- PostgreSQL (Supabase)
- SQL
- GitHub
- NotebookLM
