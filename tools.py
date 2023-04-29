import re
import webbrowser
def regler_date(date):
        date_list=date.split("-")
        if bool(re.match(r"^\d{4}-\d-\d$",date)):
                date_list[1]="0"+date_list[1]
                date_list[2]="0"+date_list[2]
        elif bool(re.match(r"^\d{4}-\d\d-\d$",date)): 
                date_list[2]="0"+date_list[2]
        elif bool(re.match(r"^\d{4}-\d-\d\d$",date)):
                date_list[1]="0"+date_list[1]
        date="-".join(date_list)
        
        return date
def open_email_client():
    webbrowser.open('mailto:equipetechniquestkinter@gmail.com')