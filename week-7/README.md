# Week 7 – Python ja Pandas

## Projekti eesmärk

Selle nädala eesmärk oli õppida kasutama Pythonit ja pandas teeki andmete laadimiseks, uurimiseks, puhastamiseks, ühendamiseks, analüüsimiseks ja visualiseerimiseks.

Minu individuaalse töö põhifookus oli UrbanStyle’i klientide RFM-analüüs. Analüüsi abil jagasin kliendid nende ostukäitumise põhjal segmentidesse, et selgitada välja:

- kes on ettevõtte kõige väärtuslikumad kliendid;
- millistel klientidel on potentsiaal muutuda lojaalsemaks;
- millised kliendid on kadumisohus;
- millise kliendisegmendiga peaks ettevõte esmajärjekorras tegelema.

## Äriküsimus

**Kes on UrbanStyle’i kõige väärtuslikumad kliendid, millised kliendid vajavad kiiret tähelepanu ja millise segmendiga peaks Marko esimesena tegelema?**

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

- `sales` ja `customers` tabelid veeru `customer_id` kaudu;
- müügi- ja tooteandmed veeru `product_id` kaudu.

Mõlema ühendamise puhul kasutasin vasakühendust ehk `how="left"`, et säilitada kõik müügikirjed.

Ühendatud DataFrame sisaldas:

- **15 234 rida**
- **28 veergu**

Ühendamise järel jäi ridade arv samaks nagu algses `sales` tabelis. See näitas, et ühendamine ei tekitanud lisaridu ega eemaldanud müügikirjeid.

## Tehtud töö

Analüüs koosnes järgmistest etappidest:

1. paigaldasin Pythoni ja vajalikud teegid;
2. seadistasin Jupyter Notebooki töökeskkonna;
3. lõin ühenduse Supabase’i andmebaasiga;
4. laadisin `sales`, `customers` ja `products` tabelid pandas DataFrame’idesse;
5. kontrollisin tabelite mõõtmeid, veerge ja andmetüüpe;
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

Kliendiandmete puudumine oli seotud eelkõige müügiridadega, kus puudus `customer_id`. Seetõttu puudusid samadel ridadel ka kliendi nimi, linn, sünniaasta ja muud klienditabelist pärinevad väärtused.

## RFM-andmete puhastamine

RFM-analüüsi jaoks kasutasin järgmisi veerge:

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

Negatiivsed ja nullväärtusega tehingud jätsin RFM-analüüsist välja, et tagastused või vigased tehingud ei vähendaks kliendi positiivset ostumahtu.

## RFM-meetod

RFM-analüüs hindab klienti kolme näitaja kaudu:

- **Recency** – mitu päeva on möödunud kliendi viimasest ostust;
- **Frequency** – mitu ostu klient tegi;
- **Monetary** – kui palju klient kokku kulutas.

Analüüsi viitekuupäevaks määrasin andmestikus oleva viimase ostukuupäeva järgmise päeva.

Analüüsi kuupäev oli **29.06.2026**.

Iga kliendi kohta arvutasin:

```text
Recency = analüüsi kuupäev − kliendi viimane ostukuupäev
Frequency = kliendi ostude arv
Monetary = kliendi tehingute kogusumma
```

RFM-analüüsi jõudis kokku **2550 klienti**.

## RFM-skooride arvutamine

Jagasin kliendid iga RFM-näitaja järgi viide gruppi ning määrasin skoorid vahemikus 1–5.

### Recency

- skoor 5 – klient ostis suhteliselt hiljuti;
- skoor 1 – kliendi viimasest ostust on möödunud palju aega.

### Frequency

- skoor 5 – klient ostab väga sageli;
- skoor 1 – klient on ostnud väga vähe.

### Monetary

- skoor 5 – klient kulutab palju;
- skoor 1 – klient kulutab vähe.

Kliendi lõplik RFM-skoor arvutati valemiga:

```text
RFM-skoor = R-skoor + F-skoor + M-skoor
```

Võimalik koguskoor oli vahemikus 3–15.

## Kliendisegmendid

Jagasin kliendid RFM-koguskoori järgi viide segmenti:

| RFM-skoor | Segment | Tähendus |
|---:|---|---|
| 13–15 | VIP Champions | kõige väärtuslikumad ja aktiivsemad kliendid |
| 10–12 | Loyal Customers | regulaarsed ja lojaalsed kliendid |
| 7–9 | Potential Loyalists | hea kasvupotentsiaaliga kliendid |
| 4–6 | At Risk | kliendid, kelle aktiivsus on vähenenud |
| 3 | Lost | kaua mitteaktiivsed ja väikese väärtusega kliendid |

## Segmentide jaotus

| Segment | Klientide arv | Osakaal klientidest |
|---|---:|---:|
| Potential Loyalists | 768 | 30,12% |
| Loyal Customers | 667 | 26,16% |
| At Risk | 538 | 21,10% |
| VIP Champions | 465 | 18,24% |
| Lost | 112 | 4,39% |
| **Kokku** | **2550** | **100%** |

Kõige suurem segment oli **Potential Loyalists**, kuhu kuulus 768 klienti.

## Segmentide tulemused

| Segment | Klientide arv | Keskmine Recency | Keskmine ostude arv | Keskmine kogukulu | Kogukäive |
|---|---:|---:|---:|---:|---:|
| VIP Champions | 465 | 524,22 päeva | 11,74 | 3829,20 € | 1 780 577,59 € |
| Loyal Customers | 667 | 634,84 päeva | 5,90 | 1799,91 € | 1 200 540,55 € |
| Potential Loyalists | 768 | 682,68 päeva | 3,63 | 964,65 € | 740 850,95 € |
| At Risk | 538 | 798,95 päeva | 2,13 | 513,41 € | 276 214,89 € |
| Lost | 112 | 981,79 päeva | 1,26 | 219,38 € | 24 570,51 € |
| **Kokku** | **2550** |  |  |  | **4 022 754,49 €** |

## Käibe jaotus segmentide vahel

| Segment | Kogukäive | Osakaal analüüsitud käibest |
|---|---:|---:|
| VIP Champions | 1 780 577,59 € | 44,26% |
| Loyal Customers | 1 200 540,55 € | 29,84% |
| Potential Loyalists | 740 850,95 € | 18,42% |
| At Risk | 276 214,89 € | 6,87% |
| Lost | 24 570,51 € | 0,61% |
| **Kokku** | **4 022 754,49 €** | **100%** |

VIP Champions ja Loyal Customers moodustasid kokku:

- **44,39% analüüsitud klientidest**
- **74,11% analüüsitud kogukäibest**

See näitab, et suur osa ettevõtte käibest sõltub aktiivsetest ja lojaalsetest klientidest.

## Peamised leiud

### 1. VIP Champions on kõige väärtuslikum segment

VIP Champions segmenti kuulus 465 klienti ehk 18,24% analüüsitud klientidest.

Nad:

- tegid keskmiselt 11,74 ostu;
- kulutasid keskmiselt 3829,20 € kliendi kohta;
- tõid kokku 1 780 577,59 € käivet;
- moodustasid 44,26% kogu RFM-analüüsi käibest.

Kuigi VIP-kliente ei olnud arvuliselt kõige rohkem, andsid nad kõige suurema osa käibest.

### 2. Loyal Customers on ettevõtte teine kõige olulisem segment

Loyal Customers segmenti kuulus 667 klienti.

Nende:

- keskmine ostude arv oli 5,90;
- keskmine kogukulu oli 1799,91 €;
- kogukäive oli 1 200 540,55 €;
- osakaal analüüsitud käibest oli 29,84%.

Koos VIP Champions segmendiga moodustasid nad üle 74% analüüsitud kogukäibest.

### 3. Potential Loyalists on suurim kasvuvõimalus

Potential Loyalists oli suurim segment 768 kliendiga.

See moodustas 30,12% kõigist analüüsitud klientidest.

Nende:

- keskmine ostude arv oli 3,63;
- keskmine kogukulu oli 964,65 €;
- kogukäive oli 740 850,95 €.

Tegemist on ettevõtte suurima kasvupotentsiaaliga grupiga, sest sobiva pakkumise korral võib osa neist liikuda Loyal Customers või VIP Champions segmenti.

### 4. At Risk segment vajab kiiret tähelepanu

At Risk segmenti kuulus 538 klienti ehk 21,10% analüüsitud klientidest.

Nende:

- viimasest ostust oli möödunud keskmiselt 798,95 päeva;
- keskmine ostude arv oli 2,13;
- keskmine kogukulu oli 513,41 €;
- kogukäive oli 276 214,89 €.

Need kliendid ei ole veel täielikult kadunud, kuid nende ostuaktiivsus on vähenenud. Seetõttu vajavad nad kiiret ja eraldi suunatud tagasivõitmise kampaaniat.

### 5. Lost segmendi majanduslik väärtus on väike

Lost segmenti kuulus 112 klienti.

Nende:

- viimasest ostust oli möödunud keskmiselt 981,79 päeva;
- keskmine ostude arv oli 1,26;
- keskmine kogukulu oli 219,38 €;
- kogukäive oli 24 570,51 €;
- osakaal analüüsitud käibest oli ainult 0,61%.

Selle segmendi tagasivõitmiseks ei ole mõistlik teha väga kulukaid personaalseid kampaaniaid enne, kui on hinnatud kampaania võimalikku tasuvust.

## Soovitused Markole

### VIP Champions

VIP-klientidele soovitan pakkuda:

- personaalset teenindust;
- varajast ligipääsu uutele toodetele;
- eksklusiivseid pakkumisi;
- VIP-programmi;
- ostuajalool põhinevaid soovitusi.

Eesmärk on hoida kõige väärtuslikumaid kliente ja vähendada nende lahkumise riski.

### Loyal Customers

Lojaalsetele klientidele sobivad:

- punktisüsteem;
- kordusostu soodustused;
- personaalsed pakkumised;
- lojaalsustasemete süsteem;
- soovitusprogrammid.

Eesmärk on suurendada ostusagedust ja aidata osal klientidest liikuda VIP Champions segmenti.

### Potential Loyalists

Potential Loyalists segmendile soovitan:

- tasuta tarnet;
- piiratud kehtivusega sooduskoodi;
- järgmise ostu boonust;
- seotud toodete soovitusi;
- personaliseeritud e-kirju.

See on arvuliselt kõige suurem segment ning seetõttu oluline võimalus kasvatada lojaalsete klientide hulka.

### At Risk

At Risk klientidele soovitan saata:

- „Me igatseme sind” kampaania;
- personaalse tagasitulekupakkumise;
- viimase ostuga seotud tootesoovitused;
- piiratud tähtajaga soodustuse;
- lühikese küsimustiku kliendi kadumise põhjuse mõistmiseks.

See segment vajab kõige kiiremat sekkumist.

### Lost

Lost segmendile sobib esmalt odavam automatiseeritud kampaania.

Suurema allahindluse või personaalse teeninduse kasutamine peaks sõltuma sellest, kas kliendi varasem väärtus ja võimalik tagasivõitmise tulu õigustavad kampaaniakulu.

## Juhtimissoovitus

UrbanStyle peaks kasutama erinevate segmentide jaoks erinevat kliendisuhtlust.

Esimene prioriteet on hoida **VIP Champions** ja **Loyal Customers** kliente, sest need kaks segmenti annavad kokku 74,11% analüüsitud kogukäibest.

Kasvu seisukohalt on kõige olulisem **Potential Loyalists**, sest see on 768 kliendiga kõige suurem segment.

Kõige kiiremat tähelepanu vajab **At Risk**, kus on 538 klienti, kelle aktiivsus on langenud, kuid kellel võib olla veel tagasivõitmise potentsiaali.

**Lost** segmendi puhul tuleb enne suurema turunduskulu tegemist hinnata kampaania tasuvust.

## Visualiseeringud

Koostasin Plotly Expressi abil kolm interaktiivset visualiseeringut:

1. **Klientide arv segmentide kaupa**  
   Näitab, kui palju kliente kuulub igasse RFM-segmenti.

2. **Kliendisegmentide kogukäive**  
   Näitab, millised segmendid annavad ettevõttele kõige suurema rahalise väärtuse.

3. **Ostusageduse ja kogukulu hajuvusdiagramm**  
   Näitab seost kliendi ostude arvu, kogukulutuse ja RFM-segmendi vahel.

Hajuvusdiagramm näitas selgelt, et VIP Champions kliendid paiknevad suurema ostusageduse ja kogukulutuse piirkonnas.

## Tulemuste kontrollimine

Kontrollisin analüüsi vahetulemusi järgmiste käskude ja meetoditega:

- `df.shape`
- `df.head()`
- `df.columns.tolist()`
- `df.dtypes`
- `df.isnull().sum()`
- `df.duplicated().sum()`
- `df.describe()`
- `value_counts()`
- segmentide kokkuvõttetabel
- segmentide klientide arvu kontroll
- segmentide kogukäibe kontroll

Kontrollisin ka, et:

- tabelite ühendamisel säilis 15 234 müügirida;
- RFM-andmetes ei olnud pärast puhastamist puuduvaid väärtusi;
- segmentide klientide arvude summa oli 2550;
- segmentide kogukäibe summa oli 4 022 754,49 €.

## Õpikohad

Selle töö käigus õppisin:

- kuidas luua Pythonis ühendus Supabase’iga;
- kuidas laadida rohkem kui 1000 rida sisaldavaid tabeleid lehekülgede kaupa;
- kuidas kasutada pandas DataFrame’e;
- kuidas kontrollida andmete struktuuri ja kvaliteeti;
- kuidas ühendada tabeleid `merge()` funktsiooniga;
- kuidas kasutada `groupby()` ja `agg()` funktsioone;
- kuidas teisendada tekstina salvestatud kuupäevi;
- kuidas arvutada RFM-näitajaid;
- kuidas kasutada `qcut()` funktsiooni skooride määramiseks;
- kuidas luua tingimusliku funktsiooniga kliendisegmente;
- kuidas visualiseerida tulemusi Plotly Expressiga;
- kuidas muuta tehniline analüüs juhtimisotsust toetavaks andmelooks.

## AI kasutamine

Kasutasin AI-d:

- Pythoni ja Jupyteri töökeskkonna seadistamisel;
- Supabase’i ühenduse loomisel;
- pandas `merge()` loogika kontrollimisel;
- RFM-arvutuse sammude koostamisel;
- `qcut()` ja skooride määramise selgitamisel;
- Plotly graafikute koostamisel;
- veateadete mõistmisel;
- README struktuuri ja sõnastuse kontrollimisel.

Kontrollisin AI abil loodud lahendused ise üle:

- käivitasin iga sammu eraldi;
- vaatasin üle vahetulemused;
- kontrollisin mõõtmeid ja puuduvaid väärtusi;
- võrdlesin segmentide loendusi;
- kontrollisin käibe summasid;
- hindasin, kas tulemused olid äriliselt loogilised.

## Failid

- `Nadal_7_Python_Pandas.ipynb` – täielik Jupyter Notebook koos koodi, tulemuste, tabelite, visualiseeringute ja järeldustega
- `README.md` – töö eesmärgi, meetodi, tulemuste ja soovituste kokkuvõte

## Kokkuvõte

Nädala 7 individuaalse töö tulemusena valmis terviklik Python ja pandas analüüs, mis ühendab andmete laadimise, puhastamise, RFM-arvutuse, kliendisegmenteerimise ja visualiseerimise.

Analüüs näitas, et UrbanStyle’i kõige väärtuslikumad kliendid on VIP Champions ja Loyal Customers. Koos annavad nad 74,11% analüüsitud kogukäibest.

Kõige suurem kasvuvõimalus on Potential Loyalists segment ning kõige kiiremat tähelepanu vajab At Risk segment.

RFM-analüüs võimaldab UrbanStyle’il loobuda kõigile klientidele sama pakkumise saatmisest ning kasutada erinevate kliendigruppide puhul sihipärasemat ja andmetel põhinevat lähenemist.
