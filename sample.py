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
# data = sheet.get_all_records()
st.set_page_config(page_title="Login page",layout="wide")
st.write(
    '''<style>
    .my-div {
        position: relative;
    }
    .my-div::after {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        width: 0.5px;
        border-right: 10px solid black;
        margin-left: 50%;
        height: 570px;
    }
</style>
<div class="my-div">
    
</div>
''',unsafe_allow_html=True)

# hide_ststyle = """
#             <style>
#             MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
c1,c2,c3=st.columns([0.2,1.2,1])
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





with c2:
	# st.write(''' 
	# <style>
    #     div{
    #         border: 4px solid black;
    #         color :white;
    #         width: 50px;
    #         height: 50px ;
            
    #         font-size : 20px;
    #         font-color
    #     }
    # </style>
    # <div>
    #    <H1>BANK 1</H1>
    #    <h1>OTHERS..</h1>
    # </div>
	# ''',unsafe_allow_html=True)
	st.write('''<h3 style="font-family:georgia,garamond,serif;font-size:90px;margin-top:100px"><span style="color: white">PSG Bank</span></h3>''',unsafe_allow_html=True)
	st.write('''<h6 style="font-family:georgia,garamond,serif;font-size:30px"><span style="color: white">For the welfare of people.</span></h6>''',unsafe_allow_html=True)
with c3:
	# st.write('''<h5 style="font-family: Helvetica; font-size: 40px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;"><span style="color: black">Username</span></h1>''',unsafe_allow_html=True)
	acc_no= st.text_input('Account number:')
	passwd= st.text_input('Password:', type="password")
	# one,two,three=c3.columns([0.3,0.3,0.4])

	if st.button('Login'):
		t=0
		print("ll")
        # Clear the text_input widget
		data=sheet.get_all_values()
		# sheet.insert_row(["data1",text_input_value],len(data)+1)
		for i in range(1,len(data)):
			if data[i][0]==acc_no:
				if data[i][1]==passwd:
					# st.write('''<h5>Account is verified.</h5>''',unsafe_allow_html=True)
					st.success("Account is verified")
					t=1
					sheet.update_cell(1,1,acc_no)
					# data[i][1]=acc_no
					break
				# else:
				# 	st.error("Invalid Account Number/Password. Please try again.")
				# 	t=0
		else:
			st.error("Invalid Account Number/Password. Please try again.")
		if t==1:
			st.write('''
					<style>
					.button {
					background-image: linear-gradient(to right, #314755 0%, #26a0da  51%, #314755  100%);
					border: none;
					color: white;
					padding: 15px 30px;
					text-align: center;
					text-decoration: none;
					display: inline-block;
					font-size: 16px;
					margin: 3px 1px;
					transition-duration: 0.4s;
					cursor: pointer;
					border-radius: 13px;
					width: auto;
					}
					.button1 {
					background-image: linear-gradient(to right, #314755 0%, #26a0da  51%, #314755  100%);; 
					color: white; 
					border: 2px solid #314755;
					}
					.button1:hover {
					background-image: linear-gradient(to right, #314755 0%, #26a0da  51%, #314755  100%);
					color: white;
					}
					</style>
					<a  href="https://raamji24-web-design-digital-challan-o4lqgl.streamlit.app/" target="_self" > 
								<button class="button button1" style="margin-left:135px">
									Click to proceed
								</button>
							</a>
					''',
					unsafe_allow_html=True)

# st.write('''<h1 style="font-family: Helvetica; font-size: 40px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;"><span style="color: #FF7A59">Hello World!</span></h1>''',unsafe_allow_html=True)

