import pandas as pd
import streamlit as st
import plotly.express as px

# Write the code for the Streamlit app
def write():
    st.title("Таҳлили фурӯши ҳармоҳаи тиҷорати электронӣ")
    uploaded_file = st.file_uploader("Маълумоти фурӯши худро ҳамчун файли CSV бор кунед", type=["csv"])
    if uploaded_file is not None:
        sales_data = pd.read_csv(uploaded_file)
        
        # Clean and transform the data
        sales_data.dropna(inplace=True)
        sales_data['date'] = pd.to_datetime(sales_data['date'])
        sales_data['month'] = sales_data['date'].dt.month
        
        # Aggregate the data by month
        monthly_sales = sales_data.groupby(['month'], as_index=False).sum()
        
        st.write("Ин панели идоракунӣ мебошад, ки маълумоти ҷамъшудаи фурӯшро аз рӯи моҳ нишон медиҳад.")
        
        # Line chart of total sales by month
        st.write("Диаграммаи хати фурӯши умумии фурӯш аз рӯи моҳ:")
        st.write(px.line(monthly_sales, x='month', y='sales'))
        
        # Bar chart of total sales by product
        st.write("Диаграммаи сатри умумии фурӯш аз рӯи маҳсулот:")
        product_sales = sales_data.groupby(['product'], as_index=False).sum()
        st.bar_chart(product_sales)
        
        # Pie chart of sales by region
        st.write("Диаграммаи фурӯш аз рӯи минтақа:")
        region_sales = sales_data.groupby(['region'], as_index=False).sum()
        st.write(px.pie(region_sales, values='sales', names='region'))

        # Histogram of product sales by month name
        st.write("Гистограммаи фурӯши маҳсулот аз рӯи номи моҳ:")
        product_monthly_sales = sales_data.groupby(['product', 'month'], as_index=False).sum()
        st.write(px.histogram(product_monthly_sales, x='month', y='sales', color='product'))
 

# Deploy the app
if __name__ == '__main__':
    write()
