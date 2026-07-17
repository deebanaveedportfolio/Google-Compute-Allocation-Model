```python
"""
Google Compute-Adjusted Margin (CAM) Allocation Model
Author: Deeba Naveed
Description: A quantitative engine simulating strategic TPU/GPU allocation 
             between internal product consumer queries and external B2B Cloud clients.
"""

class ComputeAllocationEngine:
    def __init__(self, total_tpu_capacity_pflops: float, external_gcp_rate_per_pflop: float):
        """
        Args:
            total_tpu_capacity_pflops: Total available TPU cluster capacity in PetaFLOPs.
            external_gcp_rate_per_pflop: Market pricing of 1 PetaFLOP/hour sold on Vertex AI.
        """
        self.total_capacity = total_tpu_capacity_pflops
        self.external_gcp_rate = external_gcp_rate_per_pflop

    def calculate_internal_yield(self, queries: int, rev_per_1k_queries: float, tac_rate: float, compute_pflops_consumed: float) -> dict:
        """
        Calculates Compute-Adjusted Margin (CAM) and Marginal Revenue Product of Compute (MRPC) for internal search.
        """
        # Financial Calculations
        gross_ad_revenue = (queries / 1000.0) * rev_per_1k_queries
        tac_expense = gross_ad_revenue * tac_rate
        
        # We assign an internal shadow price to compute based on the external GCP opportunity cost
        internal_compute_cost = compute_pflops_consumed * self.external_gcp_rate
        
        net_margin = gross_ad_revenue - tac_expense - internal_compute_cost
        cam_per_query = net_margin / queries if queries > 0 else 0
        
        # Marginal Revenue Product of Compute (MRPC)
        mrpc_internal = (gross_ad_revenue - tac_expense) / compute_pflops_consumed if compute_pflops_consumed > 0 else 0
        
        return {
            "Gross Revenue": round(gross_ad_revenue, 2),
            "Compute Cost (Shadow Price)": round(internal_compute_cost, 2),
            "Net CAM": round(net_margin, 2),
            "CAM per Query": round(cam_per_query, 4),
            "MRPC Internal": round(mrpc_internal, 2)
        }

    def get_strategic_allocation(self, internal_queries: int, rev_per_1k_queries: float, tac_rate: float, internal_compute_pflops: float) -> str:
        """
        Applies the strategic directive logic to advise on resource routing.
        """
        internal_metrics = self.calculate_internal_yield(
            queries=internal_queries,
            rev_per_1k_queries=rev_per_1k_queries,
            tac_rate=tac_rate,
            compute_pflops_consumed=internal_compute_pflops
        )
        
        mrpc_internal = internal_metrics["MRPC Internal"]
        mrpc_external = self.external_gcp_rate  # Opportunity cost of selling directly to cloud
        
        print(f"\n--- STRATEGIC ANALYSIS RESULTS ---")
        print(f"Internal MRPC (Yield per PFlop): ${mrpc_internal:,.2f}")
        print(f"External MRPC (GCP Opportunity Cost): ${mrpc_external:,.2f}")
        print(f"Search CAM per Query: ${internal_metrics['CAM per Query']:.4f}")
        
        if mrpc_external > mrpc_internal:
            return (
                "⚠️ WARNING: MARGIN SQUEEZE DETECTED.\n"
                "Action: Throttle lower-priority internal model testing. "
                "Route excess capacity to Google Cloud (Vertex AI) to capture higher marginal returns."
            )
        else:
            return (
                "✅ ALLOCATION OPTIMAL.\n"
                "Action: Internal consumer features are yielding higher net-ad margins than external GCP rates. "
                "Maintain current internal allocation."
            )

# Run Simulation Scenarios
if __name__ == "__main__":
    # Initialize Engine (e.g., 5,000 PetaFLOP capacity, GCP value of $150 per PetaFLOP/hour)
    engine = ComputeAllocationEngine(total_tpu_capacity_pflops=5000.0, external_gcp_rate_per_pflop=150.0)
    
    # Scenario A: Standard Search Traffic with highly optimized models (Low Compute Consumption)
    print("SCENARIO A: Low-Compute Optimized Search Models")
    recommendation_a = engine.get_strategic_allocation(
        internal_queries=1_000_000, 
        rev_per_1k_queries=45.0,  # $45 RPM
        tac_rate=0.22,             # 22% TAC
        internal_compute_pflops=100.0
    )
    print(recommendation_a)

    # Scenario B: Complex Generative Search (High Compute Consumption, Flat Ad Revenue)
    print("\nSCENARIO B: Heavy Unoptimized Generative Search Models (Peak Load)")
    recommendation_b = engine.get_strategic_allocation(
        internal_queries=1_000_000, 
        rev_per_1k_queries=45.0, 
        tac_rate=0.22, 
        internal_compute_pflops=300.0  # 3x more compute intensive
    )
    print(recommendation_b)
