import yfinance as yf
import plotly.graph_objects as go

def show_dashboard(data, initial_cash):

    spy = yf.download("SPY", period="1y")

    spy["Returns"] = spy["Close"].pct_change()

    spy["Portfolio"] = (
        1 + spy["Returns"]
    ).cumprod() * initial_cash

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Portfolio"],
            mode="lines",
            name="QuantX Strategy"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=spy.index,
            y=spy["Portfolio"],
            mode="lines",
            name="SPY Buy & Hold"
        )
    )

    fig.update_layout(
        title="QuantX Dashboard",
        xaxis_title="Date",
        yaxis_title="Portfolio Value ($)"
    )

    fig.show()