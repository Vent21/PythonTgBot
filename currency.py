from pycbrf import ExchangeRates

"""
Доллар США - R01235
Евро - R01239
Китайский юань - R01375
"""
rates = ExchangeRates()
currency_rates_RU_and_USD = (
        rates["R01235"].name + " - " + str(rates["R01235"].rate) + "\n"
        + rates["R01239"].name + " - " + str(rates["R01239"].rate) + "\n"
        + rates["R01375"].name + " - " + str(rates["R01375"].rate))


def get_rates():
    # print(self.currency_rates_RU_and_USD)
    return currency_rates_RU_and_USD
