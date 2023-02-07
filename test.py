import pandas as pd
import streamlit as st
import pyTigerGraph as tg

Domain = "https://fraud-demo.i.tgcloud.io"
Graph = "Fraud"
Secret = "o98ha1r06p1rh5t1uhqkak9svsikof0p"
conn = tg.TigerGraphConnection(host=Domain, graphname=Graph, gsqlSecret=Secret)
 
authToken = conn.getToken(Secret)
authToken = authToken[0]

st.title("Streamlit test Web app")

uploaded_file=st.text_input("Please provide a account number",value='C1557090372')

bob = conn.runInstalledQuery(queryName = "output", params={"id":uploaded_file})

df=pd.DataFrame(columns=["acc_no","hops","cid","in_giant_component"])
acc_no=[]
hops=[]
cid=[]
in_giant_component=[]

for i in range(len(bob[0]["output"])):
    value=bob[0]["output"][i]['attributes']
    acc_no.append(value['id'])
    hops.append(value['hops'])
    cid.append(value['cid'])
    in_giant_component.append([value['in_giant_component']])
    
    

df["acc_no"]=acc_no
df["hops"]=hops
df['cid']=cid
df['in_giant_component']=in_giant_component

st.header("Account Details")
st.dataframe(df)
