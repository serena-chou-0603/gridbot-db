sleep 2;


curl -X 'POST' \
  'http://0.0.0.0:8000/users/1/dcabots/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "account": "AVAX",
  "is_active": true,
  "symbol": "ETH/USD",
  "base_size": 0,
  "base_dollar": 20,
  "take_profit_pct": 0.003,
  "safety_pct": 0.003,
  "safety_size_multiplier": 1.3,
  "safety_range_multiplier": 1,
  "safety_max_times": 10,
  "trading_fee": 0.0005,
  "use_existing_coin": true,
  "dca_direction": "LONG"
  "check_orders_frequency": 5000,
  "investment": 1000,
  "start_price": 0,
  "start_date": "2022-09-13T14:10:29.592Z",
  "api_key": "9MrLOFnt9RRcQS3SkX-onWmqnG49swPs4KORPnNM",
  "secret_key": "QTRcd8e7VAUcqXRCk5H3hPf3S_LWIYWT6z-UqIuf"
}'

sleep 2;

curl -X 'POST' \
  'http://0.0.0.0:8000/users/1/dcabots/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "account": "MAIN",
  "is_active": true,
  "symbol": "ETHW/USD",
  "base_size": 0,
  "base_dollar": 20,
  "take_profit_pct": 0.003,
  "safety_pct": 0.003,
  "safety_size_multiplier": 1.3,
  "safety_range_multiplier": 1,
  "safety_max_times": 10,
  "trading_fee": 0.0005,
  "use_existing_coin": true,
  "dca_direction": "LONG",
  "check_orders_frequency": 5000,
  "investment": 1000,
  "start_price": 0,
  "start_date": "2022-09-15T14:10:29.592Z",
  "api_key": "df6rnY7n1SRUqPBWeTAkyfzOfHtpx0VmqhYhmY1Z",
  "secret_key": "N2hIFW1yv31laKeg2Y8t_tIhKe1TKIwR2VOs29ND"
}'
