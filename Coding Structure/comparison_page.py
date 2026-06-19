import pandas as pd

from Strategies import (
    moving_average,
    buy_and_hold,
    mean_reversion
)

from data_loader import load_data
from backtester import run_backtest
from metrics import calculate_metrics


def run_comparison():

    strategies = {
        "Moving Average": moving_average,
        "Buy & Hold": buy_and_hold,
        "Mean Reversion": mean_reversion
    }

    data = load_data("AAPL")

    results = []

    for name, strategy in strategies.items():

        strategy_data = data.copy()

        strategy_data = strategy.generate_signal(
            strategy_data
        )

        strategy_data = run_backtest(
            strategy_data,
            10000
        )

        (
            total_return,
            sharpe,
            max_drawdown,
            cagr,
            volatility,
            win_rate
        ) = calculate_metrics(
            strategy_data,
            10000
        )

        results.append({
            "Strategy": name,
            "Return": total_return,
            "Sharpe": sharpe,
            "Drawdown": max_drawdown,
            "CAGR": cagr,
            "Volatility": volatility,
            "Win Rate": win_rate
        })

    results_df = pd.DataFrame(results)

    return results_df