# Week 7 – Python ja Pandas

## UrbanStyle’i klientide RFM-analüüs

## Projekti eesmärk

Selle nädala eesmärk oli kasutada Pythonit ja pandas teeki UrbanStyle’i kliendi- ja müügiandmete analüüsimiseks.

Minu individuaalse töö põhifookus oli RFM-kliendisegmenteerimine, mille abil selgitasin välja:

- kes on ettevõtte kõige väärtuslikumad kliendid;
- millised kliendid on lojaalsed;
- millistel klientidel on potentsiaal muutuda lojaalsemaks;
- millised kliendid on ostmise lõpetamise ohus;
- millistele segmentidele tuleks suunata erinevaid turundustegevusi.

## Äriküsimus

**Kes on UrbanStyle’i VIP-kliendid, kui palju nad kulutavad ning millised kliendid vajavad ostuaktiivsuse languse tõttu tähelepanu?**

## Kasutatud tööriistad

- Python
- pandas
- Plotly Express
- Jupyter Notebook
- Supabase
- GitHub

## Kasutatud andmed

Andmed laadisin Pythonisse UrbanStyle’i Supabase’i andmebaasist.

Kasutasin järgmisi tabeleid:

| Tabel | Ridade arv | Veergude arv |
|---|---:|---:|
| `sales` | 15 234 | 12 |
| `customers` | 3150 | 9 |
| `products` | 362 | 9 |

Tabelid ühendasin pandas `merge()` funktsiooniga:

- `sales` ja `customers` ühendati veeru `customer_id` kaudu;
- müügi- ja tooteandmed ühendati veeru `product_id` kaudu.

Ühendamisel kasutasin vasakühendust ehk `how="left"`, et kõik müügikirjed säiliksid.

Ühendatud DataFrame sisaldas algselt:

- **15 234 rida**
- **28 veergu**

## Tehtud töö

Analüüsi käigus:

1. lõin ühenduse Supabase’i andmebaasiga;
2. laadisin tabelid pandas DataFrame’idesse;
3. kontrollisin tabelite mõõtmeid ja andmetüüpe;
4. ühendasin müügi-, kliendi- ja tooteandmed;
5. kontrollisin puuduvaid väärtusi;
6. kontrollisin täielikke duplikaate;
7. kontrollisin duplikaate `invoice_id` järgi;
8. eemaldasin korduvad arved;
9. valmistasin andmed ette RFM-analüüsiks;
10. arvutasin Recency, Frequency ja Monetary näitajad;
11. määrasin klientidele RFM-skoorid;
12. jagasin kliendid segmentidesse;
13. koostasin segmentide kokkuvõtte;
14. visualiseerisin tulemused Plotly abil;
15. sõnastasin ärilised järeldused ja soovitused.

## Andmete kvaliteedi kontroll

Enne analüüsi kontrollisin:

- DataFrame’i mõõtmeid;
- veergude nimesid;
- andmetüüpe;
- puuduvaid väärtusi;
- täielikult dubleerivaid ridu;
- korduvaid `invoice_id` väärtusi;
- `total_price` väärtuste vahemikku.

Esialgse kontrolli tulemused:

- `customer_id` puudus **1487 müügireal**;
- `store_location` puudus **5204 real**;
- `loyalty_tier` puudus **7033 real**;
- `eco_certified` puudus **829 real**;
- väikseim `total_price` väärtus oli **−1405,32 €**;
- suurim `total_price` väärtus oli **2170,40 €**.

Täielikult identsete ridade kontroll:

```python
df.duplicated().sum()
```

näitas **0 duplikaati**.

See kontroll ei olnud siiski piisav, sest sama arvega kirjed ei pruukinud olla kõikides veergudes täielikult identsed.

Seetõttu kontrollisin duplikaate ärilise võtme ehk `invoice_id` järgi:

```python
df.duplicated(subset="invoice_id").sum()
```

Tulemus:

- **5116 korduvat `invoice_id` kirjet**

Duplikaadid eemaldasin järgmise koodiga:

```python
df = df.drop_duplicates(
    subset="invoice_id",
    keep="first"
)
```

Pärast dedupeerimist jäi DataFrame’i:

- **10 118 rida**
- **28 veergu**

## RFM-andmete ettevalmistamine

RFM-analüüsi jaoks kasutasin järgmisi veerge:

- `customer_id`
- `sale_date`
- `total_price`

Puhastamise käigus:

- teisendasin `sale_date` veeru kuupäevatüübiks;
- eemaldasin read, kus puudus `customer_id`;
- eemaldasin read, kus puudus või oli vigane `sale_date`;
- eemaldasin read, kus puudus `total_price`;
- jätsin alles ainult positiivse väärtusega tehingud;
- teisendasin `customer_id` väärtused täisarvuks.

Pärast puhastamist jäi RFM-analüüsi:

- **8950 müügikirjet**
- **3 vajalikku veergu**
- **0 puuduvat väärtust**

Negatiivsed ja nullväärtusega tehingud jätsin RFM-analüüsist välja, et tagastused või paranduskanded ei vähendaks kliendi positiivset ostumahtu.

## RFM-meetod

RFM-analüüs hindab klienti kolme näitaja põhjal:

- **Recency** – mitu päeva on möödunud kliendi viimasest ostust;
- **Frequency** – mitu ostu klient on teinud;
- **Monetary** – kui palju klient on kokku kulutanud.

Analüüsi viitekuupäevaks määrasin andmestikus oleva viimase ostukuupäeva järgmise päeva.

**Analüüsi kuupäev: 29.06.2026**

Iga kliendi kohta arvutasin:

```text
Recency = analüüsi kuupäev − kliendi viimane ostukuupäev
Frequency = kliendi ostude arv
Monetary = kliendi tehingute kogusumma
```

RFM-tabelisse jõudis kokku:

- **2540 klienti**

## RFM-skooride arvutamine

Iga RFM-näitaja jagasin kvintiilide alusel viide gruppi.

Klientidele määrati skoorid vahemikus 1–5.

### Recency skoor

Recency skoor on vastupidine:

- skoor **5** – klient ostis suhteliselt hiljuti;
- skoor **1** – kliendi viimasest ostust on möödunud palju aega.

### Frequency skoor

- skoor **5** – klient ostab sageli;
- skoor **1** – klient on ostnud harva.

### Monetary skoor

- skoor **5** – klient on kulutanud palju;
- skoor **1** – klient on kulutanud vähe.

RFM-koguskoor arvutati valemiga:

```text
RFM-skoor = R-skoor + F-skoor + M-skoor
```

Skooride kontroll:

| Skoor | Miinimum | Maksimum |
|---|---:|---:|
| R-skoor | 1 | 5 |
| F-skoor | 1 | 5 |
| M-skoor | 1 | 5 |
| RFM-koguskoor | 3 | 15 |

## Kliendisegmendid

Kliendid jagasin RFM-koguskoori järgi viide segmenti:

| RFM-skoor | Segment | Kirjeldus |
|---:|---|---|
| 13–15 | VIP Champions | kõige väärtuslikumad ja aktiivsemad kliendid |
| 10–12 | Loyal Customers | regulaarsed ja lojaalsed kliendid |
| 7–9 | Potential Loyalists | hea kasvupotentsiaaliga kliendid |
| 4–6 | At Risk | vähenenud ostuaktiivsusega kliendid |
| 3 | Lost | kaua mitteaktiivsed ja väikese väärtusega kliendid |

## Segmentide jaotus

| Segment | Klientide arv | Osakaal klientidest |
|---|---:|---:|
| Potential Loyalists | 759 | 29,88% |
| Loyal Customers | 679 | 26,73% |
| At Risk | 529 | 20,83% |
| VIP Champions | 455 | 17,91% |
| Lost | 118 | 4,65% |
| **Kokku** | **2540** | **100%** |

Kõige suurem segment oli **Potential Loyalists**, kuhu kuulus 759 klienti.

## Segmentide tulemused

| Segment | Kliente | Keskmine Recency | Keskmine Frequency | Keskmine Monetary | Kogukäive |
|---|---:|---:|---:|---:|---:|
| VIP Champions | 455 | 534,66 päeva | 7,68 | 2519,33 € | 1 146 295,15 € |
| Loyal Customers | 679 | 631,29 päeva | 3,84 | 1172,84 € | 796 357,18 € |
| Potential Loyalists | 759 | 693,49 päeva | 2,49 | 687,47 € | 521 792,88 € |
| At Risk | 529 | 795,57 päeva | 1,59 | 363,27 € | 192 170,22 € |
| Lost | 118 | 1002,88 päeva | 1,01 | 171,48 € | 20 235,11 € |
| **Kokku** | **2540** |  |  |  | **2 676 850,54 €** |

## Käibe jaotus segmentide vahel

| Segment | Kogukäive | Osakaal analüüsitud käibest |
|---|---:|---:|
| VIP Champions | 1 146 295,15 € | 42,82% |
| Loyal Customers | 796 357,18 € | 29,75% |
| Potential Loyalists | 521 792,88 € | 19,49% |
| At Risk | 192 170,22 € | 7,18% |
| Lost | 20 235,11 € | 0,76% |
| **Kokku** | **2 676 850,54 €** | **100%** |

VIP Champions ja Loyal Customers moodustasid kokku:

- **44,64% analüüsitud klientidest**
- **72,57% analüüsitud kogukäibest**

See tähendab, et ligi kolmveerand analüüsitud käibest tuli ettevõtte aktiivsetelt ja lojaalsetelt klientidelt.

## Peamised leiud

### VIP Champions

VIP Champions segmenti kuulus:

- **455 klienti**
- **17,91% klientidest**

VIP-kliendid:

- tegid keskmiselt 7,68 ostu;
- kulutasid keskmiselt 2519,33 € kliendi kohta;
- tõid kokku 1 146 295,15 € käivet;
- moodustasid 42,82% analüüsitud käibest.

VIP Champions on kõige väärtuslikum kliendisegment.

### Loyal Customers

Loyal Customers segmenti kuulus:

- **679 klienti**
- **26,73% klientidest**

Nende:

- keskmine ostude arv oli 3,84;
- keskmine kogukulu oli 1172,84 €;
- kogukäive oli 796 357,18 €;
- käibe osakaal oli 29,75%.

Koos VIP Champions segmendiga andsid nad 72,57% analüüsitud kogukäibest.

### Potential Loyalists

Potential Loyalists oli suurim segment:

- **759 klienti**
- **29,88% klientidest**

Nende:

- keskmine ostude arv oli 2,49;
- keskmine kogukulu oli 687,47 €;
- kogukäive oli 521 792,88 €.

See segment kujutab endast ettevõtte suurimat kasvuvõimalust, sest osa klientidest võib sobivate pakkumiste abil liikuda lojaalsete või VIP-klientide hulka.

### At Risk

At Risk segmenti kuulus:

- **529 klienti**
- **20,83% klientidest**

Nende:

- viimasest ostust oli möödunud keskmiselt 795,57 päeva;
- keskmine ostude arv oli 1,59;
- keskmine kogukulu oli 363,27 €;
- kogukäive oli 192 170,22 €.

Need kliendid vajavad tagasivõitmise kampaaniat, sest nende ostuaktiivsus on vähenenud.

### Lost

Lost segmenti kuulus:

- **118 klienti**
- **4,65% klientidest**

Nende:

- viimasest ostust oli möödunud keskmiselt 1002,88 päeva;
- keskmine ostude arv oli 1,01;
- keskmine kogukulu oli 171,48 €;
- kogukäive oli 20 235,11 €;
- käibe osakaal oli ainult 0,76%.

Selle segmendi tagasivõitmiseks ei ole mõistlik kasutada kulukaid personaalseid kampaaniaid enne võimaliku tasuvuse hindamist.

## Soovitused Markole

### VIP Champions

VIP-klientidele soovitan pakkuda:

- personaalset teenindust;
- varajast ligipääsu uutele toodetele;
- eksklusiivseid soodustusi;
- VIP-programmi;
- ostuajalool põhinevaid tootesoovitusi.

Eesmärk on säilitada kõige väärtuslikumate klientide lojaalsus.

### Loyal Customers

Lojaalsetele klientidele sobivad:

- lojaalsusprogramm;
- punktisüsteem;
- kordusostu soodustused;
- personaalsed pakkumised;
- soovitusprogrammid.

Eesmärk on suurendada nende ostusagedust ja aidata osal klientidest liikuda VIP Champions segmenti.

### Potential Loyalists

Potential Loyalists segmendile soovitan:

- tasuta tarnet;
- järgmise ostu boonust;
- piiratud kehtivusega sooduskoodi;
- seotud toodete soovitusi;
- personaliseeritud e-kirju.

See segment on arvuliselt kõige suurem ja pakub seetõttu olulist kasvuvõimalust.

### At Risk

At Risk klientidele sobivad:

- „Me igatseme sind” kampaania;
- personaalne tagasitulekupakkumine;
- viimase ostuga seotud tootesoovitused;
- piiratud kehtivusega soodustus;
- lühike tagasisideküsimustik.

See segment vajab kiiret tähelepanu, sest kliendid ei ole veel täielikult kadunud.

### Lost

Lost segmendile sobib esmalt odavam automatiseeritud kampaania.

Suuremat allahindlust või personaalset teenindust tuleks kasutada ainult siis, kui kliendi varasem väärtus õigustab kampaania maksumust.

## Juhtimissoovitus

UrbanStyle ei peaks saatma kõigile klientidele ühesuguseid pakkumisi.

Esimene prioriteet on hoida **VIP Champions** ja **Loyal Customers** kliente, sest nad annavad kokku 72,57% analüüsitud käibest.

Kasvu seisukohalt on kõige olulisem **Potential Loyalists**, sest see on 759 kliendiga kõige suurem segment.

Kiiret tähelepanu vajab **At Risk**, kus on 529 vähenenud aktiivsusega klienti.

**Lost** segmendi puhul tuleb enne suurema turunduskulu tegemist hinnata kampaania tasuvust.

## Visualiseeringud

Koostasin Plotly Expressi abil kolm interaktiivset visualiseeringut:

1. **Klientide arv segmentide kaupa**  
   Näitab, kui palju kliente kuulub igasse RFM-segmenti.

2. **Kliendisegmentide kogukäive**  
   Näitab, millised segmendid annavad ettevõttele kõige suurema rahalise väärtuse.

3. **Ostusageduse ja kogukulu hajuvusdiagramm**  
   Näitab seost kliendi ostusageduse, kogukulutuse ja RFM-segmendi vahel.

Visualiseeringud käivitasin pärast `invoice_id` järgi duplikaatide eemaldamist uuesti, et need põhineksid parandatud andmetel.

## Tulemuste kontrollimine

Kontrollisin analüüsi järgmiste pandas käskude ja meetoditega:

- `df.shape`
- `df.head()`
- `df.columns.tolist()`
- `df.dtypes`
- `df.isnull().sum()`
- `df.duplicated().sum()`
- `df.duplicated(subset="invoice_id").sum()`
- `df.drop_duplicates(subset="invoice_id")`
- `df.describe()`
- `value_counts()`
- `groupby()`
- `agg()`
- segmentide kokkuvõttetabel
- klientide kontrollsumma
- kogukäibe kontrollsumma

Kontrolli tulemused:

- esialgne müügiridade arv oli **15 234**;
- `invoice_id` järgi leiti **5116 korduvat kirjet**;
- pärast dedupeerimist jäi **10 118 müügirida**;
- RFM-andmetesse jäi **8950 müügikirjet**;
- RFM-andmetes oli **0 puuduvat väärtust**;
- RFM-tabelisse jõudis **2540 klienti**;
- kõik kliendid said segmendi;
- segmentide klientide summa oli **2540**;
- segmentide kogukäibe summa oli **2 676 850,54 €**;
- R-, F- ja M-skoorid jäid vahemikku **1–5**;
- RFM-koguskoor jäi vahemikku **3–15**.

## Analüüsi piirangud

Analüüsi tulemuste tõlgendamisel tuleb arvestada, et:

- RFM-analüüsi kaasati ainult positiivse väärtusega tehingud;
- tagastusi ja paranduskandeid ei analüüsitud eraldi;
- `Frequency` näitab analüüsi kaasatud müügikirjete arvu;
- kliendid, kelle müügiridadel puudus `customer_id`, jäid RFM-analüüsist välja;
- segmendid moodustati andmestiku siseste kvintiilide alusel;
- kõrge Recency väärtus näitab, et andmestiku ostud ei ole väga hiljutised;
- tulemused kirjeldavad analüüsitud andmestikku ega pruugi täielikult kajastada ettevõtte praegust kliendibaasi.

## Õpikohad

Selle töö käigus õppisin:

- laadima andmeid Supabase’ist pandas DataFrame’i;
- ühendama tabeleid `merge()` funktsiooniga;
- kontrollima DataFrame’i struktuuri ja andmekvaliteeti;
- eristama täielikke duplikaate ärilise võtme duplikaatidest;
- puhastama puuduvaid ja vigaseid väärtusi;
- teisendama kuupäevi `datetime` andmetüübiks;
- kasutama `groupby()` ja `agg()` funktsioone;
- arvutama Recency, Frequency ja Monetary näitajaid;
- kasutama `pd.qcut()` funktsiooni;
- looma kliendisegmente;
- kontrollima koondtulemuste õigsust;
- visualiseerima tulemusi Plotly Expressiga;
- muutma tehnilise analüüsi ärilisteks järeldusteks.

## AI kasutamine

Kasutasin AI-d:

- Pythoni ja Jupyter Notebooki seadistamisel;
- Supabase’i ühenduse loomisel;
- pandas koodi koostamisel ja kontrollimisel;
- `merge()`, `groupby()`, `agg()` ja `qcut()` funktsioonide mõistmisel;
- veateadete selgitamisel;
- RFM-loogika kontrollimisel;
- Plotly visualiseeringute koostamisel;
- README struktuuri ja sõnastuse parandamisel.

Kontrollisin AI abil koostatud koodi ise, käivitades kõik lahtrid ning võrreldes ridade arve, puuduvaid väärtusi, segmentide tulemusi ja kogusummasid.

## Failid

- `Nadal_7_Python_Pandas.ipynb` – Jupyter Notebook koos koodi, tulemuste ja visualiseeringutega
- `README.md` – individuaalse töö eesmärgi, meetodi, tulemuste ja soovituste kokkuvõte

## Kokkuvõte

Nädala 7 individuaalse töö tulemusena valmis Pythonis ja pandas teegiga UrbanStyle’i klientide RFM-analüüs.

Pärast `invoice_id` järgi duplikaatide eemaldamist jäi analüüsi 8950 müügikirjet ja 2540 klienti.

Kõige väärtuslikum segment oli **VIP Champions**, kuhu kuulus 455 klienti. Nad moodustasid 17,91% klientidest, kuid andsid 42,82% analüüsitud käibest.

VIP Champions ja Loyal Customers moodustasid kokku 44,64% klientidest ning andsid 72,57% kogukäibest.

Kõige suurem kasvuvõimalus oli **Potential Loyalists**, kuhu kuulus 759 klienti.

Kõige kiiremat tähelepanu vajab **At Risk** segment, kuhu kuulus 529 klienti.

RFM-analüüsi põhjal saab UrbanStyle kasutada erinevate kliendisegmentide jaoks sihipärasemaid pakkumisi ja turunduskampaaniaid.
