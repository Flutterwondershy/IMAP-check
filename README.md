# IMAP-check

IMAP-check est un script python permettant d'afficher une icône polybar () lorsqu'il y a un mail non-lu dans une liste de compte mail pré-établie.
La démarche décrite ici permet de *rendre inaccessible* les différents mots de passe écrit en clair dans le script.

## Dépendances
- Polybar
- Cython
- FontAwesome

## Compilation
Dans un premier temps, il faut éditer le fichier *IMAPC.py* pour y insérer les informations relatives aux comptes mails à surveiller dans les premières lignes.
Ensuite, il suffit de se rendre dans le repository et d'écrire les commandes suivantes:
```bash
$ cython3 IMAPC.py --embed
$ gcc IMAPC.c $(pkg-config --cflags --libs python3) -o IMAP-check 
```
Puis retirer les droits de lecture de l'exécutable obtenu pour que les mots de passe ne soient pas récupérables:
```bash
$ chmod 111 IMAP-check
```
Il ne reste plus qu'à changer le propriétaire du fichier *IMAP-check* après l'avoir déplacé à l'endroit voulu:
```bash
# chown root IMAP-check
```
Seul le fichier *IMAP-check* est nécessaire pour la suite donc tout le reste peut être supprimé.
## Paramètrage de polybar
Dans le fichier *config* de polybar, ajouter les lignes suivantes:
```
[module/IMAP-check]
type = custom/script
exec = $HOME/.config/polybar/module-IMAP-check/IMAP-check
interval = 90
```
Ensuite, il suffit d'ajouter ```IMAP-check``` dans ```modules-left```, ```modules-center``` ou ```modules-right``` dans le fichier *config* de polybar.
