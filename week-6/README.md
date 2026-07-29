# Nädal 6 – Andmelugu ja dashboard'i viimistlemine

## Projekti eesmärk

Selle nädala eesmärk oli täiendada Nädal 5 jooksul loodud Power BI dashboard'i ning muuta see selgemaks, professionaalsemaks ja juhtidele sobivamaks.

Dashboard'i viimistlemisel keskendusin andmeloo loomisele, visuaalide ühtsele kujundusele, juhtide kokkuvõttele, mobiilivaatele ja dashboard'i avaldamisele Power BI Service'is.

## Äriküsimus

Kuidas muuta UrbanStyle'i müügiandmete dashboard selliseks, et juht saaks kiiresti ülevaate:

- ettevõtte kogu müügitulust;
- müügitulu muutusest aastate lõikes;
- müügitulu jaotusest müügikohtade vahel;
- enim müügitulu toonud toodetest;
- tulemustest valitud aasta lõikes?

## Kasutatud tööriistad

- Power BI Desktop
- Power BI Service
- Supabase
- PostgreSQL
- GitHub

## Minu töö

Kasutasin Nädal 5 jooksul loodud Power BI dashboard'i ning täiendasin seda järgmiste tegevustega:

- korrastasin dashboard'i visuaalide paigutuse;
- ühtlustasin diagrammide värvid;
- kasutasin UrbanStyle'i põhivärvina teal-tooni `#009B8D`;
- kasutasin müügikohtade eristamiseks navy-tooni `#1A1A2E` ja toetavaid värve;
- muutsin diagrammide väljade ja kohtspikrite nimetused eestikeelseks;
- lisasin müügitrendi diagrammile horisontaalse viitejoone;
- lisasin dashboard'i ülaossa juhtide kokkuvõtte;
- kontrollisin visuaalide omavahelisi interaktsioone;
- seadistasin KPI-kaardi näitama kogu perioodi müügitulu;
- säilitasin diagrammide ristuva filtreerimise ja esiletõstmise;
- koostasin mobiilivaate;
- avaldasin dashboard'i Power BI Service'is;
- kontrollisin avaldatud dashboard'i toimimist;
- eksportisin dashboard'i PDF-failina;
- salvestasin dashboard'i ekraanipildi GitHubi portfoolio jaoks.

## Dashboard'i sisu

Dashboard sisaldab järgmisi elemente:

1. **Juhtide kokkuvõte** – peamine leid, tõendus ja soovitus.
2. **Müügitulu KPI-kaart** – kogu perioodi müügitulu.
3. **Müügitulu trend aastate lõikes** – müügitulu muutus aastatel 2023–2026.
4. **Müügi jaotus müügikoha järgi** – Tallinna, online-müügi, Tartu ja Pärnu osakaal.
5. **TOP 5 toodet** – enim müügitulu toonud tooted.
6. **Aasta filter** – võimaldab vaadata müügikohtade ja toodete tulemusi valitud aasta lõikes.

## Peamised tulemused

- Kogu perioodi müügitulu oli **2,91 mln €**.
- Kõrgeim aastane müügitulu saavutati **2024. aastal**.
- 2024. aasta müügitulu oli ligikaudu **1,47 mln €**.
- Tallinn moodustas kogu perioodi müügitulust **37,18%**.
- Online-müük moodustas kogu perioodi müügitulust **34,89%**.
- Tallinn ja online-müük andsid kokku ligikaudu **72% kogu müügitulust**.
- Aasta filter võimaldab võrrelda müügikohtade ja TOP 5 toodete tulemusi valitud aasta lõikes.
- 2025. ja 2026. aasta andmete täielikkust tuleb enne müügitulu muutuse põhjuste hindamist täiendavalt kontrollida.

## Juhtide kokkuvõte

**Peamine leid:** UrbanStyle'i müügitulu oli kogu perioodil 2,91 mln € ning kõrgeim aastane tulemus saavutati 2024. aastal.

**Tõendus:** Tallinn moodustas müügitulust 37,18% ja online-müük 34,89% ehk kokku ligikaudu 72%.

**Soovitus:** Kontrollida 2025. ja 2026. aasta andmete täielikkust ning seejärel analüüsida müügitulu muutuse põhjuseid.

## Disainiotsused

Dashboard'i kujundamisel lähtusin selgusest, loetavusest ja ühtsest visuaalsest stiilist.

- Kasutasin valget tausta.
- Kasutasin põhivärvina teal-tooni `#009B8D`.
- Müügikohtade eristamiseks kasutasin navy-tooni `#1A1A2E` ja toetavaid värve.
- Paigutasin juhtide kokkuvõtte dashboard'i ülaossa.
- Paigutasin kogu müügitulu KPI-kaardi hästi nähtavale kohale.
- Hoidsin graafikute pealkirjad ja telgede nimetused eestikeelsed.
- Vältisin staatilisi selgitusi, mis võiksid aasta filtri kasutamisel muutuda ebatäpseks.
- Säilitasin Power BI ristuva esiletõstmise, et kasutaja näeks valitud müügikoha mõju teistele visuaalidele.
- Kohandasin dashboard'i ka mobiilivaate jaoks.

## Dashboard'i andmelugu

### Taust

UrbanStyle vajab ühte ülevaadet, kust juht saab kiiresti näha ettevõtte müügitulu, müügikohtade osakaalu ja enim müügitulu toonud tooteid.

### Probleem

Üksikud graafikud näitavad numbreid, kuid ilma kokkuvõtte ja selge visuaalse ülesehituseta ei pruugi vaataja mõista, millised tulemused on kõige olulisemad.

### Andmed

Dashboard näitab kogu perioodi müügitulu, müügitulu muutust aastate lõikes, müügikohtade osakaalu ning TOP 5 tooteid.

### Järeldus

UrbanStyle'i kogu perioodi müügitulu oli 2,91 mln €. Kõrgeim aastane tulemus saavutati 2024. aastal ning suurima osa müügitulust andsid Tallinn ja online-müük.

### Tegevus

Enne 2025. ja 2026. aasta tulemuste põhjal lõplike järelduste tegemist tuleb kontrollida nende aastate andmete täielikkust.

## Mobiilivaade

Dashboard'ile koostasin eraldi mobiilivaate.

Mobiilivaates paigutasin elemendid järgmises järjekorras:

1. juhtide kokkuvõte;
2. kogu müügitulu KPI-kaart;
3. müügitulu trend;
4. müügikohtade jaotus;
5. TOP 5 toodet;
6. aasta filter.

Selline paigutus võimaldab vaadata dashboard'i loogilises järjekorras ka väiksemal ekraanil.

## Avaldamine

Dashboard avaldati Power BI Service'is.

Avaldatud versioonis kontrollisin:

- aasta filtri toimimist;
- diagrammide omavahelist filtreerimist;
- ristuvat esiletõstmist;
- KPI-kaardi väärtust;
- mobiilivaadet;
- dashboard'i üldist loetavust.

## Dashboard'i ekraanipilt

![UrbanStyle Power BI dashboard](images/urbanstyle_dashboard_screenshot.png)

## Live-demo

[Power BI dashboard'i avamine](LISA-SIIA-POWER-BI-LINK)

## Failid

- Power BI `.pbix` fail
- dashboard'i PDF-eksport
- dashboard'i ekraanipilt
- README dokumentatsioon

## Kokkuvõte

Nädal 6 jooksul muutsin Nädal 5 Power BI prototüübi viimistletud ja avaldatud dashboard'iks.

Töö tulemusena valmis dashboard, mis:

- annab kiire ülevaate peamistest müügitulemustest;
- sisaldab juhtidele mõeldud kokkuvõtet;
- kasutab ühtset UrbanStyle'i visuaalset stiili;
- võimaldab tulemusi aasta lõikes filtreerida;
- töötab nii arvuti- kui ka mobiilivaates;
- on avaldatud Power BI Service'is;
- sobib GitHubi portfoolios esitamiseks.
