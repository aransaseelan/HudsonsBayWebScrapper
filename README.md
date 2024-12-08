## What is the Hudsons Bay Web Scrapper

The Hudson Bay web scrapper will be a Python, Selenium-based web crawler looking for discount and clearance sales. 
You can add your favourite brands and see if they reach a certain discount threshold. If they do, you will be pinged, and the information will be added to a database.  
My goal is to be able to input some keywords and check if any of those keywords match the item and discount you are looking for.

## Use case and Benefit of this product 

People will be able to get their products when they're at the best price on Hudson Bay. 

## Bot Protections

Hudson's Bay's bot protection doesn't seem too strong, as I was able to make a scrapper with Python and Selenium without trying to bypass any of their anti-bot measures. 
The use of proxies is recommended as Hudsons Bay is likely to ban IPs that are scrapping from their website. 
It seems like their products are being put on the server side, so I couldn't find any apis that I could call, which would have made this much more efficient.
