drop table etudiant;
create table ETUDIANT(
id integer primary key auto_increment,
mot_de_passe varchar(50),
nom varchar(50),
prenom varchar(50),
filière varchar(50),
email varchar(50),
tétéphone varchar(50),
cne varchar(50),
cin varchar(50),
date_de_naissance date,
image longblob




);

use projet;
DROP TABLE mODULES;
create table Modules (
filière varchar(50) references Etudiant (filière),

module varchar(150),

professeur varchar(50));

#-----------------ID1--------------------
insert into Modules values('ID1','Analyse numérique matricielle et Statistique Inférentielle','F.EL MOURADI');
insert into Modules values('ID1','Architecture des ordinateurs et systèmes d’exploitation','M.EL CHERRADI/S.EL HAMDDOUI');
insert into Modules values('ID1','Statistique en grande dimension','M.ADDAM');
insert into Modules values('ID1','Programmation Python / Les bases du Web','A.BENGAG');
insert into Modules values('ID1','Programmation Orientée Objet Java','T.BOUDAA');
insert into Modules values('ID1','Entreprenariat I','S.KOULALI');
insert into Modules values('ID1','Administration et Optimisation des Bases de Données','Y.EL MOURABIT');
insert into Modules values('ID1','Data Mining','A.BOUFFASIL');
insert into Modules values('ID1','Théorie des langages et compilation','A.KHAMJAN');
insert into Modules values('ID1','Systèmes d’Information et Bases de Données','A.EL HADDADI');
insert into Modules values('ID1','Structure de données et Algorithmique avancée','A.AL HADDADI');
insert into Modules values('ID1','Analyse numérique matricielle et Statistique Inférentielle','M.ADDAM');
insert into Modules values('ID1','Communication Professionnelle et Soft Skills -I-','A.BOUAZZA');

#---------------ID2---------------
insert into Modules values('ID2','Intelligence Artificielle II – Deep Learning','M.EL MAROUANI');
insert into Modules values('ID2','Entreprenariat II','S.KOULALI');
insert into Modules values('ID2','Data Warehouse et Data Lake','A.EL HADDADI');
insert into Modules values('ID2','Big Data Avancées','A.EL HADDADI');
insert into Modules values('ID2','Applications Web avancées avec Java et Spring','T.BOUDAA');
insert into Modules values('ID2','NLP','T.BOUDAA');
insert into Modules values('ID2','Modélisation Stochastique / Techniques Mathématiques d’Optimisation','M.ADDAM');
insert into Modules values('ID2','Intelligence Artificielle I – Machine Learning','A.EL HADDADI');
insert into Modules values('ID2','Fondements du Big Data','A.EL HADDADI');
insert into Modules values('ID2','Communication Professionnelle et Soft Skills -II-','A.BOUAZZA');
insert into Modules values('ID2','Bases de données avancées','Y. EL MOURABIT');
insert into Modules values('ID2','Architecture Logicielle et UML','T.BOUDAA');

#----GI1------#
insert into Modules values('GI1','Web1 : Technologies de Web et PHP5','E.W.DADI');
insert into Modules values('GI1','Théorie des langages et compilation','O.ZEALOUK');
insert into Modules values('GI1','Programmation Orientée Objet C++','R.RAGRAGUI');
insert into Modules values('GI1','Entreprenariat 1 & Atelier Start up','S.KOULALI');
insert into Modules values('GI1','Architecture Logicielle et UML','F.RAFII ZAKANI');
insert into Modules values('GI1','Algorithmique Avancée et complexité','E.W.DADI');
insert into Modules values('GI1','Systèmes d’Information et Bases de Données Relationnelles','Y.EL MOURABIT');
insert into Modules values('GI1','Réseaux informatiques','F.RAFII ZAKANI');
insert into Modules values('GI1','Langues et Communication Professionnelles 1','A.BOUAZZA');
insert into Modules values('GI1','Recherche opérationnelle et théorie des graphes','E.W.DADI');
insert into Modules values('GI1','Langage C avancé et structures de données','A.RAGRAGUI');
insert into Modules values('GI1','Comptabilité générale ','E.W.DADI');


#---------------GI2-------------------
insert into Modules values('GI2','Machine Learning','A.BOUFASSIL');
insert into Modules values('GI2','Gestion de projet et Génie logiciel','A.RAGRAGUI');
insert into Modules values('GI2','Frameworks Java EE avancés et .Net','T.BOUDAA/S.OUALD CHAIB');
insert into Modules values('GI2','Web 2 : Applications Web modernes','F.RAFII ZAKANI');
insert into Modules values('GI2','Entreprenariat 2','ALI BENAISSA');
insert into Modules values('GI2','Crypto-systèmes et sécurité Informatique','N.KANNOUF');
insert into Modules values('GI2','Python pour les sciences de données','E.W.DADI');
insert into Modules values('GI2','Programmation Java Avancée','T.BOUDAA');
insert into Modules values('GI2','Linux et programmation système','M.CHERADDI');
insert into Modules values('GI2','Langues et Communication Professionnelle 2 & Soft Skils','A.BOUAZZA');
insert into Modules values('GI2','sécurité informatique','A.BENGAG');
insert into Modules values('GI2','Administration des Bases de données Avancées','A.AKHLAL');



































select * from etudiant;
select * from modules;




