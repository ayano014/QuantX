import plotly.graph_objects as go

def show_equity_curves(equity_curves):
    
    fig= go.Figure()

    for name, data in equity_curves.items():

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Portfolio"],
                mode="lines",
                name=name
            )
        )

        fig.update_layout(
            title="Equity Curves Comparison",
            xaxis_title="Date",
            yaxis_title="Portfolio Value (%)",
            height=700
        )

    fig.show()