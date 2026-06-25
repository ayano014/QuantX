import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from comparison_page import run_comparison
from data_loader import load_data
from backtester import run_backtest
from metrics import calculate_metrics

from Strategies import (
    moving_average,
    buy_and_hold,
    mean_reversion
)

st.set_page_config(
    page_title="QuantX",
    layout="wide"
)

page = st.sidebar.selectbox(
    "Page",
    [
        "Single Strategy",
        "Strategy Comparison"
    ]
)

strategies = {
    "moving_average": moving_average,
    "buy_and_hold": buy_and_hold,
    "mean_reversion": mean_reversion
}

# ==========================
# SINGLE STRATEGY PAGE
# ==========================

if page == "Single Strategy":

    st.title("📈 QuantX")

    strategy = st.selectbox(
        "Choose Strategy",
        [
            "moving_average",
            "buy_and_hold",
            "mean_reversion"
        ]
    )

    ticker = st.text_input(
        "Ticker",
        value="AAPL"
    )

    capital = st.number_input(
        "Initial Capital",
        value=10000
    )

    if st.button("Run Backtest"):

        data = load_data(ticker)

        strategy_module = strategies[
            strategy
        ]

        data = strategy_module.generate_signal(
            data
        )

        data = run_backtest(
            data,
            capital
        )

        (
            total_return,
            sharpe,
            max_drawdown,
            cagr,
            volatility,
            win_rate
        ) = calculate_metrics(
            data,
            capital
        )

        benchmark = (
            data["Close"]
            / data["Close"].iloc[0]
        ) * capital

        st.success(
            "Backtest Complete"
        )

        st.subheader(
            "Performance Metrics"
        )

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        col1.metric(
            "Return",
            f"{total_return:.2f}%"
        )

        col2.metric(
            "Sharpe",
            f"{sharpe:.2f}"
        )

        col3.metric(
            "Drawdown",
            f"{max_drawdown:.2%}"
        )

        col4.metric(
            "CAGR",
            f"{cagr:.2f}%"
        )

        col5.metric(
            "Volatility",
            f"{volatility:.2f}%"
        )

        col6.metric(
            "Win Rate",
            f"{win_rate:.2f}%"
        )

        st.subheader(
            "Strategy vs Benchmark"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Portfolio"],
                mode="lines",
                name=strategy
            )
        )

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=benchmark,
                mode="lines",
                name="Buy & Hold"
            )
        )

        fig.update_layout(
            title=f"{ticker} - {strategy}",
            xaxis_title="Date",
            yaxis_title="Portfolio Value ($)",
            height=600,
            hovermode="x unified"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        results_df = pd.DataFrame({
            "Strategy": [strategy],
            "Return": [total_return],
            "Sharpe": [sharpe],
            "Drawdown": [max_drawdown],
            "CAGR": [cagr],
            "Volatility": [volatility],
            "Win Rate": [win_rate]
        })
        
        csv = results_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download Results CSV",
            data=csv,
            file_name=f"{strategy}_results.csv",
            mime="text/csv"
        )

# ==========================
# STRATEGY COMPARISON PAGE
# ==========================

elif page == "Strategy Comparison":

    st.title("📊 Strategy Comparison")

    results_df = run_comparison()

    winner = results_df.sort_values(
        by="Return",
        ascending=False
    ).iloc[0]

    st.subheader("🏆 Performance Summary")
    
    st.success(
        f"🏆 Best Strategy: {winner['Strategy']} "
        f"| Return: {winner['Return']:.2f}%"
    )

    st.dataframe(
        results_df,
        use_container_width=True
    )

    import plotly.express as px

    fig = px.bar(
        results_df,
        x="Strategy",
        y="Return",
        title="Strategy Returns (%)",
        text="Return"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Sharpe Ratio Comparison"
    )

    fig = px.bar(
        results_df,
        x="Strategy",
        y="Sharpe",
        text="Sharpe",
        title="Sharpe Ratio"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
    "Drawdown Comparison"
    )

    fig = px.bar(
        results_df,
        x="Strategy",
        y="Drawdown",
        text="Drawdown",
        title="Maximum Drawdown"
    )

    fig.update_traces(
        texttemplate="%{text:.2%}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )