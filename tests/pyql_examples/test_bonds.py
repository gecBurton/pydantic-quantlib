""" Example demonstrating pricing bonds using PyQL.

This example is based on the QuantLib Excel bond demo.

"""
import pytest
import QuantLib as ql

import pydantic_quantlib as pql

todays_date = pql.Date(d=25, m=pql.Months.August.value, y=2021)


calendar = pql.TARGET()
effective_date = pql.Date(d=10, m=pql.Months.July.value, y=2016)
termination_date = pql.Date(d=10, m=pql.Months.July.value, y=2026)


settlement_days = 3
face_amount = 100.0
coupon_rate = 0.05
redemption = 100.0


fixed_bond_schedule = pql.Schedule0(
    effectiveDate=effective_date,
    terminationDate=termination_date,
    tenor=pql.Period1(frequency=pql.Frequency.Annual.value),
    calendar=calendar,
    convention=pql.BusinessDayConvention.ModifiedFollowing,
    terminationDateConvention=pql.BusinessDayConvention.ModifiedFollowing,
    rule=pql.DateGenerationRule.Backward,
    endOfMonth=False,
)

issue_date = effective_date
bond = pql.FixedRateBond2(
    settlementDays=settlement_days,
    faceAmount=face_amount,
    schedule=fixed_bond_schedule,
    coupons=[coupon_rate],
    paymentDayCounter=pql.ActualActual(c=pql.ActualActualConvention.ISMA),
    paymentConvention=pql.BusinessDayConvention.Following,
    redemption=redemption,
    issueDate=issue_date,
)

# discounting_term_structure = pql.YieldTermStructure(relinkable=True)
#
#
flat_term_structure = pql.FlatForward1(
    settlementDays=1,
    calendar=pql.NullCalendar(),
    forward=0.044,
    dayCounter=pql.Actual365Fixed(),
    compounding=pql.Compounding.Continuous,
    frequency=pql.Frequency.Annual,
)
ytsh = pql.YieldTermStructureHandle(value=flat_term_structure)
# discounting_term_structure.link_to(flat_term_structure)
pricing_engine = pql.DiscountingBondEngine(discountCurve=ytsh)


@pytest.fixture()
def instrument():
    ql.Settings.instance().evaluation_date = todays_date.to_quantlib()
    __bond = bond.to_quantlib()
    __bond.setPricingEngine(pricing_engine.to_quantlib())
    return __bond


def test_settlement_date(instrument):
    assert instrument.settlementDate() == ql.Date(14, 1, 2021)


def test_maturity_date(instrument):
    assert instrument.maturityDate() == ql.Date(10, 7, 2026)


def test_accrued_amount(instrument):
    assert instrument.accruedAmount(instrument.settlementDate()) == 2.5613079019073615


def test_clean_price(instrument):
    assert instrument.cleanPrice() == 102.36568054588133


def test_npv(instrument):
    assert instrument.NPV() == 104.90169403139318
