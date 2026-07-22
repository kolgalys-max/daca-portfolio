# Week 5 – Visualiseerimise disain

## UrbanStyle müügidashboard Power BI-s

![UrbanStyle Week 5 dashboard](dashboard_screenshot.png)

## Projekti eesmärk

Nädala 5 eesmärk oli muuta UrbanStyle'i müügiandmed selgeks ja visuaalselt arusaadavaks dashboard'iks. Töö keskendus sobivate diagrammitüüpide valimisele, visuaalse müra vähendamisele ning tulemuste esitamisele viisil, mis võimaldab juhtkonnal olulisi mustreid kiiresti märgata.

## Äriküsimus

Kuidas esitada UrbanStyle'i müügiandmeid nii, et juhtkond saaks ühelt dashboard'ilt kiire ülevaate müügitulu muutumisest, müügikanalite tulemustest, linnade võrdlusest ja edukamatest toodetest?

## Kasutatud tööriistad

- Power BI Desktop
- PostgreSQL
- Supabase
- GitHub

## Andmeallikas

Power BI ühendati PostgreSQL-i ühenduse kaudu UrbanStyle'i Supabase'i andmebaasiga. Analüüsis kasutati peamiselt järgmisi tabeleid:

- `sales`
- `products`

Tabelite ühendamiseks kasutati toodete identifikaatorit `product_id`.

## Loodud visualiseeringud

Dashboard sisaldab nelja visualiseeringut:

1. **Müügitulu kuude kaupa** – joondiagramm müügitulu ajalise mustri esitamiseks.
2. **Müügitulu linnade kaupa** – tulpdiagramm Tallinna, Tartu ja Pärnu tulemuste võrdlemiseks.
3. **Müügitulu müügikanalite kaupa** – tulpdiagramm füüsilise poe ja veebikanali võrdlemiseks.
4. **Top 10 toodet müügitulu järgi** – horisontaalne tulpdiagramm suurima müügituluga toodete järjestamiseks.

## Peamised tulemused

### Müügitulu kuude kaupa

Müügitulu ei jagunenud kuude vahel ühtlaselt. Kõrgeim koondtulemus oli detsembris. Tugevamad olid ka juuni, juuli ja august, samal ajal kui märts, mai ja september jäid madalamale tasemele.

### Müügitulu linnade kaupa

Tallinn oli vaadeldud linnadest suurima müügituluga. Tartu tulemus oli sellest märgatavalt väiksem ning Pärnu müügitulu oli kolme linna võrdluses kõige madalam.

Puuduva `store_location` väärtusega kirjed eemaldati linnade diagrammist, sest neid ei saanud usaldusväärselt ühegi linna alla liigitada.

### Müügitulu müügikanalite kaupa

Füüsilise poe müügitulu oli **2 847 955,50 €** ja veebikanali müügitulu **1 526 275,77 €**. Kahe kanali kogutulu oli **4 374 231,27 €**.

Füüsiline pood moodustas ligikaudu kaks kolmandikku kogutulust ja veebikanal ligikaudu ühe kolmandiku. See näitab, et füüsiline kauplus oli analüüsitud andmetes peamine müügitulu allikas.

### Top 10 toodet

Suurima müügituluga toode oli **Trendikas goretex oxfordid**. Sellele järgnes **Õhuline sünteetiline sporditossud**. Top 10 visualiseering võimaldab kiiresti näha, millised tooted panustasid müügitulusse kõige rohkem.

## Disainiotsused

- Ajalise muutuse näitamiseks kasutati joondiagrammi.
- Linnade ja müügikanalite võrdlemiseks kasutati tulpdiagramme.
- Pikkade tootenimede tõttu kasutati Top 10 analüüsis horisontaalset tulpdiagrammi.
- Kõik visualiseeringud paigutati ühele lehele, et kogu ülevaade oleks nähtav ilma kerimiseta.
- Diagrammidel kasutati ühtset värvi ja eestikeelseid pealkirju.
- Tehnilised väljade nimetused asendati kasutajale arusaadavate teljenimetustega, näiteks `total_price` asemel **Müügitulu (€)**.
- Üleliigseid dekoratiivseid elemente ja 3D-efekte ei kasutatud.

## Äriline järeldus

UrbanStyle'i müügitulu sõltub tugevalt füüsilisest poest ja Tallinna müügist. Veebikanalil on oluline, kuid väiksem osakaal. Juhtkond võiks uurida, millised füüsilise poe tugevused oleks võimalik veebikanalisse üle kanda ning kuidas toetada müügi kasvu Tartus ja Pärnus.

Top 10 toodete tulemusi saab kasutada sortimendi, kampaaniate ja laovarude planeerimisel.

## AI kasutamine

Kasutasin ChatGPT-d Power BI ühenduse tõrke lahendamisel, visualiseeringute samm-sammulisel loomisel ning dashboard'i pealkirjade ja README sõnastuse kontrollimisel. Kontrollisin AI soovitusi Power BI-s tegelike andmete ja tulemuste põhjal.

## Õpikogemus

Töö käigus õppisin:

- ühendama Power BI Supabase PostgreSQL-i andmebaasiga;
- lahendama SSL-sertifikaadiga seotud ühendusprobleemi;
- valima äriküsimusele sobiva diagrammitüübi;
- looma Top N filtrit;
- eemaldama analüüsist puuduvad asukohaväärtused;
- kujundama ühe lehega dashboard'i;
- muutma tehnilised väljade nimetused kasutajale arusaadavaks;
- tõlgendama visualiseeringuid ärilisest vaatenurgast.

## Portfooliofailid

- `urbanstyle_week5_dashboard_liis.pbix`
- `dashboard_screenshot.png`

## Seos meeskonnatööga

Individuaalne dashboard on minu Nädal 5 portfoolioartefakt. Meeskonnatöö käigus koondatakse liikmete erinevad stakeholder'i vaated ühiseks UrbanStyle'i ülevaateks.

<!-- Lisa siia hiljem tiimi ühise töö link:
[UrbanStyle Team 3 ühine töö](LISA_LINK_SIIA)
-->
