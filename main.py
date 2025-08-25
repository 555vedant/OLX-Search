import requests
from bs4 import BeautifulSoup

def fetch_car_covers():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("li.EIR5N")

    results = [item.get_text(" ", strip=True) for item in items]
    return results

def save_results(results, filename="olx_car_cover_results.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")
    print(f"Saved {len(results)} results to {filename}")

if __name__ == "__main__":
    car_covers = fetch_car_covers()
    save_results(car_covers)
