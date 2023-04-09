import mysql.connector as sc

class DataBase:
    def __init__(self):
        self.mydata={}
        self.database=sc.connect(
            user="root",
            passwd="lokmane-SQL-12",
            host="localhost",
            database="projet"

        )
        print("connected")
        self.cursor=self.database.cursor()
        self.target_attribute=10

   #----------------------pour le script 1--------------------#
    def insert_data_sign_in_phase1(self,nom,prenom,email,phone,date_naissance):
        args=[("nom",nom),("prenom",prenom),("email",email),("phone",phone),("date_naissance",date_naissance)]
        file=open("data.txt","a+")
        for key,value in args:
            file.write(key+f":{value}\n")
        file.close()


   #----------------------pour le script 2--------------------#
    def insert_data_sign_in_phase2(self,cne,cni):
        args=[("cne",cne),("cni",cni)]
        for key,value in args:
            file=open("data.txt","a+")
            file.write(key+f":{value}\n")
        file.close()
    
    #----------------------pour le script 3--------------------#
    def insert_data_sign_in_phase3(self,username,passwd,section):
        args=[("username",username),("passwd",passwd),("section",section)]
        for key,value in args:
            file=open("data.txt","a+")
            file.write(key+f":{value}\n")
        file.close()



    
    def getrow(self):
        file=open("data.txt","r")
        data=file.read().split("\n")
        data.remove("")
        print(data)
        for line in data:
            items=line.split(":")
            self.mydata[items[0]]=items[1]
        return self.mydata

    
    def valide(self):

        #------insertion des donners--------#
        requete="INSERT INTO ETUDIANT (username,passwd,nom,prenom,section,email,phone,cne,cni,date_naissance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(self.mydata["username"],self.mydata["passwd"],self.mydata["nom"],self.mydata["prenom"],self.mydata["section"],
            self.mydata["email"],self.mydata["phone"],self.mydata["cne"],self.mydata["cni"],self.mydata["date_naissance"])
        self.cursor.execute(requete,data)
        self.database.commit()


        #-----supprisseion du contenu de fichier pour une autre operation------#
        with open("data.txt","w") as file:
            file.write("")
        return
    