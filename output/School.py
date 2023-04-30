import subprocess
import os 


def connecter(user,bddn,passwd):

    # Define the MySQL connection parameters
    host = "localhost"
    user = user
    password = passwd
    database = bddn

    # Read the SQL script from file
    with open("script_des_bases_de_données.sql", "r", encoding="utf-8") as file:
        script = file.read()

    # Construct the mysql command to execute the script
    command = f"mysql -h {host} -u {user} -p{password} {database}"

    # Run the command and pass the script as input
    subprocess.run(command, input=script.encode(), shell=True)


file=open(r"config.properties","r",)
var=file.read().split("=")[1].replace("\n","")
file.close()


cuurent_path =os.getcwd()
if var=="0":
    username=input("S'il vous plait entrer le nom de votre utilisateur sur Mysql: ")
    password=input("S'il vous plait entrer le mot de passe de cette utilisateur : ")
    db=input("S'il vous plait entrer le nom dubase de donnée à connecter : ")
    connecter(username,db,password)
subprocess.run(["python",cuurent_path+"\\Luncher.py"])

    

with open(r"config.properties","w") as file:
    file.write("var=1")
    
