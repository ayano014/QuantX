from data_loader import load_data
from Strategies import moving_average
from Strategies import buy_and_hold
from Strategies import mean_reversion
from backtester import run_backtest
from metrics import calculate_metrics
from dashboard import show_dashboard

strategies = {
    "moving_average": moving_average,
    "buy_and_hold": buy_and_hold,
    "mean_reversion": mean_reversion
}

data = load_data("AAPL")

strategy_name = "moving_average"

strategy = strategies[strategy_name]

data = strategy.generate_signal(data)

data = run_backtest(
    data,
    initial_cash=10000
)

(
    total_return,
    sharpe,
    max_drawdown,
    cagr,
    volatility,
    win_rate
) = calculate_metrics(data, 10000)

print(f"Return: {total_return:.2f}%")
print(f"Sharpe: {sharpe:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")
print(f"CAGR: {cagr:.2f}%")
print(f"Volatility: {volatility:.2f}%")
print(f"Win Rate: {win_rate:.2f}%")

show_dashboard(data, 10000)