# Nädal 4 – SQL Aggregation

## Projekti eesmärk

Selle nädala eesmärk oli õppida kasutama SQL agregeerimisfunktsioone ja aknafunktsioone (Window Functions), et analüüsida UrbanStyle müügiandmeid ning leida äriliste otsuste tegemiseks olulisi näitajaid.

## Äriküsimus

Milliseid trende ja mustreid on võimalik müügiandmetest leida ning kuidas saab agregeeritud andmeid kasutada ettevõtte äriotsuste toetamiseks?

## Minu ülesanne

Kasutasin SQL agregeerimisfunktsioone ja aknafunktsioone, et analüüsida müügitulemusi erinevate perioodide, linnade ja tootekategooriate lõikes.

Teostasin järgmised tegevused:

- analüüsisin müüke kuude lõikes;
- arvutasin kogukäibe, keskmise tellimuse väärtuse ja tellimuste arvu;
- võrdlesin müügitulemusi linnade ja tootekategooriate kaupa;
- kasutasin funktsioone `COUNT()`, `SUM()`, `AVG()`, `GROUP BY` ja `HAVING`;
- kasutasin aknafunktsioone `LAG()`, `RANK()` ja liikuvat keskmist (`AVG() OVER`);
- kasutasin CTE-d (`WITH`) keerukamate päringute koostamiseks.

## Tulemused

Analüüsi käigus selgus, et:

- 2024. aasta suurim kuine käive oli **170 623,28 €** (detsember 2024);
- 2024. aasta väikseim kuine käive oli **85 618,65 €** (jaanuar 2024);
- suurim kuine kasv võrreldes eelmise kuuga oli **30 221,25 €** (juuni 2023);
- suurim kuine langus oli **−43 485,94 €** (jaanuar 2024);
- suurima kogukäibega linn oli **Tallinn**, mille kogukäive oli **1 006 252,88 €**;
- suurima käibega tootekategooria oli **jalanõud**, mis moodustas **26,61%** kogukäibest;
- kaks suurimat kategooriat (jalanõud ja meeste riided) moodustasid kokku **52,38%** kogu müügikäibest;
- liikuv keskmine näitas üldiselt kasvavat müügitrendi.

## Minu soovitused

Analüüsi põhjal soovitan:

- pöörata suuremat tähelepanu kõige kasumlikumatele tootekategooriatele;
- analüüsida aasta lõpu müügikasvu põhjuseid ning kasutada neid teadmisi järgmiste müügikampaaniate planeerimisel;
- jälgida regulaarselt kuudevahelisi muutusi võimalike trendide ja kõrvalekallete avastamiseks;
- kasutada agregeeritud näitajaid juhtimisaruannete koostamisel;
- rakendada aknafunktsioone müügitrendide ja tulemuslikkuse regulaarseks jälgimiseks.

## Mida õppisin

Õppisin kasutama SQL agregeerimisfunktsioone ja aknafunktsioone müügiandmete analüüsimiseks. Sain praktilise kogemuse kogukäibe, keskmiste väärtuste, trendide ja järjestuste arvutamisel ning mõistsin, kuidas agregeeritud andmed aitavad teha põhjendatud äriotsuseid.

## Kasutatud tööriistad

- PostgreSQL (Supabase)
- SQL
- GitHub
- NotebookLM
- ChatGPT
