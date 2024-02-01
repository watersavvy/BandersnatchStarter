from altair import Chart
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:

    """ Returns a scatter plot with the option to choose different features and a target variable"""

    graph = Chart(
        df[['Type','Level', 'Rarity', 'Health', 'Energy', 'Sanity']],
        title=f"{y} by {x} for {target}"
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=[x, y, target]
    ).properties(
        width=600,
        height=600,
        background='#403c42',
        padding=30
    ).configure_axis(
        titleFontSize=16,
        labelFontSize=12
    ).configure_title(
        fontSize=24
    ).configure_legend(
        gradientLength=400,
        gradientThickness=20,
        titleFontSize=14,
        labelFontSize=12
    )

    return graph

