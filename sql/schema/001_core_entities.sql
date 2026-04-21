CREATE SCHEMA IF NOT EXISTS core;

CREATE TABLE IF NOT EXISTS core.portfolio_node (
    portfolio_node_id BIGSERIAL PRIMARY KEY,
    portfolio_node_name TEXT NOT NULL,
    portfolio_node_type TEXT NOT NULL,
    parent_portfolio_node_id BIGINT REFERENCES core.portfolio_node (portfolio_node_id),
    inception_date DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS core.instrument (
    instrument_id BIGSERIAL PRIMARY KEY,
    ticker TEXT,
    isin TEXT,
    instrument_name TEXT NOT NULL,
    asset_class TEXT,
    sector TEXT,
    region TEXT,
    currency TEXT
);

CREATE TABLE IF NOT EXISTS core.holdings_snapshot (
    holdings_snapshot_id BIGSERIAL PRIMARY KEY,
    as_of_date DATE NOT NULL,
    portfolio_node_id BIGINT NOT NULL REFERENCES core.portfolio_node (portfolio_node_id),
    instrument_id BIGINT NOT NULL REFERENCES core.instrument (instrument_id),
    quantity NUMERIC(24, 8) NOT NULL,
    market_value_base NUMERIC(24, 8),
    exposure_base NUMERIC(24, 8),
    cost_base NUMERIC(24, 8),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS core.market_data_snapshot (
    market_data_snapshot_id BIGSERIAL PRIMARY KEY,
    as_of_date DATE NOT NULL,
    instrument_id BIGINT NOT NULL REFERENCES core.instrument (instrument_id),
    close_price NUMERIC(24, 8),
    fx_rate_to_base NUMERIC(24, 8),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
