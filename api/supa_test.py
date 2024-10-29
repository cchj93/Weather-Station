import hashlib
from supabase import create_client, Client

#Supabase data connection: URL, KEY 

SUPABASE_URL = "https://zhefkeclsnsqgqxzxemu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpoZWZrZWNsc25zcWdxeHp4ZW11Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY4ODEsImV4cCI6MjA0NTc0Mjg4MX0.cNFtJgRMjV8cIOBur_YF-F4ugHHnn6_g2yn8RHpUQPQ"


#CONNECT TO SUPABASE CLIENT

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#get and save data function


def save_data(e, p):
    #insert into user model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    response = supabase.table('users').insert({"email": e, "password": enc_pass}).execute()

    if response.data:
        print(f"user has been save successfuly {response.data}")
    elif response.error:
        print(f"error saving user {response.error}")


#main

mail = input("Email:")
passwd = input ("user pasword:")
save_data(mail, passwd)