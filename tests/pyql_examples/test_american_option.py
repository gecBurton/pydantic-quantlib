"""
Copyright (C) 2011, Enthought Inc
Copyright (C) 2011, Patrick Henaff

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the license for more details.
"""
from __future__ import print_function

import pytest
import QuantLib as ql

import pydantic_quantlib as pql

# global data
todays_date = pql.Date(d=15, m=pql.enums.Months.May.value, y=1998)
settlement_date = pql.Date(d=17, m=pql.enums.Months.May.value, y=1998)

risk_free_rate = pql.FlatForward(
    referenceDate=settlement_date, forward=0.06, dayCounter=pql.Actual365Fixed()
)

# option parameters
exercise = pql.AmericanExercise(
    earliestDate=settlement_date,
    latestDate=pql.Date(d=17, m=pql.enums.Months.May.value, y=1999),
)
payoff = pql.PlainVanillaPayoff(type=pql.enums.OptionType.Put, strike=40.0)

# market data
underlying = pql.SimpleQuote(value=36.0)
volatility = pql.BlackConstantVol(
    referenceDate=todays_date,
    c=pql.UnitedStates(),
    volatility=0.20,
    dayCounter=pql.Actual365Fixed(),
)
dividend_yield = pql.FlatForward(
    referenceDate=settlement_date, forward=0.00, dayCounter=pql.Actual365Fixed()
)

# # report
# header = '%19s' % 'method' + ' |' + \
#          ' |'.join(['%17s' % tag for tag in ['value',
#                                              'estimated error',
#                                              'actual error']])
# print()
# print(header)
# print('-' * len(header))
#
# refValue = None
#
# def report(method, x, dx=None):
#     e = '%.4f' % abs(x - refValue)
#     x = '%.5f' % x
#     if dx:
#         dx = '%.4f' % dx
#     else:
#         dx = 'n/a'
#     print('%19s' % method + ' |' +
#           ' |'.join(['%17s' % y for y in [x, dx, e]]))

# good to go

process = pql.BlackScholesMertonProcess(
    s0=pql.QuoteHandle(value=underlying),
    dividendTS=pql.YieldTermStructureHandle(value=dividend_yield),
    riskFreeTS=pql.YieldTermStructureHandle(value=risk_free_rate),
    volTS=pql.BlackVolTermStructureHandle(value=volatility),
)

option = pql.VanillaOption(payoff=payoff, exercise=exercise)

refValue = 4.48667344
# report('reference value', refValue)

# method: analytic


def compute_npv(option, engine, date):
    _option = option.to_quantlib()
    _engine = engine.to_quantlib()
    _date = date.to_quantlib()
    ql.Settings.instance().evaluation_date = _date
    _option.setPricingEngine(_engine)
    return _option.NPV()


def test_barone_adesi_whaley():  # Barone-Adesi-Whaley
    engine = pql.BaroneAdesiWhaleyApproximationEngine(process=process)
    assert compute_npv(option, engine, todays_date) == 0


def test_crank_nicolson():
    # method: finite differences
    time_steps = 801
    grid_points = 800

    # CrankNicolson
    engine = pql.FDAmericanEngine(
        process=process, timeSteps=time_steps, gridPoints=grid_points
    )
    assert compute_npv(option, engine, todays_date) == 0


def test_bjerksund_stensland():

    engine = pql.BjerksundStenslandApproximationEngine(process=process)
    assert compute_npv(option, engine, todays_date) == 0


@pytest.mark.parametrize(
    "method, expected",
    [
        (pql.BinomialJRVanillaEngine, 0),
        (pql.BinomialCRRVanillaEngine, 0),
        (pql.BinomialTrigeorgisVanillaEngine, 0),
        (pql.BinomialTianVanillaEngine, 0),
    ],
)
def test_binomial(method, expected):
    timeSteps = 801
    # ("eqp", 0),
    # ('lr', 0)

    engine = method(value=process, steps=timeSteps)
    assert compute_npv(option, engine, todays_date) == expected
