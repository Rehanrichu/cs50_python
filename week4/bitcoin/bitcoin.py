import sys
import requests

# Check command-line arguments
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Replace 'YourApiKey' with your actual CoinCap API key
API_KEY = "YourApiKey"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    price_usd = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request failed")
except (KeyError, ValueError):
    sys.exit("Error parsing response")

# Calculate total cost
total = bitcoins * price_usd

# Print formatted with thousands separator and 4 decimal places
print(f"${total:,.4f}")
