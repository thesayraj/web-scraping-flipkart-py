import bs4
import requests
import csv


def make_soup(url):
    result = requests.get(url)
    print(result.status_code)
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    return soup


def find(soup):
    # based on different categories of products there are different class names used on the site
    names = soup.find_all('div', class_="_4rR01T")
    if len(names) == 0:
        names = soup.find_all('a', class_="s1Q9rs")
    if len(names) == 0:
        names = soup.find_all('a', class_="IRpwTa")

    prices = soup.find_all('div', class_="_30jeq3")
    offers = soup.find_all('div', class_="_3Ay6Sb")

    return names, prices, offers


def scrape(search_string):
    soup = make_soup("https://www.flipkart.com/search?q="+search_string)
    names, prices, offers = find(soup)

    if len(names) == 0:
        return
    return names, prices, offers


def scraper(search_string):
    names, prices, offers = ([], [], [])
    result = scrape(search_string)  # page 1 result
    if result is not None:
        names, prices, offers = result
        # go for page 2
        page2_names, page2_prices, page2_offers = ([], [], [])
        page2_result = scrape(search_string+"&page=2")  # page2 result
        if page2_result is not None:
            page2_names, page2_prices, page2_offers = page2_result
            page1_names = result[0]
            page1_prices = result[1]
            page1_offers = result[2]

            # combine all respective results from page1 and page2 in respective single lists
            names = page1_names + page2_names
            prices = page1_prices + page2_prices
            offers = page1_offers + page2_offers

        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price(in INR)", "Offer"])

            for name, price, offer in zip(names, prices, offers):
                writer.writerow([name.text, price.text[1:], offer.text])

    else:
        print("sorry no results found")


# scraper("table")
# scraper("macbook")
# scraper("kjasjfkljdskfjweljlfksdjfkjdslkfjklfs") #no results


if __name__ == "__main__":
    search_string = input("")
    scraper(search_string)
