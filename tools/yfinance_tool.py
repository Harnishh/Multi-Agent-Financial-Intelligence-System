from utils.ticker_mapper import TICKER_MAP
import yfinance as yf
def get_company_data(company):
    ticker_symbol = TICKER_MAP.get(
        company.lower(),
        company
    )
    ticker = yf.Ticker(
        ticker_symbol
    )
    info = ticker.info

    return{
        "symbol": ticker_symbol,
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("markerCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow")
    }