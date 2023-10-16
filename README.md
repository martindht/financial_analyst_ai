## Financial Analyst AI
[Still continuing to update to improve efficiency...]

## Overview
This project aims to generate stock outlook reports with up-to-date financial news data. It can generate two types of reports: Outlooks for Single Stocks and Competitor Analysis between Two Stocks. Since ChatGPT only contains data up to September 2021, fetching the most recent news online is necessary. The general steps of this project are as follows:

1. Fetch up-to-date news with Polygon.io API, obtain only the body paragraphs using BeautifulSoup, and save to the directory on a local machine
2. Index news using llama_index
3. Query news using llama_index
4. Run the Streamlit application and enter the stock ticker to generate the report and show the ticker.
   
Click on the image to see a video demonstration! 

## Single Stock Outlook
Click on the image to see a video demonstration! 
<a href="https://www.youtube.com/watch?v=TyIPcXmA3xo">
  <img src="/assets/single_outlook.jpg">
</a>

## Competitor Analysis
<a href="https://www.youtube.com/watch?v=QzaDO9fqMIc">
  <img src="/assets/comp_analysis.jpg">

  ## Potential Improvements in Future
  1. Use a different API for fetching news (instead of Polygon). Polygon works, however, there is only access to 3-5 different news websites in the free version. Additionally, Polyon does not group the news articles by ticker that well.
  2. Improve the entire fetch-index-query articles system. Right now, every time someone wants to generate an up-to-date stock report, they have to run those three programs with the stock ticker they want on their local machine. Make it so it will automatically fetch-index-query news articles based on user input on Streamlit and not have to access a local disk to generate reports.
