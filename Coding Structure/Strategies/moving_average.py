def generate_signal(data):

    data["MA20"] = data["Close"].rolling(20).mean()

    data["MA50"] = data["Close"].rolling(50).mean()

    data["Signal"] = 0

    data.loc[
        data["MA20"] > data["MA50"],
        "Signal"
    ] = 1

    return data