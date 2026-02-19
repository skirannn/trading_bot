import argparse
from bot.logging_config import setup_logger
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import *

def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        # Validate input
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n=== Order Request Summary ===")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        if price:
            print("Price:", price)

        client = BinanceClient()

        order = place_order(
            client, symbol, side, order_type, quantity, price
        )

        print("\n=== Order Response ===")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\n✅ Order successful")

    except Exception as e:
        print("\n❌ Error:", e)


if __name__ == "__main__":
    main()
