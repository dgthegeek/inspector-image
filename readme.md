# Inspector Image

Inspector Image est un outil en Python conçu pour analyser les images afin d'extraire des informations cachées, telles que les métadonnées GPS et les clés PGP dissimulées via la stéganographie. Ce projet vise à introduire des concepts tels que la reconnaissance d'image, la stéganographie, et l'analyse des métadonnées.

## Objectif

- Découvrir une nouvelle méthode d'analyse passive
- Explorer les bases de la reconnaissance d'image
- Comprendre la stéganographie et l'information qu'une image peut cacher

## Fonctionnalités

- **Extraction des coordonnées GPS** : Récupère les coordonnées GPS d'une image si elles sont disponibles dans les métadonnées.
- **Extraction des messages cachés** : Détecte et extrait les messages cachés dans une image via la stéganographie (par exemple, une clé PGP).

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez vérifier cela en exécutant :

```bash
python --version
```
## Installation des dépendances

Vous pouvez executer le setup.sh pour creer le venv et installer les dependances necessaires:

- Pillow : Manipulation d'images.
- ExifRead : Extraction des métadonnées EXIF.
- Stegano : Stéganographie pour cacher ou révéler des messages dans les images.

## Utilisation

- Extraction des coordonnées GPS d'une image :

```bash
python inspector_image.py -map image.jpeg
```

- Extraction d'un message caché via la stéganographie :

```bash
python inspector_image.py -steg image.jpeg
```

### Exemple de sortie :

```bash
$> python inspector_image.py -map image.jpeg
Lat/Lon:	(13.731) / (-1.1373)

$> python inspector_image.py -steg image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: 01

mQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU
2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE
7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg
ao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew
zD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx
9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB
AgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B
D9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8
PwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/
e/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0
6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg
+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=
=N8hc
-----END PGP PUBLIC KEY BLOCK-----
$>
```