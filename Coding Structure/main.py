from data_loader import load_data
from Strategies import moving_average
from Strategies import buy_and_hold
from Strategies import mean_reversion
from backtester import run_backtest
from metrics import calculate_metrics
from dashboard import show_dashboard

data = load_data("AAPL")

strategy_name = "moving_average"

if strategy_name == "moving_average":
    data = moving_average.generate_signal(data)

elif strategy_name == "buy_and_hold":
    data = buy_and_hold.generate_signal(data)

elif strategy_name == "mean_reversion":
    data = mean_reversion.generate_signal(data)

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

show_dashboard(data, 10000)