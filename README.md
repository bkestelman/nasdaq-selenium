# nasdaq-selenium
Collect historical stock data from nasdaq using selenium

```
python hello.py
python nasdaq.py
```

hello.py contains selenium's variant on "Hello World," which opens Firefox, goes to google.com, and searches for "Cheese!"

nasdaq.py goes to nasdaq's website and downloads historical data as .csv's for a list of stocks (taken from eTrade's list of commission-free ETF's). 

Contains some simple error checking with a timeout if a download is unsuccessful. 
