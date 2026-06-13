def calculate_metrics(data, initial_cash):

    final_value = data["Portfolio"].iloc[-1]

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

    return (
        total_return,
        sharpe,
        max_drawdown
    )