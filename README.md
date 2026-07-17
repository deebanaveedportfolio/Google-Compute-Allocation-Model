# Google Compute-Adjusted Margin (CAM) Allocation Model
### A Quantitative Framework for Strategic TPU/GPU Resource Prioritization

## Executive Summary
As organizations transition into an "AI-native enterprise," internal infrastructure demand (e.g., Gemini-powered Search, Workspace, and YouTube) is scaling exponentially. However, compute hardware is a finite, supply-constrained resource. Every unit of Tensor Processing Unit (TPU) capacity allocated to internal consumer testing represents a direct opportunity cost: high-margin, predictable B2B enterprise revenue on Google Cloud (Vertex AI).

This repository contains a lightweight, modular python simulation designed to model and optimize the **Marginal Revenue Product of Compute (MRPC)**. The simulation explores an internal shadow-pricing mechanism and calculates **Compute-Adjusted Margin (CAM)** to resolve resource allocation bottlenecks dynamically.

Business Question

If AI compute is capacity-constrained, how should it be allocated between internal AI products and external cloud customers?
---

## The Strategic Framework

### 1. Compute-Adjusted Margin (CAM) Formula
The simulation evaluates projects using Compute-Adjusted Margin (CAM), a simple metric that incorporates estimated compute costs alongside revenue:

$$CAM = \frac{\text{Ad Revenue} - \text{Traffic Acquisition Cost (TAC)} - \text{Compute Cost}}{\text{Queries}}$$

### 2. Allocation Optimization Logic
The engine dynamically balances resources across two channels:
*   **External Yield ($MRPC_{External}$):** Stable, contracted subscription revenue per PetaFLOP on GCP Vertex AI.
*   **Internal Yield ($MRPC_{Internal}$):** Variable, ad-supported or consumer subscription yield per PetaFLOP.
*   **Allocation Rule:** If $MRPC_{External} > MRPC_{Internal}$, the engine automatically throttles lower-priority internal model training/testing and routes capacity to Vertex AI to capture guaranteed enterprise margins.

---

Disclaimer

This repository is an independent educational project developed using publicly available information. The framework and simulation are illustrative and are not intended to represent Google’s internal systems, financials, or operational decision-making.

README.md
Overview of the project

compute_allocation_model.py
Python simulation

Decision Memo.pdf
Strategy memo summarizing the framework
