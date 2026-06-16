from Strategies import moving_average
from Strategies import buy_and_hold
from Strategies import mean_reversion

from data_loader import load_data
from backtester import run_backtest
from metrics import calculate_metrics
from dashboard_compare import show_strategy_comparison
from equity_dashboard import show_equity_curves

def compare_strategies():

    equity_curves = {}

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

        equity_curves[name] = strategy_data.copy()

        total_return, sharpe, max_drawdown, cagr, volatility, win_rate = (
            calculate_metrics(
                strategy_data,
                10000
            )
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

        print(
            f"CAGR: {cagr:.2f}%"
        )

        print(
            f"Volatility: {volatility:.2f}%"
        )

        print(
            f"Win Rate: {win_rate:.2f}%"
        )

    import pandas as pd

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="Return",
        ascending=False
    )

    print("\n")
    print(results_df)
    show_strategy_comparison(results_df)

    show_equity_curves(
        equity_curves
    )
    
    winner = results_df.iloc[0]

    print("\nBEST STRATEGY")
    print(f"Strategy: {winner['Strategy']}")
    print(f"Return: {winner['Return']:.2f}%")
    print(f"Sharpe: {winner['Sharpe']:.2f}")
    print(f"Drawdown: {winner['Drawdown']:.2%}")
    print(f"CAGR: {winner['CAGR']:.2f}%")
compare_strategies()
