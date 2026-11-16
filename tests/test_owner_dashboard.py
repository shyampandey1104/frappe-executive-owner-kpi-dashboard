import unittest
from owner_dashboard.engine import OwnerDashboardEngine

class TestOwnerDashboard(unittest.TestCase):
    def test_owner_kpi_computation(self):
        engine = OwnerDashboardEngine()
        snap = engine.compute_dashboard_kpis(
            as_of_date="2026-11-16",
            daily_sales=125000.0,        # ₹1.25L today
            trailing_30day_sales=3500000.0, # ₹35L month run rate
            cash_balance=4000000.0,      # ₹40L in bank
            monthly_expenses=800000.0,   # ₹8L burn rate -> Runway = 40/8 = 5 months
            overdue_debtors=450000.0,
            urgent_creditors=900000.0,
            dead_stock_value=300000.0,
            net_margin_pct=15.0          # 15% margin on 35L = 5.25L profit
        )
        self.assertEqual(snap.cash_runway_months, 5.0)
        self.assertEqual(snap.net_profit_estimate_inr, 525000.0)
        self.assertEqual(snap.owner_health_status, "CAUTION_AMBER")

if __name__ == "__main__":
    unittest.main()
