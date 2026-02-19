import argparse
from bot.logging_config import setup_logger
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


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

        # Create Binance client
        client = BinanceClient()

        # Place order
        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n=== Order Response ===")

        if order:
            print("Full Binance Response:")
            print(order)

            print("\nParsed Details:")
            print("Order ID:", order.get("orderId"))
            print("Client Order ID:", order.get("clientOrderId"))
            print("Status:", order.get("status"))
            print("Symbol:", order.get("symbol"))
            print("Side:", order.get("side"))
            print("Type:", order.get("type"))
            print("Executed Qty:", order.get("executedQty"))
            print("Price:", order.get("price"))
        else:
            print("No response received")

    except Exception as e:
        print("\n❌ Error:", e)


if __name__ == "__main__":
    main()

