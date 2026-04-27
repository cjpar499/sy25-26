import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin

# Checks robots.txt to see if scraping is allowed for the given URL
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
        print(f" Access Denied: {target_url} is restricted by robots.txt")
        return None
    return True

# Searches all book pages for a book with the exact title provided
def find_book_url(book_name, base_url):
    page = 1
    while True:
        # Construct the URL for the current catalogue page
        page_url = f"{base_url}/catalogue/page-{page}.html"
        headers = {'User-Agent': "EducationalScraperBot/1.0"}
        response = requests.get(page_url, headers=headers, timeout=900)
        if response.status_code != 200:
            print(f" Failed to fetch page {page}: {response.status_code}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')
        for article in articles:
            title = article.h3.a['title'].strip()
            # Compare the title (case-insensitive) to the user's input
            if title.lower() == book_name.lower():
                rel_url = article.h3.a['href']
                # Build the full URL to the book's detail page
                book_url = urljoin(f"{base_url}/catalogue/", rel_url)
                return book_url
        # Check if there is a next page; if not, stop searching
        next_btn = soup.find('li', class_='next')
        if not next_btn:
            break
        page += 1
    return None

# Extracts detailed information about a book from its detail page
def extract_book_details(book_url):
    headers = {'User-Agent': "EducationalScraperBot/1.0"}
    response = requests.get(book_url, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f" Failed to fetch book details: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the product information table and extract relevant fields
    table = soup.find('table', class_='table table-striped')
    details = {}
    if table:
        for row in table.find_all('tr'):
            heading = row.th.text.strip()
            value = row.td.text.strip()
            details[heading] = value

    # Extract availability information
    availability = soup.find('p', class_='instock availability')
    availability_text = availability.text.strip() if availability else "N/A"

    # Extract number of reviews
    num_reviews = details.get('Number of reviews', 'N/A')

    # Prepare and return all extracted details
    result = {
        'UPC': details.get('UPC', 'N/A'),
        'Price (excl. tax)': details.get('Price (excl. tax)', 'N/A'),
        'Price (incl. tax)': details.get('Price (incl. tax)', 'N/A'),
        'Tax': details.get('Tax', 'N/A'),
        'Availability': availability_text,
        'Number of reviews': num_reviews
    }
    return result

# Orchestrates the process of searching for a book and displaying its details
def lookup_book(book_name):
    base_url = "https://books.toscrape.com"
    # Check if scraping is allowed
    if not scrape_with_permission(base_url):
        return False

    print(f" Searching for book: '{book_name}' ...")
    # Find the book's detail page URL
    book_url = find_book_url(book_name, base_url)
    if not book_url:
        print("Invalid book name, try again")
        return False

    print(f" Book found: {book_url}")
    # Extract and display book details
    details = extract_book_details(book_url)
    if not details:
        print(" Failed to extract book details.")
        return False

    print("\n--- Book Details ---")
    print(f"1. UPC: {details['UPC']}")
    print(f"2. Price before tax: {details['Price (excl. tax)']}")
    print(f"3. Price after tax: {details['Price (incl. tax)']}")
    print(f"4. Cost of tax: {details['Tax']}")
    print(f"5. Availability: {details['Availability']}")
    print(f"6. Number of reviews: {details['Number of reviews']}")
    return True

# Main interactive loop: prompts user for book names and displays results
if __name__ == "__main__":
    while True:
        book_name = input("Enter the name of the book you want to search for (or type 'exit' to quit): ").strip()
        if book_name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if not lookup_book(book_name):
            continue