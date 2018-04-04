# SmartHome

Création d'une SmartHome sous Raspberry Pi avec une maquette.

# Introduction

Aujourd'hui, les appareils domotiques sont dits "intelligents". Par exemple, la lampe s'allume quand vous êtes dans la pièce ou le chauffage fonctionne lorsque vous êtes là de manière autonome.
Cependant "l'intelligence" d'une maison peut être bien mieux exploitée. En effet, en utilisant chacun des appareils et en les connectant à un même réseau on peut rassembler les données et créer une intelligence relative à l'économie d'énergie.

# Assomption de départ

Ce projet part également du postulat que chaque appareil ne sera jamais 100% manuel et qu'un mode manuel est nécessaire. 
Un exemple simple pour comprendre : Vous voulez reposer vos yeux dans l'après-midi et vous décidez d'éteindre les lumières de la maison, le système automatisé ne pourra jamais le détecter et vous avez besoin d'un mode manuel pour éteindre ces lumières.

# Description

Ce projet montre ainsi la faisabilité d'une tel SmartHome sous raspberry pi.
3 principaux objets de domotique sont simulés :
- Les lampes qui sont simulées par des LED. Les capteurs de celle-ci sont simulés par des capteurs à ultrason.
- Les volets qui sont simulés par des servomoteurs. Il était prévu d'utiliser des capteurs d'intensité lumineuse cependant ils ne sont pas implémentés.
- Le lave-vaisselle et le lave-linge qui sont simulés à l'aide de servomoteur.

# Fonctionnalitées

Il est ainsi possible de tout contrôler manuellement via commande vocale ou navigateur web (ordinateur ou smartphone). Le mode manuel est prioritaire sur le mode automatique. L'utilisateur doit toujours avoir le plein contrôle sur ses appareils. C'est à la fois pratique pour lui et rassurant.
Ensuite il est possible d'activer le mode automatique, de même le contrôle est vocal ou par navigateur web.
Le mode automatique est activable/désactivable sur chaque appareil, il fonctionne de la manière suivante :
- Pour les lampes : Chaque lampe est reliée à un capteur d'ultrason, si une représentation humaine (un playmobile)  est détectée par un capteur sur la maquette alors la lampe associée s'allume.
- Pour les volets, en théorie contrôlable à la lumière. (Mais uniquement manuel comme vu précédemment faute de capteurs)
- Pour le lave-vaisselle et le lave-linge, un message d'avertissement précise qu'il n'est pas possible de le lancer si la maison atteint un certain pic d'énergie. Il y a cependant une option pour forcer le lancement afin de laisser le plein contrôle à l'utilisateur.

# Technologies utilisées

Le projet est entièrement codé en Python3 sauf les pages HTML et css de la page de contrôle web.
La librairie Flask pour la mise en place du serveur web
LOpenJarvis pour la reconnaissance vocale
La librairie RPI.Gpio pour le contrôle des ports GPIO du Rapsberry Pi.

# Photo du projet abouti.

[link photo]
