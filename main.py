from datetime import datetime
from spy_signal_bot import get_current_price, get_ath_price, get_signal

def main():
    ath_price = get_ath_price()
    current_price = get_current_price()

    print(f"ATH: {ath_price:.2f} | Current: {current_price:.2f}")

    signal = get_signal(ath_price, current_price)

    date_str = datetime.utcnow().strftime("%Y-%m-%d")

    # Verlauf immer schreiben
    if signal:
        message = signal
    else:
        message = "No SPY drawdown signal today."

    line = f"[{date_str}] {message} | Close: {current_price:.2f} | ATH: {ath_price:.2f}\n"
    with open("history_SPY.txt", "a") as f:
        f.write(line)

    # Nur Nachricht an Discord, wenn Schwelle erreicht ist
    if signal:
        with open("message.txt", "w") as f:
            f.write(message)
    else:
        # Datei darf NICHT existieren, sonst schickt der Workflow sie trotzdem
        pass


if __name__ == "__main__":
    main()
