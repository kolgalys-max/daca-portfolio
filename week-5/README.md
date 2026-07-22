# Week 5 – Visualiseerimise disain

## Roll A – CEO Dashboard (Kristi vaade)

### Eesmärk

Minu ülesanne oli luua CEO vaade, mis annab kiire ülevaate UrbanStyle ettevõtte olukorrast ja aitab hinnata, kas ettevõte kasvab.

Dashboard keskendub kõrgtaseme KPI-dele:
- müügitulu;
- klientide arv;
- keskmine tellimuse väärtus;
- müügitulu trend ajas.

## Kasutatud andmed

Dashboardi koostamisel kasutasin UrbanStyle müügiandmeid.

Peamised kasutatud väljad:
- `total_price` – müügitulu arvutamiseks;
- `customer_id` – klientide arvu leidmiseks;
- `sale_date` – müügitrendi kuvamiseks.

## Loodud visualiseeringud

### KPI kaardid

Dashboard sisaldab järgmisi mõõdikuid:

- Kogu müügitulu: 2,91 mln €
- Klientide arv: 2552 unikaalset klienti
- Keskmine tellimuse väärtus: 287,53 €

### Müügitulu trend

Loodud joondiagramm näitab UrbanStyle müügitulu muutust aastate lõikes.

Visualiseering aitab hinnata ettevõtte müügikasvu ja perioodide erinevusi.

## Äritõlgendus

Dashboard näitab ettevõtte üldist müügitulu taset, klientide arvu ja keskmist tellimuse väärtust. 
Müügitulu trend annab CEO-le kiire ülevaate ettevõtte arengust ning aitab hinnata, kas müük liigub kasvavas suunas.

## Tööriist

- Power BI Desktop
- Supabase PostgreSQL andmebaas

## AI kasutamine

AI-d kasutati tööprotsessi toetamiseks visualiseerimise valikul, dashboardi struktuuri kontrollimisel ning tulemuste sõnastamisel.

## Failid

- `urbanstyle_week5_dashboard_Liis.pbix`
- `urbanstyle_week5_dashboard_screenshot.png`
