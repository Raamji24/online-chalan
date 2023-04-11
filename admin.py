import streamlit as st
import smtplib
import re
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("kriya.json", scope)
client = gspread.authorize(creds)
sheet = client.open("psg_bank").sheet1 
data = sheet.get_all_values()
st.set_page_config(page_title="Admin")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
page_bg="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://c4.wallpaperflare.com/wallpaper/303/229/316/photo-of-man-in-motorcycle-suit-riding-on-red-and-white-sport-bike-wallpaper-preview.jpg");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>
"""
# with c2:
st.markdown(page_bg,unsafe_allow_html=True)
acc=st.text_input("Enter account number: ")
t_id=st.text_input("Enter Transaction Number: ")
if st.button("Proceed"):
    for i in range(1,len(data)):
        if data[i][0]==acc:
            if data[i][9]==t_id:
            # sheet.cell(3,9).value
                sheet.update_cell(i+1,7,sheet.cell(i+1,9).value)
                sheet.update_cell(i+1,9," ")
                sheet.update_cell(i+1,10," ")
                sheet.update_cell(i+1,11," ")
                st.success("Transaction successful.")
                break
            
    else:
        print(data[i][0] ,data[i][9])
        st.error("Invalid Account number/Transction ID")
        # break
