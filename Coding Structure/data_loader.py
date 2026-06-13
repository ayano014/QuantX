import yfinance as yf

def load_data(ticker):

    data = yf.download(ticker, period="1y")

    data.columns = data.columns.droplevel(1)

    return data