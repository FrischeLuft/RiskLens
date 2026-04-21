# RiskLens Roadmap

## Phase 1 - Foundation

- Finalize project structure and coding standards.
- Define canonical PostgreSQL schema for portfolios, holdings, and market data.
- Prepare environment configuration and local development workflow.

## Phase 2 - Data Ingestion

- Build CSV or API loaders for holdings snapshots.
- Build market data loaders for prices, FX, and security reference data.
- Add validation and normalization rules for incoming datasets.

## Phase 3 - Portfolio Aggregation

- Represent portfolio hierarchy across fund, legal entity, account, and position level.
- Create reusable SQL views for gross, net, and grouped exposures.
- Publish daily exposure summary marts.

## Phase 4 - Risk Engine

- Implement volatility calculations.
- Implement max drawdown logic.
- Implement historical Value at Risk.
- Add concentration and threshold monitoring.

## Phase 5 - Scenario Engine

- Define scenario input format.
- Implement equity, rates, FX, and spread shock templates.
- Calculate stressed exposures and estimated PnL moves.

## Phase 6 - Reporting Layer

- Prepare dashboard-ready datasets.
- Build risk summary dashboards.
- Add scheduled reporting and alerting hooks.
