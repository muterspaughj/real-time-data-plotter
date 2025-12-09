"""
main.py
----------------------------------------
Runs the Real-Time Crypto Price Plotter program.
Handles user input and starts the plotting loop.
Author: Jack Muterspaugh
"""

from get_crypto import GetCrypto
from real_time_plotter import RealTimePlotter

def main():
    coin = input("Enter crypto (BTC, ETH, etc.) (default: BTC): ")

    # If nothing is entered, BTC will be default
    if not coin.strip():
        coin = "BTC"

    crypto = GetCrypto(coin)
    plotter = RealTimePlotter(crypto)

    print(f"Starting plot for {coin}...")
    plotter.start()

if __name__ == "__main__":
    main()