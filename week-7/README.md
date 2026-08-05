# Week 7 – Python ja Pandas

## Projekti eesmärk

Selle nädala eesmärk oli õppida kasutama Pythonit ja pandas teeki andmete laadimiseks, ühendamiseks, puhastamiseks, analüüsimiseks ja visualiseerimiseks.

Minu individuaalse töö põhifookus oli UrbanStyle’i klientide RFM-analüüs. Analüüsi abil jagasin kliendid ostukäitumise põhjal segmentidesse, et selgitada välja:

- kes on ettevõtte kõige väärtuslikumad kliendid;
- millistel klientidel on potentsiaal muutuda lojaalsemaks;
- millised kliendid on kadumisohus;
- milliste segmentidega peaks ettevõte esmajärjekorras tegelema.

## Äriküsimus

**Kes on UrbanStyle’i kõige väärtuslikumad kliendid, millised kliendid vajavad kiiret tähelepanu ja millise kliendisegmendiga peaks Marko esimesena tegelema?**

## Kasutatud tööriistad

- Python 3.13
- pandas
- Plotly Express
- Jupyter Notebook
- Supabase
- GitHub

## Kasutatud andmed

Laadisin andmed Pythonisse otse Supabase’i andmebaasist.

Kasutasin järgmisi tabeleid:

| Tabel | Ridade arv | Veergude arv |
|---|---:|---:|
| `sales` | 15 234 | 12 |
| `customers` | 3 150 | 9 |
| `products` | 362 | 9 |

Ühendasin tabelid pandas `merge()` funktsiooniga:

- müügi- ja kliendiandmed veeru `customer_id` kaudu;
- müügi- ja tooteandmed veeru `product_id` kaudu.

Kasutasin mõlema ühendamise puhul vasakühendust ehk `how="left"`, et säilitada kõik müügikirjed.

Ühendatud DataFrame sisaldas:

- **15 234 rida**
- **28 veergu**

Ühendamise järel jäi ridade arv samaks nagu algses `sales` tabelis. See näitas, et ühendamine ei tekitanud lisaridu ega eemaldanud müügikirjeid.

## Minu töö

Tegin analüüsi järgmiste sammudena:

1. seadistasin Python 3 ja Jupyter Notebooki töökeskkonna;
2. paigaldasin vajalikud teegid;
3. lõin ühenduse Supabase’i andmebaasiga;
4. laadisin tabelid pandas DataFrame’idesse;
5. kontrollisin andmete mõõtmeid, veerge ja andmetüüpe;
6. ühendasin müügi-, kliendi- ja tooteandmed;
7. kontrollisin puuduvaid väärtusi ja duplikaate;
8. valmistasin ette RFM-analüüsiks vajalikud andmed;
9. arvutasin Recency, Frequency ja Monetary näitajad;
10. määrasin klientidele RFM-skoorid;
11. jagasin kliendid viide segmenti;
12. koostasin segmentide kokkuvõttetabeli;
13. lõin Plotly abil interaktiivsed visualiseeringud;
14. sõnastasin analüüsi põhjal ärilised järeldused ja soovitused.

## Andmete esmane kontroll

Enne RFM-analüüsi kontrollisin:

- DataFrame’i mõõtmeid;
- veergude nimesid;
- andmetüüpe;
- puuduvaid väärtusi;
- täielikult dubleerivaid ridu;
- numbriliste veergude miinimum-, maksimum- ja keskmisi väärtusi.

Kontrolli tulemusena selgus:

- täielikult dubleerivaid ridu oli **0**;
- `customer_id` puudus **1487 müügireal**;
- `store_location` puudus **5204 real**;
- `loyalty_tier` puudus **7033 real**;
- `eco_certified` puudus **829 real**;
- väikseim `total_price` väärtus oli **−1405,32 €**;
- suurim `total_price` väärtus oli **2170,40 €**.

Kliendiandmete puudumine oli seotud eelkõige nende müügiridadega, kus puudus `customer_id`. Seetõttu puudusid samadel ridadel ka kliendi nimi, linn, sünniaasta ja muud klienditabelist pärinevad väärtused.

## RFM-andmete puhastamine

RFM-analüüsi jaoks kasutasin ainult järgmisi veerge:

- `customer_id`
- `sale_date`
- `total_price`

Puhastamise käigus:

- teisendasin `sale_date` veeru kuupäevatüübiks;
- eemaldasin read, kus puudus `customer_id`;
- eemaldasin read, kus puudus või ei olnud korrektne `sale_date`;
- eemaldasin read, kus puudus `total_price`;
- jätsin analüüsi ainult positiivse väärtusega tehingud;
- teisendasin `customer_id` täisarvuks.

Pärast puhastamist jäi RFM-analüüsi:

- **13 468 tehingut**
- **0 puuduvat väärtust**
- väikseim positiivne tehing **15,09 €**
- suurim tehing **2170,40 €**

Negatiivsed ja nullväärtusega tehingud jätsin RFM ostukäitumise analüüsist välja, et need ei vähendaks kliendi tegelikku positiivset ostumahtu.

## RFM-meetod

RFM-analüüs hindab klienti kolme näitaja kaudu:

- **Recency** – mitu päeva on möödunud kliendi viimasest ostust;
- **Frequency** – mitu ostu klient analüüsitaval perioodil tegi;
- **Monetary** – kui palju klient kokku kulutas.

Analüüsi viitekuupäevaks määrasin viimase andmestikus oleva ostukuupäeva järgmise päeva.

Analüüsi kuupäev oli:

**29.06.2026**

Iga kliendi kohta arvutasin:

```text
Recency = analüüsi kuupäev − kliendi viimane ostukuupäev
Frequency = kliendi ostude arv
Monetary = kliendi tehingute kogusumma
