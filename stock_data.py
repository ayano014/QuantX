import yfinance as yf

initial_cash = 10000

data = yf.download("AAPL", period="1y")

data["MA20"] = data["Close"].rolling(20).mean()

data["MA50"] = data["Close"].rolling(50).mean()

data["Signal"] = 0

# Signal generation

data.loc[data["MA20"] > data["MA50"], "Signal"] = 1
data["Position"] = data["Signal"]
data["Returns"] = data["Close"].pct_change()

data["Strategy_Returns"] = (
    data["Position"].shift(1)
    *data["Returns"]
)

#portfolio value calculation

data["Portfolio"] = (
    1 + data["Strategy_Returns"]
).cumprod() * initial_cash

data = data.dropna()
print("Rows remaining:", len(data))

final_value = data["Portfolio"].iloc[-1]
print("Final Portfolio Value: ", final_value)

#return calculation

total_return = (
    (final_value - initial_cash)/initial_cash
)*100

#sharpe ratio calculation

sharpe = (
    data["Strategy_Returns"].mean()/data["Strategy_Returns"].std()
)* (252**0.5)

print(f"Sharpe: {sharpe:.2f}")
print(f"Total Return: {total_return:.2f}%")

#max drawdown calculation

rolling_max = data["Portfolio"].cummax()

drawdown = (data["Portfolio"] - rolling_max)/rolling_max

max_drawdown = drawdown.min()
print(f"Max Drawdown: {max_drawdown:.2%}")

print(data[["Close",
            "Signal",
            "Position",
            "Returns",
            "Strategy_Returns",
            "Portfolio"
]].tail(10))

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["Portfolio"],
        mode="lines",
        name="Portfolio value"
    )
)

fig.update_layout(
    title="Quantx Equity Curve",
    xaxis_title="Date",
    yaxis_title="Portfolio Value ($)"
)
fig.show()