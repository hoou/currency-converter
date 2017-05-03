#! /usr/bin/env python2.7
# coding=utf-8

import argparse
import json

from forex_python.converter import CurrencyRates, CurrencyCodes

# Dictionary for converting currency symbols to codes
CURRENCY_SYMBOL_DICT = {
    u"$": u"USD",
    u"BGN": u"BGN",
    u"Fr.": u"CHF",
    u"Ft": u"HUF",
    u"HK$": u"HKD",
    u"Kr": u"DKK",
    u"Kč": u"CZK",
    u"L": u"RON",
    u"NZ$": u"NZD",
    u"R": u"ZAR",
    u"R$": u"BRL",
    u"RM": u"MYR",
    u"Rp": u"IDR",
    u"S$": u"SGD",
    u"TRY": u"TRY",
    u"W": u"KRW",
    u"kn": u"HRK",
    u"kr": u"NOK",
    u"zł": u"PLN",
    u"£": u"GBP",
    u"¥": u"CNY",
    u"฿": u"THB",
    u"₪": u"ILS",
    u"€": u"EUR",
    u"₱": u"PHP",
    u"₹": u"INR"
}


# Parse input arguments
def parse_args():
    parser = argparse.ArgumentParser(description='help')

    required_arguments_group = parser.add_argument_group(
        'required arguments')

    required_arguments_group.add_argument(
        '--amount',
        type=float,
        required=True,
        help='amount which we want to convert'
    )
    required_arguments_group.add_argument(
        '--input_currency',
        type=Currency,
        required=True,
        help='input currency - 3 letters name OR currency symbol'
    )
    parser.add_argument(
        '--output_currency',
        type=Currency,
        help='output currency - 3 letters name OR currency symbol'
    )

    return parser.parse_args()


class Currency:
    def __init__(self, string):
        self.__check_format(string)

    def __check_format(self, string):
        currency_codes = CurrencyCodes()

        try:
            # First, think of input currency argument as symbol and try to find
            # it in dictionary
            self.code = CURRENCY_SYMBOL_DICT[string.decode('utf8')]

            # When symbol found in dictionary, we already saved its code,
            # so now just setup symbol member field
            self.symbol = string

        except KeyError:
            # When symbol not found in dictionary, input currency argument is
            # rather code
            self.code = string

            # Now try to get its symbol
            self.symbol = currency_codes.get_symbol(self.code)
            if not self.symbol:
                # When it cannot find its symbol, it must be invalid
                raise argparse.ArgumentTypeError('Invalid currency name/symbol')

    def get_code(self):
        return self.code

    def get_symbol(self):
        return self.symbol


def main():
    arguments = parse_args()

    currency_rates = CurrencyRates()

    # Print float values in json with maximum 2 decimal digits
    json.encoder.FLOAT_REPR = lambda f: ("%.2f" % f)

    if arguments.output_currency:
        # If output currency set, print one rate
        converted_amount = currency_rates.convert(
            arguments.input_currency.get_code(),
            arguments.output_currency.get_code(),
            arguments.amount
        )
        output = {arguments.output_currency.get_code(): converted_amount}
    else:
        # If output currency not set, print all rates

        # Get rates for input currency
        currency_rates_for_input = currency_rates.get_rates(
            arguments.input_currency.get_code())

        # Multiple all rates by input amount
        for code, value in currency_rates_for_input.iteritems():
            currency_rates_for_input[code] = value * arguments.amount

        output = currency_rates_for_input

    # Print output JSON
    print json.dumps(
        {
            "input": {
                "amount": arguments.amount,
                "currency": arguments.input_currency.get_code()
            },
            "output": output
        },
        indent=4
    )


if __name__ == "__main__":
    main()
