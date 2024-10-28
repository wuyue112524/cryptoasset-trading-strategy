import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_plot(value_flow, price):
    value_flow['outUSD_chart'] = -value_flow['outUSD']
    
    # Create subplots with shared x-axes and no vertical spacing
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0)

    # Add the scatter trace to the first row
    fig.add_trace(
        go.Scatter(x=price['time'], y=price['close'], mode='lines', name="Price (USDT)", line=dict(color='#436AFB')),
        row=1, col=1
    )

    # Add the first bar trace to the second row
    fig.add_trace(
        go.Bar(x=value_flow['time'], y=value_flow['inUSD'], name="USD inflow",marker=dict(color='#48CC87') ),
        row=2, col=1,
    )

    # Add the second bar trace to the second row
    fig.add_trace(
        go.Bar(x=value_flow['time'], y=value_flow['outUSD_chart'], name="USD outflow",
               marker=dict(color='#EA3943') ),
        row=2, col=1
    )

    # Update layout to adjust figure height
    fig.update_layout(
        height=800,  # Adjust the height of the entire figure
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    )

    # Set grid properties
    fig.update_xaxes(showgrid=True, gridcolor='black', gridwidth=1)
    fig.update_yaxes(showgrid=True, gridcolor='black', gridwidth=1)

    # Show the figure
    return fig

# Example usage:
# create_plot(value_flow_dataframe, price_dataframe)
