from plyer import notification
from bs4 import BeautifulSoup
import requests

URL = "https://www.mohfw.gov.in/" #using indiam website to fetch data because i was'nt able to find any us one :)
ICON_PATH = "C:\\Users\\HP\\Desktop\\Python\\covid-icon.ico"

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=ICON_PATH,
        timeout=5
    )

def get_covid_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_covid_data(html_data):
    if html_data:
        soup = BeautifulSoup(html_data, "html.parser")
        table = soup.find('table', {'id': 'state-data'})
        if table:
            rows = table.find_all('tr')[1:]  # Skip the header row
            stats = []
            for row in rows:
                columns = row.find_all('td')
                state_name = columns[1].text.strip()
                cases = columns[2].text.strip()
                deaths = columns[3].text.strip()
                stats.append(f"State: {state_name}\nCases: {cases}\nDeaths: {deaths}")
            return stats
        else:
            print("Table not found on the page.")
    else:
        print("No HTML data to parse.")
    return []

if __name__ == "__main":
    html_data = get_covid_data(URL)
    covid_stats = parse_covid_data(html_data)

    if covid_stats:
        for info in covid_stats:
            notify("COVID-19 Stats", info)
    else:
        print("No COVID-19 stats data available.")
