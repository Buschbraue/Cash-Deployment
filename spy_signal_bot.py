import yfinance as yf
from constants import SYMBOL, THRESHOLDS

def get_current_price():
    ticker = yf.Ticker(SYMBOL)
    hist = ticker.history(period="1d")
    return hist['Close'].iloc[-1]

def get_ath_price():
    ticker = yf.Ticker(SYMBOL)
    hist = ticker.history(period="max")
    return hist['Close'].max()

def get_signal(ath_price: float, current_price: float):
    drawdown = ((ath_price - current_price) / ath_price) * 100
    for threshold, invest_pct in sorted(THRESHOLDS, reverse=True):
        if drawdown >= threshold:
            return f"SPY is {threshold}% down from ATH — invest {invest_pct}%"
    return None