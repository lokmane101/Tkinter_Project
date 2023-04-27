
SELECT * FROM projet.etudiant;
use projet;
drop table projet.adress cascade;
drop table projet.etudiant cascade ;
create table  Etudiant (
id integer primary key auto_increment ,
mot_de_passe varchar(30),
nom varchar(20) ,
prenom  varchar(20),
filière  varchar(20),
email  varchar(50),
téléphone  varchar(40),
cne  varchar(20),
cin varchar(20),
date_de_naissance date,
image longblob
);

create table adress (id_Etud int, num int, rue varchar(30), ville varchar(30),
	constraint fk_addr foreign key (id_Etud) references Etudiant(id)
);

select * from etudiant;
select * from adress;