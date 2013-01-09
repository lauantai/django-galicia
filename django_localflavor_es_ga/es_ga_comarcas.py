# -*- coding: utf-8 -*-
"""
List of Galician comarcas (as of January 2013) to use as select choices.

Sorted alphabetically, ignoring initial articles.

Also included is a dictionary mapping each comarca to the list of municipalities it contains.

The choice tuple value is the geographical code for the comarca,
as per the comarca listing by Francisco Ruiz at
http://alarcos.esi.uclm.es/per/fruiz/pobesp/ter_com.htm
"""

from django.utils.translation import ugettext_lazy as _
from __future__ import unicode_literals


COMARCA_CHOICES = (
    ('1232', _(u'Allariz-Maceda')),
    ('1219', _(u'Os Ancares')),
    ('1201', _(u'Arzúa')),
    ('1233', _(u'A Baixa Limia')),
    ('1244', _(u'O Baixo Miño')),
    ('1202', _(u'Barbanza')),
    ('1203', _(u'A Barcala')),
    ('1204', _(u'Bergantiños')),
    ('1205', _(u'Betanzos')),
    ('1245', _(u'Caldas')),
    ('1235', _(u'O Carballiño')),
    ('1220', _(u'Chantada')),
    ('1246', _(u'O Condado')),
    ('1206', _(u'A Coruña')),
    ('1247', _(u'Deza')),
    ('1207', _(u'Eume')),
    ('1208', _(u'Ferrol')),
    ('1209', _(u'Fisterra')),
    ('1221', _(u'A Fonsagrada')),
    ('1234', _(u'A Limia')),
    ('1222', _(u'Lugo')),
    ('1223', _(u'A Mariña Central')),
    ('1224', _(u'A Mariña Occidental')),
    ('1225', _(u'A Mariña Oriental')),
    ('1226', _(u'Meira')),
    ('1248', _(u'O Morrazo')),
    ('1210', _(u'Muros')),
    ('1211', _(u'Noia')),
    ('1212', _(u'Ordes')),
    ('1213', _(u'Ortegal')),
    ('1236', _(u'Ourense')),
    ('1249', _(u'A Paradanta')),
    ('1250', _(u'Pontevedra')),
    ('1227', _(u'Quiroga')),
    ('1237', _(u'O Ribeiro')),
    ('1251', _(u'O Salnés')),
    ('1214', _(u'Santiago')),
    ('1215', _(u'O Sar')),
    ('1228', _(u'Sarria')),
    ('1252', _(u'Tabeirós-Terra de Montes')),
    ('1229', _(u'Terra Chá')),
    ('1238', _(u'Terra de Caldelas')),
    ('1239', _(u'Terra de Celanova')),
    ('1230', _(u'Terra de Lemos')),
    ('1216', _(u'Terra de Melide')),
    ('1217', _(u'Terra de Soneira')),
    ('1240', _(u'Terra de Trives')),
    ('1231', _(u'A Ulloa')),
    ('1241', _(u'Valdeorras')),
    ('1242', _(u'Verín')),
    ('1243', _(u'Viana')),
    ('1253', _(u'Vigo')),
    ('1218', _(u'Xallas')),
)


COMARCAS_WITH_MUNICIPALITIES = {
    '1201': [
        _('Arzúa'),
        _('Boimorto'),
        _('O Pino'),
        _('Touro'),
        ],
    '1202': [
        _('Boiro'),
        _('A Pobra do Caramiñal'),
        _('Rianxo'),
        _('Ribeira'),
        ],
    '1203': [
        _('A Baña'),
        _('Negreira'),
        ],
    '1204': [
        _('Cabana de Bergantiños'),
        _('Carballo'),
        _('Coristanco'),
        _('A Laracha'),
        _('Laxe'),
        _('Malpica de Bergantiños'),
        _('Ponteceso'),
        ],
    '1205': [
        _('Aranga'),
        _('Betanzos'),
        _('Cesuras'),
        _('Coirós'),
        _('Curtis'),
        _('Irixoa'),
        _('Miño'),
        _('Oza dos Ríos'),
        _('Paderne'),
        _('Vilarmaior'),
        _('Vilasantar'),
        ],
    '1206': [
        _('Abegondo'),
        _('Arteixo'),
        _('Bergondo'),
        _('Cambre'),
        _('Carral'),
        _('A Coruña'),
        _('Culleredo'),
        _('Oleiros'),
        _('Sada'),
        ],
    '1207': [
        _('Cabanas'),
        _('A Capela'),
        _('Monfero'),
        _('Pontedeume'),
        _('As Pontes de García Rodríguez'),
        ],
    '1208': [
        _('Ares'),
        _('Cedeira'),
        _('Fene'),
        _('Ferrol'),
        _('Moeche'),
        _('Mugardos'),
        _('Narón'),
        _('Neda'),
        _('San Sadurniño'),
        _('As Somozas'),
        _('Valdoviño'),
        ],
    '1209': [
        _('Cee'),
        _('Corcubión'),
        _('Dumbría'),
        _('Fisterra'),
        _('Muxía'),
        ],
    '1210': [
        _('Carnota'),
        _('Muros'),
        ],
    '1211': [
        _('Lousame'),
        _('Noia'),
        _('Outes'),
        _('Porto do Son'),
        ],
    '1212': [
        _('Cerceda'),
        _('Frades'),
        _('Mesía'),
        _('Ordes'),
        _('Oroso'),
        _('Tordoia'),
        _('Trazo'),
        ],
    '1213': [
        _('Cariño'),
        _('Cerdido'),
        _('Mañón'),
        _('Ortigueira'),
        ],
    '1214': [
        _('Ames'),
        _('Boqueixón'),
        _('Brión'),
        _('Santiago de Compostela'),
        _('Teo'),
        _('Val do Dubra'),
        _('Vedra'),
        ],
    '1215': [
        _('Dodro'),
        _('Padrón'),
        _('Rois'),
        ],
    '1216': [
        _('Melide'),
        _('Santiso'),
        _('Sobrado'),
        _('Toques'),
        ],
    '1217': [
        _('Camariñas'),
        _('Vimianzo'),
        _('Zas'),
        ],
    '1218': [
        _('Mazaricos'),
        _('Santa Comba'),
        ],
    '1219': [
        _('Baralla'),
        _('Becerreá'),
        _('Cervantes'),
        _('Navia de Suarna'),
        _('As Nogais'),
        _('Pedrafita do Cebreiro'),
        ],
    '1220': [
        _('Carballedo'),
        _('Chantada'),
        _('Taboada'),
        ],
    '1221': [
        _('Baleira'),
        _('A Fonsagrada'),
        _('Negueira de Muñiz'),
        ],
    '1222': [
        _('Castroverde'),
        _('O Corgo'),
        _('Friol'),
        _('Guntín'),
        _('Lugo'),
        _('Outeiro de Rei'),
        _('Portomarín'),
        _('Rábade'),
        ],
    '1223': [
        _('Alfoz'),
        _('Burela'),
        _('Foz'),
        _('Lourenzá'),
        _('Mondoñedo'),
        _('O Valadouro'),
        ],
    '1224': [
        _('Cervo'),
        _('Ourol'),
        _('O Vicedo'),
        _('Viveiro'),
        _('Xove'),
        ],
    '1225': [
        _('Barreiros'),
        _('A Pontenova'),
        _('Ribadeo'),
        _('Trabada'),
        ],
    '1226': [
        _('Meira'),
        _('Pol'),
        _('Ribeira de Piquín'),
        _('Riotorto'),
        ],
    '1227': [
        _('Folgoso do Courel'),
        _('Quiroga'),
        _('Ribas de Sil'),
        ],
    '1228': [
        _('O Incio'),
        _('Láncara'),
        _('Paradela'),
        _('O Páramo'),
        _('Samos'),
        _('Sarria'),
        _('Triacastela'),
        ],
    '1229': [
        _('Abadín'),
        _('Begonte'),
        _('Castro de Rei'),
        _('Cospeito'),
        _('Guitiriz'),
        _('Muras'),
        _('A Pastoriza'),
        _('Vilalba'),
        _('Xermade'),
        ],
    '1230': [
        _('Bóveda'),
        _('Monforte de Lemos'),
        _('Pantón'),
        _('A Pobra do Brollón'),
        _('O Saviñao'),
        _('Sober'),
        ],
    '1231': [
        _('Antas de Ulla'),
        _('Monterroso'),
        _('Palas de Rei'),
        ],
    '1232': [
        _('Allariz'),
        _('Baños de Molgas'),
        _('Maceda'),
        _('Paderne de Allariz'),
        _('Xunqueira de Ambía'),
        _('Xunqueira de Espadanedo'),
        ],
    '1233': [
        _('Bande'),
        _('Entrimo'),
        _('Lobeira'),
        _('Lobios'),
        _('Muíños'),
        ],
    '1234': [
        _('Baltar'),
        _('Os Blancos'),
        _('Calvos de Randín'),
        _('Porqueira'),
        _('Rairiz de Veiga'),
        _('Sandiás'),
        _('Sarreaus'),
        _('Trasmiras'),
        _('Vilar de Barrio'),
        _('Vilar de Santos'),
        _('Xinzo de Limia'),
        ],
    '1235': [
        _('Beariz'),
        _('Boborás'),
        _('O Carballiño'),
        _('O Irixo'),
        _('Maside'),
        _('Piñor'),
        _('Punxín'),
        _('San Amaro'),
        _('San Cristovo de Cea'),
        ],
    '1236': [
        _('Amoeiro'),
        _('Barbadás'),
        _('Coles'),
        _('Esgos'),
        _('Nogueira de Ramuín'),
        _('Ourense'),
        _('O Pereiro de Aguiar'),
        _('A Peroxa'),
        _('San Cibrao das Viñas'),
        _('Taboadela'),
        _('Toén'),
        _('Vilamarín'),
        ],
    '1237': [
        _('A Arnoia'),
        _('Avión'),
        _('Beade'),
        _('Carballeda de Avia'),
        _('Castrelo de Miño'),
        _('Cenlle'),
        _('Cortegada'),
        _('Leiro'),
        _('Melón'),
        _('Ribadavia'),
        ],
    '1238': [
        _('Castro Caldelas'),
        _('Montederramo'),
        _('Parada de Sil'),
        _('A Teixeira'),
        ],
    '1239': [
        _('A Bola'),
        _('Cartelle'),
        _('Celanova'),
        _('Gomesende'),
        _('A Merca'),
        _('Padrenda'),
        _('Pontedeva'),
        _('Quintela de Leirado'),
        _('Ramirás'),
        _('Verea'),
        ],
    '1240': [
        _('Chandrexa de Queixa'),
        _('Manzaneda'),
        _('A Pobra de Trives'),
        _('San Xoán de Río'),
        ],
    '1241': [
        _('O Barco de Valdeorras'),
        _('O Bolo'),
        _('Carballeda de Valdeorras'),
        _('Larouco'),
        _('Petín'),
        _('Rubiá'),
        _('A Rúa'),
        _('A Veiga'),
        _('Vilamartín de Valdeorras'),
        ],
    '1242': [
        _('Castrelo do Val'),
        _('Cualedro'),
        _('Laza'),
        _('Monterrei'),
        _('Oímbra'),
        _('Riós'),
        _('Verín'),
        _('Vilardevós'),
        ],
    '1243': [
        _('A Gudiña'),
        _('A Mezquita'),
        _('Viana do Bolo'),
        _('Vilariño de Conso'),
        ],
    '1244': [
        _('A Guarda'),
        _('Oia'),
        _('O Rosal'),
        _('Tomiño'),
        _('Tui'),
        ],
    '1245': [
        _('Caldas de Reis'),
        _('Catoira'),
        _('Cuntis'),
        _('Moraña'),
        _('Pontecesures'),
        _('Portas'),
        _('Valga'),
        ],
    '1246': [
        _('Mondariz'),
        _('Mondariz-Balneario'),
        _('As Neves'),
        _('Ponteareas'),
        _('Salvaterra de Miño'),
        ],
    '1247': [
        _('Agolada'),
        _('Dozón'),
        _('Lalín'),
        _('Rodeiro'),
        _('Silleda'),
        _('Vila de Cruces'),
        ],
    '1248': [
        _('Bueu'),
        _('Cangas'),
        _('Marín'),
        _('Moaña'),
        ],
    '1249': [
        _('Arbo'),
        _('A Cañiza'),
        _('Covelo'),
        _('Crecente'),
        ],
    '1250': [
        _('Barro'),
        _('Campo Lameiro'),
        _('Cotobade'),
        _('A Lama'),
        _('Poio'),
        _('Ponte Caldelas'),
        _('Pontevedra'),
        _('Vilaboa'),
        ],
    '1251': [
        _('Cambados'),
        _('O Grove'),
        _('A Illa de Arousa'),
        _('Meaño'),
        _('Meis'),
        _('Ribadumia'),
        _('Sanxenxo'),
        _('Vilagarcía de Arousa'),
        _('Vilanova de Arousa'),
        ],
    '1252': [
        _('Cerdedo'),
        _('A Estrada'),
        _('Forcarei'),
        ],
    '1253': [
        _('Baiona'),
        _('Fornelos de Montes'),
        _('Gondomar'),
        _('Mos'),
        _('Nigrán'),
        _('Pazos de Borbén'),
        _('O Porriño'),
        _('Redondela'),
        _('Salceda de Caselas'),
        _('Soutomaior'),
        _('Vigo'),
        ],
}