# Used Cars Price Prediction in Tunisia

## I) Business Understanding
<div style="font-size:20px">1. Objective </div>  
<p style="font-size: 15px">Predict the price of a used car in Tunisia based on its specifications, mileage, and features to help 
sellers price their vehicles competitively 
or buyers make informed decisions.</p>
<div style="font-size:20px">2. Output </div>  
<p style="font-size: 15px">A machine learning model that predicts car prices based on available features.</p>

## II) Data Understanding
<div style="font-size: 20px"> 1. Data Source: <span style="font-size: 15px">automobiles.tn</span></div>
<div style="font-size: 20px">2. Tool Used for Scraping: <span style="font-size: 15px">BeautifulSoup</span></div>
<div style="font-size: 20px">3. Understanding the website structure</div>
<div style="font-size: 20px">4. Problems We met while scrapping:</div>
<ul style="font-size: 15px">
<li>Dynamic Pagination on the Website</li>
<li>Getting all the luxury features names</li>
<li>The website blocking our requests, so we tried the following:
<ul style="font-size: 15px">
<li>Wait before each request</li>
<li>Set headers, so the request looks like it's from a browser</li>
<li>Using ScraperAPI, it helped us to Send requests through a pool of proxies and ensures that the scraper does not use the same IP address repeatedly</li>
</ul>
</li>
</ul>