def calculate_metrics(data, initial_cash):

    final_value = data["Portfolio"].dropna().iloc[-1]

    total_return = (
        (final_value - initial_cash)
        / initial_cash
    ) * 100

    sharpe = (
        data["Strategy_Returns"].mean()
        /
        data["Strategy_Returns"].std()
    ) * (252 ** 0.5)

    rolling_max = data["Portfolio"].cummax()

    drawdown = (
        data["Portfolio"]
        - rolling_max
    ) / rolling_max

    max_drawdown = drawdown.min()

    years = len(data) / 252

    cagr = (
        (final_value / initial_cash) ** (1/years) - 1
    ) * 100

    volatility =(
        data["Strategy_Returns"]
        .std()
        * (252**0.5)
        *100
    )

    winning_days = (
        data["Strategy_Returns"] > 0
    ).sum()

    total_days = (
        data["Strategy_Returns"] != 0
    ).sum()

    win_rate = (
        winning_days / total_days
    )*100

    return (
        total_return,
        sharpe,
        max_drawdown,
        cagr,
        volatility,
        win_rate
    )
        