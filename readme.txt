Scraping product info(title,price and offer) from 'flipkart.com' based on search_string
___________________________________________________________________________________________________


Summary
--------
 Use requests module to make request to site and get
 response.
 Use BeautifulSoup to parse the received data so
 that it can be scraped.
 After scraping save the data in a csv file.
 ___________________________________________________________________________________________



What the program does

>
    Takes input from user for what product to scrape. 

>
    calls scraper() function with given input string.
        -- The scraper() function calls scrape()
                which makes soup by calling make_soup().
                Then gets info(names, prices, offers) from soup using the find() function

        -- If there is no result from
        page1 then we do not go for page2.
        Otherwise just get result from page2.

        -- After this we combine all results from page1 and page2.
        And store the results in csv file.
            The result is written row by row to the csv file.
            Each row is of format ["Name", "Price", "Offer"]



function 'make_soup'
----------------
  makes the soup from url. It involves making request to the url
 and making soup from received data so that it can be scraped.

 function 'find' 
 ----------------
  takes the 'soup' and finds the data
 we need from the page.
 


 _______________________________________________________________________________
 Challenges:

 >   There were different class names used
    for displaying the name data of different kind of product.
    I was having no results when I searched for different kind of products.
    It took me about 30 mins to figure out that there are basically 3 classes
    used for displaying names of products of different categories.
    
    So the find function starts finding for a class_name
    if there is no name found using that class,
    then different class name used and so on upto 3rd class_name.

    After getting names we scrape prices. 
    Prices are using same class over the website.
    Same goes for the offers.

    At the end we return names,prices and offers.


>   While writing the price there was a problem.
    It was a unicode error because of rupee symbol.
    For now I just simply escaped it and stored the price without
    rupee symbol using
            price.text[1:]


______________________________________________________________________________________


It took me about 2-3 hours in total to get everything working properly.