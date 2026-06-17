# EdgeAI-SIG

## Real-Time TinyML Framework for Signal Integrity Forecasting and Adaptive Reconstruction in Resource-Constrained Edge Systems

### Overview

EdgeAI-SIG is a real-time signal intelligence framework designed for signal quality monitoring, forecasting, and adaptive reconstruction in resource-constrained edge environments.

The system generates synthetic RF and sensor-inspired signals, injects realistic noise conditions, computes a Signal Quality Index (SQI), forecasts future signal degradation using a TinyML model, and applies adaptive reconstruction techniques to improve signal integrity.

### Key Features

* Synthetic real-time signal generation
* Multi-noise simulation environment
* Signal Quality Index (SQI) computation
* TinyML-based SQI forecasting
* Adaptive signal reconstruction
* TensorFlow Lite INT8 deployment
* Dash + Plotly interactive dashboard
* FFT spectrum analysis
* Experiment logging and benchmarking

### Supported Signal Types

* RF Signals
* Chirp Signals
* Telemetry Signals
* Multi-Frequency Signals

### Noise Conditions

* Gaussian Noise
* Impulse Noise
* Burst Noise
* Quantization Noise
* Sensor Drift
* Packet Loss Simulation

### TinyML Model

* Architecture: Lightweight MLP
* Parameters: 897
* Model Size: 4.25 KB
* TensorFlow Lite INT8 Quantization
* Forecast MAE: 4.29

### Dashboard

The dashboard provides:

* Signal Quality Monitoring
* SQI Forecast Visualization
* Signal Reconstruction Visualization
* FFT Spectrum Analysis
* TinyML Performance Metrics
* System Health Monitoring

### Future Work

* Learned Reconstruction Policy
* Real Signal Validation
* Live Streaming Signal Processing
* Microcontroller Deployment
* Edge Impulse Integration

### Author

Anukriti Sharma
Electronics and Communication Engineering
