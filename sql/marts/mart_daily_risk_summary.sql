CREATE OR REPLACE VIEW core.mart_daily_risk_summary AS
SELECT
    as_of_date,
    portfolio_node_name,
    portfolio_node_type,
    SUM(total_exposure_base) AS total_exposure_base
FROM core.vw_portfolio_exposure
GROUP BY
    as_of_date,
    portfolio_node_name,
    portfolio_node_type;
