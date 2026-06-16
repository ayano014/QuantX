import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go 


def show_strategy_comparison(results_df):

    results_df["Abs_Drawdown"] = (
        results_df["Drawdown"].abs()*100
    )

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Returns (%)",
            "Sharpe Ratio",
            "Max Drawdown (%)",
            "CAGR (%)"
        )
    )

    fig.add_trace(
        go.Bar(
            x=results_df["Strategy"],
            y=results_df["Return"],
            text=results_df["Return"].round(2),
            name="Return"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=results_df["Strategy"],
            y=results_df["Sharpe"],
            text=results_df["Sharpe"].round(2),
            name="Sharpe"
        ),
        row=1,
        col=2
    )

    fig.add_trace(
        go.Bar(
            x=results_df["Strategy"],
            y=results_df["Abs_Drawdown"],
            text=results_df["Abs_Drawdown"].round(2),
            name="Drawdown"
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=results_df["Strategy"],
            y=results_df["CAGR"],
            text=results_df["CAGR"].round(2),
            name="CAGR"
        ),
        row=2,
        col=2
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title="QuantX Research Dashboard",
        height=800,
        showlegend=False
    )

    fig.show()