# RiskLens Architecture

## Logical Flow

```text
Source files / APIs
        |
        v
Ingestion and normalization
        |
        v
Structured PostgreSQL model
        |
        +--> Exposure aggregation
        |
        +--> Risk engine
        |
        +--> Scenario engine
        |
        v
Reporting marts and dashboards
```

## Main Domains

### Portfolio structure

- Funds
- Legal entities
- Accounts
- Positions

This domain captures ownership and reporting hierarchy so that risk can be viewed at multiple levels.

### Market and reference data

- Security master
- Prices
- FX rates
- Sector and region mappings
- Asset class classifications

This domain provides the reference context required for aggregation and analytics.

### Risk analytics

- Gross and net exposures
- Concentration metrics
- Volatility
- Max drawdown
- Historical Value at Risk

### Scenario analytics

- Historical replay scenarios
- Hypothetical market shocks
- Cross-asset stress assumptions

### Reporting

- Daily risk snapshots
- Dashboard marts
- Automated limit-breach reporting

## Suggested Processing Sequence

1. Load holdings snapshots and normalize instruments.
2. Load market data and enrich holdings with price, FX, sector, and region mappings.
3. Attach each holding to the portfolio hierarchy.
4. Aggregate exposures at required reporting levels.
5. Compute risk metrics on portfolio and sub-portfolio views.
6. Apply scenario shocks and calculate stressed PnL or exposure shifts.
7. Publish final marts for dashboards and scheduled reports.
