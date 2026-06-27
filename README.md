# EdgeAI-SIG

## Real-Time TinyML Framework for Signal Integrity Forecasting and Adaptive Reconstruction in Resource-Constrained Edge Systems

[Dash is running on http://127.0.0.1:8050/]


EdgeAI-SIG is an Edge AI and TinyML framework designed for real-time signal quality monitoring, forecasting, and reconstruction in resource-constrained environments.
Unlike traditional predictive maintenance systems that focus on equipment failures, EdgeAI-SIG focuses on **signal intelligence**. The system continuously generates communication and sensor-inspired signals, simulates realistic degradation conditions, evaluates signal quality using a composite Signal Quality Index (SQI), forecasts future signal quality using a lightweight neural network, and adaptively reconstructs degraded signals.
The framework demonstrates how signal integrity can be monitored and improved directly at the edge using TinyML-compatible models.

Motivation:Modern edge devices operate in noisy and resource-constrained environments where communication and sensing signals are frequently degraded by interference, quantization effects, transmission errors, and environmental noise.
Conventional approaches typically react after signal corruption has already occurred.
EdgeAI-SIG introduces a proactive approach:
1. Monitor signal quality continuously.
2. Forecast future signal degradation.
3. Apply adaptive reconstruction before severe quality loss.
4. Deploy lightweight inference suitable for embedded systems.

Supported Signal Types
* RF-inspired signals
* Chirp signals
* Telemetry signals
* Multi-frequency communication signals

Noise Models:The framework supports multiple degradation mechanisms:
* Gaussian Noise
* Impulse Noise
* Burst Noise
* Quantization Noise
* Sensor Drift
* Packet Loss Simulation

Signal Quality Index (SQI):Signal quality is evaluated using a composite Signal Quality Index derived from multiple signal integrity metrics:
* Signal-to-Noise Ratio (SNR)
* Root Mean Square Error (RMSE)
* Correlation Coefficient
* Spectral Similarity
* Energy Ratio
The resulting SQI provides a normalized measure of overall signal integrity.

TinyML Forecasting Model:A lightweight neural network is trained to forecast future SQI values from extracted signal features.
Model Characteristics

 Metric              Value          
 Parameters - 897            
 Model Size  - 4.25 KB       
 Quantization  - INT8          
 Deployment Format - TensorFlow Lite 
 Forecast MAE   - 4.29            
The model is intentionally designed for deployment on memory-constrained embedded platforms.

Adaptive Reconstruction Engine:The reconstruction engine dynamically selects reconstruction strategies based on forecasted signal quality.

Supported methods include:
* Savitzky-Golay Filtering
* Median + Savitzky-Golay Filtering
* Hybrid Reconstruction Policy
* No Reconstruction (Baseline)
The objective is to improve signal quality while maintaining low computational overhead.

Dashboard Features:The Dash + Plotly dashboard provides:
* Signal Quality Monitoring
* SQI Forecast Visualization
* Signal Reconstruction Visualization
* FFT Spectrum Analysis
* TinyML Performance Metrics
* System Health Monitoring

Example Results
Forecasting Performance
* Average Forecast Error: 4.29 SQI units

TinyML Deployment
* Model Size: 4.25 KB
* Parameters: 897
* Average Inference Latency: 0.0079 ms

 Reconstruction Performance
* Average SQI Improvement: 11.62
* Average SQI Gain: 24.31%


Technologies Used
Programming
* Python

Machine Learning
* TensorFlow
* TensorFlow Lite

Data Processing
* NumPy
* Pandas
* SciPy

Visualization
* Dash
* Plotly

Signal Processing
* FFT Analysis
* Spectral Similarity Metrics
* Digital Filtering


Potential applications include:
* Edge Communication Systems
* Wireless Sensor Networks
* Scientific Instrumentation
* Embedded Monitoring Systems
* Remote Sensing Platforms
* Resource-Constrained IoT Devices


 Future Work
* Interactive Real-Time Signal Streaming
* Learned Reconstruction Policies
* Edge Impulse Integration
* Embedded MCU Deployment
* Real Hardware Validation
* SDR-Based Signal Experiments



Author
Anukriti Sharma

