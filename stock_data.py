import yfinance as yf

initial_cash = 10000

data = yf.download("AAPL", period="1y")

data["MA20"] = data["Close"].rolling(20).mean()

data["MA50"] = data["Close"].rolling(50).mean()

data["Signal"] = 0

data.loc[data["MA20"] > data["MA50"], "Signal"] = 1
data["Position"] = data["Signal"]
data["Returns"] = data["Close"].pct_change()

data["Strategy_Returns"] = (
    data["Position"].shift(1)
    *data["Returns"]
)

data["Portfolio"] = (
    1 + data["Strategy_Returns"]
).cumprod() * initial_cash

data = data.dropna()
print("Rows remaining:", len(data))

final_value = data["Portfolio"].iloc[-1]
print("Final Portfolio Value: ", final_value)

total_return = (
    (final_value - initial_cash)/initial_cash
)*100

print(f"Total Return: {total_return:.2f}%")

print(data[["Close",
            "Signal",
            "Position",
            "Returns",
            "Strategy_Returns",
            "Portfolio"
]].tail(10))

