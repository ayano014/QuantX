import yfinance as yf

def load_data(ticker):
    
    data = yf.download(ticker, period="1y")

    return data