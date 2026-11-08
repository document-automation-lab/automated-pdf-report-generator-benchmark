#!/usr/bin/env python3
"""Multi-Page PDF Report Generation Benchmark."""
import argparse
import sys

def benchmark_report_generation(monthly_reports, pages_per_report=15):
    # Multi-page business reports (e.g. quarterly analytics, financial summaries)
    total_pages = monthly_reports * pages_per_report
    
    # Self-hosted: Multi-page reports cause high memory spikes during pagination & header/footer rendering
    # Requires high-memory instances (8GB RAM minimum, $48/mo)
    # Plus 4 hrs/mo layout debugging (page-break-inside avoid glitches)
    infra_cost = 48.0 if monthly_reports <= 2000 else 96.0
    debug_labor = 4.0 * 65.0
    self_hosted_tco = infra_cost + debug_labor

    # Cloud Managed API:
    if monthly_reports <= 300:
        api_tier = "Basic ($19/mo)"
        api_cost = 19.0
    elif monthly_reports <= 1200:
        api_tier = "Standard ($69/mo)"
        api_cost = 69.0
    else:
        api_tier = "Enterprise ($139/mo)"
        api_cost = 139.0

    savings = self_hosted_tco - api_cost
    return {
        "monthly_reports": monthly_reports,
        "pages_per_report": pages_per_report,
        "total_pages": total_pages,
        "self_hosted_tco": self_hosted_tco,
        "api_tier": api_tier,
        "api_cost": api_cost,
        "savings": savings,
        "savings_pct": (savings / self_hosted_tco) * 100 if self_hosted_tco > 0 else 0.0
    }

def main():
    parser = argparse.ArgumentParser(description="Multi-Page Business Report PDF Generator Benchmark")
    parser.add_argument("--reports", type=int, default=800, help="Monthly multi-page reports generated (default: 800)")
    parser.add_argument("--pages", type=int, default=15, help="Average page count per report (default: 15)")
    args = parser.parse_args()

    r = benchmark_report_generation(args.reports, args.pages)
    print("=" * 68)
    print(" Multi-Page Business Report PDF Generation Benchmark")
    print("=" * 68)
    print(f" Monthly Report Volume        : {r['monthly_reports']:,} reports ({r['total_pages']:,} total pages)")
    print(f" Self-Hosted Rendering TCO    : ${r['self_hosted_tco']:.2f}/mo (Infra + Page-break triage)")
    print(f" Managed Cloud REST Solution  : {r['api_tier']} (${r['api_cost']:.2f}/mo)")
    print("-" * 68)
    print(f" Projected Monthly Savings    : ${r['savings']:.2f}/mo ({r['savings_pct']:.1f}% reduction)")
    print("=" * 68)
    return 0

if __name__ == "__main__":
    sys.exit(main())
