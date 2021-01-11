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
todays_date = pql.Date(d=4, m=1, y=2021)
settlement_date = pql.Date(d=6, m=1, y=2021)

# options parameters
option_type = pql.OptionType.Put
maturity = pql.Date(d=4, m=1, y=2022)
daycounter = pql.Actual365Fixed()


risk_free_rate = pql.FlatForward0(
    referenceDate=settlement_date, forward=0.06, dayCounter=daycounter
)

# option parameters
exercise = pql.AmericanExercise(earliestDate=settlement_date, latestDate=maturity,)
payoff = pql.PlainVanillaPayoff(type=pql.OptionType.Put, strike=40)

# market data
underlying = pql.SimpleQuote(value=36)
volatility = pql.BlackConstantVol1(
    referenceDate=todays_date, c=pql.TARGET(), volatility=0.20, dayCounter=daycounter,
)
dividend_yield = pql.FlatForward0(
    referenceDate=settlement_date, forward=0.00, dayCounter=daycounter
)


# good to go

process = pql.BlackScholesMertonProcess(
    s0=pql.QuoteHandle(value=underlying),
    dividendTS=pql.YieldTermStructureHandle(value=dividend_yield),
    riskFreeTS=pql.YieldTermStructureHandle(value=risk_free_rate),
    volTS=pql.BlackVolTermStructureHandle(value=volatility),
)

option = pql.EuropeanOption(payoff=payoff, exercise=exercise)

_option = option.to_quantlib()
ql.Settings.instance().evaluation_date = todays_date.to_quantlib()


def compute_npv(engine):
    _engine = engine.to_quantlib()
    _option.setPricingEngine(_engine)
    return _option.NPV()


def test_barone_adesi_whaley():  # Barone-Adesi-Whaley
    engine = pql.BaroneAdesiWhaleyApproximationEngine(process=process)
    assert compute_npv(engine) == 4.463028111890139


def test_crank_nicolson():
    # method: finite differences
    time_steps = 801
    grid_points = 800

    # CrankNicolson
    engine = pql.FDAmericanEngine(
        process=process, timeSteps=time_steps, gridPoints=grid_points
    )
    assert compute_npv(engine) == 4.491333609168073


def test_bjerksund_stensland():

    engine = pql.BjerksundStenslandApproximationEngine(process=process)
    assert compute_npv(engine) == 4.456252976863002


@pytest.mark.parametrize(
    "method, expected",
    [
        (pql.BinomialJRVanillaEngine, 4.4840051360265285),
        (pql.BinomialCRRVanillaEngine, 4.483783154218361),
        (pql.BinomialTrigeorgisVanillaEngine, 4.483828512119),
        (pql.BinomialTianVanillaEngine, 4.483744968939698),
    ],
)
def test_binomial(method, expected):
    timeSteps = 801
    # ("eqp", 0),
    # ('lr', 0)

    engine = method(value=process, steps=timeSteps)
    assert compute_npv(engine) == expected
