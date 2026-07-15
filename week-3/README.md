# Nädal 3 – SQL JOINs

## Projekti eesmärk

Selle nädala eesmärk oli õppida kasutama SQL JOIN lauseid erinevate andmetabelite ühendamiseks ning analüüsida UrbanStyle andmebaasi andmeid mitme tabeli põhjal.

## Äriküsimus

Kuidas ühendada erinevates tabelites olevad andmed, et saada terviklik ülevaade klientidest, toodetest, müügist ja laoseisust ning toetada äriliste otsuste tegemist?

## Minu ülesanne

Kasutasin SQL JOIN päringuid UrbanStyle andmebaasi tabelite ühendamiseks ning erinevate äriküsimuste lahendamiseks.

Teostasin järgmised tegevused:

- ühendasin tabelid `sales`, `customers`, `products` ja `inventory`;
- kasutasin `INNER JOIN` ja `LEFT JOIN` lauseid;
- kasutasin tabelite aliaseid (`s`, `c`, `p`, `i`);
- koostasin SQL päringuid klientide, toodete, müügi ja laoseisu analüüsimiseks;
- kasutasin funktsioone `GROUP BY`, `COUNT()`, `SUM()` ja `ORDER BY`;
- kontrollisin päringute tulemusi Supabase SQL Editoris.

## Tulemused

Analüüsi käigus selgus, et:

- erinevate tabelite ühendamine võimaldas koostada terviklikumaid müügi- ja kliendianalüüse;
- `INNER JOIN` tagastas ainult omavahel seotud kirjed;
- `LEFT JOIN` võimaldas leida ka kirjed, millel puudus vastav seos teises tabelis;
- tabelite aliased muutsid SQL päringud loetavamaks ja lihtsamini hallatavaks.

## Minu soovitused

Analüüsi põhjal soovitan:

- kasutada tabelite ühendamisel alati õigeid `PRIMARY KEY` ja `FOREIGN KEY` seoseid;
- valida `INNER JOIN` või `LEFT JOIN` vastavalt analüüsi eesmärgile;
- kasutada tabelite aliaseid SQL päringute loetavuse parandamiseks;
- kontrollida JOIN päringute tulemusi enne aruannete koostamist.

## Mida õppisin

Õppisin kasutama SQL JOIN lauseid erinevate tabelite ühendamiseks ning sain parema arusaama sellest, kuidas on UrbanStyle andmebaasi kliendid, müügid, tooted ja laoseis omavahel seotud. Sain praktilise kogemuse mitme tabeli andmete ühendamisel ja nende põhjal äriküsimustele vastuste leidmisel.

## Kasutatud tööriistad

- PostgreSQL (Supabase)
- SQL
- GitHub
- NotebookLM
- ChatGPT
