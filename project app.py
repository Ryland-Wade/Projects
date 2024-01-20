import streamlit as st 
import requests
import json
st.title("Do They Border?")
st.divider()
country1 = st.text_input("Enter one country here")  #New 
country2 = st.text_input("Enter the other here")  #New

def borders(c1,c2):
  try:
    r1=requests.get("https://restcountries.com/v3/all")
    data=r1.text
    data=json.loads(data)

    for item in data:
      if item["name"]["common"]==c1:
        c1data = item
        
      if item["name"]["common"]==c2:
        c2data = item
        

    if c1data["cca3"] in c2data["borders"]:
      st.text("They share a Border!")
    
    else:
      st.text("These two don't have any borders, sorry :()")


    b1=requests.get("https://restcountries.com/v3/all")
    datb=b1.text
    datb=json.loads(datb)
    llist=[]
    for c in datb:
      if c["name"]["common"]== country1:
        c1link = c["flags"][0]
        c1pic= f'<a><img src= {c1link} width=250 ></a>'
        st.markdown(c1pic, unsafe_allow_html = True)

      if c["name"]["common"]== country2:
        c2link = c["flags"][0]
        
        c2pic= f'<a><img src= {c2link} width =250 ></a>'
        st.markdown(c2pic, unsafe_allow_html = True)
  except:
    st.text("Please enter two countries with correct spelling and capitalization")

  


    
borders(country1,country2)

