"""
CoinGecko cryptocurrency market data utilities.
https://www.coingecko.com/
"""

import requests

BASE_URL = "https://api.coingecko.com/api/v3"


# ---------------------------------------------------------------------------
# Shared helpers (extracted to eliminate duplication)
# ---------------------------------------------------------------------------

def _get(endpoint, params=None):
    """Make a GET request to the CoinGecko API and return parsed JSON."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params, timeout=10)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as exc:
        raise requests.exceptions.HTTPError(
            f"CoinGecko API error for {url} (status {response.status_code}): {exc}"
        ) from exc
    return response.json()


def _format_price(coin_id, price, currency):
    """Return a human-readable price string for a coin."""
    return f"{coin_id.capitalize()}: {price:,.2f} {currency.upper()}"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_coin_price(coin_id, vs_currency="usd"):
    """Return the current price of *coin_id* in *vs_currency*."""
    data = _get("/simple/price", params={"ids": coin_id, "vs_currencies": vs_currency})
    if coin_id not in data:
        raise ValueError(f"Coin '{coin_id}' not found in CoinGecko response.")
    if vs_currency not in data[coin_id]:
        raise ValueError(f"Currency '{vs_currency}' not found for coin '{coin_id}'.")
    return data[coin_id][vs_currency]


def get_coin_market_data(coin_id):
    """Return market data (price, market cap, 24 h change) for *coin_id*."""
    data = _get(f"/coins/{coin_id}", params={"localization": "false", "tickers": "false",
                                              "community_data": "false", "developer_data": "false"})
    market = data["market_data"]
    return {
        "price_usd": market["current_price"]["usd"],
        "market_cap_usd": market["market_cap"]["usd"],
        "price_change_24h": market["price_change_percentage_24h"],
    }


def get_prices(coin_ids, vs_currency="usd"):
    """Return a dict mapping each coin in *coin_ids* to its current price."""
    ids_param = ",".join(coin_ids)
    data = _get("/simple/price", params={"ids": ids_param, "vs_currencies": vs_currency})
    prices = {}
    for coin in coin_ids:
        if coin not in data:
            raise ValueError(f"Coin '{coin}' not found in CoinGecko response.")
        if vs_currency not in data[coin]:
            raise ValueError(f"Currency '{vs_currency}' not found for coin '{coin}'.")
        prices[coin] = data[coin][vs_currency]
    return prices


def display_prices(coin_ids, vs_currency="usd"):
    """Print the current price for each coin in *coin_ids*."""
    prices = get_prices(coin_ids, vs_currency)
    for coin_id, price in prices.items():
        print(_format_price(coin_id, price, vs_currency))


def display_market_summary(coin_ids):
    """Print a market summary (price, market cap, 24 h change) for each coin."""
    for coin_id in coin_ids:
        data = get_coin_market_data(coin_id)
        print(
            f"{coin_id.capitalize():12s} | "
            f"Price: ${data['price_usd']:>12,.2f} | "
            f"Market cap: ${data['market_cap_usd']:>18,.0f} | "
            f"24 h: {data['price_change_24h']:+.2f}%"
        )


if __name__ == "__main__":
    COINS = ["bitcoin", "ethereum", "litecoin"]
    print("=== Current Prices ===")
    display_prices(COINS)
    print()
    print("=== Market Summary ===")
    display_market_summary(COINS)
