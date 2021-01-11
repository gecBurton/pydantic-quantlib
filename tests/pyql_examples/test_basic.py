""" Simple example pricing a European option
using a Black&Scholes Merton process.
"""

import QuantLib as ql

import pydantic_quantlib as pql

settings = ql.Settings.instance()
calendar = pql.TARGET()

offset = 366

todays_date = pql.Date(d=4, m=1, y=2021)
settlement_date = pql.Date(d=6, m=1, y=2021)

# options parameters
option_type = pql.OptionType.Put
underlying = 36
strike = 40
dividend_yield = 0.00
risk_free_rate = 0.06
volatility = 0.20
maturity = pql.Date(d=4, m=1, y=2022)
daycounter = pql.Actual365Fixed()

underlyingH = pql.QuoteHandle(value=pql.SimpleQuote(value=underlying))

# bootstrap the yield/dividend/vol curves
flat_term_structure = pql.YieldTermStructureHandle(
    value=pql.FlatForward0(
        referenceDate=settlement_date, forward=risk_free_rate, dayCounter=daycounter
    )
)

flat_dividend_ts = pql.YieldTermStructureHandle(
    value=pql.FlatForward0(
        referenceDate=settlement_date, forward=0.01, dayCounter=daycounter
    )
)

flat_vol_ts = pql.BlackVolTermStructureHandle(
    value=pql.BlackConstantVol1(
        referenceDate=settlement_date,
        c=calendar,
        volatility=volatility,
        dayCounter=daycounter,
    )
)

black_scholes_merton_process = pql.BlackScholesMertonProcess(
    s0=underlyingH,
    dividendTS=flat_dividend_ts,
    riskFreeTS=flat_term_structure,
    volTS=flat_vol_ts,
)

payoff = pql.PlainVanillaPayoff(type=option_type, strike=strike)

european_exercise = pql.EuropeanExercise(date=maturity)

european_option = pql.VanillaOptionBase(payoff=payoff, exercise=european_exercise)


method = "Black-Scholes"
analytic_european_engine = pql.AnalyticEuropeanEngine(
    value=black_scholes_merton_process
)


def test_npv():
    settings.evaluation_date = todays_date.to_quantlib()
    _european_option = european_option.to_quantlib()
    _analytic_european_engine = analytic_european_engine.to_quantlib()
    _european_option.setPricingEngine(_analytic_european_engine)
    assert _european_option.NPV() == 4.044235366488596
