![DrivingQuestions logo][https://github.com/Ryanhtech/driving-questions/blob/main/logo.png]
# DrivingQuestions

DrivingQuestions est un logiciel simple, conçu pour vous aider à réviser les questions pouvant être posées lors de l'examen pratique du permis de conduire français (catégorie B).

## Comment se déroulent les questions de l'examen pratique du permis de conduire ?

Lors de l'examen pratique du permis de conduire, en fonction des deux derniers chiffres du compteur kilométrique du véhicule d'examen, l'examinateur.ice vous posera **trois** questions :

* Une question de vérification du véhicule : si le nombre formé par les deux derniers chiffres de votre compteur est impair, il s'agit d'une vérification intérieure (dans l'habitacle) ; dans le cas contraire, il s'agit d'une vérification extérieure (sortie du véhicule nécessaire).

* Une question de sécurité routière, en suivant le même principe intérieur/extérieur selon les conditions spécifiées ci-dessus.

* Une question de premiers secours.

Chacune de ces trois questions est notée sur un point, sur les 20 nécessaires à l'obtention du permis de conduire.

## Comment fonctionne DrivingQuestions ?

DrivingQuestions est un petit logiciel, écrit en langage Python et disposant d'une intérface graphique réalisée avec la bibliothèque `dearpygui`. Cette interface vous permet d'ouvrir une base de données de questions, et de sélectionner par exemple un nombre aléatoire entre 0 et 99 pour simuler les questions de l'examen. Les trois questions s'affichent, et un bouton vous permet de consulter la réponse dans une nouvelle boîte de dialogue.

Le but est de s'entraîner à répondre aux questions sans voir la réponse, et de vérifier si la réponse correspond bien à ce que vous pensiez.
