# RiskLens

Portfolio Risk and Exposure Analytics Platform for hedge-fund-style, legal-entity, and managed-account structures.

## Overview

RiskLens is an end-to-end portfolio risk analytics platform designed to show how Risk IT can support investment and risk teams through:

- holdings ingestion and normalization;
- hierarchical portfolio aggregation;
- exposure analytics;
- core risk metric calculation;
- concentration and limit monitoring;
- scenario analysis and stress testing;
- dashboard-based reporting.

The platform is not intended to make investment decisions. Its purpose is to provide a structured analytical layer for portfolio oversight, transparency, and risk monitoring.

## Why This Project

RiskLens is designed as:

- a strong portfolio project for interviews in Risk IT, hedge funds, portfolio analytics, and investment risk;
- a modular sandbox for building realistic risk pipelines;
- a potential foundation for a future niche B2B product in portfolio risk monitoring and reporting.

## Core Capabilities

- Ingest portfolio holdings, market data, and portfolio structure data.
- Normalize security, account, fund, and entity-level records into a consistent data model.
- Aggregate positions across fund, legal entity, account, and position levels.
- Analyze exposures by asset class, sector, region, currency, issuer, and strategy.
- Calculate portfolio analytics such as volatility, drawdown, and Value at Risk.
- Monitor concentration, issuer limits, country limits, and custom threshold rules.
- Run historical and hypothetical stress scenarios.
- Publish dashboard-ready datasets and automated reporting outputs.

## Target Users

- Risk teams
- Portfolio managers
- Investment operations teams
- Risk IT and data teams
- Business stakeholders who need portfolio-level transparency

## Architecture

RiskLens is split into five logical layers:

1. Ingestion layer  
   Loads holdings, market data, and reference data from source systems.

2. Data model layer  
   Organizes normalized portfolio, instrument, hierarchy, and pricing datasets in PostgreSQL.

3. Risk engine  
   Computes exposures, concentration metrics, volatility, drawdown, and Value at Risk.

4. Scenario engine  
   Applies shocks and stress scenarios to simulate portfolio vulnerability.

5. Reporting layer  
   Feeds BI dashboards, scheduled reporting jobs, and alerting workflows.

More detail lives in [docs/architecture.md](/Users/igor.pokhotelov/Desktop/RiskLens/docs/architecture.md).

## Repository Structure

```text
RiskLens/
|- config/                  # YAML and environment-driven runtime configuration
|- data/
|  |- raw/                  # Landing zone for source extracts
|  |- staging/              # Cleaned intermediate datasets
|  `- curated/              # Analytics-ready outputs
|- docs/                    # Architecture, roadmap, and design notes
|- notebooks/               # Exploratory analysis and prototyping
|- sql/
|  |- schema/               # Core PostgreSQL DDL
|  |- views/                # Reusable analytics views
|  `- marts/                # Dashboard-facing marts
|- src/risklens/
|  |- aggregation/          # Portfolio hierarchy rollups
|  |- ingestion/            # Source loaders and normalization logic
|  |- monitoring/           # Limits and threshold checks
|  |- reporting/            # Reporting dataset builders
|  |- risk/                 # Risk calculations
|  `- scenarios/            # Stress and scenario logic
|- tests/                   # Unit and smoke tests
`- .github/workflows/       # CI definitions
```

## Tech Stack

- Python 3.11+
- SQL
- PostgreSQL
- Pandas / NumPy / SciPy
- SQLAlchemy
- BI or dashboard tooling such as Power BI, Metabase, or Tableau

## MVP Scope

The first practical MVP can focus on:

- ingesting daily holdings snapshots;
- loading security master and market price history;
- mapping portfolio hierarchy from fund to account;
- calculating long/short and net exposures;
- measuring top issuer, sector, region, and currency concentrations;
- producing volatility, max drawdown, and historical VaR;
- generating a dashboard-ready daily risk summary table.

## Example Analytics Questions

- What is the total exposure by asset class across all legal entities?
- Which issuers exceed internal concentration limits?
- How much of portfolio risk comes from one sector or region?
- How would the portfolio behave under a rates shock, equity selloff, or FX devaluation?
- How has portfolio drawdown evolved over the last 12 months?

## Getting Started

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install the project in editable mode

```bash
python3 -m pip install -e ".[dev]"
```

### 3. Configure environment variables

Copy `.env.example` into `.env` and update the database settings.

### 4. Run the local smoke tests

```bash
python3 -m unittest discover -s tests -v
```

## Roadmap

- Phase 1: project scaffolding and canonical data model
- Phase 2: ingestion pipelines and portfolio hierarchy mapping
- Phase 3: exposure analytics and dashboard marts
- Phase 4: risk engine metrics and concentration monitoring
- Phase 5: scenario engine and automated reporting

The working project roadmap is in [docs/roadmap.md](/Users/igor.pokhotelov/Desktop/RiskLens/docs/roadmap.md).

## Non-Goals

- No trade execution
- No investment recommendation logic
- No order management or portfolio rebalancing workflows

## Disclaimer

RiskLens is an analytics and monitoring platform. It does not provide investment advice and should not be used as a substitute for regulated risk governance or production investment controls without further hardening.
