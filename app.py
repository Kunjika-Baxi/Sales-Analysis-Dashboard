import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import gdown

file_id = "1wZzbbgXaBYyp6M7nk39RpR36fI9MVQML"
url = f"https://drive.google.com/uc?id={file_id}"

# Download locally
output = "Sales_analysis.csv"
gdown.download(url, output, quiet=False)

# Read with pandas
df = pd.read_csv(output)
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])

df['Order_Year']=df['Order Date'].dt.year
df['Ship_Year']=df['Ship Date'].dt.year
df['Order_Month']=df['Order Date'].dt.month
df['Ship_Month']=df['Ship Date'].dt.month

def catp(p):
    if p<=100000:
        return 'Slow Performer'
    elif p>100000 and p<=800000:
        return 'Steady Sellers'
    else:
        return 'Star Performer'


def format_inr(num):
    return "{:,}".format(int(num))

df['Profit_Status']=df['Total Profit'].apply(catp)

st.title("Sales Analysis Dashboard")
st.sidebar.header("Filters")
shipyear=st.sidebar.selectbox("Select Ship Year",sorted(df['Ship_Year'].dropna().unique()))

filter_df=df[df['Ship_Year']==shipyear]
rdf=filter_df.groupby('Region')['Total Profit'].mean()
avgp=filter_df['Total Profit'].mean()
maxp=filter_df['Total Profit'].max()
maxpregion=filter_df['Region'][filter_df['Total Profit']==maxp]
maxpcountry=filter_df['Country'][filter_df['Total Profit']==maxp]

productsbymaxp=filter_df.groupby('Item Type')['Total Profit'].mean()
maxppro=productsbymaxp.sort_values(ascending=False).head(1)
maxppro_item = maxppro.index[0]
maxppro_value = round(maxppro.values[0], 2)

st.set_page_config(layout="wide")

col1,col2,col3,col4,col5=st.columns(5)
col1.metric("Average Profit",format_inr(avgp))
col2.metric("Maximum Profit",format_inr(maxp))
col3.markdown(
    f"""
    <div>
        <div>{"Max Profit Region"}</div>
        <div style="font-size:20px;">{maxpregion.iloc[0]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

col4.metric("Max Profit Country",maxpcountry.iloc[0])
col5.metric("Product that drives max profit",maxppro_item,maxppro_value)

col6,col7,col8,col9,col10=st.columns(5)
shm=filter_df.groupby('Ship_Month')['Total Profit'].mean()
shm.sort_index(inplace=True)

itemsprofit=filter_df.groupby('Item Type')['Total Profit'].mean()

with col9:
    fig1=px.bar(itemsprofit,title="Product wise Profit Distribution",color_discrete_sequence=['purple'])
with col6:
    fig2=px.line(shm,title="Profit Trend based on Shipment",color_discrete_sequence=['orange'])
with col7:
    ct=filter_df['Profit_Status'].value_counts()
    fig3=px.pie(ct,color_discrete_sequence=['purple','orange','yellow'],names=ct.index,values=ct.values,title="Profit Cateory")
with col10:
    stp=filter_df['Sales Channel'].value_counts()
    fig5=px.pie(stp,color_discrete_sequence=['orange','purple'],names=stp.index,values=stp.values,title="Online v/s Offline Sales")
with col8:
    ct=filter_df.groupby('Country')['Total Profit'].mean().reset_index()
    fig4=px.choropleth(ct,locations='Country',locationmode="country names",color_continuous_scale='plasma',color='Total Profit',title="Average Profit Country wise")
tab1,tab2, tab3, tab4, tab5 = st.tabs(["Products","Shipments","Categorical Distribution","GeoMaps","Sales Channel"])

with tab1:
    st.plotly_chart(fig1,use_container_width=True)
with tab2:
    st.plotly_chart(fig2,use_container_width=True)
with tab3:
    st.plotly_chart(fig3,use_container_width=True)
with tab4:
    st.plotly_chart(fig4,use_container_width=True)
with tab5:
    st.plotly_chart(fig5,use_container_width=True)




