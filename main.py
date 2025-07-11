from datetime import datetime
from spy_signal_bot import get_current_price, get_ath_price, get_signal

def main():
    ath_price = get_ath_price()
    current_price = get_current_price()

    print(f"ATH: {ath_price:.2f} | Current: {current_price:.2f}")

    signal = get_signal(ath_price, current_price)

    if signal:
        with open("message.txt", "w") as f:
            f.write(signal)

        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        line = f"[{date_str}] {signal} | Close: {current_price:.2f} | ATH: {ath_price:.2f}\\n"
        with open("history_SPY.txt", "a") as f:
            f.write(line)

        print(f"Signal written: {signal}")
    else:
        print("No signal today.")

if __name__ == "__main__":
    main()