## Description

This is simple currency converter using [forex-python](https://pypi.python.org/pypi/forex-python) package.

## Installation

```
$ pip install git+https://github.com/hoou/currency-converter
```

## Usage

```
$ currency-converter [-h] --amount AMOUNT --input_currency INPUT_CURRENCY
                          [--output_currency OUTPUT_CURRENCY]
```

- --amount - amount which we want to convert - float
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol

### Currency codes supported:
EUR, IDR, BGN, ILS, GBP, DKK, CAD, JPY, HUF, RON, MYR, SEK, SGD, HKD, AUD, CHF, KRW, CNY, TRY, HRK, NZD, THB, USD, NOK, RUB, INR, MXN, CZK, BRL, PLN, PHP, ZAR

### Currency symbols supported:
$, BGN, Fr., Ft, HK$, Kr, Kč, L, NZ$, R, R$, RM, Rp, S$, TRY, W, kn, kr, zł, £, ¥, ฿, ₪, €, ₱, ₹

## Examples
Basic usage:
```
$ currency-converter --amount 100 --input_currency EUR --output_currency USD
{
    "input": {
        "currency": "EUR",
        "amount": 100.00
    },
    "output": {
        "USD": 109.19
    }
}
```

Symbols support:
```
$ currency-converter --amount 50 --input_currency $ --output_currency EUR
{
    "input": {
        "currency": "USD",
        "amount": 50.00
    },
    "output": {
        "EUR": 45.79
    }
}
```

No output currency specified (list all of them):

```
$ currency-converter --amount 66.64 --input_currency GBP
{
    "input": {
        "currency": "GBP",
        "amount": 66.64
    },
    "output": {
        "USD": 86.17,
        "IDR": 1146541.20,
        "BGN": 154.35,
        "ILS": 311.70,
        "DKK": 586.95,
        "CAD": 118.30,
        "JPY": 9665.47,
        "HUF": 24634.81,
        "RON": 358.97,
        "MYR": 372.18,
        "SEK": 759.76,
        "SGD": 120.19,
        "HKD": 670.53,
        "AUD": 115.34,
        "CHF": 85.33,
        "KRW": 97507.65,
        "CNY": 594.01,
        "TRY": 304.65,
        "HRK": 587.90,
        "NZD": 124.44,
        "THB": 2971.68,
        "EUR": 78.92,
        "NOK": 740.90,
        "RUB": 4936.16,
        "INR": 5528.65,
        "MXN": 1620.68,
        "CZK": 2120.68,
        "BRL": 271.67,
        "PLN": 330.77,
        "PHP": 4307.68,
        "ZAR": 1150.07
    }
}
```

## Contributors

Tibor Mikita

## License

MIT