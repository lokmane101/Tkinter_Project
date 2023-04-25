import mysql.connector as sc

class DataBase:
    def __init__(self):
        self.mydata={}
        self.database=sc.connect(
            user="root",
            passwd="root",
            host="localhost",
            database="projet"

        )
        print("connected")

        self.cursor=self.database.cursor()
        self.target_attribute=10

   #----------------------pour le script 1(collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase1(self,nom,prenom,email,téléphone,date_de_naissance):
        args=[("nom",nom),("prenom",prenom),("email",email),("téléphone",téléphone),("date_de_naissance",date_de_naissance)]
        file=open("data.txt","a+")
        for key,value in args:
            file.write(key+f":::{value}\n")
        file.close()


   #----------------------pour le script 2 (collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase2(self,adress,cne,cin,image):
        args=[("cne",cne),("cin",cin),("adress",adress),("image",image)]
        file=open("data.txt","a+")
        for key,value in args:
            file.write(key+f":::{value}\n")
        file.close()
    
    #----------------------pour le script 3 (collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase3(self,passwd,filière):
        args=[("passwd",passwd),("filière",filière)]
        for key,value in args:
            file=open("data.txt","a+")
            file.write(key+f":::{value}\n")
        file.close()



    #------------------------selection les données depuis le fichier data.txt puis les stocker dans une list pour les enregister sur la base des donneés------------    
    def getrow(self):
        file=open("data.txt","r")
        data=file.read().split("\n")
        data.remove("")
        print(data)
        for line in data:
            items=line.split(":::")
            self.mydata[items[0]]=items[1]
        return self.mydata

    #-------------une method static qui permet de convertir une phote en forme binaire-------------------------------------------------------------------------
    @staticmethod
    def convertToBinary(image_path):
        with open(image_path,"rb") as image :
            db= image.read()
        return db
    
    #-----------------enregistrement des données dans a base des données--------------

    def valide(self):
        #-----definition d'image path 
        Myimage_path=self.mydata["image"].split(" ")
        if "png" in Myimage_path[2] or "jpg"in Myimage_path[2]:
            Myimage_path =Myimage_path[1].split("=")[1].replace("'","")+" "+Myimage_path[2].replace("'","")
        else:
            Myimage_path=Myimage_path[1].split("=")[1].replace("'","")

        


        print(Myimage_path)
        #------insertion des données (sans l'adress)--------#
        requeste="INSERT INTO ETUDIANT (mot_de_passe,nom,prenom,filière,email,téléphone,cne,cin,date_de_naissance,image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(self.mydata["passwd"],self.mydata["nom"],self.mydata["prenom"],self.mydata["filière"],
            self.mydata["email"],self.mydata["téléphone"],self.mydata["cne"],self.mydata["cin"],self.mydata["date_de_naissance"],DataBase.convertToBinary(image_path=Myimage_path))
        self.cursor.execute(requeste,data)
        self.database.commit()
         
        print("saved data without adress ")
        

        #--------fetch the id of the student------
        self.cursor.execute("SELECT id from Etudiant order by id desc")
        valide_id=self.cursor.fetchall()
        v_valide_id=valide_id[0][0]
        print(v_valide_id)
        #----------insertion de l'adress----------
        adress=self.mydata["adress"].split("-")
        requeste="INSERT INTO Adress VALUES (%s,%s,%s,%s);"
        data=(v_valide_id,adress[0],adress[1],adress[2])
        self.cursor.execute(requeste,data)


        self.database.commit()
        print("saved adress data")

        #-----supprisseion du contenu de fichier pour une autre operation------#
        with open("data.txt","w") as file:
            file.write("")
        return
            