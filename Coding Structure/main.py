from data_loader import load_data
from Strategies.moving_average import generate_signal
from backtester import run_backtest
from metrics import calculate_metrics


data = load_data("AAPL")

data = generate_signal(data)

data = run_backtest(data, initial_cash=10000)

total_return, sharpe, max_drawdown = (
    calculate_metrics(data,10000)
)

print(f"Return: {total_return:.2f}%")
print(f"Sharpe: {sharpe:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")

print(
    data[
        [
            "Close",
            "Signal",
            "Portfolio"
        ]
    ].tail()
)