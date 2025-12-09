# Real-Time Crypto Price Plotter

A Python program that fetches real-time cryptocurrency prices from the Coinbase API and plots them live using `matplotlib`. Users can choose which cryptocurrency to track (BTC, ETH, etc.), and the plot updates continuously until stopped.  

## Features
- Pulls real-time crypto prices from Coinbase  
- Live-updating plot using `matplotlib`  
- User selects which coin to track  
- Cross-platform (Mac and Windows)  

## File Structure
- `get_crypto.py` → Fetches live crypto prices  
- `real_time_plotter.py` → Stores data and plots it live  
- `main.py` → Handles user input and runs the program  

## Setup

### 1. Extract the zip file
Unzip the downloaded file to a location of your choice.

### 2. Create the Conda environment
Make sure you have **Conda installed**.  
Navigate to the **real-time-data-plotter-main** directory and run this command:

```bash
conda env create -f environment.yml
```

### 3. Activate the environment

```bash
conda activate rtdp
```

### 4. Run the program
```bash
python main.py
```
