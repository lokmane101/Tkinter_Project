use projet;

create table  Etudiant (id integer primary key auto_increment ,
username varchar(30),
passwd varchar(30),
nom varchar(20) ,
prenom  varchar(20),
section  varchar(20),
email  varchar(50),
phone  varchar(40),
cne  varchar(20),
cni varchar(20),
date_naissance date,
image longblob
);

create table adress (id_Etud int, num int, rue varchar(30), ville varchar(30),
	constraint fk_addr foreign key (id_Etud) references Etudiant(id)
);

select * from etudiant;
select * from adress;