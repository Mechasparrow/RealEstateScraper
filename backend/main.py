import requests
from bs4 import BeautifulSoup
import json
from property import Property, PropertyEncoder

def perform_search(result_id, page=None):
    
    url = f'https://www.themlsonline.com/minnesota-real-estate/search/results/{result_id}'
    
    if (page != None):
        url = f'{url}/{page}'
    
    response = requests.get(url)
    search_soup = BeautifulSoup(response.content,features="html.parser")
    return search_soup

def parse_page_info(search_results: BeautifulSoup):
    listing_pager = search_soup.select_one('.pager').select('li')[1].text.split(' ')
    current_page = int(listing_pager[1])
    total_pages = int(listing_pager[3])

    return (current_page, total_pages)

def parse_listing(listing: BeautifulSoup):
    listing_body = listing.select_one(".panel-body")

    # Extract the data from the elements and store it in a data structure
    house_info = {}

    list_elements = listing_body.select_one('.list-1').select("li") + listing_body.select_one('.list-2').select("li")

    for item in list_elements:
        item_raw_text = item.text
        item_class = item.get("class")[1]

        if (item_class == 'financial'):
            item_raw_text = item.select('.price')[0].text
        elif (item_class == 'date'):
            item_raw_text = item.select_one('time').get("datetime")
        elif (item_class == 'data-group-2' and '\u2022' in item_raw_text):
            split_items = item_raw_text.split('\u2022')
            house_info["bedrooms"] = split_items[0].strip()
            house_info["bathrooms"] = split_items[1].strip()
            house_info["year_built"] = split_items[2].strip()
            continue
        elif (item_class == 'data-group-3' and '\u2022' in item_raw_text):
            split_items = item_raw_text.split('\u2022')
            house_info["square_feet"] = split_items[0].strip()
            house_info["acres"] = split_items[1].strip()
            continue
        elif (item_class == 'data-group-4'):
            item_class = "school_district"
            
        item_text = item_raw_text.replace('\n','').strip()

        house_info[item_class] = item_text
       
    return house_info
        
result_id = '3bd83cfeb2c186634c2ddb019b7f8ff'
search_soup = perform_search(result_id)
current_page, total_pages = parse_page_info(search_soup)

parsed_listings: list[Property] = []

while (current_page <= total_pages):
    print(f'Page {current_page}')
    
    listings = search_soup.select(".listing-lg.listing.panel")

    for listing in listings:
        parsed_listing = parse_listing(listing)
        prop: Property = Property.json_to_property(parsed_listing)
        parsed_listings.append(prop)

    if (current_page == total_pages):
        break

    search_soup = perform_search(result_id,current_page + 1)
    current_page, total_pages = parse_page_info(search_soup)


with open("house_info.json", "w") as f:
    json.dump(parsed_listings, f, indent=4, cls=PropertyEncoder)
