import requests
from bs4 import BeautifulSoup

# Function to clean and extract text content from a webpage URL with GB2312 encoding
def extract_text_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'gb2312'  # Specify GB2312 encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the text content from the webpage, customize as needed
        text_content = soup.get_text()
        return text_content
    except Exception as e:
        print(f"Error extracting content from {url}: {e}")
        return None

# Create a list to store extracted content
all_text_content = []

# Define the range of years (1958 to 1979)
start_year = 1958
end_year = 1979

# Generate subpage URLs and extract content for each year
for year in range(start_year, end_year + 1):
    subpage_url = f"https://www.marxistphilosophy.org/Hongqi/{year}.htm"
    text_content = extract_text_from_page(subpage_url)
    if text_content:
        all_text_content.append(text_content)

# Combine all extracted content into one text
combined_text = "\n\n".join(all_text_content)

# Specify the encoding (UTF-8) and save the combined text to a text file
with open("hongqi-1958-1979-index.txt", "w", encoding="utf-8") as text_file:
    text_file.write("红旗\n")
    text_file.write("一九五八年创刊，一九七九年停刊\n")
    text_file.write("目录列表\n")
    text_file.write(combined_text)

print("Combined text saved to hongqi-1958-1979-index.txt")
