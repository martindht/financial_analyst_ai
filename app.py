import os, config
import openai
import streamlit as st
from llama_index import ServiceContext, LLMPredictor
from langchain.chat_models import ChatOpenAI
from llama_index import StorageContext, load_index_from_storage


os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY
openai.api_key = os.environ.get('OPENAI_API_KEY')

llm = ChatOpenAI(model_name='gpt-4', max_tokens=6000)
llm_predictor = LLMPredictor(llm=llm)

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

st.sidebar.title('Financial Analyst AI')
st.sidebar.header('Financial Report')

report = st.sidebar.selectbox(
    'What type of report do you want?',
    ('Single Stock Outlook', 'Competitor Analysis'))

if report == 'Single Stock Outlook':
    symbol = st.sidebar.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f'Generating report for {symbol}...'):
            response = query_engine.query(f"Write a report on the outlook for"
                                          f" {symbol} stock from the years 2023-2027. Be sure to include potential risks and headwinds.")
            response_text = response.response
            st.title(f"Single Stock Outlook for {symbol}")
            st.write(response_text)
            st.image(f"https://finviz.com/chart.ashx?t={symbol}")


if report == 'Competitor Analysis':
    symbol1 = st.sidebar.text_input("Stock Symbol 1")
    symbol2 = st.sidebar.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f'Generating report for {symbol1} vs. {symbol2}...'):
            response = query_engine.query(f"Write a report with a comparison between {symbol1} stock and {symbol2} stock. "
                                          f"Be as detailed as possible with the information provided, including "
                                          f"various factors that may affect the current/future price, potential risks for both, and more.")
            response_text = response.response
            st.title(f"Competitor Analysis between {symbol1} and {symbol2}")
            st.write(response_text)
            st.image(f"https://finviz.com/chart.ashx?t={symbol1}")
            st.image(f"https://finviz.com/chart.ashx?t={symbol2}")

