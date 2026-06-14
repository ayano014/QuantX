import plotly.express as px

def show_strategy_comparison(results_df):

    fig_return = px.bar(
        results_df,
        x="Strategy",
        y="Return",
        title="Strategy Returns (%)",
        text=results_df["Return"].round(2)
    )

    fig_return.update_traces(
        textposition="outside"
    )

    fig_return.show()

    fig_sharpe = px.bar(
        results_df,
        x="Strategy",
        y="Sharpe",
        title="Sharpe Ratio",
        text=results_df["Sharpe"].round(2)
    )

    fig_sharpe.update_traces(
        textposition="outside"
    )

    fig_sharpe.show()
    
    results_df["Abs_Drawdown"] = (
        results_df["Drawdown"].abs() * 100
    )

    fig_drawdown = px.bar(
        results_df,
        x="Strategy",
        y="Abs_Drawdown",
        title="Max Drawdown (%)",
        text=results_df["Abs_Drawdown"].round(2)
    )

    fig_drawdown.update_traces(
        textposition="outside"
    )

    fig_drawdown.show()
