# Week 8 – Python API-d ja automatiseerimine

## Eesmärk

Nädala 8 eesmärk oli õppida kasutama Pythonit ja Supabase API-t automatiseeritud andmetöötluses ning ühendada andmete pärimine, töötlemine, analüüs ja visualiseerimine üheks terviklikuks pipeline'iks.

Varasemalt kasutatud staatiliste CSV-failide asemel võimaldab API pärida andmed otse andmebaasist ning sama analüüsiprotsessi uuesti käivitada värskendatud andmetega.

## Minu alaülesanne

Minu ülesanne oli automatiseerimise skripti ehk `pipeline.py` loomine ja pipeline'i erinevate etappide ühendamine.

`pipeline.py` ülesanne on juhtida kogu protsessi ning käivitada vajalikud etapid õiges järjekorras:

1. andmete pärimine Supabase API-st;
2. andmete puhastamine ja transformeerimine;
3. KPI-de arvutamine;
4. vajalike andmete ühendamine;
5. visualiseeringute loomine;
6. tulemuste salvestamine;
7. protsessi käigu logimine ja vigade käsitlemine.

Pipeline käivitatakse ühe käsuga: `python pipeline.py`.

## Minu artefakt

Minu individuaalne artefakt on:

`individual/pipeline.py`

Skript ühendab meeskonnatöö käigus loodud eraldi moodulid üheks automatiseeritud töövooks.

Pipeline'i üldine loogika:

**Supabase API → andmete pärimine → transformatsioon → analüüs → visualiseerimine → väljundfailid**

## Tulemus

Pipeline'i testimisel käivitus protsess algusest lõpuni edukalt.

Eduka käivitamise tulemusena luuakse automaatselt analüüsi väljundid, sealhulgas:

- nädalapõhise tulu visualiseering;
- KPI-de visualiseering;
- RFM-andmestik CSV-formaadis.

Pipeline võimaldab sama analüüsi uuesti käivitada ilma, et kõiki töötlusetappe peaks käsitsi eraldi kordama.

## Meeskonna tulemus

Meeskonnatöö tulemusena valmis modulaarne automatiseeritud pipeline, mis:

- pärib andmed UrbanStyle Supabase API-st;
- töötleb andmed pandas abil;
- arvutab analüüsiks vajalikud näitajad;
- loob visualiseeringud;
- salvestab tulemused väljundfailidesse;
- ühendab erinevad tööetapid üheks käivitatavaks protsessiks.

Pipeline'i toimimist kontrolliti tervikuna käsuga `python pipeline.py`.

Meeskonna ühise töö dokumentatsioon:

`team/week8_pipeline_demo.md`

## Mida õppisin

Selle nädala töö käigus õppisin, kuidas eraldi Python-moodulid üheks terviklikuks andmepipeline'iks ühendada.

Sain paremini aru, et automatiseeritud analüüsi puhul ei piisa ainult sellest, et erinevad koodiosad eraldi töötavad. Oluline on ka nende omavaheline sobivus, õige käivitamise järjekord, veakäsitlus ning kontroll, et kogu protsess töötaks algusest lõpuni.

API kasutamine võimaldab vähendada käsitsi failide laadimist ning kasutada analüüsis värskemaid andmeid kui staatiliste CSV-failide puhul.

## Refleksioon

### Kuidas API parandab töövoogu võrreldes CSV-failidega?

API võimaldab andmeid pärida otse andmeallikast. CSV-faili puhul tuleb fail eraldi alla laadida ja analüüsi jaoks avada, kuid API abil saab andmete pärimise lisada otse automatiseeritud pipeline'i.

### Milline pipeline'i etapp oli kõige keerulisem ühendada?

Kõige rohkem tähelepanu nõudis erinevate moodulite ühendamine üheks terviklikuks protsessiks. Moodulite sisendid ja väljundid peavad omavahel sobima ning pipeline peab käivitama kõik etapid õiges järjekorras.

### Kuidas veakäsitlus muudab koodi tootmisvalmimaks?

Veakäsitlus võimaldab tuvastada, millises pipeline'i etapis probleem tekkis, ning väldib olukorda, kus protsess ebaõnnestub ilma arusaadava veateateta.

### Mida tahaksin automatiseerida järgmises projektis?

Järgmises projektis tahaksin automatiseerida regulaarse andmeanalüüsi nii, et andmed päringutest kuni valmis raporti või visualiseeringuni uueneksid võimalikult vähese käsitsi sekkumisega.

## AI kasutamine

Kasutasin AI-d pipeline'i loogika kontrollimiseks, vigade põhjuste leidmiseks ning dokumentatsiooni struktureerimise toetamiseks. AI aitas mõista, kuidas eraldi moodulid terviklikuks automatiseeritud töövooks ühendada.

## Kokkuvõte

Nädala 8 tulemusena õppisin, kuidas muuta mitmest eraldi etapist koosnev andmeanalüüs automatiseeritud ja korratavaks protsessiks.

Minu individuaalne artefakt `pipeline.py` ühendab pipeline'i erinevad etapid ning võimaldab kogu protsessi käivitada ühe käsuga.

Töö tulemusena sain praktilise kogemuse Python-moodulite integreerimisest, API-põhisest andmetöötlusest, veakäsitlusest ja analüüsiprotsessi automatiseerimisest.
