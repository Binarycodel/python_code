import streamlit as st
import pandas as pd


st.set_page_config(page_title="Home" , page_icon='📈')

c1 , c2 = st.columns([3,1])
c1.text_input('', label_visibility='collapsed', value ='Search drugs')
c2.button('Search')
st.markdown('## Nigeria Drug Discovery and Distribution.')



detail_tab , dist_tab, Reg_tab, Auth_tab = st.tabs(['Details', 'Distribute Drug', 'Register Drugs', 'Authenticate Drug'])

# import data
with detail_tab:
    
    data  = pd.read_csv('datasource/drug_data_mini.csv')
    
    for index in range(len(data)):
        tup_list = tuple(data.iloc[index].values)
        print(tup_list)
        d, name ,  medtype, ingredient, address, manufacturer = tup_list
        img_col , detail_col = st.columns([2,3])
        img_col.image('image/drug2.jpg' , width=200)
        
        with detail_col.container():
            # detail_col

            

            detail_col.write(f'NAME : {name.title()}')
            detail_col.write(f'MEDICATION TYPE : {medtype.title()}')
            detail_col.write(f'INGREDIENT : {ingredient.title()}')
            detail_col.write(f'ADDRESS : {address.title()}')
            detail_col.write(f'MANUFACTURE : {manufacturer.title()}')
            # detail_col.write(f'DRUG WALLET')
        txtbox , btn = st.columns([2,1])
        # txtbox.text_input('', label_visibility='collapsed', value ='Drug Value', key=index)
        # btn.button('Send', key= f'b{index}')

    
with dist_tab:
    # data  = pd.read_csv('datasource/drug_data_mini.csv')
    # st.dataframe(data)
    with st.form('dist_form', clear_on_submit=True):
        
        st.subheader('Distribute Drug using Public key Address')

        st.text_input('Quatity of Drugs')
        st.text_area('Wallet Address')

        submit_but = st.form_submit_button('Send Drug')

        if submit_but:
            st.write('successfully')



with Reg_tab:
    with st.form('Reg_form', clear_on_submit=True):
        
        st.subheader('Registered Drugs')

        st.text_input('Drug Name')
        st.text_input('Medication Type')
        st.text_input('Ingredient')
        st.text_area('Manufacturere')
        st.text_area('Address')

        submit_but = st.form_submit_button('Register')

        if submit_but:
            st.write('successfully') 


with Auth_tab:
    with st.form('Auth_form', clear_on_submit=True):
        st.subheader('Registered Drugs')
        st.text_area('Public Key Address')

        submit_but = st.form_submit_button('Authenticate')

        if submit_but:
            st.write('successfully') 

    

    
    