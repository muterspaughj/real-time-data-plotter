"""
real-time-plotter.py
----------------------------------------
Contains the RealTimePlotter class, which stores
price data and displays a live updating matplotlib plot.
Author: Jack Muterspaugh
"""

import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates

class RealTimePlotter:
    def __init__(self, retrieve, interval=1.0):
        self.retrieve = retrieve # Used to get price
        self.interval = interval # Amount of time between updates
        self.prices = []
        self.timestamps = []

    # Starts the live plot
    def start(self):
        plt.ion() # Turns on interactive mode
        fig, ax = plt.subplots()

        try:
            while True:
                price = self.retrieve.get_price()

                self.prices.append(price)
                self.timestamps.append(datetime.now())

                ax.clear()
                ax.plot(self.timestamps, self.prices, linewidth=2)
                ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
                ax.set_title(f"Real-time Price for {self.retrieve.coin}")
                ax.set_xlabel("Time")
                ax.set_ylabel("Price (USD)")
                plt.tight_layout()
                plt.pause(0.01)
                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("\nPlotting stopped.")
            plt.close(fig)
        