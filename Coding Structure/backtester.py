def run_backtest(data, initial_cash):

    data["Position"] = data["Signal"]

    data["Returns"] = data["Close"].pct_change()

    data["Strategy_Returns"] = (
        data["Position"].shift(1)
        * data["Returns"]
    )

    data["Portfolio"] = (
        1 + data["Strategy_Returns"]
    ).cumprod() * initial_cash

    return data