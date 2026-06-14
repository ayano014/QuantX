from Strategies import moving_average
from Strategies import buy_and_hold
from Strategies import mean_reversion

from data_loader import load_data
from backtester import run_backtest
from metrics import calculate_metrics

def compare_strategies():

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

        total_return, sharpe, max_drawdown = (
            calculate_metrics(
                strategy_data,
                10000
            )
        )

        results.append({
            "Strategy": name,
            "Return": total_return,
            "Sharpe": sharpe,
            "Drawdown": max_drawdown
        })

        print("\n-----------------------------")
        print(name)
        print("-------------------------------")

        print(
            f"Return:{total_return:.2f}%"
        )

        print(
            f"Sharpe:{sharpe:.2f}"
        )

        print(
            f"Drawdown: {max_drawdown:.2%}"
        )
        
    import pandas as pd

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="Return",
        ascending=False
    )

    print("\n")
    print(results_df)

compare_strategies()
