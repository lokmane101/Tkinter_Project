use projet;
drop table etudiant;
create table  Etudiant (id integer primary key auto_increment,
 
mot_de_passe varchar(30),
nom varchar(20) ,
prenom  varchar(20),
filière  varchar(20),
email  varchar(50),
téléphone  varchar(40),
cne  varchar(20),
cni varchar(20),
date_de_naissance date,
image longblob
);

create table adress (id_Etud int, num int, rue varchar(30), ville varchar(30),
	constraint fk_addr foreign key (id_Etud) references Etudiant(id)
);


# table filiere
drop table filiere;
CREATE TABLE FILIERE ( NOM varchar(100) primary key,module1 varchar(150),module2 varchar(150),module3 varchar(150),module4 varchar(150),
module5 varchar(150),module6 varchar(150),module7 varchar(150)
,module8 varchar(150),module9 varchar(150),module10 varchar(150),module11 varchar(150),module12 varchar(150));

alter table filiere add column module12 varchar(150);


# cahngement dans la base de données
use projet;

delete from etudiant where nom='karim';

alter table etudiant drop column username;

alter table etudiant change passwd mot_de_passe varchar(50) not null ;
alter table etudiant change section filière varchar(50) not null;
alter table etudiant change phone téléphone varchar(50) not null;
alter table etudiant change date_naissance date_de_naissance varchar(50) not null;
alter table etudiant change cni cin varchar(50) not null;
truncate table etudiant;

select * from etudiant;








 
 
 
select * from etudiant;
select * from adress;
select * from filiere;