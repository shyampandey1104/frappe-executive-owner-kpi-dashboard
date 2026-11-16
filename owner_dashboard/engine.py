"""Executive Business Owner KPI Dashboard, Cash Runway & Stock Health Analytics Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class BusinessOwnerKPISnapshot:
    as_of_date: str
    daily_sales_total_inr: float
    monthly_sales_run_rate_inr: float
    net_profit_estimate_inr: float
    total_bank_cash_balance_inr: float
    monthly_burn_rate_inr: float
    cash_runway_months: float
    total_receivables_overdue_inr: float
    total_payables_due_next_15days_inr: float
    dead_stock_aging_above_90days_inr: float
    owner_health_status: str  # THRIVING_GREEN, CAUTION_AMBER, DANGER_CASH_CRUNCH


class OwnerDashboardEngine:
    """Summarizes enterprise KPIs into concise actionable metrics for business founders and CEOs."""

    def compute_dashboard_kpis(
        self,
        as_of_date: str,
        daily_sales: float,
        trailing_30day_sales: float,
        cash_balance: float,
        monthly_expenses: float,
        overdue_debtors: float,
        urgent_creditors: float,
        dead_stock_value: float,
        net_margin_pct: float = 12.0
    ) -> BusinessOwnerKPISnapshot:
        # Cash Runway = Cash Balance / Monthly Burn Rate
        runway = round(cash_balance / monthly_expenses, 1) if monthly_expenses > 0 else 99.0
        profit_est = round((trailing_30day_sales * net_margin_pct) / 100.0, 2)

        if runway >= 6.0 and urgent_creditors < cash_balance:
            status = "THRIVING_GREEN"
        elif runway >= 2.5:
            status = "CAUTION_AMBER"
        else:
            status = "DANGER_CASH_CRUNCH"

        return BusinessOwnerKPISnapshot(
            as_of_date=as_of_date,
            daily_sales_total_inr=daily_sales,
            monthly_sales_run_rate_inr=trailing_30day_sales,
            net_profit_estimate_inr=profit_est,
            total_bank_cash_balance_inr=cash_balance,
            monthly_burn_rate_inr=monthly_expenses,
            cash_runway_months=runway,
            total_receivables_overdue_inr=overdue_debtors,
            total_payables_due_next_15days_inr=urgent_creditors,
            dead_stock_aging_above_90days_inr=dead_stock_value,
            owner_health_status=status
        )
