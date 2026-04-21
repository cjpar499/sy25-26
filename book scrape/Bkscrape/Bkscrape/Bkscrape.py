import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin

def scrape_with_permission(target_url):
    user_agent = "EducationalScraperBot/1.0"
    parsed_url = urlparse(target_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    robots_url = f"{base_url}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_url)

    try:
        rp.read()
        can_scrape = rp.can_fetch(user_agent, target_url)
    except Exception as e:
        print(f"Could not read robots.txt ({e}), proceeding with caution...")
        can_scrape = True

    if not can_scrape:
        print(f"🚫 Access Denied: {target_url} is restricted by robots.txt")
        return None
    return True

def find_book_url(book_name, base_url):
    # Search all pages for the book
    page = 1
    while True:
        page_url = f"{base_url}/catalogue/page-{page}.html"
        headers = {'User-Agent': "EducationalScraperBot/1.0"}
        response = requests.get(page_url, headers=headers, timeout=900)
        if response.status_code != 200:
            print(f"❌ Failed to fetch page {page}: {response.status_code}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')
        for article in articles:
            title = article.h3.a['title'].strip()
            if title.lower() == book_name.lower():
                rel_url = article.h3.a['href']
                # Normalize relative URL
                book_url = urljoin(f"{base_url}/catalogue/", rel_url)
                return book_url
        # Check if there is a next page
        next_btn = soup.find('li', class_='next')
        if not next_btn:
            break
        page += 1
    return None

def extract_book_details(book_url):
    headers = {'User-Agent': "EducationalScraperBot/1.0"}
    response = requests.get(book_url, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f"❌ Failed to fetch book details: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product information table
    table = soup.find('table', class_='table table-striped')
    details = {}
    if table:
        for row in table.find_all('tr'):
            heading = row.th.text.strip()
            value = row.td.text.strip()
            details[heading] = value

    # Extract availability
    availability = soup.find('p', class_='instock availability')
    availability_text = availability.text.strip() if availability else "N/A"

    # Extract number of reviews
    num_reviews = details.get('Number of reviews', 'N/A')

    # Prepare results
    result = {
        'UPC': details.get('UPC', 'N/A'),
        'Price (excl. tax)': details.get('Price (excl. tax)', 'N/A'),
        'Price (incl. tax)': details.get('Price (incl. tax)', 'N/A'),
        'Tax': details.get('Tax', 'N/A'),
        'Availability': availability_text,
        'Number of reviews': num_reviews
    }
    return result

def lookup_book(book_name):
    base_url = "https://books.toscrape.com"
    if not scrape_with_permission(base_url):
        return False

    print(f"🔎 Searching for book: '{book_name}' ...")
    book_url = find_book_url(book_name, base_url)
    if not book_url:
        print("Invalid book name, try again")
        return False

    print(f"✅ Book found: {book_url}")
    details = extract_book_details(book_url)
    if not details:
        print("❌ Failed to extract book details.")
        return False

    print("\n--- Book Details ---")
    print(f"1. UPC: {details['UPC']}")
    print(f"2. Price before tax: {details['Price (excl. tax)']}")
    print(f"3. Price after tax: {details['Price (incl. tax)']}")
    print(f"4. Cost of tax: {details['Tax']}")
    print(f"5. Availability: {details['Availability']}")
    print(f"6. Number of reviews: {details['Number of reviews']}")
    return True

if __name__ == "__main__":
    while True:
        book_name = input("Enter the name of the book you want to search for (or type 'exit' to quit): ").strip()
        if book_name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if not lookup_book(book_name):
            continue