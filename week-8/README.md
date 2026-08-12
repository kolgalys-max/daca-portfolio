# Week 8 – Python APIs ja automatiseeritud andmepipeline

## Individuaalne töö

### Eesmärk

Individuaalse töö eesmärk oli rakendada nädala jooksul õpitut automatiseeritud andmepipeline'i loomisel ning mõista, kuidas erinevad andmetöötluse etapid ühendatakse üheks terviklikuks protsessiks.

Töö keskendus Pythonis loodud pipeline'i käivitamisele, mis ühendab andmete pärimise, töötlemise, analüüsi, visualiseerimise ja tulemuste salvestamise.

## Töö kirjeldus

Individuaalse töö käigus kasutasin `pipeline.py` faili, mis juhib kogu andmetöötluse protsessi.

Pipeline ühendab järgmised etapid:

1. andmete pärimine;
2. andmete puhastamine ja transformatsioon;
3. KPI-de ja nädalapõhiste koondnäitajate arvutamine;
4. andmestike ühendamine;
5. visualiseeringute loomine;
6. tulemuste eksportimine;
7. protsessi käigu logimine ja vigade käsitlemine.

Pipeline käivitatakse ühe käsuga:

```bash
python pipeline.py
```

## Pipeline'i töövoog

```text
Andmete pärimine
      ↓
Andmete puhastamine ja transformatsioon
      ↓
KPI-de ja koondnäitajate arvutamine
      ↓
Andmestike ühendamine
      ↓
Visualiseeringute loomine
      ↓
Tulemuste eksport
```

`pipeline.py` kasutab eraldi moodulites olevaid funktsioone ning ühendab need üheks järjestikuseks tööprotsessiks.

## Automatiseerimine

Pipeline'i kasutamise peamine eelis on see, et erinevaid tööetappe ei pea eraldi käsitsi käivitama.

Ühe käivitusega toimub kogu protsess järjest:

- andmed loetakse sisse;
- andmed töödeldakse;
- arvutatakse vajalikud näitajad;
- luuakse visualiseeringud;
- tulemused eksporditakse;
- protsessi käik logitakse.

See muudab analüüsi korratavaks ning võimaldab sama protsessi uuesti käivitada värskendatud andmetega.

## Väljundid

Pipeline'i tulemusena luuakse analüüsi väljundid `output` kausta.

Töö käigus kasutatud pipeline loob muu hulgas:

- nädalapõhise müügitulu visualiseeringu;
- KPI-de kokkuvõtte;
- töödeldud andmefaili.

Pipeline mõõdab ka protsessi täitmise aega ning kuvab pärast edukat käivitamist töödeldud ridade arvu.

## Veakäsitlus ja logimine

Pipeline sisaldab protsessi jälgimiseks logimist.

Logides kuvatakse pipeline'i peamised etapid:

- andmete pärimine;
- andmete töötlemine;
- visualiseeringute loomine;
- tulemuste eksportimine;
- pipeline'i lõpetamine.

Kui protsessi käigus tekib viga, salvestatakse veateade logisse ning viga tõstetakse edasi. See aitab tuvastada, millises tööetapis probleem tekkis.

## Õpitulemus

Töö käigus sain praktilise ülevaate sellest, kuidas eraldi Pythonis loodud andmetöötluse moodulid ühendatakse üheks automatiseeritud pipeline'iks.

Olulisemad õppetunnid:

- pipeline võimaldab ühendada mitu andmetöötluse etappi üheks protsessiks;
- automatiseerimine vähendab käsitsi tehtavate sammude hulka;
- logimine aitab jälgida protsessi käiku ja leida vigu;
- väljundite automaatne loomine muudab analüüsi korratavaks;
- sama pipeline'i saab uuesti kasutada värskendatud andmetega.

## Failid

```text
week-8/
└── individual/
    ├── pipeline.py
    └── README.md
```

`pipeline.py` sisaldab automatiseeritud andmepipeline'i käivitamise loogikat ning `README.md` dokumenteerib individuaalse töö eesmärgi, töövoo ja õpitulemuse.
