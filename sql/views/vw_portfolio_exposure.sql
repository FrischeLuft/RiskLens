CREATE OR REPLACE VIEW core.vw_portfolio_exposure AS
SELECT
    h.as_of_date,
    p.portfolio_node_name,
    p.portfolio_node_type,
    i.asset_class,
    i.sector,
    i.region,
    i.currency,
    SUM(COALESCE(h.exposure_base, h.market_value_base, 0)) AS total_exposure_base
FROM core.holdings_snapshot h
JOIN core.portfolio_node p
  ON p.portfolio_node_id = h.portfolio_node_id
JOIN core.instrument i
  ON i.instrument_id = h.instrument_id
GROUP BY
    h.as_of_date,
    p.portfolio_node_name,
    p.portfolio_node_type,
    i.asset_class,
    i.sector,
    i.region,
    i.currency;
