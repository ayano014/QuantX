def generate_signal(data):

    data["MA20"] = data["Close"].rolling(20).mean()
    
    data["Signal"] = 0

    data.loc[
        data["Close"] < data["MA20"] * 0.98, "Signal"
    ] = 1

    return data