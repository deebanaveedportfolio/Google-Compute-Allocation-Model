# Google Compute-Adjusted Margin (CAM) Allocation Model
### A Quantitative Framework for Strategic TPU/GPU Resource Prioritization

## Executive Summary
As Google transitions into an "AI-native enterprise," internal infrastructure demand (e.g., Gemini-powered Search, Workspace, and YouTube) is scaling exponentially. However, compute hardware is a finite, supply-constrained resource. Every unit of Tensor Processing Unit (TPU) capacity allocated to internal consumer testing represents a direct opportunity cost: high-margin, predictable B2B enterprise revenue on Google Cloud (Vertex AI).

This repository contains a lightweight, modular python simulation designed to model and optimize the **Marginal Revenue Product of Compute (MRPC)**. It introduces a strategic transfer pricing mechanism and calculates **Compute-Adjusted Margin (CAM)** to resolve resource allocation bottlenecks dynamically.

---

## The Strategic Framework

### 1. Compute-Adjusted Margin (CAM) Formula
Rather than evaluating product features on raw user engagement, this model calculates CAM to account for the direct physical cost of AI inference:

$$CAM = \frac{\text{Ad Revenue} - \text{Traffic Acquisition Cost (TAC)} - \text{Compute Cost}}{\text{Queries}}$$

### 2. Allocation Optimization Logic
The engine dynamically balances resources across two channels:
*   **External Yield ($MRPC_{External}$):** Stable, contracted subscription revenue per PetaFLOP on GCP Vertex AI.
*   **Internal Yield ($MRPC_{Internal}$):** Variable, ad-supported or consumer subscription yield per PetaFLOP.
*   **Optimization Directive:** If $MRPC_{External} > MRPC_{Internal}$, the engine automatically throttles lower-priority internal model training/testing and routes capacity to Vertex AI to capture guaranteed enterprise margins.

---

## File Structure & Usage

### Setup & Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/google-compute-allocation-model.git](https://github.com/yourusername/google-compute-allocation-model.git)
   cd google-compute-allocation-model
