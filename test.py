import yfinance as yf
import pandas as pd
import time

#amd = yf.Ticker("AMD")
#time.sleep(5)
#amd_share_data = amd.history(period = "1d")
#amd_share_data.plot(x = "Date", y = "Open")

data = yf.download("AAPL", period = "1d")
print(data)
