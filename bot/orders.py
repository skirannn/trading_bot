def place_order(client, symbol, side, order_type, quantity, price=None):

    if order_type == "MARKET":
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
        }

    elif order_type == "LIMIT":
        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "quantity": quantity,
            "price": price,
            "timeInForce": "GTC",
        }

    return client.create_order(params)
