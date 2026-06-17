import pickle
import pandas as pd
import numpy as np

import dash
from dash import html
from dash import dcc

import dash_bootstrap_components as dbc

import plotly.graph_objects as go

# ====================================
# LOAD DATA
# ====================================

print("APP STARTING...")

with open(
    "data/edgeai_sig_dashboard_data.pkl",
    "rb"
) as f:

    dashboard_data = pickle.load(f)

results_df = pd.read_csv(
    "data/edgeai_sig_master_results.csv"
)

# ====================================
# KPI VALUES
# ====================================

forecast_error = round(
    results_df["forecast_error"].mean(),
    2
)

sqi_gain = round(
    results_df["sqi_gain"].mean(),
    2
)
# ====================================
# GENERATOR FIGURE
# ====================================

generator_fig = go.Figure()

generator_fig.add_trace(

    go.Scatter(

        y=dashboard_data[
            "clean_signal"
        ],

        name="Generated Signal"

    )

)

generator_fig.update_layout(

    title="Synthetic Signal Generator Output",

    xaxis_title="Sample",

    yaxis_title="Amplitude"

)
# ====================================
# SIGNAL FIGURE
# ====================================

signal_fig = go.Figure()

signal_fig.add_trace(
    go.Scatter(
        y=dashboard_data["clean_signal"],
        name="Original"
    )
)

signal_fig.add_trace(
    go.Scatter(
        y=dashboard_data["corrupted_signal"],
        name="Corrupted"
    )
)

signal_fig.add_trace(
    go.Scatter(
        y=dashboard_data["reconstructed_signal"],
        name="Reconstructed"
    )
)

signal_fig.update_layout(
    title="Signal Reconstruction"
)

# ====================================
# FORECAST FIGURE
# ====================================

forecast_fig = go.Figure()

forecast_fig.add_trace(
    go.Scatter(
        y=results_df["actual_sqi"],
        name="Actual SQI"
    )
)

forecast_fig.add_trace(
    go.Scatter(
        y=results_df["predicted_sqi"],
        name="Predicted SQI"
    )
)

forecast_fig.update_layout(
    title="SQI Forecasting",
    xaxis_title="Sample",
    yaxis_title="SQI"
)

# ====================================
# SQI GAUGE
# ====================================

gauge_fig = go.Figure(

    go.Indicator(

        mode="gauge+number",

        value=float(
            dashboard_data["actual_sqi"]
        ),

        title={
            "text": "Current SQI"
        },

        gauge={
            "axis": {
                "range": [0, 100]
            },

            "bar": {
                "color": "green"
            }
        }

    )

)

# ====================================
# FFT FIGURE
# ====================================

fft_values = np.abs(
    np.fft.rfft(
        dashboard_data[
            "reconstructed_signal"
        ]
    )
)

fft_fig = go.Figure()

fft_fig.add_trace(
    go.Scatter(
        y=fft_values,
        name="FFT Spectrum"
    )
)

fft_fig.update_layout(
    title="Reconstructed Signal Spectrum",
    xaxis_title="Frequency Bin",
    yaxis_title="Magnitude"
)

# ====================================
# TINYML DATA
# ====================================

tinyml_df = dashboard_data[
    "tinyml_metrics"
].copy()

tinyml_df["Value"] = (
    tinyml_df["Value"]
    .astype(float)
    .round(4)
)

latency_value = float(

    tinyml_df.loc[
        tinyml_df["Metric"]
        ==
        "Latency (ms)",
        "Value"
    ].values[0]

)

model_size = float(

    tinyml_df.loc[
        tinyml_df["Metric"]
        ==
        "Model Size (KB)",
        "Value"
    ].values[0]

)

# ====================================
# SYSTEM HEALTH CARD
# ====================================

health_card = dbc.Card(

    dbc.CardBody([

        html.H4(
            "System Health"
        ),

        html.Hr(),

        html.P(
            f"Current SQI: {dashboard_data['actual_sqi']:.2f}"
        ),

        html.P(
            f"Predicted SQI: {dashboard_data['predicted_sqi']:.2f}"
        ),

        html.P(
            f"Average Gain: {dashboard_data['average_gain']:.2f}"
        ),

        html.P(

            "Status: Excellent"

            if dashboard_data[
                "actual_sqi"
            ] > 75

            else

            "Status: Stable"

            if dashboard_data[
                "actual_sqi"
            ] > 50

            else

            "Status: Recovering"

        )

    ])

)

# ====================================
# TINYML TABLE
# ====================================

tinyml_table = dbc.Table.from_dataframe(

    tinyml_df,

    striped=True,

    bordered=True,

    hover=True

)

# ====================================
# DASH APP
# ====================================

app = dash.Dash(

    __name__,

    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]

)

# ====================================
# LAYOUT
# ====================================

app.layout = dbc.Container([

    html.H1(
    "EdgeAI-SIG Dashboard"
),

html.H5(
    "Real-Time TinyML Framework for Signal Integrity Forecasting and Adaptive Reconstruction"
),

    html.Hr(),

    # ==========================
    # KPI ROW
    # ==========================

    dbc.Row([

        dbc.Col(

            dbc.Card(

                dbc.CardBody([

                    html.H5(
                        "Forecast Error"
                    ),

                    html.H3(
                        str(
                            forecast_error
                        )
                    )

                ])

            )

        ),

        dbc.Col(

            dbc.Card(

                dbc.CardBody([

                    html.H5(
                        "SQI Gain"
                    ),

                    html.H3(
                        str(
                            sqi_gain
                        )
                    )

                ])

            )

        ),

        dbc.Col(

            dbc.Card(

                dbc.CardBody([

                    html.H5(
                        "Latency (ms)"
                    ),

                    html.H3(
                        f"{latency_value:.4f}"
                    )

                ])

            )

        ),

        dbc.Col(

            dbc.Card(

                dbc.CardBody([

                    html.H5(
                        "Model Size (KB)"
                    ),

                    html.H3(
                        f"{model_size:.2f}"
                    )

                ])

            )

        )

    ]),

    html.Br(),

    # ==========================
    # GAUGE + HEALTH
    # ==========================

    dbc.Row([

        dbc.Col(

            dcc.Graph(
                figure=gauge_fig
            ),

            width=4

        ),

        dbc.Col(

            health_card,

            width=8

        )

    ]),

    html.Br(),
# ==========================
# GENERATED SIGNAL
# ==========================

dbc.Row([

    dbc.Col(

        dcc.Graph(
            figure=generator_fig
        )

    )

]),

html.Br(),
    # ==========================
    # FORECAST
    # ==========================

    dbc.Row([

        dbc.Col(

            dcc.Graph(
                figure=forecast_fig
            )

        )

    ]),

    html.Br(),

    # ==========================
    # SIGNAL RECONSTRUCTION
    # ==========================

    dbc.Row([

        dbc.Col(

            dcc.Graph(
                figure=signal_fig
            )

        )

    ]),

    html.Br(),

    # ==========================
    # FFT
    # ==========================

    dbc.Row([

        dbc.Col(

            dcc.Graph(
                figure=fft_fig
            )

        )

    ]),

    html.Br(),

    # ==========================
    # TINYML TABLE
    # ==========================

    html.H3(
        "TinyML Metrics"
    ),

    tinyml_table

], fluid=True)

# ====================================
# RUN APP
# ====================================

print("REACHED END OF FILE")

if __name__ == "__main__":

    print("STARTING DASH SERVER")

    app.run(debug=True)