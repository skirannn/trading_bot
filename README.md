# Binance Futures Trading Bot

## Setup
pip install -r requirements.txt

Create .env file:
API_KEY=your_key
API_SECRET=your_secret

## Run

Market order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs
Logs saved in trading_bot.log
