from __future__ import annotations

__version__ = "0.3.0"


from enum import Enum
from typing import List, Literal, Optional, Union

import QuantLib as ql
from pydantic import Field, conint

from .core import BaseModel


class Frequency(Enum):
    Annual = ql.Annual


class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class TimeUnit(Enum):
    Days = 0
    Weeks = 1
    Months = 2
    Years = 3
    Hours = 4
    Minutes = 5
    Seconds = 6
    Milliseconds = 7


class OptionType(Enum):
    Call = 1
    Put = -1


class BusinessDayConvention(Enum):
    Following = 0
    ModifiedFollowing = 1
    Preceding = 2
    ModifiedPreceding = 3
    Unadjusted = 4
    HalfMonthModifiedFollowing = 5
    Nearest = 6


class DateGenerationRule(Enum):
    Backward = 0
    Forward = 1
    Zero = 2
    ThirdWednesday = 3
    Twentieth = 4
    TwentiethIMM = 5
    OldCDS = 6
    CDS = 7
    CDS2015 = 8


class Compounding(Enum):
    Simple = 0
    Compounded = 1
    Continuous = 2
    SimpleThenCompounded = 3
    CompoundedThenSimple = 4


class ActualActualConvention(Enum):
    ISMA = 0
    Bond = 1
    ISDA = 2
    Historical = 3
    Actual365 = 4
    AFB = 5
    Euro = 6


class CallabilityPriceType(Enum):
    Clean = 1
    Dirty = 0


class CallabilityType(Enum):
    Call = 0
    Put = 1


class VanillaSwapType(Enum):
    Payer = 1
    Receiver = -1


class VolatilityType(Enum):
    ShiftedLognormal = 0
    Normal = 1


class IMM(Enum):
    F = 1
    G = 2
    H = 3
    J = 4
    K = 5
    M = 6
    N = 7
    Q = 8
    U = 9
    V = 10
    X = 11
    Z = 12


class ASX(Enum):
    F = 1
    G = 2
    H = 3
    J = 4
    K = 5
    M = 6
    N = 7
    Q = 8
    U = 9
    V = 10
    X = 11
    Z = 12


class CzechRepublicMarket(Enum):
    Republic_PSE = 0


class FranceMarket(Enum):
    Exchange = 1
    Settlement = 0


class HongKongMarket(Enum):
    HKEx = 0


class GermanyMarket(Enum):
    Eurex = 3
    FrankfurtStockExchange = 1
    Settlement = 0
    Xetra = 2


class IcelandMarket(Enum):
    ICEX = 0


class IndiaMarket(Enum):
    NSE = 0


class IndonesiaMarket(Enum):
    JSX = 1


class IsraelMarket(Enum):
    Settlement = 0
    TASE = 1


class ItalyMarket(Enum):
    Exchange = 1
    Settlement = 0


class MexicoMarket(Enum):
    BMV = 0


class RussiaMarket(Enum):
    MOEX = 1
    Settlement = 0


class SaudiArabiaMarket(Enum):
    Tadawul = 0


class SingaporeMarket(Enum):
    SGX = 0


class SlovakiaMarket(Enum):
    BSSE = 0


class TaiwanMarket(Enum):
    TSEC = 0


class UkraineMarket(Enum):
    USE = 0


class ArgentinaMarket(Enum):
    Merval = 0


class BrazilMarket(Enum):
    Exchange = 1
    Settlement = 0


class CanadaMarket(Enum):
    Settlement = 0
    TSX = 1


class ChinaMarket(Enum):
    IB = 1
    SSE = 0


class SouthKoreaMarket(Enum):
    KRX = 1
    Settlement = 0


class SalvagingAlgorithm(Enum):
    NoAlgorithm = 0
    Spectral = 1


class CmsMarketCalibrationCalibrationType(Enum):
    OnForwardCmsPrice = 2
    OnPrice = 1
    OnSpread = 0


class GFunctionFactoryYieldCurveModel(Enum):
    ExactYield = 1
    NonParallelShifts = 3
    ParallelShifts = 2
    Standard = 0


class AnalyticPTDHestonEngineComplexLogFormula(Enum):
    AndersenPiterbarg = 1
    Gatheral = 0


class YearOnYearInflationSwapType(Enum):
    Payer = 1
    Receiver = -1


class Actual365FixedConvention(Enum):
    Standard = 0
    Canadian = 1
    NoLeap = 2


class AnalyticHestonEngineIntegrationAlgorithm(Enum):
    BroadieKayaExactSchemeLaguerre = 7
    BroadieKayaExactSchemeLobatto = 6
    BroadieKayaExactSchemeTrapezoidal = 8
    FullTruncation = 1
    NonCentralChiSquareVariance = 3
    PartialTruncation = 0
    QuadraticExponential = 4
    QuadraticExponentialMartingale = 5
    Reflection = 2


class SobolRsgDirectionIntegers(Enum):
    Unit = 0
    Jaeckel = 1
    SobolLevitan = 2
    SobolLevitanLemieux = 3
    JoeKuoD5 = 4
    JoeKuoD6 = 5
    JoeKuoD7 = 6
    Kuo = 7
    Kuo2 = 8
    Kuo3 = 9


class FdBlackScholesVanillaEngineCashDividendModel(Enum):
    Escrowed = 1
    Spot = 0


class FdmSchemeDescFdmSchemeType(Enum):
    CraigSneydType = 2
    CrankNicolsonType = 8
    DouglasType = 1
    ExplicitEulerType = 5
    HundsdorferType = 0
    ImplicitEulerType = 4
    MethodOfLinesType = 6
    ModifiedCraigSneydType = 3
    TrBDF2Type = 7


class BarrierType(Enum):
    DownIn = 0
    DownOut = 2
    UpIn = 1
    UpOut = 3


class OvernightIndexFutureNettingType(Enum):
    Averaging = 0
    Compounding = 1


class UnitedKingdomMarket(Enum):
    Exchange = 1
    Metals = 2
    Settlement = 0


class UnitedStatesMarket(Enum):
    FederalReserve = 5
    GovernmentBond = 2
    LiborImpact = 4
    NERC = 3
    NYSE = 1
    Settlement = 0


class DateGeneration(Enum):
    Backward = 0
    CDS = 7
    CDS2015 = 8
    Forward = 1
    OldCDS = 6
    ThirdWednesday = 3
    Twentieth = 4
    TwentiethIMM = 5
    Zero = 2


class LsmBasisSystem(Enum):
    Chebyshev = 5
    Chebyshev2nd = 6
    Hermite = 2
    Hyperbolic = 3
    Laguerre = 1
    Legendre = 4
    Monomial = 0


class Average(Enum):
    Arithmetic = 0
    Geometric = 1


class GJRGARCHProcessDiscretization(Enum):
    FullTruncation = 1
    PartialTruncation = 0
    Reflection = 2


class BlackCalibrationHelperCalibrationErrorType(Enum):
    ImpliedVolError = 2
    PriceError = 1
    RelativePriceError = 0


class DeltaVolQuoteDeltaType(Enum):
    AtmDeltaNeutral = 3
    AtmFwd = 2
    AtmGammaMax = 5
    AtmNull = 0
    AtmPutCall50 = 6
    AtmSpot = 1
    AtmVegaMax = 4
    Fwd = 1
    PaFwd = 3
    PaSpot = 2
    Spot = 0


class Thirty360Convention(Enum):
    BondBasis = 1
    EurobondBasis = 3
    European = 2
    Italian = 4
    USA = 0


class PillarChoice(Enum):
    CustomDate = 2
    LastRelevantDate = 1
    MaturityDate = 0


class SettlementType(Enum):
    Physical = 0
    Cash = 1
    CollateralizedCashPrice = 2
    ParYieldCurve = 3


class AverageType(Enum):
    Arithmetic = 0
    Geometric = 1


class PositionType(Enum):
    Long = 0
    Short = 1


class OvernightIndexedSwapType(Enum):
    Payer = 1
    Receiver = -1


class ImplicitEulerSchemeSolverType(Enum):
    BiCGstab = 0
    GMRES = 1


class MirrorGaussianSimulatedAnnealingResetScheme(Enum):
    NoResetScheme = 0
    ResetToBestPoint = 1
    ResetToOrigin = 2


class FuturesType(Enum):
    IMM = 0
    ASX = 1


class ProtectionSide(Enum):
    Buyer = 0
    Seller = 1


class IsdaCdsEngineNumericalFix(Enum):
    Flat = 0
    HalfDayBias = 0
    NoBias = 1
    NoFix = 0
    Piecewise = 1
    Taylor = 1


class DoubleBarrierType(Enum):
    KIKO = 2
    KnockIn = 0
    KnockOut = 1
    KOKI = 3


class GaussianSimulatedAnnealingResetScheme(Enum):
    NoResetScheme = 0
    ResetToBestPoint = 1
    ResetToOrigin = 2


class JointCalendarRule(Enum):
    BusinessDays = 1
    Holidays = 0


class ZeroCouponInflationSwapType(Enum):
    Payer = 1
    Receiver = -1


class Gaussian1dSwaptionEngineProbabilities(Enum):
    Digital = 2
    Naive = 1
    NoProb = 0


class Gaussian1dFloatFloatSwaptionEngineProbabilities(Enum):
    Digital = 2
    Naive = 1
    NoProb = 0


class LogNormalSimulatedAnnealingResetScheme(Enum):
    NoResetScheme = 0
    ResetToBestPoint = 1
    ResetToOrigin = 2


class CPIInterpolationType(Enum):
    AsIndex = 0
    Flat = 1
    Linear = 2


class ExerciseType(Enum):
    American = 0
    Bermuda = 1
    European = 2


class CPISwapType(Enum):
    Payer = 1
    Receiver = -1


class FdmSquareRootFwdOpTransformationType(Enum):
    Log = 2
    Plain = 0
    Power = 1


class AndreasenHugeVolatilityInterplInterpolationType(Enum):
    Put = -1
    CallPut = 0
    Call = 1
    Linear = 1
    CubicSpline = 2


class SobolBrownianGeneratorOrdering(Enum):
    Diagonal = 2
    Factors = 0
    Steps = 1


class Model(BaseModel):
    resource_name: Optional[Literal["Model"]] = "Model"


class Period1(BaseModel):
    resource_name: Optional[Literal["Period"]] = "Period"
    frequency: Frequency


class Date(BaseModel):
    resource_name: Optional[Literal["Date"]] = "Date"
    d: conint(ge=1, le=31)  # type: ignore
    m: conint(ge=1, le=12)  # type: ignore
    y: conint(ge=1900, le=2999)  # type: ignore


class DateParser(BaseModel):
    resource_name: Optional[Literal["DateParser"]] = "DateParser"


class PeriodParser(BaseModel):
    resource_name: Optional[Literal["PeriodParser"]] = "PeriodParser"


class EuropeanExercise(BaseModel):
    resource_name: Optional[Literal["EuropeanExercise"]] = "EuropeanExercise"
    date: Date


class AmericanExercise(BaseModel):
    resource_name: Optional[Literal["AmericanExercise"]] = "AmericanExercise"
    earliestDate: Date
    latestDate: Date
    payoffAtExpiry: Optional[bool] = None


class BermudanExercise(BaseModel):
    resource_name: Optional[Literal["BermudanExercise"]] = "BermudanExercise"
    dates: List[Date]
    payoffAtExpiry: Optional[bool] = None


class SwingExercise(BaseModel):
    resource_name: Optional[Literal["SwingExercise"]] = "SwingExercise"
    dates: List[Date]


class Array0(BaseModel):
    resource_name: Optional[Literal["Array"]] = "Array"
    n: Optional[int] = None
    fill: Optional[float] = None


class Array1(BaseModel):
    resource_name: Optional[Literal["Array"]] = "Array"
    n: int


class DefaultLexicographicalViewColumn(BaseModel):
    resource_name: Optional[
        Literal["DefaultLexicographicalViewColumn"]
    ] = "DefaultLexicographicalViewColumn"


class MatrixRow(BaseModel):
    resource_name: Optional[Literal["MatrixRow"]] = "MatrixRow"


class Matrix0(BaseModel):
    resource_name: Optional[Literal["Matrix"]] = "Matrix"
    rows: Optional[int] = None
    columns: Optional[int] = None
    fill: Optional[float] = None


class Matrix1(BaseModel):
    resource_name: Optional[Literal["Matrix"]] = "Matrix"
    rows: int
    columns: int


class SVD(BaseModel):
    resource_name: Optional[Literal["SVD"]] = "SVD"
    value: Matrix


class QuoteHandle(BaseModel):
    resource_name: Optional[Literal["QuoteHandle"]] = "QuoteHandle"
    value: Optional[Quote] = None


class RelinkableQuoteHandle(BaseModel):
    resource_name: Optional[Literal["RelinkableQuoteHandle"]] = "RelinkableQuoteHandle"
    value: Optional[Quote] = None


class SimpleQuote(BaseModel):
    resource_name: Optional[Literal["SimpleQuote"]] = "SimpleQuote"
    value: float


class Australia(BaseModel):
    resource_name: Optional[Literal["Australia"]] = "Australia"


class Denmark(BaseModel):
    resource_name: Optional[Literal["Denmark"]] = "Denmark"


class Finland(BaseModel):
    resource_name: Optional[Literal["Finland"]] = "Finland"


class Hungary(BaseModel):
    resource_name: Optional[Literal["Hungary"]] = "Hungary"


class Japan(BaseModel):
    resource_name: Optional[Literal["Japan"]] = "Japan"


class NewZealand(BaseModel):
    resource_name: Optional[Literal["NewZealand"]] = "NewZealand"


class Norway(BaseModel):
    resource_name: Optional[Literal["Norway"]] = "Norway"


class Poland(BaseModel):
    resource_name: Optional[Literal["Poland"]] = "Poland"


class Romania(BaseModel):
    resource_name: Optional[Literal["Romania"]] = "Romania"


class SouthAfrica(BaseModel):
    resource_name: Optional[Literal["SouthAfrica"]] = "SouthAfrica"


class Sweden(BaseModel):
    resource_name: Optional[Literal["Sweden"]] = "Sweden"


class Switzerland(BaseModel):
    resource_name: Optional[Literal["Switzerland"]] = "Switzerland"


class TARGET(BaseModel):
    resource_name: Optional[Literal["TARGET"]] = "TARGET"


class Thailand(BaseModel):
    resource_name: Optional[Literal["Thailand"]] = "Thailand"


class Turkey(BaseModel):
    resource_name: Optional[Literal["Turkey"]] = "Turkey"


class NullCalendar(BaseModel):
    resource_name: Optional[Literal["NullCalendar"]] = "NullCalendar"


class WeekendsOnly(BaseModel):
    resource_name: Optional[Literal["WeekendsOnly"]] = "WeekendsOnly"


class BespokeCalendar(BaseModel):
    resource_name: Optional[Literal["BespokeCalendar"]] = "BespokeCalendar"
    name: str


class Actual360(BaseModel):
    resource_name: Optional[Literal["Actual36"]] = "Actual36"
    includeLastDay: Optional[bool] = None


class OneDayCounter(BaseModel):
    resource_name: Optional[Literal["OneDayCounter"]] = "OneDayCounter"


class SimpleDayCounter(BaseModel):
    resource_name: Optional[Literal["SimpleDayCounter"]] = "SimpleDayCounter"


class Business252(BaseModel):
    resource_name: Optional[Literal["Business25"]] = "Business25"
    c: Optional[Calendar] = None


class UpRounding(BaseModel):
    resource_name: Optional[Literal["UpRounding"]] = "UpRounding"
    precision: int
    digit: Optional[int] = None


class DownRounding(BaseModel):
    resource_name: Optional[Literal["DownRounding"]] = "DownRounding"
    precision: int
    digit: Optional[int] = None


class ClosestRounding(BaseModel):
    resource_name: Optional[Literal["ClosestRounding"]] = "ClosestRounding"
    precision: int
    digit: Optional[int] = None


class CeilingTruncation(BaseModel):
    resource_name: Optional[Literal["CeilingTruncation"]] = "CeilingTruncation"
    precision: int
    digit: Optional[int] = None


class FloorTruncation(BaseModel):
    resource_name: Optional[Literal["FloorTruncation"]] = "FloorTruncation"
    precision: int
    digit: Optional[int] = None


class ARSCurrency(BaseModel):
    resource_name: Optional[Literal["ARSCurrency"]] = "ARSCurrency"


class ATSCurrency(BaseModel):
    resource_name: Optional[Literal["ATSCurrency"]] = "ATSCurrency"


class AUDCurrency(BaseModel):
    resource_name: Optional[Literal["AUDCurrency"]] = "AUDCurrency"


class BDTCurrency(BaseModel):
    resource_name: Optional[Literal["BDTCurrency"]] = "BDTCurrency"


class BEFCurrency(BaseModel):
    resource_name: Optional[Literal["BEFCurrency"]] = "BEFCurrency"


class BGLCurrency(BaseModel):
    resource_name: Optional[Literal["BGLCurrency"]] = "BGLCurrency"


class BRLCurrency(BaseModel):
    resource_name: Optional[Literal["BRLCurrency"]] = "BRLCurrency"


class BYRCurrency(BaseModel):
    resource_name: Optional[Literal["BYRCurrency"]] = "BYRCurrency"


class CADCurrency(BaseModel):
    resource_name: Optional[Literal["CADCurrency"]] = "CADCurrency"


class CHFCurrency(BaseModel):
    resource_name: Optional[Literal["CHFCurrency"]] = "CHFCurrency"


class CLPCurrency(BaseModel):
    resource_name: Optional[Literal["CLPCurrency"]] = "CLPCurrency"


class CNYCurrency(BaseModel):
    resource_name: Optional[Literal["CNYCurrency"]] = "CNYCurrency"


class COPCurrency(BaseModel):
    resource_name: Optional[Literal["COPCurrency"]] = "COPCurrency"


class CYPCurrency(BaseModel):
    resource_name: Optional[Literal["CYPCurrency"]] = "CYPCurrency"


class CZKCurrency(BaseModel):
    resource_name: Optional[Literal["CZKCurrency"]] = "CZKCurrency"


class DEMCurrency(BaseModel):
    resource_name: Optional[Literal["DEMCurrency"]] = "DEMCurrency"


class DKKCurrency(BaseModel):
    resource_name: Optional[Literal["DKKCurrency"]] = "DKKCurrency"


class EEKCurrency(BaseModel):
    resource_name: Optional[Literal["EEKCurrency"]] = "EEKCurrency"


class ESPCurrency(BaseModel):
    resource_name: Optional[Literal["ESPCurrency"]] = "ESPCurrency"


class EURCurrency(BaseModel):
    resource_name: Optional[Literal["EURCurrency"]] = "EURCurrency"


class FIMCurrency(BaseModel):
    resource_name: Optional[Literal["FIMCurrency"]] = "FIMCurrency"


class FRFCurrency(BaseModel):
    resource_name: Optional[Literal["FRFCurrency"]] = "FRFCurrency"


class GBPCurrency(BaseModel):
    resource_name: Optional[Literal["GBPCurrency"]] = "GBPCurrency"


class GRDCurrency(BaseModel):
    resource_name: Optional[Literal["GRDCurrency"]] = "GRDCurrency"


class HKDCurrency(BaseModel):
    resource_name: Optional[Literal["HKDCurrency"]] = "HKDCurrency"


class HUFCurrency(BaseModel):
    resource_name: Optional[Literal["HUFCurrency"]] = "HUFCurrency"


class IEPCurrency(BaseModel):
    resource_name: Optional[Literal["IEPCurrency"]] = "IEPCurrency"


class IDRCurrency(BaseModel):
    resource_name: Optional[Literal["IDRCurrency"]] = "IDRCurrency"


class ILSCurrency(BaseModel):
    resource_name: Optional[Literal["ILSCurrency"]] = "ILSCurrency"


class INRCurrency(BaseModel):
    resource_name: Optional[Literal["INRCurrency"]] = "INRCurrency"


class IQDCurrency(BaseModel):
    resource_name: Optional[Literal["IQDCurrency"]] = "IQDCurrency"


class IRRCurrency(BaseModel):
    resource_name: Optional[Literal["IRRCurrency"]] = "IRRCurrency"


class ISKCurrency(BaseModel):
    resource_name: Optional[Literal["ISKCurrency"]] = "ISKCurrency"


class ITLCurrency(BaseModel):
    resource_name: Optional[Literal["ITLCurrency"]] = "ITLCurrency"


class JPYCurrency(BaseModel):
    resource_name: Optional[Literal["JPYCurrency"]] = "JPYCurrency"


class KRWCurrency(BaseModel):
    resource_name: Optional[Literal["KRWCurrency"]] = "KRWCurrency"


class KWDCurrency(BaseModel):
    resource_name: Optional[Literal["KWDCurrency"]] = "KWDCurrency"


class LTLCurrency(BaseModel):
    resource_name: Optional[Literal["LTLCurrency"]] = "LTLCurrency"


class LUFCurrency(BaseModel):
    resource_name: Optional[Literal["LUFCurrency"]] = "LUFCurrency"


class LVLCurrency(BaseModel):
    resource_name: Optional[Literal["LVLCurrency"]] = "LVLCurrency"


class MTLCurrency(BaseModel):
    resource_name: Optional[Literal["MTLCurrency"]] = "MTLCurrency"


class MXNCurrency(BaseModel):
    resource_name: Optional[Literal["MXNCurrency"]] = "MXNCurrency"


class MYRCurrency(BaseModel):
    resource_name: Optional[Literal["MYRCurrency"]] = "MYRCurrency"


class NLGCurrency(BaseModel):
    resource_name: Optional[Literal["NLGCurrency"]] = "NLGCurrency"


class NOKCurrency(BaseModel):
    resource_name: Optional[Literal["NOKCurrency"]] = "NOKCurrency"


class NPRCurrency(BaseModel):
    resource_name: Optional[Literal["NPRCurrency"]] = "NPRCurrency"


class NZDCurrency(BaseModel):
    resource_name: Optional[Literal["NZDCurrency"]] = "NZDCurrency"


class PEHCurrency(BaseModel):
    resource_name: Optional[Literal["PEHCurrency"]] = "PEHCurrency"


class PEICurrency(BaseModel):
    resource_name: Optional[Literal["PEICurrency"]] = "PEICurrency"


class PENCurrency(BaseModel):
    resource_name: Optional[Literal["PENCurrency"]] = "PENCurrency"


class PKRCurrency(BaseModel):
    resource_name: Optional[Literal["PKRCurrency"]] = "PKRCurrency"


class PLNCurrency(BaseModel):
    resource_name: Optional[Literal["PLNCurrency"]] = "PLNCurrency"


class PTECurrency(BaseModel):
    resource_name: Optional[Literal["PTECurrency"]] = "PTECurrency"


class ROLCurrency(BaseModel):
    resource_name: Optional[Literal["ROLCurrency"]] = "ROLCurrency"


class RONCurrency(BaseModel):
    resource_name: Optional[Literal["RONCurrency"]] = "RONCurrency"


class RUBCurrency(BaseModel):
    resource_name: Optional[Literal["RUBCurrency"]] = "RUBCurrency"


class SARCurrency(BaseModel):
    resource_name: Optional[Literal["SARCurrency"]] = "SARCurrency"


class SEKCurrency(BaseModel):
    resource_name: Optional[Literal["SEKCurrency"]] = "SEKCurrency"


class SGDCurrency(BaseModel):
    resource_name: Optional[Literal["SGDCurrency"]] = "SGDCurrency"


class SITCurrency(BaseModel):
    resource_name: Optional[Literal["SITCurrency"]] = "SITCurrency"


class SKKCurrency(BaseModel):
    resource_name: Optional[Literal["SKKCurrency"]] = "SKKCurrency"


class THBCurrency(BaseModel):
    resource_name: Optional[Literal["THBCurrency"]] = "THBCurrency"


class TRLCurrency(BaseModel):
    resource_name: Optional[Literal["TRLCurrency"]] = "TRLCurrency"


class TRYCurrency(BaseModel):
    resource_name: Optional[Literal["TRYCurrency"]] = "TRYCurrency"


class TTDCurrency(BaseModel):
    resource_name: Optional[Literal["TTDCurrency"]] = "TTDCurrency"


class TWDCurrency(BaseModel):
    resource_name: Optional[Literal["TWDCurrency"]] = "TWDCurrency"


class USDCurrency(BaseModel):
    resource_name: Optional[Literal["USDCurrency"]] = "USDCurrency"


class VEBCurrency(BaseModel):
    resource_name: Optional[Literal["VEBCurrency"]] = "VEBCurrency"


class VNDCurrency(BaseModel):
    resource_name: Optional[Literal["VNDCurrency"]] = "VNDCurrency"


class ZARCurrency(BaseModel):
    resource_name: Optional[Literal["ZARCurrency"]] = "ZARCurrency"


class SafeLinearInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeLinearInterpolation"]
    ] = "SafeLinearInterpolation"
    x: Array
    y: Array


class SafeLogLinearInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeLogLinearInterpolation"]
    ] = "SafeLogLinearInterpolation"
    x: Array
    y: Array


class SafeBackwardFlatInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeBackwardFlatInterpolation"]
    ] = "SafeBackwardFlatInterpolation"
    x: Array
    y: Array


class SafeForwardFlatInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeForwardFlatInterpolation"]
    ] = "SafeForwardFlatInterpolation"
    x: Array
    y: Array


class SafeCubicNaturalSpline(BaseModel):
    resource_name: Optional[
        Literal["SafeCubicNaturalSpline"]
    ] = "SafeCubicNaturalSpline"
    x: Array
    y: Array


class SafeLogCubicNaturalSpline(BaseModel):
    resource_name: Optional[
        Literal["SafeLogCubicNaturalSpline"]
    ] = "SafeLogCubicNaturalSpline"
    x: Array
    y: Array


class SafeMonotonicCubicNaturalSpline(BaseModel):
    resource_name: Optional[
        Literal["SafeMonotonicCubicNaturalSpline"]
    ] = "SafeMonotonicCubicNaturalSpline"
    x: Array
    y: Array


class SafeMonotonicLogCubicNaturalSpline(BaseModel):
    resource_name: Optional[
        Literal["SafeMonotonicLogCubicNaturalSpline"]
    ] = "SafeMonotonicLogCubicNaturalSpline"
    x: Array
    y: Array


class SafeKrugerCubic(BaseModel):
    resource_name: Optional[Literal["SafeKrugerCubic"]] = "SafeKrugerCubic"
    x: Array
    y: Array


class SafeKrugerLogCubic(BaseModel):
    resource_name: Optional[Literal["SafeKrugerLogCubic"]] = "SafeKrugerLogCubic"
    x: Array
    y: Array


class SafeFritschButlandCubic(BaseModel):
    resource_name: Optional[
        Literal["SafeFritschButlandCubic"]
    ] = "SafeFritschButlandCubic"
    x: Array
    y: Array


class SafeFritschButlandLogCubic(BaseModel):
    resource_name: Optional[
        Literal["SafeFritschButlandLogCubic"]
    ] = "SafeFritschButlandLogCubic"
    x: Array
    y: Array


class SafeParabolic(BaseModel):
    resource_name: Optional[Literal["SafeParabolic"]] = "SafeParabolic"
    x: Array
    y: Array


class SafeLogParabolic(BaseModel):
    resource_name: Optional[Literal["SafeLogParabolic"]] = "SafeLogParabolic"
    x: Array
    y: Array


class SafeMonotonicParabolic(BaseModel):
    resource_name: Optional[
        Literal["SafeMonotonicParabolic"]
    ] = "SafeMonotonicParabolic"
    x: Array
    y: Array


class SafeMonotonicLogParabolic(BaseModel):
    resource_name: Optional[
        Literal["SafeMonotonicLogParabolic"]
    ] = "SafeMonotonicLogParabolic"
    x: Array
    y: Array


class SafeBilinearInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeBilinearInterpolation"]
    ] = "SafeBilinearInterpolation"
    x: Array
    y: Array
    m: Matrix


class SafeBicubicSpline(BaseModel):
    resource_name: Optional[Literal["SafeBicubicSpline"]] = "SafeBicubicSpline"
    x: Array
    y: Array
    m: Matrix


class BackwardFlat(BaseModel):
    resource_name: Optional[Literal["BackwardFlat"]] = "BackwardFlat"


class ForwardFlat(BaseModel):
    resource_name: Optional[Literal["ForwardFlat"]] = "ForwardFlat"


class Linear(BaseModel):
    resource_name: Optional[Literal["Linear"]] = "Linear"


class LogLinear(BaseModel):
    resource_name: Optional[Literal["LogLinear"]] = "LogLinear"


class Cubic(BaseModel):
    resource_name: Optional[Literal["Cubic"]] = "Cubic"


class MonotonicCubic(BaseModel):
    resource_name: Optional[Literal["MonotonicCubic"]] = "MonotonicCubic"


class DefaultLogCubic(BaseModel):
    resource_name: Optional[Literal["DefaultLogCubic"]] = "DefaultLogCubic"


class MonotonicLogCubic(BaseModel):
    resource_name: Optional[Literal["MonotonicLogCubic"]] = "MonotonicLogCubic"


class SplineCubic(BaseModel):
    resource_name: Optional[Literal["SplineCubic"]] = "SplineCubic"


class Kruger(BaseModel):
    resource_name: Optional[Literal["Kruger"]] = "Kruger"


class KrugerLog(BaseModel):
    resource_name: Optional[Literal["KrugerLog"]] = "KrugerLog"


class ConvexMonotone(BaseModel):
    resource_name: Optional[Literal["ConvexMonotone"]] = "ConvexMonotone"
    quadraticity: Optional[float] = None
    monotonicity: Optional[float] = None
    forcePositive: Optional[bool] = None


class SafeConvexMonotoneInterpolation(BaseModel):
    resource_name: Optional[
        Literal["SafeConvexMonotoneInterpolation"]
    ] = "SafeConvexMonotoneInterpolation"
    x: Array
    y: Array
    quadraticity: Optional[float] = None
    monotonicity: Optional[float] = None
    forcePositive: Optional[bool] = None


class YieldTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["YieldTermStructureHandle"]
    ] = "YieldTermStructureHandle"
    value: Optional[YieldTermStructure] = None


class RelinkableYieldTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableYieldTermStructureHandle"]
    ] = "RelinkableYieldTermStructureHandle"
    value: Optional[YieldTermStructure] = None


class ImpliedTermStructure(BaseModel):
    resource_name: Optional[Literal["ImpliedTermStructure"]] = "ImpliedTermStructure"
    curveHandle: YieldTermStructureHandle
    referenceDate: Date


class ForwardSpreadedTermStructure(BaseModel):
    resource_name: Optional[
        Literal["ForwardSpreadedTermStructure"]
    ] = "ForwardSpreadedTermStructure"
    curveHandle: YieldTermStructureHandle
    spreadHandle: QuoteHandle


class RealTimeSeries(BaseModel):
    resource_name: Optional[Literal["RealTimeSeries"]] = "RealTimeSeries"


class IntervalPriceTimeSeries(BaseModel):
    resource_name: Optional[
        Literal["IntervalPriceTimeSeries"]
    ] = "IntervalPriceTimeSeries"


class IntervalPrice(BaseModel):
    resource_name: Optional[Literal["IntervalPrice"]] = "IntervalPrice"
    arg_0: float
    arg_1: float
    arg_2: float
    arg_3: float


class IndexManager(BaseModel):
    resource_name: Optional[Literal["IndexManager"]] = "IndexManager"


class OvernightIndexBase(BaseModel):
    resource_name: Optional[Literal["OvernightIndex"]] = "OvernightIndex"
    familyName: str
    settlementDays: int
    currency: Currency
    calendar: Calendar
    dayCounter: DayCounter
    h: Optional[YieldTermStructureHandle] = None


class DailyTenorLiborBase(BaseModel):
    resource_name: Optional[Literal["DailyTenorLibor"]] = "DailyTenorLibor"
    familyName: str
    settlementDays: float
    currency: Currency
    financialCenterCalendar: Calendar
    dayCounter: DayCounter
    h: Optional[YieldTermStructureHandle] = None


class CADLiborON(BaseModel):
    resource_name: Optional[Literal["CADLiborON"]] = "CADLiborON"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw1M(BaseModel):
    resource_name: Optional[Literal["Bbsw1M"]] = "Bbsw1M"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw2M(BaseModel):
    resource_name: Optional[Literal["Bbsw2M"]] = "Bbsw2M"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw3M(BaseModel):
    resource_name: Optional[Literal["Bbsw3M"]] = "Bbsw3M"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw4M(BaseModel):
    resource_name: Optional[Literal["Bbsw4M"]] = "Bbsw4M"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw5M(BaseModel):
    resource_name: Optional[Literal["Bbsw5M"]] = "Bbsw5M"
    h: Optional[YieldTermStructureHandle] = None


class Bbsw6M(BaseModel):
    resource_name: Optional[Literal["Bbsw6M"]] = "Bbsw6M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm1M(BaseModel):
    resource_name: Optional[Literal["Bkbm1M"]] = "Bkbm1M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm2M(BaseModel):
    resource_name: Optional[Literal["Bkbm2M"]] = "Bkbm2M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm3M(BaseModel):
    resource_name: Optional[Literal["Bkbm3M"]] = "Bkbm3M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm4M(BaseModel):
    resource_name: Optional[Literal["Bkbm4M"]] = "Bkbm4M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm5M(BaseModel):
    resource_name: Optional[Literal["Bkbm5M"]] = "Bkbm5M"
    h: Optional[YieldTermStructureHandle] = None


class Bkbm6M(BaseModel):
    resource_name: Optional[Literal["Bkbm6M"]] = "Bkbm6M"
    h: Optional[YieldTermStructureHandle] = None


class EuriborSW(BaseModel):
    resource_name: Optional[Literal["EuriborSW"]] = "EuriborSW"
    h: Optional[YieldTermStructureHandle] = None


class Euribor2W(BaseModel):
    resource_name: Optional[Literal["Euribor2W"]] = "Euribor2W"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3W(BaseModel):
    resource_name: Optional[Literal["Euribor3W"]] = "Euribor3W"
    h: Optional[YieldTermStructureHandle] = None


class Euribor1M(BaseModel):
    resource_name: Optional[Literal["Euribor1M"]] = "Euribor1M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor2M(BaseModel):
    resource_name: Optional[Literal["Euribor2M"]] = "Euribor2M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3M(BaseModel):
    resource_name: Optional[Literal["Euribor3M"]] = "Euribor3M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor4M(BaseModel):
    resource_name: Optional[Literal["Euribor4M"]] = "Euribor4M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor5M(BaseModel):
    resource_name: Optional[Literal["Euribor5M"]] = "Euribor5M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor6M(BaseModel):
    resource_name: Optional[Literal["Euribor6M"]] = "Euribor6M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor7M(BaseModel):
    resource_name: Optional[Literal["Euribor7M"]] = "Euribor7M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor8M(BaseModel):
    resource_name: Optional[Literal["Euribor8M"]] = "Euribor8M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor9M(BaseModel):
    resource_name: Optional[Literal["Euribor9M"]] = "Euribor9M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor10M(BaseModel):
    resource_name: Optional[Literal["Euribor10M"]] = "Euribor10M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor11M(BaseModel):
    resource_name: Optional[Literal["Euribor11M"]] = "Euribor11M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor1Y(BaseModel):
    resource_name: Optional[Literal["Euribor1Y"]] = "Euribor1Y"
    h: Optional[YieldTermStructureHandle] = None


class Euribor365SW(BaseModel):
    resource_name: Optional[Literal["Euribor365SW"]] = "Euribor365SW"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3652W(BaseModel):
    resource_name: Optional[Literal["Euribor3652W"]] = "Euribor3652W"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3653W(BaseModel):
    resource_name: Optional[Literal["Euribor3653W"]] = "Euribor3653W"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3651M(BaseModel):
    resource_name: Optional[Literal["Euribor3651M"]] = "Euribor3651M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3652M(BaseModel):
    resource_name: Optional[Literal["Euribor3652M"]] = "Euribor3652M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3653M(BaseModel):
    resource_name: Optional[Literal["Euribor3653M"]] = "Euribor3653M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3654M(BaseModel):
    resource_name: Optional[Literal["Euribor3654M"]] = "Euribor3654M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3655M(BaseModel):
    resource_name: Optional[Literal["Euribor3655M"]] = "Euribor3655M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3656M(BaseModel):
    resource_name: Optional[Literal["Euribor3656M"]] = "Euribor3656M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3657M(BaseModel):
    resource_name: Optional[Literal["Euribor3657M"]] = "Euribor3657M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3658M(BaseModel):
    resource_name: Optional[Literal["Euribor3658M"]] = "Euribor3658M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3659M(BaseModel):
    resource_name: Optional[Literal["Euribor3659M"]] = "Euribor3659M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor36510M(BaseModel):
    resource_name: Optional[Literal["Euribor36510M"]] = "Euribor36510M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor36511M(BaseModel):
    resource_name: Optional[Literal["Euribor36511M"]] = "Euribor36511M"
    h: Optional[YieldTermStructureHandle] = None


class Euribor3651Y(BaseModel):
    resource_name: Optional[Literal["Euribor3651Y"]] = "Euribor3651Y"
    h: Optional[YieldTermStructureHandle] = None


class EURLiborSW(BaseModel):
    resource_name: Optional[Literal["EURLiborSW"]] = "EURLiborSW"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor2W(BaseModel):
    resource_name: Optional[Literal["EURLibor2W"]] = "EURLibor2W"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor1M(BaseModel):
    resource_name: Optional[Literal["EURLibor1M"]] = "EURLibor1M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor2M(BaseModel):
    resource_name: Optional[Literal["EURLibor2M"]] = "EURLibor2M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor3M(BaseModel):
    resource_name: Optional[Literal["EURLibor3M"]] = "EURLibor3M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor4M(BaseModel):
    resource_name: Optional[Literal["EURLibor4M"]] = "EURLibor4M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor5M(BaseModel):
    resource_name: Optional[Literal["EURLibor5M"]] = "EURLibor5M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor6M(BaseModel):
    resource_name: Optional[Literal["EURLibor6M"]] = "EURLibor6M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor7M(BaseModel):
    resource_name: Optional[Literal["EURLibor7M"]] = "EURLibor7M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor8M(BaseModel):
    resource_name: Optional[Literal["EURLibor8M"]] = "EURLibor8M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor9M(BaseModel):
    resource_name: Optional[Literal["EURLibor9M"]] = "EURLibor9M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor10M(BaseModel):
    resource_name: Optional[Literal["EURLibor10M"]] = "EURLibor10M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor11M(BaseModel):
    resource_name: Optional[Literal["EURLibor11M"]] = "EURLibor11M"
    h: Optional[YieldTermStructureHandle] = None


class EURLibor1Y(BaseModel):
    resource_name: Optional[Literal["EURLibor1Y"]] = "EURLibor1Y"
    h: Optional[YieldTermStructureHandle] = None


class GBPLiborON(BaseModel):
    resource_name: Optional[Literal["GBPLiborON"]] = "GBPLiborON"
    h: Optional[YieldTermStructureHandle] = None


class USDLiborON(BaseModel):
    resource_name: Optional[Literal["USDLiborON"]] = "USDLiborON"
    h: Optional[YieldTermStructureHandle] = None


class Aonia(BaseModel):
    resource_name: Optional[Literal["Aonia"]] = "Aonia"
    h: Optional[YieldTermStructureHandle] = None


class Eonia(BaseModel):
    resource_name: Optional[Literal["Eonia"]] = "Eonia"
    h: Optional[YieldTermStructureHandle] = None


class Sonia(BaseModel):
    resource_name: Optional[Literal["Sonia"]] = "Sonia"
    h: Optional[YieldTermStructureHandle] = None


class FedFunds(BaseModel):
    resource_name: Optional[Literal["FedFunds"]] = "FedFunds"
    h: Optional[YieldTermStructureHandle] = None


class Nzocr(BaseModel):
    resource_name: Optional[Literal["Nzocr"]] = "Nzocr"
    h: Optional[YieldTermStructureHandle] = None


class Sofr(BaseModel):
    resource_name: Optional[Literal["Sofr"]] = "Sofr"
    h: Optional[YieldTermStructureHandle] = None


class BiborSW(BaseModel):
    resource_name: Optional[Literal["BiborSW"]] = "BiborSW"
    h: Optional[YieldTermStructureHandle] = None


class Bibor1M(BaseModel):
    resource_name: Optional[Literal["Bibor1M"]] = "Bibor1M"
    h: Optional[YieldTermStructureHandle] = None


class Bibor2M(BaseModel):
    resource_name: Optional[Literal["Bibor2M"]] = "Bibor2M"
    h: Optional[YieldTermStructureHandle] = None


class Bibor3M(BaseModel):
    resource_name: Optional[Literal["Bibor3M"]] = "Bibor3M"
    h: Optional[YieldTermStructureHandle] = None


class Bibor6M(BaseModel):
    resource_name: Optional[Literal["Bibor6M"]] = "Bibor6M"
    h: Optional[YieldTermStructureHandle] = None


class Bibor9M(BaseModel):
    resource_name: Optional[Literal["Bibor9M"]] = "Bibor9M"
    h: Optional[YieldTermStructureHandle] = None


class Bibor1Y(BaseModel):
    resource_name: Optional[Literal["Bibor1Y"]] = "Bibor1Y"
    h: Optional[YieldTermStructureHandle] = None


class Brent(BaseModel):
    resource_name: Optional[Literal["Brent"]] = "Brent"


class Bisection(BaseModel):
    resource_name: Optional[Literal["Bisection"]] = "Bisection"


class FalsePosition(BaseModel):
    resource_name: Optional[Literal["FalsePosition"]] = "FalsePosition"


class Ridder(BaseModel):
    resource_name: Optional[Literal["Ridder"]] = "Ridder"


class Secant(BaseModel):
    resource_name: Optional[Literal["Secant"]] = "Secant"


class Newton(BaseModel):
    resource_name: Optional[Literal["Newton"]] = "Newton"


class NewtonSafe(BaseModel):
    resource_name: Optional[Literal["NewtonSafe"]] = "NewtonSafe"


class BoundaryConstraint(BaseModel):
    resource_name: Optional[Literal["BoundaryConstraint"]] = "BoundaryConstraint"
    lower: float
    upper: float


class NoConstraint(BaseModel):
    resource_name: Optional[Literal["NoConstraint"]] = "NoConstraint"


class PositiveConstraint(BaseModel):
    resource_name: Optional[Literal["PositiveConstraint"]] = "PositiveConstraint"


class CompositeConstraint(BaseModel):
    resource_name: Optional[Literal["CompositeConstraint"]] = "CompositeConstraint"
    c1: Constraint
    c2: Constraint


class NonhomogeneousBoundaryConstraint(BaseModel):
    resource_name: Optional[
        Literal["NonhomogeneousBoundaryConstraint"]
    ] = "NonhomogeneousBoundaryConstraint"
    l: Array
    u: Array


class EndCriteria(BaseModel):
    resource_name: Optional[Literal["EndCriteria"]] = "EndCriteria"
    maxIteration: int
    maxStationaryStateIterations: int
    rootEpsilon: float
    functionEpsilon: float
    gradientNormEpsilon: float


class ConjugateGradient(BaseModel):
    resource_name: Optional[Literal["ConjugateGradient"]] = "ConjugateGradient"


class Simplex(BaseModel):
    resource_name: Optional[Literal["Simplex"]] = "Simplex"
    lambda_: float = Field(..., alias="lambda")


class SteepestDescent(BaseModel):
    resource_name: Optional[Literal["SteepestDescent"]] = "SteepestDescent"


class BFGS(BaseModel):
    resource_name: Optional[Literal["BFGS"]] = "BFGS"


class LevenbergMarquardt(BaseModel):
    resource_name: Optional[Literal["LevenbergMarquardt"]] = "LevenbergMarquardt"
    epsfcn: Optional[float] = None
    xtol: Optional[float] = None
    gtol: Optional[float] = None
    useCostFunctionsJacobian: Optional[bool] = None


class DifferentialEvolution(BaseModel):
    resource_name: Optional[Literal["DifferentialEvolution"]] = "DifferentialEvolution"


class SamplerGaussian(BaseModel):
    resource_name: Optional[Literal["SamplerGaussian"]] = "SamplerGaussian"
    seed: Optional[int] = None


class SamplerLogNormal(BaseModel):
    resource_name: Optional[Literal["SamplerLogNormal"]] = "SamplerLogNormal"
    seed: Optional[int] = None


class SamplerMirrorGaussian(BaseModel):
    resource_name: Optional[Literal["SamplerMirrorGaussian"]] = "SamplerMirrorGaussian"
    lower: Array
    upper: Array
    seed: Optional[int] = None


class ProbabilityBoltzmannDownhill(BaseModel):
    resource_name: Optional[
        Literal["ProbabilityBoltzmannDownhill"]
    ] = "ProbabilityBoltzmannDownhill"
    seed: Optional[int] = None


class TemperatureExponential(BaseModel):
    resource_name: Optional[
        Literal["TemperatureExponential"]
    ] = "TemperatureExponential"
    initialTemp: float
    dimension: int
    power: Optional[float] = None


class ReannealingTrivial(BaseModel):
    resource_name: Optional[Literal["ReannealingTrivial"]] = "ReannealingTrivial"


class Optimizer(BaseModel):
    resource_name: Optional[Literal["Optimizer"]] = "Optimizer"


class BlackVolTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["BlackVolTermStructureHandle"]
    ] = "BlackVolTermStructureHandle"
    value: Optional[BlackVolTermStructure] = None


class RelinkableBlackVolTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableBlackVolTermStructureHandle"]
    ] = "RelinkableBlackVolTermStructureHandle"
    value: Optional[BlackVolTermStructure] = None


class LocalVolTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["LocalVolTermStructureHandle"]
    ] = "LocalVolTermStructureHandle"
    value: Optional[LocalVolTermStructure] = None


class RelinkableLocalVolTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableLocalVolTermStructureHandle"]
    ] = "RelinkableLocalVolTermStructureHandle"
    value: Optional[LocalVolTermStructure] = None


class OptionletVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["OptionletVolatilityStructureHandle"]
    ] = "OptionletVolatilityStructureHandle"
    value: Optional[OptionletVolatilityStructure] = None


class RelinkableOptionletVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableOptionletVolatilityStructureHandle"]
    ] = "RelinkableOptionletVolatilityStructureHandle"
    value: Optional[OptionletVolatilityStructure] = None


class SwaptionVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["SwaptionVolatilityStructureHandle"]
    ] = "SwaptionVolatilityStructureHandle"
    value: Optional[SwaptionVolatilityStructure] = None


class RelinkableSwaptionVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableSwaptionVolatilityStructureHandle"]
    ] = "RelinkableSwaptionVolatilityStructureHandle"
    value: Optional[SwaptionVolatilityStructure] = None


class BlackConstantVol0(BaseModel):
    resource_name: Optional[Literal["BlackConstantVol"]] = "BlackConstantVol"
    settlementDays: float
    calendar: Calendar
    volatility: Union[float, QuoteHandle]
    dayCounter: DayCounter


class BlackConstantVol1(BaseModel):
    resource_name: Optional[Literal["BlackConstantVol"]] = "BlackConstantVol"
    referenceDate: Date
    c: Calendar
    volatility: Union[float, QuoteHandle]
    dayCounter: DayCounter


class BlackVarianceCurve(BaseModel):
    resource_name: Optional[Literal["BlackVarianceCurve"]] = "BlackVarianceCurve"
    referenceDate: Date
    dates: List[Date]
    volatilities: List[float]
    dayCounter: DayCounter
    forceMonotoneVariance: Optional[bool] = None


class LocalConstantVol0(BaseModel):
    resource_name: Optional[Literal["LocalConstantVol"]] = "LocalConstantVol"
    settlementDays: int
    calendar: Calendar
    volatility: Union[float, QuoteHandle]
    dayCounter: DayCounter


class LocalConstantVol1(BaseModel):
    resource_name: Optional[Literal["LocalConstantVol"]] = "LocalConstantVol"
    referenceDate: Date
    volatility: Union[float, QuoteHandle]
    dayCounter: DayCounter


class LocalVolSurface(BaseModel):
    resource_name: Optional[Literal["LocalVolSurface"]] = "LocalVolSurface"
    blackTS: BlackVolTermStructureHandle
    riskFreeTS: YieldTermStructureHandle
    dividendTS: YieldTermStructureHandle
    underlying: Union[QuoteHandle, float]


class SabrSmileSection0(BaseModel):
    resource_name: Optional[Literal["SabrSmileSection"]] = "SabrSmileSection"
    timeToExpiry: float
    forward: float
    sabrParameters: List[float]
    shift: Optional[float] = None


class SabrSmileSection1(BaseModel):
    resource_name: Optional[Literal["SabrSmileSection"]] = "SabrSmileSection"
    d: Date
    forward: float
    sabrParameters: List[float]
    dc: Optional[DayCounter] = None
    shift: Optional[float] = None


class KahaleSmileSection(BaseModel):
    resource_name: Optional[Literal["KahaleSmileSection"]] = "KahaleSmileSection"
    source: SmileSection
    atm: Optional[float] = None
    interpolate: Optional[bool] = None
    exponentialExtrapolation: Optional[bool] = None
    deleteArbitragePoints: Optional[bool] = None
    moneynessGrid: Optional[List[float]] = None
    gap: Optional[float] = None
    forcedLeftIndex: Optional[int] = None
    forcedRightIndex: Optional[int] = None


class ZabrShortMaturityLognormal(BaseModel):
    resource_name: Optional[
        Literal["ZabrShortMaturityLognormal"]
    ] = "ZabrShortMaturityLognormal"


class ZabrShortMaturityNormal(BaseModel):
    resource_name: Optional[
        Literal["ZabrShortMaturityNormal"]
    ] = "ZabrShortMaturityNormal"


class ZabrLocalVolatility(BaseModel):
    resource_name: Optional[Literal["ZabrLocalVolatility"]] = "ZabrLocalVolatility"


class ZabrFullFd(BaseModel):
    resource_name: Optional[Literal["ZabrFullFd"]] = "ZabrFullFd"


class NoArbSabrSmileSection0(BaseModel):
    resource_name: Optional[Literal["NoArbSabrSmileSection"]] = "NoArbSabrSmileSection"
    d: Date
    forward: float
    sabrParameters: List[float]
    dc: Optional[DayCounter] = None
    shift: Optional[float] = None


class NoArbSabrSmileSection1(BaseModel):
    resource_name: Optional[Literal["NoArbSabrSmileSection"]] = "NoArbSabrSmileSection"
    timeToExpiry: float
    forward: float
    sabrParameters: List[float]
    shift: Optional[float] = None


class NoArbSabrInterpolatedSmileSection0(BaseModel):
    resource_name: Optional[
        Literal["NoArbSabrInterpolatedSmileSection"]
    ] = "NoArbSabrInterpolatedSmileSection"
    optionDate: Date
    forward: float
    strikes: List[float]
    hasFloatingStrikes: bool
    atmVolatility: float
    vols: List[float]
    alpha: float
    beta: float
    nu: float
    rho: float
    isAlphaFixed: Optional[bool] = None
    isBetaFixed: Optional[bool] = None
    isNuFixed: Optional[bool] = None
    isRhoFixed: Optional[bool] = None
    vegaWeighted: Optional[bool] = None
    endCriteria: Optional[EndCriteria] = None
    method: Optional[OptimizationMethod] = None
    dc: Optional[DayCounter] = None


class NoArbSabrInterpolatedSmileSection1(BaseModel):
    resource_name: Optional[
        Literal["NoArbSabrInterpolatedSmileSection"]
    ] = "NoArbSabrInterpolatedSmileSection"
    optionDate: Date
    forward: QuoteHandle
    strikes: List[float]
    hasFloatingStrikes: bool
    atmVolatility: QuoteHandle
    volHandles: List[QuoteHandle]
    alpha: float
    beta: float
    nu: float
    rho: float
    isAlphaFixed: Optional[bool] = None
    isBetaFixed: Optional[bool] = None
    isNuFixed: Optional[bool] = None
    isRhoFixed: Optional[bool] = None
    vegaWeighted: Optional[bool] = None
    endCriteria: Optional[EndCriteria] = None
    method: Optional[OptimizationMethod] = None
    dc: Optional[DayCounter] = None


class GeneralizedBlackScholesProcess0(BaseModel):
    resource_name: Optional[
        Literal["GeneralizedBlackScholesProcess"]
    ] = "GeneralizedBlackScholesProcess"
    s0: QuoteHandle
    dividendTS: YieldTermStructureHandle
    riskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle


class GeneralizedBlackScholesProcess1(BaseModel):
    resource_name: Optional[
        Literal["GeneralizedBlackScholesProcess"]
    ] = "GeneralizedBlackScholesProcess"
    x0: QuoteHandle
    dividendTS: YieldTermStructureHandle
    riskFreeTS: YieldTermStructureHandle
    blackVolTS: BlackVolTermStructureHandle
    localVolTS: LocalVolTermStructureHandle


class BlackScholesProcess(BaseModel):
    resource_name: Optional[Literal["BlackScholesProcess"]] = "BlackScholesProcess"
    s0: QuoteHandle
    riskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle


class BlackScholesMertonProcess(BaseModel):
    resource_name: Optional[
        Literal["BlackScholesMertonProcess"]
    ] = "BlackScholesMertonProcess"
    s0: QuoteHandle
    dividendTS: YieldTermStructureHandle
    riskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle


class BlackProcess(BaseModel):
    resource_name: Optional[Literal["BlackProcess"]] = "BlackProcess"
    s0: QuoteHandle
    riskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle


class GarmanKohlagenProcess(BaseModel):
    resource_name: Optional[Literal["GarmanKohlagenProcess"]] = "GarmanKohlagenProcess"
    s0: QuoteHandle
    foreignRiskFreeTS: YieldTermStructureHandle
    domesticRiskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle


class Merton76Process(BaseModel):
    resource_name: Optional[Literal["Merton76Process"]] = "Merton76Process"
    stateVariable: QuoteHandle
    dividendTS: YieldTermStructureHandle
    riskFreeTS: YieldTermStructureHandle
    volTS: BlackVolTermStructureHandle
    jumpIntensity: QuoteHandle
    meanLogJump: QuoteHandle
    jumpVolatility: QuoteHandle


class GeometricBrownianMotionProcess(BaseModel):
    resource_name: Optional[
        Literal["GeometricBrownianMotionProcess"]
    ] = "GeometricBrownianMotionProcess"
    initialValue: float
    mu: float
    sigma: float


class VarianceGammaProcess(BaseModel):
    resource_name: Optional[Literal["VarianceGammaProcess"]] = "VarianceGammaProcess"
    s0: QuoteHandle
    dividendYield: YieldTermStructureHandle
    riskFreeRate: YieldTermStructureHandle
    sigma: float
    nu: float
    theta: float


class HestonProcessBase(BaseModel):
    resource_name: Optional[Literal["HestonProcess"]] = "HestonProcess"
    riskFreeTS: YieldTermStructureHandle
    dividendTS: YieldTermStructureHandle
    s0: QuoteHandle
    v0: float
    kappa: float
    theta: float
    sigma: float
    rho: float


class BatesProcess(BaseModel):
    resource_name: Optional[Literal["BatesProcess"]] = "BatesProcess"
    riskFreeRate: YieldTermStructureHandle
    dividendYield: YieldTermStructureHandle
    s0: QuoteHandle
    v0: float
    kappa: float
    theta: float
    sigma: float
    rho: float
    lambda_: float = Field(..., alias="lambda")
    nu: float
    delta: float


class HullWhiteProcess(BaseModel):
    resource_name: Optional[Literal["HullWhiteProcess"]] = "HullWhiteProcess"
    riskFreeTS: YieldTermStructureHandle
    a: float
    sigma: float


class HullWhiteForwardProcess(BaseModel):
    resource_name: Optional[
        Literal["HullWhiteForwardProcess"]
    ] = "HullWhiteForwardProcess"
    riskFreeTS: YieldTermStructureHandle
    a: float
    sigma: float


class G2Process(BaseModel):
    resource_name: Optional[Literal["G2Process"]] = "G2Process"
    a: float
    sigma: float
    b: float
    eta: float
    rho: float


class G2ForwardProcess(BaseModel):
    resource_name: Optional[Literal["G2ForwardProcess"]] = "G2ForwardProcess"
    a: float
    sigma: float
    b: float
    eta: float
    rho: float


class GsrProcess(BaseModel):
    resource_name: Optional[Literal["GsrProcess"]] = "GsrProcess"
    times: Array
    vols: Array
    reversions: Array
    T: Optional[float] = None


class OrnsteinUhlenbeckProcess(BaseModel):
    resource_name: Optional[
        Literal["OrnsteinUhlenbeckProcess"]
    ] = "OrnsteinUhlenbeckProcess"
    speed: float
    vol: float
    x0: Optional[float] = None
    level: Optional[float] = None


class Stock(BaseModel):
    resource_name: Optional[Literal["Stock"]] = "Stock"
    quote: QuoteHandle


class CompositeInstrument(BaseModel):
    resource_name: Optional[Literal["CompositeInstrument"]] = "CompositeInstrument"


class MakeSchedule(BaseModel):
    resource_name: Optional[Literal["MakeSchedule"]] = "MakeSchedule"


class SimpleCashFlow(BaseModel):
    resource_name: Optional[Literal["SimpleCashFlow"]] = "SimpleCashFlow"
    amount: float
    date: Date


class Redemption(BaseModel):
    resource_name: Optional[Literal["Redemption"]] = "Redemption"
    amount: float
    date: Date


class AmortizingPayment(BaseModel):
    resource_name: Optional[Literal["AmortizingPayment"]] = "AmortizingPayment"
    amount: float
    date: Date


class FixedRateCoupon(BaseModel):
    resource_name: Optional[Literal["FixedRateCoupon"]] = "FixedRateCoupon"
    paymentDate: Date
    nominal: float
    rate: float
    dayCounter: DayCounter
    startDate: Date
    endDate: Date
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    exCouponDate: Optional[Date] = None


class OvernightIndexedCoupon(BaseModel):
    resource_name: Optional[
        Literal["OvernightIndexedCoupon"]
    ] = "OvernightIndexedCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    overnightIndex: OvernightIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    telescopicValueDates: Optional[bool] = None


class CappedFlooredCouponBase(BaseModel):
    resource_name: Optional[Literal["CappedFlooredCoupon"]] = "CappedFlooredCoupon"
    underlying: FloatingRateCoupon
    cap: Optional[float] = None
    floor: Optional[float] = None


class BlackIborCouponPricer(BaseModel):
    resource_name: Optional[Literal["BlackIborCouponPricer"]] = "BlackIborCouponPricer"
    v: Optional[OptionletVolatilityStructureHandle] = None


class GFunctionFactory(BaseModel):
    resource_name: Optional[Literal["GFunctionFactory"]] = "GFunctionFactory"


class LinearTsrPricerSettings(BaseModel):
    resource_name: Optional[
        Literal["LinearTsrPricerSettings"]
    ] = "LinearTsrPricerSettings"


class Duration(BaseModel):
    resource_name: Optional[Literal["Duration"]] = "Duration"


class CashFlows(BaseModel):
    resource_name: Optional[Literal["CashFlows"]] = "CashFlows"
    value: Optional[CashFlows] = None


class TermStructureConsistentModel(BaseModel):
    resource_name: Optional[
        Literal["TermStructureConsistentModel"]
    ] = "TermStructureConsistentModel"


class CalibratedModelHandle(BaseModel):
    resource_name: Optional[Literal["CalibratedModelHandle"]] = "CalibratedModelHandle"
    value: Optional[CalibratedModel] = None


class RelinkableCalibratedModelHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableCalibratedModelHandle"]
    ] = "RelinkableCalibratedModelHandle"
    value: Optional[CalibratedModel] = None


class TimeGrid(BaseModel):
    resource_name: Optional[Literal["TimeGrid"]] = "TimeGrid"
    end: Optional[float] = None
    steps: Optional[int] = None


class ConstantParameter0(BaseModel):
    resource_name: Optional[Literal["ConstantParameter"]] = "ConstantParameter"
    constraint: Constraint


class ConstantParameter1(BaseModel):
    resource_name: Optional[Literal["ConstantParameter"]] = "ConstantParameter"
    value: float
    constraint: Constraint


class NullParameter(BaseModel):
    resource_name: Optional[Literal["NullParameter"]] = "NullParameter"


class PiecewiseConstantParameter(BaseModel):
    resource_name: Optional[
        Literal["PiecewiseConstantParameter"]
    ] = "PiecewiseConstantParameter"
    times: List[float]
    constraint: Optional[Constraint] = None


class Barrier(BaseModel):
    resource_name: Optional[Literal["Barrier"]] = "Barrier"


class DoubleBarrier(BaseModel):
    resource_name: Optional[Literal["DoubleBarrier"]] = "DoubleBarrier"


class AnalyticEuropeanEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticEuropeanEngine"]
    ] = "AnalyticEuropeanEngine"
    value: GeneralizedBlackScholesProcess


class HestonModelBase(BaseModel):
    resource_name: Optional[Literal["HestonModel"]] = "HestonModel"
    process: HestonProcess


class HestonModelHandle(BaseModel):
    resource_name: Optional[Literal["HestonModelHandle"]] = "HestonModelHandle"
    value: Optional[HestonModel] = None


class PiecewiseTimeDependentHestonModel(BaseModel):
    resource_name: Optional[
        Literal["PiecewiseTimeDependentHestonModel"]
    ] = "PiecewiseTimeDependentHestonModel"
    riskFreeRate: YieldTermStructureHandle
    dividendYield: YieldTermStructureHandle
    s0: QuoteHandle
    v0: float
    theta: Parameter
    kappa: Parameter
    sigma: Parameter
    rho: Parameter
    timeGrid: TimeGrid


class AnalyticHestonEngine1(BaseModel):
    resource_name: Optional[Literal["AnalyticHestonEngine"]] = "AnalyticHestonEngine"
    model: HestonModel
    integrationOrder: Optional[int] = None


class AnalyticHestonEngine2(BaseModel):
    resource_name: Optional[Literal["AnalyticHestonEngine"]] = "AnalyticHestonEngine"
    model: HestonModel
    relTolerance: float
    maxEvaluations: int


class COSHestonEngine(BaseModel):
    resource_name: Optional[Literal["COSHestonEngine"]] = "COSHestonEngine"
    model: HestonModel
    L: Optional[float] = None
    N: Optional[int] = None


class AnalyticPTDHestonEngine1(BaseModel):
    resource_name: Optional[
        Literal["AnalyticPTDHestonEngine"]
    ] = "AnalyticPTDHestonEngine"
    model: PiecewiseTimeDependentHestonModel
    relTolerance: Optional[float] = None
    maxEvaluations: Optional[int] = None


class AnalyticPTDHestonEngine2(BaseModel):
    resource_name: Optional[
        Literal["AnalyticPTDHestonEngine"]
    ] = "AnalyticPTDHestonEngine"
    model: PiecewiseTimeDependentHestonModel
    integrationOrder: Optional[int] = None


class BatesModel(BaseModel):
    resource_name: Optional[Literal["BatesModel"]] = "BatesModel"
    process: BatesProcess


class BatesEngine0(BaseModel):
    resource_name: Optional[Literal["BatesEngine"]] = "BatesEngine"
    model: BatesModel
    integrationOrder: Optional[int] = None


class BatesEngine1(BaseModel):
    resource_name: Optional[Literal["BatesEngine"]] = "BatesEngine"
    model: BatesModel
    relTolerance: float
    maxEvaluations: int


class IntegralEngine(BaseModel):
    resource_name: Optional[Literal["IntegralEngine"]] = "IntegralEngine"
    value: GeneralizedBlackScholesProcess


class FDBermudanEngine(BaseModel):
    resource_name: Optional[Literal["FDBermudanEngine"]] = "FDBermudanEngine"
    process: GeneralizedBlackScholesProcess
    timeSteps: Optional[int] = None
    gridPoints: Optional[int] = None
    timeDependent: Optional[bool] = None


class FDEuropeanEngine(BaseModel):
    resource_name: Optional[Literal["FDEuropeanEngine"]] = "FDEuropeanEngine"
    process: GeneralizedBlackScholesProcess
    timeSteps: Optional[int] = None
    gridPoints: Optional[int] = None
    timeDependent: Optional[bool] = None


class BinomialCRRVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialCRRVanillaEngine"]
    ] = "BinomialCRRVanillaEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialJRVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialJRVanillaEngine"]
    ] = "BinomialJRVanillaEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialTrigeorgisVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialTrigeorgisVanillaEngine"]
    ] = "BinomialTrigeorgisVanillaEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialTianVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialTianVanillaEngine"]
    ] = "BinomialTianVanillaEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialJoshi4VanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialJoshi4VanillaEngine"]
    ] = "BinomialJoshi4VanillaEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class FDAmericanEngine(BaseModel):
    resource_name: Optional[Literal["FDAmericanEngine"]] = "FDAmericanEngine"
    process: GeneralizedBlackScholesProcess
    timeSteps: Optional[int] = None
    gridPoints: Optional[int] = None
    timeDependent: Optional[bool] = None


class FDShoutEngine(BaseModel):
    resource_name: Optional[Literal["FDShoutEngine"]] = "FDShoutEngine"
    process: GeneralizedBlackScholesProcess
    timeSteps: Optional[int] = None
    gridPoints: Optional[int] = None
    timeDependent: Optional[bool] = None


class ContinuousArithmeticAsianLevyEngine(BaseModel):
    resource_name: Optional[
        Literal["ContinuousArithmeticAsianLevyEngine"]
    ] = "ContinuousArithmeticAsianLevyEngine"
    process: GeneralizedBlackScholesProcess
    runningAverage: QuoteHandle
    startDate: Date


class FdBlackScholesAsianEngine(BaseModel):
    resource_name: Optional[
        Literal["FdBlackScholesAsianEngine"]
    ] = "FdBlackScholesAsianEngine"
    process: GeneralizedBlackScholesProcess
    tGrid: int
    xGrid: int
    aGrid: int


class BaroneAdesiWhaleyApproximationEngine(BaseModel):
    resource_name: Optional[
        Literal["BaroneAdesiWhaleyApproximationEngine"]
    ] = "BaroneAdesiWhaleyApproximationEngine"
    process: GeneralizedBlackScholesProcess


class BjerksundStenslandApproximationEngine(BaseModel):
    resource_name: Optional[
        Literal["BjerksundStenslandApproximationEngine"]
    ] = "BjerksundStenslandApproximationEngine"
    process: GeneralizedBlackScholesProcess


class JuQuadraticApproximationEngine(BaseModel):
    resource_name: Optional[
        Literal["JuQuadraticApproximationEngine"]
    ] = "JuQuadraticApproximationEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticDigitalAmericanEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDigitalAmericanEngine"]
    ] = "AnalyticDigitalAmericanEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticDigitalAmericanKOEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDigitalAmericanKOEngine"]
    ] = "AnalyticDigitalAmericanKOEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticDividendEuropeanEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDividendEuropeanEngine"]
    ] = "AnalyticDividendEuropeanEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticBarrierEngine(BaseModel):
    resource_name: Optional[Literal["AnalyticBarrierEngine"]] = "AnalyticBarrierEngine"
    value: GeneralizedBlackScholesProcess


class FdmQuantoHelper(BaseModel):
    resource_name: Optional[Literal["FdmQuantoHelper"]] = "FdmQuantoHelper"
    rTS: YieldTermStructure
    fTS: YieldTermStructure
    fxVolTS: BlackVolTermStructure
    equityFxCorrelation: float
    exchRateATMlevel: float


class AnalyticCEVEngine(BaseModel):
    resource_name: Optional[Literal["AnalyticCEVEngine"]] = "AnalyticCEVEngine"
    f0: float
    alpha: float
    beta: float
    rTS: YieldTermStructureHandle


class AnalyticBinaryBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticBinaryBarrierEngine"]
    ] = "AnalyticBinaryBarrierEngine"
    process: GeneralizedBlackScholesProcess


class ForwardEuropeanEngine(BaseModel):
    resource_name: Optional[Literal["ForwardEuropeanEngine"]] = "ForwardEuropeanEngine"
    value: GeneralizedBlackScholesProcess


class QuantoEuropeanEngine(BaseModel):
    resource_name: Optional[Literal["QuantoEuropeanEngine"]] = "QuantoEuropeanEngine"
    process: GeneralizedBlackScholesProcess
    foreignRiskFreeRate: YieldTermStructureHandle
    exchangeRateVolatility: BlackVolTermStructureHandle
    correlation: QuoteHandle


class QuantoForwardEuropeanEngine(BaseModel):
    resource_name: Optional[
        Literal["QuantoForwardEuropeanEngine"]
    ] = "QuantoForwardEuropeanEngine"
    process: GeneralizedBlackScholesProcess
    foreignRiskFreeRate: YieldTermStructureHandle
    exchangeRateVolatility: BlackVolTermStructureHandle
    correlation: QuoteHandle


class BlackCalculator(BaseModel):
    resource_name: Optional[Literal["BlackCalculator"]] = "BlackCalculator"
    payoff: StrikedTypePayoff
    forward: float
    stdDev: float
    discount: Optional[float] = None


class AnalyticContinuousGeometricAveragePriceAsianEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticContinuousGeometricAveragePriceAsianEngine"]
    ] = "AnalyticContinuousGeometricAveragePriceAsianEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticDiscreteGeometricAveragePriceAsianEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDiscreteGeometricAveragePriceAsianEngine"]
    ] = "AnalyticDiscreteGeometricAveragePriceAsianEngine"
    process: GeneralizedBlackScholesProcess


class AnalyticDiscreteGeometricAverageStrikeAsianEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDiscreteGeometricAverageStrikeAsianEngine"]
    ] = "AnalyticDiscreteGeometricAverageStrikeAsianEngine"
    process: GeneralizedBlackScholesProcess


class VarianceGammaEngine(BaseModel):
    resource_name: Optional[Literal["VarianceGammaEngine"]] = "VarianceGammaEngine"
    process: VarianceGammaProcess


class FFTVarianceGammaEngine(BaseModel):
    resource_name: Optional[
        Literal["FFTVarianceGammaEngine"]
    ] = "FFTVarianceGammaEngine"
    process: VarianceGammaProcess
    logStrikeSpacing: Optional[float] = None


class AnalyticDoubleBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDoubleBarrierEngine"]
    ] = "AnalyticDoubleBarrierEngine"
    process: GeneralizedBlackScholesProcess
    series: Optional[int] = None


class WulinYongDoubleBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["WulinYongDoubleBarrierEngine"]
    ] = "WulinYongDoubleBarrierEngine"
    process: GeneralizedBlackScholesProcess
    series: Optional[int] = None


class AnalyticDoubleBarrierBinaryEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticDoubleBarrierBinaryEngine"]
    ] = "AnalyticDoubleBarrierBinaryEngine"
    process: GeneralizedBlackScholesProcess


class VanillaSwingOption(BaseModel):
    resource_name: Optional[Literal["VanillaSwingOption"]] = "VanillaSwingOption"
    payoff: Payoff
    ex: SwingExercise
    minExerciseRights: int
    maxExerciseRights: int


class MinBasketPayoff(BaseModel):
    resource_name: Optional[Literal["MinBasketPayoff"]] = "MinBasketPayoff"
    p: Payoff


class MaxBasketPayoff(BaseModel):
    resource_name: Optional[Literal["MaxBasketPayoff"]] = "MaxBasketPayoff"
    p: Payoff


class AverageBasketPayoff0(BaseModel):
    resource_name: Optional[Literal["AverageBasketPayoff"]] = "AverageBasketPayoff"
    p: Payoff
    a: Array


class AverageBasketPayoff1(BaseModel):
    resource_name: Optional[Literal["AverageBasketPayoff"]] = "AverageBasketPayoff"
    p: Payoff
    n: int


class SpreadBasketPayoff(BaseModel):
    resource_name: Optional[Literal["SpreadBasketPayoff"]] = "SpreadBasketPayoff"
    p: Payoff


class StulzEngine(BaseModel):
    resource_name: Optional[Literal["StulzEngine"]] = "StulzEngine"
    process1: GeneralizedBlackScholesProcess
    process2: GeneralizedBlackScholesProcess
    correlation: float


class KirkEngine(BaseModel):
    resource_name: Optional[Literal["KirkEngine"]] = "KirkEngine"
    process1: BlackProcess
    process2: BlackProcess
    correlation: float


class HimalayaOption(BaseModel):
    resource_name: Optional[Literal["HimalayaOption"]] = "HimalayaOption"
    fixingDates: List[Date]
    strike: float


class TimeBasket(BaseModel):
    resource_name: Optional[Literal["TimeBasket"]] = "TimeBasket"
    arg_0: Optional[List[Date]] = None
    arg_1: Optional[List[float]] = None


class SwapBase(BaseModel):
    resource_name: Optional[Literal["Swap"]] = "Swap"
    firstLeg: List[CashFlow]
    secondLeg: List[CashFlow]


class DiscountingSwapEngine(BaseModel):
    resource_name: Optional[Literal["DiscountingSwapEngine"]] = "DiscountingSwapEngine"
    discountCurve: YieldTermStructureHandle
    includeSettlementDateFlows: bool
    settlementDate: Optional[Date] = None
    npvDate: Optional[Date] = None


class MultiplicativePriceSeasonality(BaseModel):
    resource_name: Optional[
        Literal["MultiplicativePriceSeasonality"]
    ] = "MultiplicativePriceSeasonality"
    seasonalityBaseDate: Date
    frequency: float
    seasonalityFactors: List[float]


class YoYInflationTermStructure(BaseModel):
    resource_name: Optional[
        Literal["YoYInflationTermStructure"]
    ] = "YoYInflationTermStructure"


class YoYInflationTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["YoYInflationTermStructureHandle"]
    ] = "YoYInflationTermStructureHandle"
    value: Optional[YoYInflationTermStructure] = None


class RelinkableYoYInflationTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableYoYInflationTermStructureHandle"]
    ] = "RelinkableYoYInflationTermStructureHandle"
    value: Optional[YoYInflationTermStructure] = None


class ZeroInflationTermStructure(BaseModel):
    resource_name: Optional[
        Literal["ZeroInflationTermStructure"]
    ] = "ZeroInflationTermStructure"


class ZeroInflationTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["ZeroInflationTermStructureHandle"]
    ] = "ZeroInflationTermStructureHandle"
    value: Optional[ZeroInflationTermStructure] = None


class RelinkableZeroInflationTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableZeroInflationTermStructureHandle"]
    ] = "RelinkableZeroInflationTermStructureHandle"
    value: Optional[ZeroInflationTermStructure] = None


class CustomRegion(BaseModel):
    resource_name: Optional[Literal["CustomRegion"]] = "CustomRegion"
    name: str
    code: str


class EUHICP(BaseModel):
    resource_name: Optional[Literal["EUHICP"]] = "EUHICP"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class EUHICPXT(BaseModel):
    resource_name: Optional[Literal["EUHICPXT"]] = "EUHICPXT"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class FRHICP(BaseModel):
    resource_name: Optional[Literal["FRHICP"]] = "FRHICP"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class UKRPI(BaseModel):
    resource_name: Optional[Literal["UKRPI"]] = "UKRPI"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class USCPI(BaseModel):
    resource_name: Optional[Literal["USCPI"]] = "USCPI"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class ZACPI(BaseModel):
    resource_name: Optional[Literal["ZACPI"]] = "ZACPI"
    interpolated: bool
    h: Optional[ZeroInflationTermStructureHandle] = None


class YYEUHICP(BaseModel):
    resource_name: Optional[Literal["YYEUHICP"]] = "YYEUHICP"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class YYEUHICPXT(BaseModel):
    resource_name: Optional[Literal["YYEUHICPXT"]] = "YYEUHICPXT"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class YYFRHICP(BaseModel):
    resource_name: Optional[Literal["YYFRHICP"]] = "YYFRHICP"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class YYUKRPI(BaseModel):
    resource_name: Optional[Literal["YYUKRPI"]] = "YYUKRPI"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class YYUSCPI(BaseModel):
    resource_name: Optional[Literal["YYUSCPI"]] = "YYUSCPI"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class YYZACPI(BaseModel):
    resource_name: Optional[Literal["YYZACPI"]] = "YYZACPI"
    interpolated: bool
    h: Optional[YoYInflationTermStructureHandle] = None


class CPI(BaseModel):
    resource_name: Optional[Literal["CPI"]] = "CPI"


class CPICoupon(BaseModel):
    resource_name: Optional[Literal["CPICoupon"]] = "CPICoupon"


class YoYInflationCap(BaseModel):
    resource_name: Optional[Literal["YoYInflationCap"]] = "YoYInflationCap"
    leg: List[CashFlow]
    capRates: List[float]


class YoYInflationFloor(BaseModel):
    resource_name: Optional[Literal["YoYInflationFloor"]] = "YoYInflationFloor"
    leg: List[CashFlow]
    floorRates: List[float]


class YoYInflationCollar(BaseModel):
    resource_name: Optional[Literal["YoYInflationCollar"]] = "YoYInflationCollar"
    leg: List[CashFlow]
    capRates: List[float]
    floorRates: List[float]


class ShortRateModelHandle(BaseModel):
    resource_name: Optional[Literal["ShortRateModelHandle"]] = "ShortRateModelHandle"
    value: Optional[ShortRateModel] = None


class RelinkableShortRateModelHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableShortRateModelHandle"]
    ] = "RelinkableShortRateModelHandle"
    value: Optional[ShortRateModel] = None


class VasicekBase(BaseModel):
    resource_name: Optional[Literal["Vasicek"]] = "Vasicek"
    r0: Optional[float] = None
    a: Optional[float] = None
    b: Optional[float] = None
    sigma: Optional[float] = None
    lambda_: Optional[float] = Field(None, alias="lambda")


class HullWhite(BaseModel):
    resource_name: Optional[Literal["HullWhite"]] = "HullWhite"
    termStructure: YieldTermStructureHandle
    a: Optional[float] = None
    sigma: Optional[float] = None


class BlackKarasinski(BaseModel):
    resource_name: Optional[Literal["BlackKarasinski"]] = "BlackKarasinski"
    termStructure: YieldTermStructureHandle
    a: Optional[float] = None
    sigma: Optional[float] = None


class G2(BaseModel):
    resource_name: Optional[Literal["G"]] = "G"
    termStructure: YieldTermStructureHandle
    a: Optional[float] = None
    sigma: Optional[float] = None
    b: Optional[float] = None
    eta: Optional[float] = None
    rho: Optional[float] = None


class JamshidianSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["JamshidianSwaptionEngine"]
    ] = "JamshidianSwaptionEngine"
    model: OneFactorAffineModel
    termStructure: Optional[YieldTermStructureHandle] = None


class TreeSwaptionEngine0(BaseModel):
    resource_name: Optional[Literal["TreeSwaptionEngine"]] = "TreeSwaptionEngine"
    model: Union[ShortRateModelHandle, ShortRateModel]
    timeSteps: int
    termStructure: Optional[YieldTermStructureHandle] = None


class TreeSwaptionEngine1(BaseModel):
    resource_name: Optional[Literal["TreeSwaptionEngine"]] = "TreeSwaptionEngine"
    model: ShortRateModel
    grid: TimeGrid
    termStructure: Optional[YieldTermStructureHandle] = None


class AnalyticCapFloorEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticCapFloorEngine"]
    ] = "AnalyticCapFloorEngine"
    model: OneFactorAffineModel
    termStructure: Optional[YieldTermStructureHandle] = None


class TreeCapFloorEngine0(BaseModel):
    resource_name: Optional[Literal["TreeCapFloorEngine"]] = "TreeCapFloorEngine"
    model: ShortRateModel
    grid: TimeGrid
    termStructure: Optional[YieldTermStructureHandle] = None


class TreeCapFloorEngine1(BaseModel):
    resource_name: Optional[Literal["TreeCapFloorEngine"]] = "TreeCapFloorEngine"
    model: ShortRateModel
    timeSteps: int
    termStructure: Optional[YieldTermStructureHandle] = None


class G2SwaptionEngine(BaseModel):
    resource_name: Optional[Literal["G2SwaptionEngine"]] = "G2SwaptionEngine"
    model: G2
    range: float
    intervals: int


class DiscountingBondEngine(BaseModel):
    resource_name: Optional[Literal["DiscountingBondEngine"]] = "DiscountingBondEngine"
    discountCurve: YieldTermStructureHandle


class TreeCallableFixedRateBondEngine0(BaseModel):
    resource_name: Optional[
        Literal["TreeCallableFixedRateBondEngine"]
    ] = "TreeCallableFixedRateBondEngine"
    model: ShortRateModel
    grid: TimeGrid
    termStructure: Optional[YieldTermStructureHandle] = None


class TreeCallableFixedRateBondEngine1(BaseModel):
    resource_name: Optional[
        Literal["TreeCallableFixedRateBondEngine"]
    ] = "TreeCallableFixedRateBondEngine"
    model: ShortRateModel
    timeSteps: int
    termStructure: Optional[YieldTermStructureHandle] = None


class BlackCallableFixedRateBondEngine(BaseModel):
    resource_name: Optional[
        Literal["BlackCallableFixedRateBondEngine"]
    ] = "BlackCallableFixedRateBondEngine"
    fwdYieldVol: QuoteHandle
    discountCurve: YieldTermStructureHandle


class BondFunctions(BaseModel):
    resource_name: Optional[Literal["BondFunctions"]] = "BondFunctions"


class Cap(BaseModel):
    resource_name: Optional[Literal["Cap"]] = "Cap"
    leg: List[CashFlow]
    capRates: List[float]


class Floor(BaseModel):
    resource_name: Optional[Literal["Floor"]] = "Floor"
    leg: List[CashFlow]
    floorRates: List[float]


class Collar(BaseModel):
    resource_name: Optional[Literal["Collar"]] = "Collar"
    leg: List[CashFlow]
    capRates: List[float]
    floorRates: List[float]


class BlackCapFloorEngine(BaseModel):
    resource_name: Optional[Literal["BlackCapFloorEngine"]] = "BlackCapFloorEngine"
    termStructure: YieldTermStructureHandle
    vol: Union[QuoteHandle, OptionletVolatilityStructureHandle]


class BachelierCapFloorEngine(BaseModel):
    resource_name: Optional[
        Literal["BachelierCapFloorEngine"]
    ] = "BachelierCapFloorEngine"
    termStructure: YieldTermStructureHandle
    vol: Union[QuoteHandle, OptionletVolatilityStructureHandle]


class FixedDividend(BaseModel):
    resource_name: Optional[Literal["FixedDividend"]] = "FixedDividend"
    amount: float
    date: Date


class FractionalDividend(BaseModel):
    resource_name: Optional[Literal["FractionalDividend"]] = "FractionalDividend"
    rate: float
    date: Date


class BinomialCRRConvertibleEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialCRRConvertibleEngine"]
    ] = "BinomialCRRConvertibleEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialJRConvertibleEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialJRConvertibleEngine"]
    ] = "BinomialJRConvertibleEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialTrigeorgisConvertibleEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialTrigeorgisConvertibleEngine"]
    ] = "BinomialTrigeorgisConvertibleEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialTianConvertibleEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialTianConvertibleEngine"]
    ] = "BinomialTianConvertibleEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class BinomialJoshi4ConvertibleEngine(BaseModel):
    resource_name: Optional[
        Literal["BinomialJoshi4ConvertibleEngine"]
    ] = "BinomialJoshi4ConvertibleEngine"
    value: GeneralizedBlackScholesProcess
    steps: int


class Futures(BaseModel):
    resource_name: Optional[Literal["Futures"]] = "Futures"


class OvernightIndexFuture(BaseModel):
    resource_name: Optional[Literal["OvernightIndexFuture"]] = "OvernightIndexFuture"


class Pillar(BaseModel):
    resource_name: Optional[Literal["Pillar"]] = "Pillar"


class DatedOISRateHelper(BaseModel):
    resource_name: Optional[Literal["DatedOISRateHelper"]] = "DatedOISRateHelper"
    startDate: Date
    endDate: Date
    rate: QuoteHandle
    index: OvernightIndex
    discountingCurve: Optional[YieldTermStructureHandle] = None


class Discount(BaseModel):
    resource_name: Optional[Literal["Discount"]] = "Discount"


class ZeroYield(BaseModel):
    resource_name: Optional[Literal["ZeroYield"]] = "ZeroYield"


class ForwardRate(BaseModel):
    resource_name: Optional[Literal["ForwardRate"]] = "ForwardRate"


class IterativeBootstrap(BaseModel):
    resource_name: Optional[Literal["IterativeBootstrap"]] = "IterativeBootstrap"
    accuracy: Optional[Optional[float]] = None
    minValue: Optional[Optional[float]] = None
    maxValue: Optional[Optional[float]] = None


class GlobalBootstrap0(BaseModel):
    resource_name: Optional[Literal["GlobalBootstrap"]] = "GlobalBootstrap"
    additionalHelpers: List[RateHelper]
    additionalDates: List[Date]
    accuracy: Optional[Optional[float]] = None


class GlobalBootstrap1(BaseModel):
    resource_name: Optional[Literal["GlobalBootstrap"]] = "GlobalBootstrap"
    accuracy: Optional[Optional[float]] = None


class DefaultProbabilityTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["DefaultProbabilityTermStructureHandle"]
    ] = "DefaultProbabilityTermStructureHandle"
    value: Optional[DefaultProbabilityTermStructure] = None


class RelinkableDefaultProbabilityTermStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableDefaultProbabilityTermStructureHandle"]
    ] = "RelinkableDefaultProbabilityTermStructureHandle"
    value: Optional[DefaultProbabilityTermStructure] = None


class FlatHazardRate0(BaseModel):
    resource_name: Optional[Literal["FlatHazardRate"]] = "FlatHazardRate"
    settlementDays: int
    calendar: Calendar
    hazardRate: QuoteHandle
    dayCounter: DayCounter


class FlatHazardRate1(BaseModel):
    resource_name: Optional[Literal["FlatHazardRate"]] = "FlatHazardRate"
    todaysDate: Date
    hazardRate: QuoteHandle
    dayCounter: DayCounter


class HazardRate(BaseModel):
    resource_name: Optional[Literal["HazardRate"]] = "HazardRate"


class DefaultDensity(BaseModel):
    resource_name: Optional[Literal["DefaultDensity"]] = "DefaultDensity"


class Protection(BaseModel):
    resource_name: Optional[Literal["Protection"]] = "Protection"


class FaceValueClaim(BaseModel):
    resource_name: Optional[Literal["FaceValueClaim"]] = "FaceValueClaim"


class MidPointCdsEngine(BaseModel):
    resource_name: Optional[Literal["MidPointCdsEngine"]] = "MidPointCdsEngine"
    probability: DefaultProbabilityTermStructureHandle
    recoveryRate: float
    discountCurve: YieldTermStructureHandle


class BlackCdsOptionEngine(BaseModel):
    resource_name: Optional[Literal["BlackCdsOptionEngine"]] = "BlackCdsOptionEngine"
    value: DefaultProbabilityTermStructureHandle
    recoveryRate: float
    termStructure: YieldTermStructureHandle
    vol: QuoteHandle


class NormalDistribution(BaseModel):
    resource_name: Optional[Literal["NormalDistribution"]] = "NormalDistribution"
    average: Optional[float] = None
    sigma: Optional[float] = None


class CumulativeNormalDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativeNormalDistribution"]
    ] = "CumulativeNormalDistribution"
    average: Optional[float] = None
    sigma: Optional[float] = None


class InverseCumulativeNormal(BaseModel):
    resource_name: Optional[
        Literal["InverseCumulativeNormal"]
    ] = "InverseCumulativeNormal"
    average: Optional[float] = None
    sigma: Optional[float] = None


class MoroInverseCumulativeNormal(BaseModel):
    resource_name: Optional[
        Literal["MoroInverseCumulativeNormal"]
    ] = "MoroInverseCumulativeNormal"
    average: Optional[float] = None
    sigma: Optional[float] = None


class BivariateCumulativeNormalDistribution(BaseModel):
    resource_name: Optional[
        Literal["BivariateCumulativeNormalDistribution"]
    ] = "BivariateCumulativeNormalDistribution"
    rho: float


class BinomialDistribution(BaseModel):
    resource_name: Optional[Literal["BinomialDistribution"]] = "BinomialDistribution"
    p: float
    n: float


class CumulativeBinomialDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativeBinomialDistribution"]
    ] = "CumulativeBinomialDistribution"
    p: float
    n: float


class BivariateCumulativeNormalDistributionDr78(BaseModel):
    resource_name: Optional[
        Literal["BivariateCumulativeNormalDistributionDr7"]
    ] = "BivariateCumulativeNormalDistributionDr7"
    rho: float


class BivariateCumulativeNormalDistributionWe04DP(BaseModel):
    resource_name: Optional[
        Literal["BivariateCumulativeNormalDistributionWe04DP"]
    ] = "BivariateCumulativeNormalDistributionWe04DP"
    rho: float


class CumulativeChiSquareDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativeChiSquareDistribution"]
    ] = "CumulativeChiSquareDistribution"
    df: float


class NonCentralCumulativeChiSquareDistribution(BaseModel):
    resource_name: Optional[
        Literal["NonCentralCumulativeChiSquareDistribution"]
    ] = "NonCentralCumulativeChiSquareDistribution"
    df: float
    ncp: float


class InverseNonCentralCumulativeChiSquareDistribution(BaseModel):
    resource_name: Optional[
        Literal["InverseNonCentralCumulativeChiSquareDistribution"]
    ] = "InverseNonCentralCumulativeChiSquareDistribution"
    df: float
    ncp: float
    maxEvaluations: Optional[int] = None
    accuracy: Optional[float] = None


class CumulativeGammaDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativeGammaDistribution"]
    ] = "CumulativeGammaDistribution"
    a: float


class GammaFunction(BaseModel):
    resource_name: Optional[Literal["GammaFunction"]] = "GammaFunction"


class PoissonDistribution(BaseModel):
    resource_name: Optional[Literal["PoissonDistribution"]] = "PoissonDistribution"
    mu: float


class CumulativePoissonDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativePoissonDistribution"]
    ] = "CumulativePoissonDistribution"
    mu: float


class InverseCumulativePoisson(BaseModel):
    resource_name: Optional[
        Literal["InverseCumulativePoisson"]
    ] = "InverseCumulativePoisson"
    lambda_: float = Field(..., alias="lambda")


class StudentDistribution(BaseModel):
    resource_name: Optional[Literal["StudentDistribution"]] = "StudentDistribution"
    n: int


class CumulativeStudentDistribution(BaseModel):
    resource_name: Optional[
        Literal["CumulativeStudentDistribution"]
    ] = "CumulativeStudentDistribution"
    n: int


class InverseCumulativeStudent(BaseModel):
    resource_name: Optional[
        Literal["InverseCumulativeStudent"]
    ] = "InverseCumulativeStudent"
    n: int
    accuracy: Optional[float] = None
    maxIterations: Optional[int] = None


class Money0(BaseModel):
    resource_name: Optional[Literal["Money"]] = "Money"
    currency: Currency
    value: float


class Money1(BaseModel):
    resource_name: Optional[Literal["Money"]] = "Money"
    value: float
    currency: Currency


class ExchangeRate(BaseModel):
    resource_name: Optional[Literal["ExchangeRate"]] = "ExchangeRate"
    source: Currency
    target: Currency
    rate: float


class ExchangeRateManager(BaseModel):
    resource_name: Optional[Literal["ExchangeRateManager"]] = "ExchangeRateManager"


class Settings(BaseModel):
    resource_name: Optional[Literal["Settings"]] = "Settings"


class Fdm1dMesherBase(BaseModel):
    resource_name: Optional[Literal["Fdm1dMesher"]] = "Fdm1dMesher"
    size: int


class FdmBlackScholesMesher(BaseModel):
    resource_name: Optional[Literal["FdmBlackScholesMesher"]] = "FdmBlackScholesMesher"
    size: int
    process: GeneralizedBlackScholesProcess
    maturity: float
    strike: float
    xMinConstraint: Optional[Optional[float]] = None
    xMaxConstraint: Optional[Optional[float]] = None
    eps: Optional[float] = None
    scaleFactor: Optional[float] = None
    cPoint: Optional[List[Union[float, float]]] = None
    dividendSchedule: Optional[List[Dividend]] = None
    fdmQuantoHelper: Optional[FdmQuantoHelper] = None
    spotAdjustment: Optional[float] = None


class Concentrating1dMesher0(BaseModel):
    resource_name: Optional[Literal["Concentrating1dMesher"]] = "Concentrating1dMesher"
    start: float
    end: float
    size: int
    cPoints: List[List[Union[float, float, bool]]]
    tol: Optional[float] = None


class Concentrating1dMesher1(BaseModel):
    resource_name: Optional[Literal["Concentrating1dMesher"]] = "Concentrating1dMesher"
    start: float
    end: float
    size: int
    cPoints: Optional[List[Union[float, float]]] = None
    requireCPoint: Optional[bool] = None


class ExponentialJump1dMesher(BaseModel):
    resource_name: Optional[
        Literal["ExponentialJump1dMesher"]
    ] = "ExponentialJump1dMesher"
    steps: int
    beta: float
    jumpIntensity: float
    eta: float
    eps: Optional[float] = None


class FdmCEV1dMesher(BaseModel):
    resource_name: Optional[Literal["FdmCEV1dMesher"]] = "FdmCEV1dMesher"
    size: int
    f0: float
    alpha: float
    beta: float
    maturity: float
    eps: Optional[float] = None
    scaleFactor: Optional[float] = None
    cPoint: Optional[List[Union[float, float]]] = None


class FdmHestonVarianceMesher(BaseModel):
    resource_name: Optional[
        Literal["FdmHestonVarianceMesher"]
    ] = "FdmHestonVarianceMesher"
    size: int
    process: HestonProcess
    maturity: float
    tAvgSteps: Optional[int] = None
    epsilon: Optional[float] = None


class FdmHestonLocalVolatilityVarianceMesher(BaseModel):
    resource_name: Optional[
        Literal["FdmHestonLocalVolatilityVarianceMesher"]
    ] = "FdmHestonLocalVolatilityVarianceMesher"
    size: int
    process: HestonProcess
    leverageFct: LocalVolTermStructure
    maturity: float
    tAvgSteps: Optional[int] = None
    epsilon: Optional[float] = None


class Uniform1dMesher(BaseModel):
    resource_name: Optional[Literal["Uniform1dMesher"]] = "Uniform1dMesher"
    start: float
    end: float
    size: int


class Predefined1dMesher(BaseModel):
    resource_name: Optional[Literal["Predefined1dMesher"]] = "Predefined1dMesher"
    x: List[float]


class Glued1dMesher(BaseModel):
    resource_name: Optional[Literal["Glued1dMesher"]] = "Glued1dMesher"
    leftMesher: Fdm1dMesher
    rightMesher: Fdm1dMesher


class MesherItem(BaseModel):
    resource_name: Optional[Literal["MesherItem"]] = "MesherItem"


class FdmMesherComposite0(BaseModel):
    resource_name: Optional[Literal["FdmMesherComposite"]] = "FdmMesherComposite"
    mesher: Union[MesherItem, Fdm1dMesher]


class FdmMesherComposite1(BaseModel):
    resource_name: Optional[Literal["FdmMesherComposite"]] = "FdmMesherComposite"
    m1: Fdm1dMesher
    m2: Fdm1dMesher
    m3: Optional[Fdm1dMesher] = None
    m4: Optional[Fdm1dMesher] = None


class FdmBlackScholesOp(BaseModel):
    resource_name: Optional[Literal["FdmBlackScholesOp"]] = "FdmBlackScholesOp"
    mesher: FdmMesher
    process: GeneralizedBlackScholesProcess
    strike: float
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[Optional[float]] = None
    direction: Optional[int] = None
    quantoHelper: Optional[FdmQuantoHelper] = None


class Fdm2dBlackScholesOp(BaseModel):
    resource_name: Optional[Literal["Fdm2dBlackScholesOp"]] = "Fdm2dBlackScholesOp"
    mesher: FdmMesher
    p1: GeneralizedBlackScholesProcess
    p2: GeneralizedBlackScholesProcess
    correlation: float
    maturity: float
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[Optional[float]] = None


class FdmCEVOp(BaseModel):
    resource_name: Optional[Literal["FdmCEVOp"]] = "FdmCEVOp"
    mesher: FdmMesher
    rTS: YieldTermStructure
    f0: float
    alpha: float
    beta: float
    direction: int


class FdmG2Op(BaseModel):
    resource_name: Optional[Literal["FdmG2Op"]] = "FdmG2Op"
    mesher: FdmMesher
    model: G2
    direction1: int
    direction2: int


class FdmHestonHullWhiteOp(BaseModel):
    resource_name: Optional[Literal["FdmHestonHullWhiteOp"]] = "FdmHestonHullWhiteOp"
    mesher: FdmMesher
    hestonProcess: HestonProcess
    hwProcess: HullWhiteProcess
    equityShortRateCorrelation: float


class FdmHestonOp(BaseModel):
    resource_name: Optional[Literal["FdmHestonOp"]] = "FdmHestonOp"
    mesher: FdmMesher
    hestonProcess: HestonProcess
    quantoHelper: Optional[FdmQuantoHelper] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class FdmHullWhiteOp(BaseModel):
    resource_name: Optional[Literal["FdmHullWhiteOp"]] = "FdmHullWhiteOp"
    mesher: FdmMesher
    model: HullWhite
    direction: int


class FdmLocalVolFwdOp(BaseModel):
    resource_name: Optional[Literal["FdmLocalVolFwdOp"]] = "FdmLocalVolFwdOp"
    mesher: FdmMesher
    spot: Quote
    rTS: YieldTermStructure
    qTS: YieldTermStructure
    localVol: LocalVolTermStructure
    direction: Optional[int] = None


class FdmOrnsteinUhlenbeckOp(BaseModel):
    resource_name: Optional[
        Literal["FdmOrnsteinUhlenbeckOp"]
    ] = "FdmOrnsteinUhlenbeckOp"
    mesher: FdmMesher
    p: OrnsteinUhlenbeckProcess
    rTS: YieldTermStructure
    direction: Optional[int] = None


class FdmSabrOp(BaseModel):
    resource_name: Optional[Literal["FdmSabrOp"]] = "FdmSabrOp"
    mesher: FdmMesher
    rTS: YieldTermStructure
    f0: float
    alpha: float
    beta: float
    nu: float
    rho: float


class FdmZabrOp(BaseModel):
    resource_name: Optional[Literal["FdmZabrOp"]] = "FdmZabrOp"
    mesher: FdmMesher
    beta: float
    nu: float
    rho: float
    gamma: float


class FdmDupire1dOp(BaseModel):
    resource_name: Optional[Literal["FdmDupire1dOp"]] = "FdmDupire1dOp"
    mesher: FdmMesher
    localVolatility: Array


class FdmBlackScholesFwdOp(BaseModel):
    resource_name: Optional[Literal["FdmBlackScholesFwdOp"]] = "FdmBlackScholesFwdOp"
    mesher: FdmMesher
    process: GeneralizedBlackScholesProcess
    strike: float
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[float] = None
    direction: Optional[int] = None


class TripleBandLinearOpBase(BaseModel):
    resource_name: Optional[Literal["TripleBandLinearOp"]] = "TripleBandLinearOp"
    direction: int
    mesher: FdmMesher


class FirstDerivativeOp(BaseModel):
    resource_name: Optional[Literal["FirstDerivativeOp"]] = "FirstDerivativeOp"
    direction: int
    mesher: FdmMesher


class SecondDerivativeOp(BaseModel):
    resource_name: Optional[Literal["SecondDerivativeOp"]] = "SecondDerivativeOp"
    direction: int
    mesher: FdmMesher


class NinePointLinearOpBase(BaseModel):
    resource_name: Optional[Literal["NinePointLinearOp"]] = "NinePointLinearOp"
    d0: int
    d1: int
    mesher: FdmMesher


class SecondOrderMixedDerivativeOp(BaseModel):
    resource_name: Optional[
        Literal["SecondOrderMixedDerivativeOp"]
    ] = "SecondOrderMixedDerivativeOp"
    d0: int
    d1: int
    mesher: FdmMesher


class NthOrderDerivativeOp(BaseModel):
    resource_name: Optional[Literal["NthOrderDerivativeOp"]] = "NthOrderDerivativeOp"
    direction: int
    order: int
    nPoints: int
    mesher: FdmMesher


class FdmLogInnerValue(BaseModel):
    resource_name: Optional[Literal["FdmLogInnerValue"]] = "FdmLogInnerValue"
    payoff: Payoff
    mesher: FdmMesher
    direction: int


class FdmLogBasketInnerValue(BaseModel):
    resource_name: Optional[
        Literal["FdmLogBasketInnerValue"]
    ] = "FdmLogBasketInnerValue"
    payoff: BasketPayoff
    mesher: FdmMesher


class FdmSnapshotCondition(BaseModel):
    resource_name: Optional[Literal["FdmSnapshotCondition"]] = "FdmSnapshotCondition"
    t: float


class FdmAmericanStepCondition(BaseModel):
    resource_name: Optional[
        Literal["FdmAmericanStepCondition"]
    ] = "FdmAmericanStepCondition"
    mesher: FdmMesher
    calculator: FdmInnerValueCalculator


class FdmArithmeticAverageCondition(BaseModel):
    resource_name: Optional[
        Literal["FdmArithmeticAverageCondition"]
    ] = "FdmArithmeticAverageCondition"
    averageTimes: List[float]
    real: float
    pastFixings: int
    mesher: FdmMesher
    equityDirection: int


class FdmBermudanStepCondition(BaseModel):
    resource_name: Optional[
        Literal["FdmBermudanStepCondition"]
    ] = "FdmBermudanStepCondition"
    exerciseDates: List[Date]
    referenceDate: Date
    dayCounter: DayCounter
    mesher: FdmMesher
    calculator: FdmInnerValueCalculator


class FdmSimpleStorageCondition(BaseModel):
    resource_name: Optional[
        Literal["FdmSimpleStorageCondition"]
    ] = "FdmSimpleStorageCondition"
    exerciseTimes: List[float]
    mesher: FdmMesher
    calculator: FdmInnerValueCalculator
    changeRate: float


class FdmSimpleSwingCondition(BaseModel):
    resource_name: Optional[
        Literal["FdmSimpleSwingCondition"]
    ] = "FdmSimpleSwingCondition"
    exerciseTimes: List[float]
    mesher: FdmMesher
    calculator: FdmInnerValueCalculator
    swingDirection: int
    minExercises: Optional[int] = None


class FdmDividendHandler(BaseModel):
    resource_name: Optional[Literal["FdmDividendHandler"]] = "FdmDividendHandler"
    schedule: List[Dividend]
    mesher: FdmMesher
    referenceDate: Date
    dayCounter: DayCounter
    equityDirection: int


class BSMRNDCalculator(BaseModel):
    resource_name: Optional[Literal["BSMRNDCalculator"]] = "BSMRNDCalculator"
    process: GeneralizedBlackScholesProcess


class CEVRNDCalculator(BaseModel):
    resource_name: Optional[Literal["CEVRNDCalculator"]] = "CEVRNDCalculator"
    f0: float
    alpha: float
    beta: float


class GBSMRNDCalculator(BaseModel):
    resource_name: Optional[Literal["GBSMRNDCalculator"]] = "GBSMRNDCalculator"
    process: GeneralizedBlackScholesProcess


class HestonRNDCalculator(BaseModel):
    resource_name: Optional[Literal["HestonRNDCalculator"]] = "HestonRNDCalculator"
    hestonProcess: HestonProcess
    integrationEps: Optional[float] = None
    maxIntegrationIterations: Optional[int] = None


class LocalVolRNDCalculator(BaseModel):
    resource_name: Optional[Literal["LocalVolRNDCalculator"]] = "LocalVolRNDCalculator"
    spot: Quote
    rTS: YieldTermStructure
    qTS: YieldTermStructure
    localVol: LocalVolTermStructure
    xGrid: Optional[int] = None
    tGrid: Optional[int] = None
    x0Density: Optional[float] = None
    localVolProbEps: Optional[float] = None
    maxIter: Optional[int] = None
    gaussianStepSize: Optional[float] = None


class SquareRootProcessRNDCalculator(BaseModel):
    resource_name: Optional[
        Literal["SquareRootProcessRNDCalculator"]
    ] = "SquareRootProcessRNDCalculator"
    v0: float
    kappa: float
    theta: float
    sigma: float


class ExponentialSplinesFitting(BaseModel):
    resource_name: Optional[
        Literal["ExponentialSplinesFitting"]
    ] = "ExponentialSplinesFitting"
    constrainAtZero: Optional[bool] = None
    weights: Optional[Array] = None


class NelsonSiegelFitting(BaseModel):
    resource_name: Optional[Literal["NelsonSiegelFitting"]] = "NelsonSiegelFitting"
    weights: Optional[Array] = None


class SvenssonFitting(BaseModel):
    resource_name: Optional[Literal["SvenssonFitting"]] = "SvenssonFitting"
    weights: Optional[Array] = None


class CubicBSplinesFitting(BaseModel):
    resource_name: Optional[Literal["CubicBSplinesFitting"]] = "CubicBSplinesFitting"
    knotVector: List[float]
    constrainAtZero: Optional[bool] = None
    weights: Optional[Array] = None


class SimplePolynomialFitting(BaseModel):
    resource_name: Optional[
        Literal["SimplePolynomialFitting"]
    ] = "SimplePolynomialFitting"
    degree: float
    constrainAtZero: Optional[bool] = None
    weights: Optional[Array] = None


class Position(BaseModel):
    resource_name: Optional[Literal["Position"]] = "Position"


class Gsr(BaseModel):
    resource_name: Optional[Literal["Gsr"]] = "Gsr"
    termStructure: YieldTermStructureHandle
    volstepdates: List[Date]
    volatilities: List[QuoteHandle]
    reversions: List[QuoteHandle]
    T: Optional[float] = None


class MarkovFunctionalModelSettings0(BaseModel):
    resource_name: Optional[
        Literal["MarkovFunctionalModelSettings"]
    ] = "MarkovFunctionalModelSettings"
    yGridPoints: Optional[int] = None
    yStdDevs: Optional[float] = None
    gaussHermitePoints: Optional[int] = None
    digitalGap: Optional[float] = None
    marketRateAccuracy: Optional[float] = None
    lowerRateBound: Optional[float] = None
    upperRateBound: Optional[float] = None
    adjustments: Optional[int] = None
    smileMoneyCheckpoints: Optional[List[float]] = None


class MarkovFunctionalModelSettings1(BaseModel):
    resource_name: Optional[
        Literal["MarkovFunctionalModelSettings"]
    ] = "MarkovFunctionalModelSettings"
    yGridPoints: int
    yStdDevs: float
    gaussHermitePoints: int
    digitalGap: float
    marketRateAccuracy: float
    lowerRateBound: float
    upperRateBound: float
    adjustments: int


MarkovFunctionalModelSettings = Union[
    MarkovFunctionalModelSettings0, MarkovFunctionalModelSettings1
]


class SegmentIntegral(BaseModel):
    resource_name: Optional[Literal["SegmentIntegral"]] = "SegmentIntegral"
    intervals: int


class SimpsonIntegral(BaseModel):
    resource_name: Optional[Literal["SimpsonIntegral"]] = "SimpsonIntegral"
    accuracy: float
    maxIterations: int


class GaussKronrodAdaptive(BaseModel):
    resource_name: Optional[Literal["GaussKronrodAdaptive"]] = "GaussKronrodAdaptive"
    tolerance: float
    maxFunctionEvaluations: Optional[int] = None


class GaussKronrodNonAdaptive(BaseModel):
    resource_name: Optional[
        Literal["GaussKronrodNonAdaptive"]
    ] = "GaussKronrodNonAdaptive"
    absoluteAccuracy: float
    maxEvaluations: int
    relativeAccuracy: float


class GaussLobattoIntegral(BaseModel):
    resource_name: Optional[Literal["GaussLobattoIntegral"]] = "GaussLobattoIntegral"
    maxIterations: int
    absAccuracy: float
    relAccuracy: Optional[float] = None
    useConvergenceEstimate: Optional[bool] = None


class GaussLaguerreIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussLaguerreIntegration"]
    ] = "GaussLaguerreIntegration"
    n: int
    s: Optional[float] = None


class GaussHermiteIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussHermiteIntegration"]
    ] = "GaussHermiteIntegration"
    n: int
    mu: Optional[float] = None


class GaussJacobiIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussJacobiIntegration"]
    ] = "GaussJacobiIntegration"
    n: int
    alpha: float
    beta: float


class GaussHyperbolicIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussHyperbolicIntegration"]
    ] = "GaussHyperbolicIntegration"
    n: int


class GaussLegendreIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussLegendreIntegration"]
    ] = "GaussLegendreIntegration"
    n: int


class GaussChebyshevIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussChebyshevIntegration"]
    ] = "GaussChebyshevIntegration"
    n: int


class GaussChebyshev2ndIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussChebyshev2ndIntegration"]
    ] = "GaussChebyshev2ndIntegration"
    n: int


class GaussGegenbauerIntegration(BaseModel):
    resource_name: Optional[
        Literal["GaussGegenbauerIntegration"]
    ] = "GaussGegenbauerIntegration"
    n: int
    lambda_: float = Field(..., alias="lambda")


class SampleReal(BaseModel):
    resource_name: Optional[Literal["SampleReal"]] = "SampleReal"


class SampleArray(BaseModel):
    resource_name: Optional[Literal["SampleArray"]] = "SampleArray"


class LecuyerUniformRng(BaseModel):
    resource_name: Optional[Literal["LecuyerUniformRng"]] = "LecuyerUniformRng"
    seed: Optional[int] = None


class KnuthUniformRng(BaseModel):
    resource_name: Optional[Literal["KnuthUniformRng"]] = "KnuthUniformRng"
    seed: Optional[int] = None


class MersenneTwisterUniformRng(BaseModel):
    resource_name: Optional[
        Literal["MersenneTwisterUniformRng"]
    ] = "MersenneTwisterUniformRng"
    seed: Optional[int] = None


class UniformRandomGenerator(BaseModel):
    resource_name: Optional[
        Literal["UniformRandomGenerator"]
    ] = "UniformRandomGenerator"
    seed: Optional[int] = None


class LecuyerUniformRngCLGaussianRng(BaseModel):
    resource_name: Optional[
        Literal["LecuyerUniformRngCLGaussianRng"]
    ] = "LecuyerUniformRngCLGaussianRng"
    rng: LecuyerUniformRng


class KnuthUniformRngCLGaussianRng(BaseModel):
    resource_name: Optional[
        Literal["KnuthUniformRngCLGaussianRng"]
    ] = "KnuthUniformRngCLGaussianRng"
    rng: KnuthUniformRng


class MersenneTwisterUniformRngCLGaussianRng(BaseModel):
    resource_name: Optional[
        Literal["MersenneTwisterUniformRngCLGaussianRng"]
    ] = "MersenneTwisterUniformRngCLGaussianRng"
    rng: MersenneTwisterUniformRng


class GaussianRandomGenerator(BaseModel):
    resource_name: Optional[
        Literal["GaussianRandomGenerator"]
    ] = "GaussianRandomGenerator"
    rng: UniformRandomGenerator


class HaltonRsg(BaseModel):
    resource_name: Optional[Literal["HaltonRsg"]] = "HaltonRsg"
    dimensionality: int
    seed: Optional[int] = None
    randomStart: Optional[bool] = None
    randomShift: Optional[bool] = None


class SobolBrownianBridgeRsg(BaseModel):
    resource_name: Optional[
        Literal["SobolBrownianBridgeRsg"]
    ] = "SobolBrownianBridgeRsg"
    factors: int
    steps: int


class UniformRandomSequenceGenerator(BaseModel):
    resource_name: Optional[
        Literal["UniformRandomSequenceGenerator"]
    ] = "UniformRandomSequenceGenerator"
    dimensionality: int
    rng: UniformRandomGenerator


class GaussianRandomSequenceGenerator(BaseModel):
    resource_name: Optional[
        Literal["GaussianRandomSequenceGenerator"]
    ] = "GaussianRandomSequenceGenerator"
    uniformSequenceGenerator: UniformRandomSequenceGenerator


class Path(BaseModel):
    resource_name: Optional[Literal["Path"]] = "Path"


class SamplePath(BaseModel):
    resource_name: Optional[Literal["SamplePath"]] = "SamplePath"


class MultiPath(BaseModel):
    resource_name: Optional[Literal["MultiPath"]] = "MultiPath"


class SampleMultiPath(BaseModel):
    resource_name: Optional[Literal["SampleMultiPath"]] = "SampleMultiPath"


class BrownianBridge0(BaseModel):
    resource_name: Optional[Literal["BrownianBridge"]] = "BrownianBridge"
    steps: int


class BrownianBridge1(BaseModel):
    resource_name: Optional[Literal["BrownianBridge"]] = "BrownianBridge"
    times: List[float]


class BrownianBridge2(BaseModel):
    resource_name: Optional[Literal["BrownianBridge"]] = "BrownianBridge"
    timeGrid: TimeGrid


class TridiagonalOperatorBase(BaseModel):
    resource_name: Optional[Literal["TridiagonalOperator"]] = "TridiagonalOperator"
    low: Array
    mid: Array
    high: Array


class DPlus(BaseModel):
    resource_name: Optional[Literal["DPlus"]] = "DPlus"
    gridPoints: int
    h: float


class DMinus(BaseModel):
    resource_name: Optional[Literal["DMinus"]] = "DMinus"
    gridPoints: int
    h: float


class DZero(BaseModel):
    resource_name: Optional[Literal["DZero"]] = "DZero"
    gridPoints: int
    h: float


class DPlusDMinus(BaseModel):
    resource_name: Optional[Literal["DPlusDMinus"]] = "DPlusDMinus"
    gridPoints: int
    h: float


class SampledCurve(BaseModel):
    resource_name: Optional[Literal["SampledCurve"]] = "SampledCurve"
    value: Optional[Array] = None


class HestonSLVProcess(BaseModel):
    resource_name: Optional[Literal["HestonSLVProcess"]] = "HestonSLVProcess"
    hestonProcess: HestonProcess
    leverageFct: LocalVolTermStructure


class MTBrownianGeneratorFactory(BaseModel):
    resource_name: Optional[
        Literal["MTBrownianGeneratorFactory"]
    ] = "MTBrownianGeneratorFactory"
    seed: Optional[int] = None


class SobolBrownianGenerator(BaseModel):
    resource_name: Optional[
        Literal["SobolBrownianGenerator"]
    ] = "SobolBrownianGenerator"


class FdmHestonGreensFct(BaseModel):
    resource_name: Optional[Literal["FdmHestonGreensFct"]] = "FdmHestonGreensFct"


class IncrementalStatistics(BaseModel):
    resource_name: Optional[Literal["IncrementalStatistics"]] = "IncrementalStatistics"


class RiskStatistics(BaseModel):
    resource_name: Optional[Literal["RiskStatistics"]] = "RiskStatistics"


class CapFloorTermVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["CapFloorTermVolatilityStructureHandle"]
    ] = "CapFloorTermVolatilityStructureHandle"
    value: Optional[CapFloorTermVolatilityStructure] = None


class RelinkableCapFloorTermVolatilityStructureHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableCapFloorTermVolatilityStructureHandle"]
    ] = "RelinkableCapFloorTermVolatilityStructureHandle"
    value: Optional[CapFloorTermVolatilityStructure] = None


class StrippedOptionletAdapter(BaseModel):
    resource_name: Optional[
        Literal["StrippedOptionletAdapter"]
    ] = "StrippedOptionletAdapter"
    value: StrippedOptionletBase


class Settlement(BaseModel):
    resource_name: Optional[Literal["Settlement"]] = "Settlement"


class BlackSwaptionEngine0(BaseModel):
    resource_name: Optional[Literal["BlackSwaptionEngine"]] = "BlackSwaptionEngine"
    discountCurve: YieldTermStructureHandle
    vol: QuoteHandle
    dc: Optional[DayCounter] = None
    displacement: Optional[float] = None


class BlackSwaptionEngine1(BaseModel):
    resource_name: Optional[Literal["BlackSwaptionEngine"]] = "BlackSwaptionEngine"
    discountCurve: YieldTermStructureHandle
    v: SwaptionVolatilityStructureHandle


class BachelierSwaptionEngine0(BaseModel):
    resource_name: Optional[
        Literal["BachelierSwaptionEngine"]
    ] = "BachelierSwaptionEngine"
    discountCurve: YieldTermStructureHandle
    vol: QuoteHandle
    dc: Optional[DayCounter] = None


class BachelierSwaptionEngine1(BaseModel):
    resource_name: Optional[
        Literal["BachelierSwaptionEngine"]
    ] = "BachelierSwaptionEngine"
    discountCurve: YieldTermStructureHandle
    v: SwaptionVolatilityStructureHandle


class ConstantEstimator(BaseModel):
    resource_name: Optional[Literal["ConstantEstimator"]] = "ConstantEstimator"
    size: int


class ParkinsonSigma(BaseModel):
    resource_name: Optional[Literal["ParkinsonSigma"]] = "ParkinsonSigma"
    yearFraction: float


class GarmanKlassSigma1(BaseModel):
    resource_name: Optional[Literal["GarmanKlassSigma"]] = "GarmanKlassSigma"
    yearFraction: float
    marketOpenFraction: float


class GarmanKlassSigma3(BaseModel):
    resource_name: Optional[Literal["GarmanKlassSigma"]] = "GarmanKlassSigma"
    yearFraction: float
    marketOpenFraction: float


class GarmanKlassSigma4(BaseModel):
    resource_name: Optional[Literal["GarmanKlassSigma"]] = "GarmanKlassSigma"
    yearFraction: float


class GarmanKlassSigma5(BaseModel):
    resource_name: Optional[Literal["GarmanKlassSigma"]] = "GarmanKlassSigma"
    yearFraction: float


class GarmanKlassSigma6(BaseModel):
    resource_name: Optional[Literal["GarmanKlassSigma"]] = "GarmanKlassSigma"
    yearFraction: float
    marketOpenFraction: float


class Gaussian1dNonstandardSwaptionEngineProbabilities(BaseModel):
    resource_name: Optional[
        Literal["Gaussian1dNonstandardSwaptionEngineProbabilities"]
    ] = "Gaussian1dNonstandardSwaptionEngineProbabilities"


class ExtendedOrnsteinUhlenbeckProcess(BaseModel):
    resource_name: Optional[
        Literal["ExtendedOrnsteinUhlenbeckProcess"]
    ] = "ExtendedOrnsteinUhlenbeckProcess"


class FdmSolverDesc(BaseModel):
    resource_name: Optional[Literal["FdmSolverDesc"]] = "FdmSolverDesc"


class AndreasenHugeVolatilityInterplCalibrationType(BaseModel):
    resource_name: Optional[
        Literal["AndreasenHugeVolatilityInterplCalibrationType"]
    ] = "AndreasenHugeVolatilityInterplCalibrationType"


class FdmDirichletBoundarySide(BaseModel):
    resource_name: Optional[
        Literal["FdmDirichletBoundarySide"]
    ] = "FdmDirichletBoundarySide"


class Leg(BaseModel):
    resource_name: Optional[Literal["Leg"]] = "Leg"


class FdmLinearOpLayout(BaseModel):
    resource_name: Optional[Literal["FdmLinearOpLayout"]] = "FdmLinearOpLayout"


class Integrator(BaseModel):
    resource_name: Optional[Literal["Integrator"]] = "Integrator"


class IsdaCdsEngineAccrualBias(BaseModel):
    resource_name: Optional[
        Literal["IsdaCdsEngineAccrualBias"]
    ] = "IsdaCdsEngineAccrualBias"


class Market(BaseModel):
    resource_name: Optional[Literal["Market"]] = "Market"


class AndreasenHugeVolatilityInterplCalibrationSet(BaseModel):
    resource_name: Optional[
        Literal["AndreasenHugeVolatilityInterplCalibrationSet"]
    ] = "AndreasenHugeVolatilityInterplCalibrationSet"


class AnalyticPTDHestonEngineIntegration(BaseModel):
    resource_name: Optional[
        Literal["AnalyticPTDHestonEngineIntegration"]
    ] = "AnalyticPTDHestonEngineIntegration"


class SettlementMethod(BaseModel):
    resource_name: Optional[Literal["SettlementMethod"]] = "SettlementMethod"


class DeltaVolQuoteAtmType(BaseModel):
    resource_name: Optional[Literal["DeltaVolQuoteAtmType"]] = "DeltaVolQuoteAtmType"


class IsdaCdsEngineForwardsInCouponPeriod(BaseModel):
    resource_name: Optional[
        Literal["IsdaCdsEngineForwardsInCouponPeriod"]
    ] = "IsdaCdsEngineForwardsInCouponPeriod"


class GaussianQuadrature(BaseModel):
    resource_name: Optional[Literal["GaussianQuadrature"]] = "GaussianQuadrature"


class FdmBoundaryConditionSet(BaseModel):
    resource_name: Optional[
        Literal["FdmBoundaryConditionSet"]
    ] = "FdmBoundaryConditionSet"


class DiscountFactor(BaseModel):
    resource_name: Optional[Literal["DiscountFactor"]] = "DiscountFactor"


class FdmDiscountDirichletBoundarySide(BaseModel):
    resource_name: Optional[
        Literal["FdmDiscountDirichletBoundarySide"]
    ] = "FdmDiscountDirichletBoundarySide"


class DefaultBoundaryConditionSide(BaseModel):
    resource_name: Optional[
        Literal["DefaultBoundaryConditionSide"]
    ] = "DefaultBoundaryConditionSide"


class FdmStepConditionComposite(BaseModel):
    resource_name: Optional[
        Literal["FdmStepConditionComposite"]
    ] = "FdmStepConditionComposite"


class AnalyticHestonEngineComplexLogFormula(BaseModel):
    resource_name: Optional[
        Literal["AnalyticHestonEngineComplexLogFormula"]
    ] = "AnalyticHestonEngineComplexLogFormula"


class Period0(BaseModel):
    resource_name: Optional[Literal["Period"]] = "Period"
    n: Optional[int] = None
    units: Optional[TimeUnit] = None


class ExerciseBase(BaseModel):
    resource_name: Optional[Literal["Exercise"]] = "Exercise"
    type: ExerciseType


class RebatedExercise(BaseModel):
    resource_name: Optional[Literal["RebatedExercise"]] = "RebatedExercise"
    exercise: Exercise
    rebates: List[float]
    rebateSettlementDays: Optional[float] = None
    rebatePaymentCalendar: Optional[Calendar] = None
    rebatePaymentConvention: Optional[BusinessDayConvention] = None


class Argentina(BaseModel):
    resource_name: Optional[Literal["Argentina"]] = "Argentina"
    m: Optional[ArgentinaMarket] = None


class Brazil(BaseModel):
    resource_name: Optional[Literal["Brazil"]] = "Brazil"
    m: Optional[BrazilMarket] = None


class Canada(BaseModel):
    resource_name: Optional[Literal["Canada"]] = "Canada"
    m: Optional[CanadaMarket] = None


class China(BaseModel):
    resource_name: Optional[Literal["China"]] = "China"
    m: Optional[ChinaMarket] = None


class CzechRepublic(BaseModel):
    resource_name: Optional[Literal["CzechRepublic"]] = "CzechRepublic"
    m: Optional[CzechRepublicMarket] = None


class France(BaseModel):
    resource_name: Optional[Literal["France"]] = "France"
    m: Optional[FranceMarket] = None


class Germany(BaseModel):
    resource_name: Optional[Literal["Germany"]] = "Germany"
    m: Optional[GermanyMarket] = None


class HongKong(BaseModel):
    resource_name: Optional[Literal["HongKong"]] = "HongKong"
    m: Optional[HongKongMarket] = None


class Iceland(BaseModel):
    resource_name: Optional[Literal["Iceland"]] = "Iceland"
    m: Optional[IcelandMarket] = None


class India(BaseModel):
    resource_name: Optional[Literal["India"]] = "India"
    m: Optional[IndiaMarket] = None


class Indonesia(BaseModel):
    resource_name: Optional[Literal["Indonesia"]] = "Indonesia"
    m: Optional[IndonesiaMarket] = None


class Israel(BaseModel):
    resource_name: Optional[Literal["Israel"]] = "Israel"
    m: Optional[IsraelMarket] = None


class Italy(BaseModel):
    resource_name: Optional[Literal["Italy"]] = "Italy"
    m: Optional[ItalyMarket] = None


class Mexico(BaseModel):
    resource_name: Optional[Literal["Mexico"]] = "Mexico"
    m: Optional[MexicoMarket] = None


class Russia(BaseModel):
    resource_name: Optional[Literal["Russia"]] = "Russia"
    m: Optional[RussiaMarket] = None


class SaudiArabia(BaseModel):
    resource_name: Optional[Literal["SaudiArabia"]] = "SaudiArabia"
    m: Optional[SaudiArabiaMarket] = None


class Singapore(BaseModel):
    resource_name: Optional[Literal["Singapore"]] = "Singapore"
    m: Optional[SingaporeMarket] = None


class Slovakia(BaseModel):
    resource_name: Optional[Literal["Slovakia"]] = "Slovakia"
    m: Optional[SlovakiaMarket] = None


class SouthKorea(BaseModel):
    resource_name: Optional[Literal["SouthKorea"]] = "SouthKorea"
    m: Optional[SouthKoreaMarket] = None


class Taiwan(BaseModel):
    resource_name: Optional[Literal["Taiwan"]] = "Taiwan"
    m: Optional[TaiwanMarket] = None


class Ukraine(BaseModel):
    resource_name: Optional[Literal["Ukraine"]] = "Ukraine"
    m: Optional[UkraineMarket] = None


class UnitedKingdom(BaseModel):
    resource_name: Optional[Literal["UnitedKingdom"]] = "UnitedKingdom"
    m: Optional[UnitedKingdomMarket] = None


class UnitedStates(BaseModel):
    resource_name: Optional[Literal["UnitedStates"]] = "UnitedStates"
    m: Optional[UnitedStatesMarket] = None


class JointCalendar0(BaseModel):
    resource_name: Optional[Literal["JointCalendar"]] = "JointCalendar"
    arg_0: Calendar
    arg_1: Calendar
    arg_2: Calendar
    arg_3: Calendar
    rule: Optional[JointCalendarRule] = None


class JointCalendar1(BaseModel):
    resource_name: Optional[Literal["JointCalendar"]] = "JointCalendar"
    arg_0: Calendar
    arg_1: Calendar
    arg_2: Calendar
    rule: Optional[JointCalendarRule] = None


class JointCalendar2(BaseModel):
    resource_name: Optional[Literal["JointCalendar"]] = "JointCalendar"
    arg_0: Calendar
    arg_1: Calendar
    rule: Optional[JointCalendarRule] = None


class Actual365Fixed(BaseModel):
    resource_name: Optional[Literal["Actual365Fixed"]] = "Actual365Fixed"
    c: Optional[Actual365FixedConvention] = None


class Thirty360(BaseModel):
    resource_name: Optional[Literal["Thirty36"]] = "Thirty36"
    c: Optional[Thirty360Convention] = None


class InterestRate(BaseModel):
    resource_name: Optional[Literal["InterestRate"]] = "InterestRate"
    r: Optional[float] = None
    dc: Optional[DayCounter] = None
    comp: Optional[Compounding] = None
    freq: Optional[float] = None


class ZeroSpreadedTermStructure(BaseModel):
    resource_name: Optional[
        Literal["ZeroSpreadedTermStructure"]
    ] = "ZeroSpreadedTermStructure"
    curveHandle: YieldTermStructureHandle
    spreadHandle: QuoteHandle
    comp: Optional[Compounding] = None
    freq: Optional[float] = None
    dc: Optional[DayCounter] = None


class FlatForward0(BaseModel):
    resource_name: Optional[Literal["FlatForward"]] = "FlatForward"
    referenceDate: Date
    forward: Union[float, QuoteHandle]
    dayCounter: DayCounter
    compounding: Optional[Compounding] = None
    frequency: Optional[Frequency] = None


class FlatForward1(BaseModel):
    resource_name: Optional[Literal["FlatForward"]] = "FlatForward"
    settlementDays: int
    calendar: Calendar
    forward: Union[float, QuoteHandle]
    dayCounter: DayCounter
    compounding: Optional[Compounding] = None
    frequency: Optional[Frequency] = None


class IborIndexBase(BaseModel):
    resource_name: Optional[Literal["IborIndex"]] = "IborIndex"
    familyName: str
    tenor: Period
    settlementDays: int
    currency: Currency
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    dayCounter: DayCounter
    h: Optional[YieldTermStructureHandle] = None


class Libor(BaseModel):
    resource_name: Optional[Literal["Libor"]] = "Libor"
    familyName: str
    tenor: Period
    settlementDays: float
    currency: Currency
    financialCenterCalendar: Calendar
    dayCounter: DayCounter
    h: Optional[YieldTermStructureHandle] = None


class SwapIndexBase(BaseModel):
    resource_name: Optional[Literal["SwapIndex"]] = "SwapIndex"
    familyName: str
    tenor: Period
    settlementDays: int
    currency: Currency
    calendar: Calendar
    fixedLegTenor: Period
    fixedLegConvention: BusinessDayConvention
    fixedLegDayCounter: DayCounter
    iborIndex: IborIndex
    discountCurve: Optional[YieldTermStructureHandle] = None


class SwapSpreadIndex(BaseModel):
    resource_name: Optional[Literal["SwapSpreadIndex"]] = "SwapSpreadIndex"
    familyName: str
    swapIndex1: SwapIndex
    swapIndex2: SwapIndex
    gearing1: Optional[float] = None
    gearing2: Optional[float] = None


class AUDLibor(BaseModel):
    resource_name: Optional[Literal["AUDLibor"]] = "AUDLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class CADLibor(BaseModel):
    resource_name: Optional[Literal["CADLibor"]] = "CADLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Cdor(BaseModel):
    resource_name: Optional[Literal["Cdor"]] = "Cdor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class CHFLibor(BaseModel):
    resource_name: Optional[Literal["CHFLibor"]] = "CHFLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class DKKLibor(BaseModel):
    resource_name: Optional[Literal["DKKLibor"]] = "DKKLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class BbswBase(BaseModel):
    resource_name: Optional[Literal["Bbsw"]] = "Bbsw"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class BkbmBase(BaseModel):
    resource_name: Optional[Literal["Bkbm"]] = "Bkbm"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EuriborBase(BaseModel):
    resource_name: Optional[Literal["Euribor"]] = "Euribor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Euribor365Base(BaseModel):
    resource_name: Optional[Literal["Euribor365"]] = "Euribor365"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EURLiborBase(BaseModel):
    resource_name: Optional[Literal["EURLibor"]] = "EURLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class GBPLibor(BaseModel):
    resource_name: Optional[Literal["GBPLibor"]] = "GBPLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Jibar(BaseModel):
    resource_name: Optional[Literal["Jibar"]] = "Jibar"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class JPYLibor(BaseModel):
    resource_name: Optional[Literal["JPYLibor"]] = "JPYLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Mosprime(BaseModel):
    resource_name: Optional[Literal["Mosprime"]] = "Mosprime"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class NZDLibor(BaseModel):
    resource_name: Optional[Literal["NZDLibor"]] = "NZDLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Pribor(BaseModel):
    resource_name: Optional[Literal["Pribor"]] = "Pribor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Robor(BaseModel):
    resource_name: Optional[Literal["Robor"]] = "Robor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class SEKLibor(BaseModel):
    resource_name: Optional[Literal["SEKLibor"]] = "SEKLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Shibor(BaseModel):
    resource_name: Optional[Literal["Shibor"]] = "Shibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Tibor(BaseModel):
    resource_name: Optional[Literal["Tibor"]] = "Tibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class THBFIX(BaseModel):
    resource_name: Optional[Literal["THBFIX"]] = "THBFIX"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class TRLibor(BaseModel):
    resource_name: Optional[Literal["TRLibor"]] = "TRLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class USDLibor(BaseModel):
    resource_name: Optional[Literal["USDLibor"]] = "USDLibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Wibor(BaseModel):
    resource_name: Optional[Literal["Wibor"]] = "Wibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class Zibor(BaseModel):
    resource_name: Optional[Literal["Zibor"]] = "Zibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EuriborSwapIsdaFixA0(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIsdaFixA"]] = "EuriborSwapIsdaFixA"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EuriborSwapIsdaFixA1(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIsdaFixA"]] = "EuriborSwapIsdaFixA"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class EuriborSwapIsdaFixB0(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIsdaFixB"]] = "EuriborSwapIsdaFixB"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EuriborSwapIsdaFixB1(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIsdaFixB"]] = "EuriborSwapIsdaFixB"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class EuriborSwapIfrFix0(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIfrFix"]] = "EuriborSwapIfrFix"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EuriborSwapIfrFix1(BaseModel):
    resource_name: Optional[Literal["EuriborSwapIfrFix"]] = "EuriborSwapIfrFix"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class EurLiborSwapIsdaFixA0(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIsdaFixA"]] = "EurLiborSwapIsdaFixA"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EurLiborSwapIsdaFixA1(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIsdaFixA"]] = "EurLiborSwapIsdaFixA"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class EurLiborSwapIsdaFixB0(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIsdaFixB"]] = "EurLiborSwapIsdaFixB"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EurLiborSwapIsdaFixB1(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIsdaFixB"]] = "EurLiborSwapIsdaFixB"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class EurLiborSwapIfrFix0(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIfrFix"]] = "EurLiborSwapIfrFix"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class EurLiborSwapIfrFix1(BaseModel):
    resource_name: Optional[Literal["EurLiborSwapIfrFix"]] = "EurLiborSwapIfrFix"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class ChfLiborSwapIsdaFix0(BaseModel):
    resource_name: Optional[Literal["ChfLiborSwapIsdaFix"]] = "ChfLiborSwapIsdaFix"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class ChfLiborSwapIsdaFix1(BaseModel):
    resource_name: Optional[Literal["ChfLiborSwapIsdaFix"]] = "ChfLiborSwapIsdaFix"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class GbpLiborSwapIsdaFix0(BaseModel):
    resource_name: Optional[Literal["GbpLiborSwapIsdaFix"]] = "GbpLiborSwapIsdaFix"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class GbpLiborSwapIsdaFix1(BaseModel):
    resource_name: Optional[Literal["GbpLiborSwapIsdaFix"]] = "GbpLiborSwapIsdaFix"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class JpyLiborSwapIsdaFixAm0(BaseModel):
    resource_name: Optional[Literal["JpyLiborSwapIsdaFixAm"]] = "JpyLiborSwapIsdaFixAm"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class JpyLiborSwapIsdaFixAm1(BaseModel):
    resource_name: Optional[Literal["JpyLiborSwapIsdaFixAm"]] = "JpyLiborSwapIsdaFixAm"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class JpyLiborSwapIsdaFixPm0(BaseModel):
    resource_name: Optional[Literal["JpyLiborSwapIsdaFixPm"]] = "JpyLiborSwapIsdaFixPm"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class JpyLiborSwapIsdaFixPm1(BaseModel):
    resource_name: Optional[Literal["JpyLiborSwapIsdaFixPm"]] = "JpyLiborSwapIsdaFixPm"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class UsdLiborSwapIsdaFixAm0(BaseModel):
    resource_name: Optional[Literal["UsdLiborSwapIsdaFixAm"]] = "UsdLiborSwapIsdaFixAm"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class UsdLiborSwapIsdaFixAm1(BaseModel):
    resource_name: Optional[Literal["UsdLiborSwapIsdaFixAm"]] = "UsdLiborSwapIsdaFixAm"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class UsdLiborSwapIsdaFixPm0(BaseModel):
    resource_name: Optional[Literal["UsdLiborSwapIsdaFixPm"]] = "UsdLiborSwapIsdaFixPm"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class UsdLiborSwapIsdaFixPm1(BaseModel):
    resource_name: Optional[Literal["UsdLiborSwapIsdaFixPm"]] = "UsdLiborSwapIsdaFixPm"
    tenor: Period
    h1: YieldTermStructureHandle
    h2: YieldTermStructureHandle


class BiborBase(BaseModel):
    resource_name: Optional[Literal["Bibor"]] = "Bibor"
    tenor: Period
    h: Optional[YieldTermStructureHandle] = None


class GaussianSimulatedAnnealing(BaseModel):
    resource_name: Optional[
        Literal["GaussianSimulatedAnnealing"]
    ] = "GaussianSimulatedAnnealing"
    sampler: SamplerGaussian
    probability: ProbabilityBoltzmannDownhill
    temperature: TemperatureExponential
    reannealing: Optional[ReannealingTrivial] = None
    startTemperature: Optional[float] = None
    endTemperature: Optional[float] = None
    reAnnealSteps: Optional[int] = None
    resetScheme: Optional[GaussianSimulatedAnnealingResetScheme] = None
    resetSteps: Optional[int] = None


class MirrorGaussianSimulatedAnnealing(BaseModel):
    resource_name: Optional[
        Literal["MirrorGaussianSimulatedAnnealing"]
    ] = "MirrorGaussianSimulatedAnnealing"
    sampler: SamplerMirrorGaussian
    probability: ProbabilityBoltzmannDownhill
    temperature: TemperatureExponential
    reannealing: Optional[ReannealingTrivial] = None
    startTemperature: Optional[float] = None
    endTemperature: Optional[float] = None
    reAnnealSteps: Optional[int] = None
    resetScheme: Optional[MirrorGaussianSimulatedAnnealingResetScheme] = None
    resetSteps: Optional[int] = None


class LogNormalSimulatedAnnealing(BaseModel):
    resource_name: Optional[
        Literal["LogNormalSimulatedAnnealing"]
    ] = "LogNormalSimulatedAnnealing"
    sampler: SamplerLogNormal
    probability: ProbabilityBoltzmannDownhill
    temperature: TemperatureExponential
    reannealing: Optional[ReannealingTrivial] = None
    startTemperature: Optional[float] = None
    endTemperature: Optional[float] = None
    reAnnealSteps: Optional[int] = None
    resetScheme: Optional[LogNormalSimulatedAnnealingResetScheme] = None
    resetSteps: Optional[int] = None


class ConstantOptionletVolatility0(BaseModel):
    resource_name: Optional[
        Literal["ConstantOptionletVolatility"]
    ] = "ConstantOptionletVolatility"
    referenceDate: Date
    cal: Calendar
    bdc: BusinessDayConvention
    volatility: Union[QuoteHandle, float]
    dayCounter: DayCounter
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class ConstantOptionletVolatility1(BaseModel):
    resource_name: Optional[
        Literal["ConstantOptionletVolatility"]
    ] = "ConstantOptionletVolatility"
    settlementDays: float
    cal: Calendar
    bdc: BusinessDayConvention
    volatility: Union[QuoteHandle, float]
    dayCounter: DayCounter
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class ConstantSwaptionVolatility0(BaseModel):
    resource_name: Optional[
        Literal["ConstantSwaptionVolatility"]
    ] = "ConstantSwaptionVolatility"
    settlementDays: float
    cal: Calendar
    bdc: BusinessDayConvention
    volatility: Union[float, QuoteHandle]
    dc: DayCounter
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class ConstantSwaptionVolatility1(BaseModel):
    resource_name: Optional[
        Literal["ConstantSwaptionVolatility"]
    ] = "ConstantSwaptionVolatility"
    referenceDate: Date
    cal: Calendar
    bdc: BusinessDayConvention
    volatility: Union[float, QuoteHandle]
    dc: DayCounter
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class SwaptionVolatilityMatrix0(BaseModel):
    resource_name: Optional[
        Literal["SwaptionVolatilityMatrix"]
    ] = "SwaptionVolatilityMatrix"
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    swapTenors: List[Period]
    vols: Matrix
    dayCounter: DayCounter
    flatExtrapolation: Optional[bool] = None
    type: Optional[VolatilityType] = None
    shifts: Optional[Matrix] = None


class SwaptionVolatilityMatrix1(BaseModel):
    resource_name: Optional[
        Literal["SwaptionVolatilityMatrix"]
    ] = "SwaptionVolatilityMatrix"
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    swapTenors: List[Period]
    vols: List[List[QuoteHandle]]
    dayCounter: DayCounter
    flatExtrapolation: Optional[bool] = None
    type: Optional[VolatilityType] = None
    shifts: Optional[List[List[float]]] = None


class SwaptionVolatilityMatrix2(BaseModel):
    resource_name: Optional[
        Literal["SwaptionVolatilityMatrix"]
    ] = "SwaptionVolatilityMatrix"
    referenceDate: Date
    calendar: Calendar
    bdc: BusinessDayConvention
    dates: List[Date]
    lengths: List[Period]
    vols: Matrix
    dayCounter: DayCounter
    flatExtrapolation: Optional[bool] = None
    type: Optional[VolatilityType] = None
    shifts: Optional[Matrix] = None


class SwaptionVolCube1(BaseModel):
    resource_name: Optional[Literal["SwaptionVolCube"]] = "SwaptionVolCube"
    atmVolStructure: SwaptionVolatilityStructureHandle
    optionTenors: List[Period]
    swapTenors: List[Period]
    strikeSpreads: List[float]
    volSpreads: List[List[QuoteHandle]]
    swapIndex: SwapIndex
    shortSwapIndex: SwapIndex
    vegaWeightedSmileFit: bool
    parametersGuess: List[List[QuoteHandle]]
    isParameterFixed: List[bool]
    isAtmCalibrated: bool
    endCriteria: Optional[EndCriteria] = None
    maxErrorTolerance: Optional[float] = None
    optMethod: Optional[OptimizationMethod] = None
    errorAccept: Optional[float] = None
    useMaxError: Optional[bool] = None
    maxGuesses: Optional[int] = None
    backwardFlat: Optional[bool] = None
    cutoffStrike: Optional[float] = None


class SwaptionVolCube2(BaseModel):
    resource_name: Optional[Literal["SwaptionVolCube"]] = "SwaptionVolCube"
    atmVolStructure: SwaptionVolatilityStructureHandle
    optionTenors: List[Period]
    swapTenors: List[Period]
    strikeSpreads: List[float]
    volSpreads: List[List[QuoteHandle]]
    swapIndex: SwapIndex
    shortSwapIndex: SwapIndex
    vegaWeightedSmileFit: bool


class FlatSmileSection0(BaseModel):
    resource_name: Optional[Literal["FlatSmileSection"]] = "FlatSmileSection"
    exerciseTime: float
    vol: float
    dc: DayCounter
    atmLevel: Optional[float] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class FlatSmileSection1(BaseModel):
    resource_name: Optional[Literal["FlatSmileSection"]] = "FlatSmileSection"
    d: Date
    vol: float
    dc: DayCounter
    referenceDate: Optional[Date] = None
    atmLevel: Optional[float] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class AndreasenHugeVolatilityInterpl(BaseModel):
    resource_name: Optional[
        Literal["AndreasenHugeVolatilityInterpl"]
    ] = "AndreasenHugeVolatilityInterpl"
    calibrationSet: AndreasenHugeVolatilityInterplCalibrationSet
    spot: QuoteHandle
    rTS: YieldTermStructureHandle
    qTS: YieldTermStructureHandle
    interpolationType: Optional[AndreasenHugeVolatilityInterplInterpolationType] = None
    calibrationType: Optional[AndreasenHugeVolatilityInterplCalibrationType] = None
    nGridPoints: Optional[int] = None
    minStrike: Optional[float] = None
    maxStrike: Optional[float] = None
    optimizationMethod: Optional[OptimizationMethod] = None
    endCriteria: Optional[EndCriteria] = None


class AndreasenHugeVolatilityAdapter(BaseModel):
    resource_name: Optional[
        Literal["AndreasenHugeVolatilityAdapter"]
    ] = "AndreasenHugeVolatilityAdapter"
    volInterpl: AndreasenHugeVolatilityInterpl
    eps: Optional[float] = None


class AndreasenHugeLocalVolAdapter(BaseModel):
    resource_name: Optional[
        Literal["AndreasenHugeLocalVolAdapter"]
    ] = "AndreasenHugeLocalVolAdapter"
    localVol: AndreasenHugeVolatilityInterpl


class CmsMarket(BaseModel):
    resource_name: Optional[Literal["CmsMarket"]] = "CmsMarket"
    swapLengths: List[Period]
    swapIndexes: List[SwapIndex]
    iborIndex: IborIndex
    bidAskSpreads: List[List[QuoteHandle]]
    pricers: List[CmsCouponPricer]
    discountingTS: YieldTermStructureHandle


class CmsMarketCalibration(BaseModel):
    resource_name: Optional[Literal["CmsMarketCalibration"]] = "CmsMarketCalibration"
    volCube: SwaptionVolatilityStructureHandle
    cmsMarket: CmsMarket
    weights: Matrix
    calibrationType: CmsMarketCalibrationCalibrationType


class StochasticProcessArray(BaseModel):
    resource_name: Optional[
        Literal["StochasticProcessArray"]
    ] = "StochasticProcessArray"
    array: List[StochasticProcess1D]
    correlation: Matrix


class ExtOUWithJumpsProcess(BaseModel):
    resource_name: Optional[Literal["ExtOUWithJumpsProcess"]] = "ExtOUWithJumpsProcess"
    process: ExtendedOrnsteinUhlenbeckProcess
    Y0: float
    beta: float
    jumpIntensity: float
    eta: float


class KlugeExtOUProcess(BaseModel):
    resource_name: Optional[Literal["KlugeExtOUProcess"]] = "KlugeExtOUProcess"
    rho: float
    kluge: ExtOUWithJumpsProcess
    extOU: ExtendedOrnsteinUhlenbeckProcess


class GJRGARCHProcess(BaseModel):
    resource_name: Optional[Literal["GJRGARCHProcess"]] = "GJRGARCHProcess"
    riskFreeRate: YieldTermStructureHandle
    dividendYield: YieldTermStructureHandle
    s0: QuoteHandle
    v0: float
    omega: float
    alpha: float
    beta: float
    gamma: float
    lambda_: float = Field(..., alias="lambda")
    daysPerYear: Optional[float] = None
    d: Optional[GJRGARCHProcessDiscretization] = None


class Schedule0(BaseModel):
    resource_name: Optional[Literal["Schedule"]] = "Schedule"
    effectiveDate: Optional[Date] = None
    terminationDate: Optional[Date] = None
    tenor: Optional[Period] = None
    calendar: Optional[Calendar] = None
    convention: Optional[BusinessDayConvention] = None
    terminationDateConvention: Optional[BusinessDayConvention] = None
    rule: Optional[DateGenerationRule] = None
    endOfMonth: Optional[bool] = None
    firstDate: Optional[Date] = None
    nextToLastDate: Optional[Date] = None


class Schedule1(BaseModel):
    resource_name: Optional[Literal["Schedule"]] = "Schedule"
    value: List[Date]
    calendar: Optional[Calendar] = None
    convention: Optional[BusinessDayConvention] = None
    terminationDateConvention: Optional[BusinessDayConvention] = None
    tenor: Optional[Period] = None
    rule: Optional[DateGenerationRule] = None
    endOfMonth: Optional[bool] = None
    isRegular: Optional[List[bool]] = None


class IborCoupon(BaseModel):
    resource_name: Optional[Literal["IborCoupon"]] = "IborCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: int
    index: IborIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class CappedFlooredIborCoupon(BaseModel):
    resource_name: Optional[
        Literal["CappedFlooredIborCoupon"]
    ] = "CappedFlooredIborCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: int
    index: IborIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    cap: Optional[float] = None
    floor: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class CmsCoupon(BaseModel):
    resource_name: Optional[Literal["CmsCoupon"]] = "CmsCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: int
    index: SwapIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class CmsSpreadCoupon(BaseModel):
    resource_name: Optional[Literal["CmsSpreadCoupon"]] = "CmsSpreadCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: float
    index: SwapSpreadIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class AnalyticHaganPricer(BaseModel):
    resource_name: Optional[Literal["AnalyticHaganPricer"]] = "AnalyticHaganPricer"
    v: SwaptionVolatilityStructureHandle
    model: GFunctionFactoryYieldCurveModel
    meanReversion: QuoteHandle


class NumericHaganPricer(BaseModel):
    resource_name: Optional[Literal["NumericHaganPricer"]] = "NumericHaganPricer"
    v: SwaptionVolatilityStructureHandle
    model: GFunctionFactoryYieldCurveModel
    meanReversion: QuoteHandle
    lowerLimit: Optional[float] = None
    upperLimit: Optional[float] = None
    precision: Optional[float] = None


class CappedFlooredCmsCoupon(BaseModel):
    resource_name: Optional[
        Literal["CappedFlooredCmsCoupon"]
    ] = "CappedFlooredCmsCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: float
    index: SwapIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    cap: Optional[float] = None
    floor: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class CappedFlooredCmsSpreadCoupon(BaseModel):
    resource_name: Optional[
        Literal["CappedFlooredCmsSpreadCoupon"]
    ] = "CappedFlooredCmsSpreadCoupon"
    paymentDate: Date
    nominal: float
    startDate: Date
    endDate: Date
    fixingDays: float
    index: SwapSpreadIndex
    gearing: Optional[float] = None
    spread: Optional[float] = None
    cap: Optional[float] = None
    floor: Optional[float] = None
    refPeriodStart: Optional[Date] = None
    refPeriodEnd: Optional[Date] = None
    dayCounter: Optional[DayCounter] = None
    isInArrears: Optional[bool] = None
    exCouponDate: Optional[Date] = None


class LinearTsrPricer(BaseModel):
    resource_name: Optional[Literal["LinearTsrPricer"]] = "LinearTsrPricer"
    swaptionVol: SwaptionVolatilityStructureHandle
    meanReversion: QuoteHandle
    couponDiscountCurve: Optional[YieldTermStructureHandle] = None
    settings: Optional[LinearTsrPricerSettings] = None


class LognormalCmsSpreadPricer(BaseModel):
    resource_name: Optional[
        Literal["LognormalCmsSpreadPricer"]
    ] = "LognormalCmsSpreadPricer"
    cmsPricer: CmsCouponPricer
    correlation: QuoteHandle
    couponDiscountCurve: Optional[YieldTermStructureHandle] = None
    IntegrationPoints: Optional[int] = None
    volatilityType: Optional[VolatilityType] = None
    shift1: Optional[float] = None
    shift2: Optional[float] = None


class SwaptionHelper0(BaseModel):
    resource_name: Optional[Literal["SwaptionHelper"]] = "SwaptionHelper"
    exerciseDate: Date
    endDate: Date
    volatility: QuoteHandle
    index: IborIndex
    fixedLegTenor: Period
    fixedLegDayCounter: DayCounter
    floatingLegDayCounter: DayCounter
    termStructure: YieldTermStructureHandle
    errorType: Optional[BlackCalibrationHelperCalibrationErrorType] = None
    strike: Optional[float] = None
    nominal: Optional[float] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class SwaptionHelper1(BaseModel):
    resource_name: Optional[Literal["SwaptionHelper"]] = "SwaptionHelper"
    exerciseDate: Date
    length: Period
    volatility: QuoteHandle
    index: IborIndex
    fixedLegTenor: Period
    fixedLegDayCounter: DayCounter
    floatingLegDayCounter: DayCounter
    termStructure: YieldTermStructureHandle
    errorType: Optional[BlackCalibrationHelperCalibrationErrorType] = None
    strike: Optional[float] = None
    nominal: Optional[float] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class SwaptionHelper2(BaseModel):
    resource_name: Optional[Literal["SwaptionHelper"]] = "SwaptionHelper"
    maturity: Period
    length: Period
    volatility: QuoteHandle
    index: IborIndex
    fixedLegTenor: Period
    fixedLegDayCounter: DayCounter
    floatingLegDayCounter: DayCounter
    termStructure: YieldTermStructureHandle
    errorType: Optional[BlackCalibrationHelperCalibrationErrorType] = None
    strike: Optional[float] = None
    nominal: Optional[float] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class CapHelper(BaseModel):
    resource_name: Optional[Literal["CapHelper"]] = "CapHelper"
    length: Period
    volatility: QuoteHandle
    index: IborIndex
    fixedLegFrequency: float
    fixedLegDayCounter: DayCounter
    includeFirstSwaplet: bool
    termStructure: YieldTermStructureHandle
    errorType: Optional[BlackCalibrationHelperCalibrationErrorType] = None
    type: Optional[VolatilityType] = None
    shift: Optional[float] = None


class HestonModelHelper(BaseModel):
    resource_name: Optional[Literal["HestonModelHelper"]] = "HestonModelHelper"
    maturity: Period
    calendar: Calendar
    s0: float
    strikePrice: float
    volatility: QuoteHandle
    riskFreeRate: YieldTermStructureHandle
    dividendYield: YieldTermStructureHandle
    errorType: Optional[BlackCalibrationHelperCalibrationErrorType] = None


class VanillaOptionBase(BaseModel):
    resource_name: Optional[Literal["VanillaOption"]] = "VanillaOption"
    payoff: StrikedTypePayoff
    exercise: Exercise


class EuropeanOption(BaseModel):
    resource_name: Optional[Literal["EuropeanOption"]] = "EuropeanOption"
    payoff: StrikedTypePayoff
    exercise: Exercise


class ForwardVanillaOptionBase(BaseModel):
    resource_name: Optional[Literal["ForwardVanillaOption"]] = "ForwardVanillaOption"
    moneyness: float
    resetDate: Date
    payoff: StrikedTypePayoff
    exercise: Exercise


class QuantoVanillaOption(BaseModel):
    resource_name: Optional[Literal["QuantoVanillaOption"]] = "QuantoVanillaOption"
    payoff: StrikedTypePayoff
    exercise: Exercise


class QuantoForwardVanillaOption(BaseModel):
    resource_name: Optional[
        Literal["QuantoForwardVanillaOption"]
    ] = "QuantoForwardVanillaOption"
    moneyness: float
    resetDate: Date
    payoff: StrikedTypePayoff
    exercise: Exercise


class AnalyticHestonEngineIntegration0(BaseModel):
    resource_name: Optional[
        Literal["AnalyticHestonEngineIntegration"]
    ] = "AnalyticHestonEngineIntegration"
    intAlgo: AnalyticHestonEngineIntegrationAlgorithm
    quadrature: GaussianQuadrature


class AnalyticHestonEngineIntegration1(BaseModel):
    resource_name: Optional[
        Literal["AnalyticHestonEngineIntegration"]
    ] = "AnalyticHestonEngineIntegration"
    intAlgo: AnalyticHestonEngineIntegrationAlgorithm
    integrator: Integrator


AnalyticHestonEngineIntegration = Union[
    AnalyticHestonEngineIntegration0, AnalyticHestonEngineIntegration1
]


class AnalyticPTDHestonEngine0(BaseModel):
    resource_name: Optional[
        Literal["AnalyticPTDHestonEngine"]
    ] = "AnalyticPTDHestonEngine"
    model: PiecewiseTimeDependentHestonModel
    cpxLog: AnalyticPTDHestonEngineComplexLogFormula
    itg: AnalyticPTDHestonEngineIntegration
    andersenPiterbargEpsilon: Optional[float] = None


class DividendVanillaOption(BaseModel):
    resource_name: Optional[Literal["DividendVanillaOption"]] = "DividendVanillaOption"
    payoff: StrikedTypePayoff
    exercise: Exercise
    dividendDates: List[Date]
    dividends: List[float]


class BarrierOption(BaseModel):
    resource_name: Optional[Literal["BarrierOption"]] = "BarrierOption"
    barrierType: BarrierType
    barrier: float
    rebate: float
    payoff: StrikedTypePayoff
    exercise: Exercise


class FdmSchemeDesc(BaseModel):
    resource_name: Optional[Literal["FdmSchemeDesc"]] = "FdmSchemeDesc"
    type: FdmSchemeDescFdmSchemeType
    theta: float
    mu: float


class FdBlackScholesVanillaEngine0(BaseModel):
    resource_name: Optional[
        Literal["FdBlackScholesVanillaEngine"]
    ] = "FdBlackScholesVanillaEngine"
    value: GeneralizedBlackScholesProcess
    quantoHelper: FdmQuantoHelper
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[float] = None
    cashDividendModel: Optional[FdBlackScholesVanillaEngineCashDividendModel] = None


class FdBlackScholesVanillaEngine1(BaseModel):
    resource_name: Optional[
        Literal["FdBlackScholesVanillaEngine"]
    ] = "FdBlackScholesVanillaEngine"
    process: GeneralizedBlackScholesProcess
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[float] = None
    cashDividendModel: Optional[FdBlackScholesVanillaEngineCashDividendModel] = None


class FdOrnsteinUhlenbeckVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["FdOrnsteinUhlenbeckVanillaEngine"]
    ] = "FdOrnsteinUhlenbeckVanillaEngine"
    value: OrnsteinUhlenbeckProcess
    rTS: YieldTermStructure
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    epsilon: Optional[float] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class FdBatesVanillaEngine(BaseModel):
    resource_name: Optional[Literal["FdBatesVanillaEngine"]] = "FdBatesVanillaEngine"
    model: BatesModel
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    vGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class FdHestonVanillaEngine0(BaseModel):
    resource_name: Optional[Literal["FdHestonVanillaEngine"]] = "FdHestonVanillaEngine"
    model: HestonModel
    quantoHelper: FdmQuantoHelper
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    vGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class FdHestonVanillaEngine1(BaseModel):
    resource_name: Optional[Literal["FdHestonVanillaEngine"]] = "FdHestonVanillaEngine"
    model: HestonModel
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    vGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class FdCEVVanillaEngine(BaseModel):
    resource_name: Optional[Literal["FdCEVVanillaEngine"]] = "FdCEVVanillaEngine"
    f0: float
    alpha: float
    beta: float
    rTS: YieldTermStructureHandle
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    scalingFactor: Optional[float] = None
    eps: Optional[float] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class FdSabrVanillaEngine(BaseModel):
    resource_name: Optional[Literal["FdSabrVanillaEngine"]] = "FdSabrVanillaEngine"
    f0: float
    alpha: float
    beta: float
    nu: float
    rho: float
    rTS: YieldTermStructureHandle
    tGrid: Optional[int] = None
    fGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    scalingFactor: Optional[float] = None
    eps: Optional[float] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class FdBlackScholesBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["FdBlackScholesBarrierEngine"]
    ] = "FdBlackScholesBarrierEngine"
    process: GeneralizedBlackScholesProcess
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[float] = None


class ContinuousAveragingAsianOption(BaseModel):
    resource_name: Optional[
        Literal["ContinuousAveragingAsianOption"]
    ] = "ContinuousAveragingAsianOption"
    averageType: AverageType
    payoff: StrikedTypePayoff
    exercise: Exercise


class DiscreteAveragingAsianOption(BaseModel):
    resource_name: Optional[
        Literal["DiscreteAveragingAsianOption"]
    ] = "DiscreteAveragingAsianOption"
    averageType: AverageType
    runningAccumulator: float
    pastFixings: int
    fixingDates: List[Date]
    payoff: StrikedTypePayoff
    exercise: Exercise


class DoubleBarrierOptionBase(BaseModel):
    resource_name: Optional[Literal["DoubleBarrierOption"]] = "DoubleBarrierOption"
    barrierType: DoubleBarrierType
    barrier_lo: float
    barrier_hi: float
    rebate: float
    payoff: StrikedTypePayoff
    exercise: Exercise


class QuantoDoubleBarrierOption(BaseModel):
    resource_name: Optional[
        Literal["QuantoDoubleBarrierOption"]
    ] = "QuantoDoubleBarrierOption"
    barrierType: DoubleBarrierType
    barrier_lo: float
    barrier_hi: float
    rebate: float
    payoff: StrikedTypePayoff
    exercise: Exercise


class DeltaVolQuote0(BaseModel):
    resource_name: Optional[Literal["DeltaVolQuote"]] = "DeltaVolQuote"
    delta: float
    vol: QuoteHandle
    maturity: float
    deltaType: DeltaVolQuoteDeltaType


class DeltaVolQuote1(BaseModel):
    resource_name: Optional[Literal["DeltaVolQuote"]] = "DeltaVolQuote"
    vol: QuoteHandle
    deltaType: DeltaVolQuoteDeltaType
    maturity: float
    atmType: DeltaVolQuoteAtmType


class DeltaVolQuoteHandle(BaseModel):
    resource_name: Optional[Literal["DeltaVolQuoteHandle"]] = "DeltaVolQuoteHandle"
    value: Optional[DeltaVolQuote] = None


class RelinkableDeltaVolQuoteHandle(BaseModel):
    resource_name: Optional[
        Literal["RelinkableDeltaVolQuoteHandle"]
    ] = "RelinkableDeltaVolQuoteHandle"
    value: Optional[DeltaVolQuote] = None


class VannaVolgaBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["VannaVolgaBarrierEngine"]
    ] = "VannaVolgaBarrierEngine"
    atmVol: DeltaVolQuoteHandle
    vol25Put: DeltaVolQuoteHandle
    vol25Call: DeltaVolQuoteHandle
    spotFX: QuoteHandle
    domesticTS: YieldTermStructureHandle
    foreignTS: YieldTermStructureHandle
    adaptVanDelta: Optional[bool] = None
    bsPriceWithSmile: Optional[float] = None


class FdSimpleBSSwingEngine(BaseModel):
    resource_name: Optional[Literal["FdSimpleBSSwingEngine"]] = "FdSimpleBSSwingEngine"
    process: GeneralizedBlackScholesProcess
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class GJRGARCHModel(BaseModel):
    resource_name: Optional[Literal["GJRGARCHModel"]] = "GJRGARCHModel"
    process: GJRGARCHProcess


class AnalyticGJRGARCHEngine(BaseModel):
    resource_name: Optional[
        Literal["AnalyticGJRGARCHEngine"]
    ] = "AnalyticGJRGARCHEngine"
    process: GJRGARCHModel


class PlainVanillaPayoff(BaseModel):
    resource_name: Optional[Literal["PlainVanillaPayoff"]] = "PlainVanillaPayoff"
    type: OptionType
    strike: float


class PercentageStrikePayoff(BaseModel):
    resource_name: Optional[
        Literal["PercentageStrikePayoff"]
    ] = "PercentageStrikePayoff"
    type: OptionType
    moneyness: float


class CashOrNothingPayoff(BaseModel):
    resource_name: Optional[Literal["CashOrNothingPayoff"]] = "CashOrNothingPayoff"
    type: OptionType
    strike: float
    payoff: float


class AssetOrNothingPayoff(BaseModel):
    resource_name: Optional[Literal["AssetOrNothingPayoff"]] = "AssetOrNothingPayoff"
    type: OptionType
    strike: float


class SuperSharePayoff(BaseModel):
    resource_name: Optional[Literal["SuperSharePayoff"]] = "SuperSharePayoff"
    type: OptionType
    strike: float
    increment: float


class GapPayoff(BaseModel):
    resource_name: Optional[Literal["GapPayoff"]] = "GapPayoff"
    type: OptionType
    strike: float
    strikePayoff: float


class VanillaForwardPayoff(BaseModel):
    resource_name: Optional[Literal["VanillaForwardPayoff"]] = "VanillaForwardPayoff"
    type: OptionType
    strike: float


class BasketOption(BaseModel):
    resource_name: Optional[Literal["BasketOption"]] = "BasketOption"
    payoff: BasketPayoff
    exercise: Exercise


class Fd2dBlackScholesVanillaEngine(BaseModel):
    resource_name: Optional[
        Literal["Fd2dBlackScholesVanillaEngine"]
    ] = "Fd2dBlackScholesVanillaEngine"
    p1: GeneralizedBlackScholesProcess
    p2: GeneralizedBlackScholesProcess
    correlation: float
    xGrid: Optional[int] = None
    yGrid: Optional[int] = None
    tGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    localVol: Optional[bool] = None
    illegalLocalVolOverwrite: Optional[float] = None


class EverestOption(BaseModel):
    resource_name: Optional[Literal["EverestOption"]] = "EverestOption"
    notional: float
    guarantee: float
    exercise: Exercise


class BlackDeltaCalculator(BaseModel):
    resource_name: Optional[Literal["BlackDeltaCalculator"]] = "BlackDeltaCalculator"
    ot: OptionType
    dt: DeltaVolQuoteDeltaType
    spot: float
    dDiscount: DiscountFactor
    fDiscount: DiscountFactor
    stDev: float


class CallabilityPrice(BaseModel):
    resource_name: Optional[Literal["CallabilityPrice"]] = "CallabilityPrice"
    amount: float
    type: CallabilityPriceType


class CallabilityBase(BaseModel):
    resource_name: Optional[Literal["Callability"]] = "Callability"
    price: CallabilityPrice
    type: CallabilityType
    date: Date


class SoftCallability(BaseModel):
    resource_name: Optional[Literal["SoftCallability"]] = "SoftCallability"
    price: CallabilityPrice
    date: Date
    trigger: float


class VanillaSwap(BaseModel):
    resource_name: Optional[Literal["VanillaSwap"]] = "VanillaSwap"
    type: VanillaSwapType
    nominal: float
    fixedSchedule: Schedule
    fixedRate: float
    fixedDayCount: DayCounter
    floatSchedule: Schedule
    index: IborIndex
    spread: float
    floatingDayCount: DayCounter


class MakeVanillaSwap(BaseModel):
    resource_name: Optional[Literal["MakeVanillaSwap"]] = "MakeVanillaSwap"
    swapTenor: Period
    index: IborIndex
    fixedRate: float
    forwardStart: Period


class NonstandardSwap(BaseModel):
    resource_name: Optional[Literal["NonstandardSwap"]] = "NonstandardSwap"
    type: VanillaSwapType
    fixedNominal: List[float]
    floatingNominal: List[float]
    fixedSchedule: Schedule
    fixedRate: List[float]
    fixedDayCount: DayCounter
    floatSchedule: Schedule
    index: IborIndex
    gearing: List[float]
    spread: List[float]
    floatDayCount: DayCounter
    intermediateCapitalExchange: Optional[bool] = None
    finalCapitalExchange: Optional[bool] = None
    paymentConvention: Optional[BusinessDayConvention] = None


class FloatFloatSwap(BaseModel):
    resource_name: Optional[Literal["FloatFloatSwap"]] = "FloatFloatSwap"
    type: VanillaSwapType
    nominal1: List[float]
    nominal2: List[float]
    schedule1: Schedule
    index1: InterestRateIndex
    dayCount1: DayCounter
    schedule2: Schedule
    index2: InterestRateIndex
    dayCount2: DayCounter
    intermediateCapitalExchange: Optional[bool] = None
    finalCapitalExchange: Optional[bool] = None
    gearing1: Optional[List[float]] = None
    spread1: Optional[List[float]] = None
    cappedRate1: Optional[List[float]] = None
    flooredRate1: Optional[List[float]] = None
    gearing2: Optional[List[float]] = None
    spread2: Optional[List[float]] = None
    cappedRate2: Optional[List[float]] = None
    flooredRate2: Optional[List[float]] = None
    paymentConvention1: Optional[BusinessDayConvention] = None
    paymentConvention2: Optional[BusinessDayConvention] = None


class OvernightIndexedSwap0(BaseModel):
    resource_name: Optional[Literal["OvernightIndexedSwap"]] = "OvernightIndexedSwap"
    type: OvernightIndexedSwapType
    nominals: List[float]
    schedule: Schedule
    fixedRate: float
    fixedDC: DayCounter
    index: OvernightIndex
    spread: Optional[float] = None
    paymentLag: Optional[float] = None
    paymentAdjustment: Optional[BusinessDayConvention] = None
    paymentCalendar: Optional[Calendar] = None
    telescopicValueDates: Optional[bool] = None


class OvernightIndexedSwap1(BaseModel):
    resource_name: Optional[Literal["OvernightIndexedSwap"]] = "OvernightIndexedSwap"
    type: OvernightIndexedSwapType
    nominal: float
    schedule: Schedule
    fixedRate: float
    fixedDC: DayCounter
    index: OvernightIndex
    spread: Optional[float] = None
    paymentLag: Optional[float] = None
    paymentAdjustment: Optional[BusinessDayConvention] = None
    paymentCalendar: Optional[Calendar] = None
    telescopicValueDates: Optional[bool] = None


class MakeOIS(BaseModel):
    resource_name: Optional[Literal["MakeOIS"]] = "MakeOIS"
    swapTenor: Period
    overnightIndex: OvernightIndex
    fixedRate: Optional[float] = None
    fwdStart: Optional[Period] = None


class OvernightIndexedSwapIndex(BaseModel):
    resource_name: Optional[
        Literal["OvernightIndexedSwapIndex"]
    ] = "OvernightIndexedSwapIndex"
    familyName: str
    tenor: Period
    settlementDays: float
    currency: Currency
    overnightIndex: OvernightIndex
    telescopicValueDates: Optional[bool] = None


class ZeroInflationIndexBase(BaseModel):
    resource_name: Optional[Literal["ZeroInflationIndex"]] = "ZeroInflationIndex"
    familyName: str
    region: Region
    revised: bool
    interpolated: bool
    frequency: float
    availabilityLag: Period
    currency: Currency
    h: Optional[ZeroInflationTermStructureHandle] = None


class ZeroCouponInflationSwap(BaseModel):
    resource_name: Optional[
        Literal["ZeroCouponInflationSwap"]
    ] = "ZeroCouponInflationSwap"
    type: ZeroCouponInflationSwapType
    nominal: float
    start: Date
    maturity: Date
    calendar: Calendar
    convention: BusinessDayConvention
    dayCounter: DayCounter
    fixedRate: float
    index: ZeroInflationIndex
    lag: Period
    adjustInfObsDates: Optional[bool] = None
    infCalendar: Optional[Calendar] = None
    infConvention: Optional[BusinessDayConvention] = None


class YearOnYearInflationSwap(BaseModel):
    resource_name: Optional[
        Literal["YearOnYearInflationSwap"]
    ] = "YearOnYearInflationSwap"
    type: YearOnYearInflationSwapType
    nominal: float
    fixedSchedule: Schedule
    fixedRate: float
    fixedDayCounter: DayCounter
    yoySchedule: Schedule
    index: YoYInflationIndex
    lag: Period
    spread: float
    yoyDayCounter: DayCounter
    paymentCalendar: Calendar
    paymentConvention: Optional[BusinessDayConvention] = None


class CPISwap(BaseModel):
    resource_name: Optional[Literal["CPISwap"]] = "CPISwap"
    type: CPISwapType
    nominal: float
    subtractInflationNominal: bool
    spread: float
    floatDayCount: DayCounter
    floatSchedule: Schedule
    floatRoll: BusinessDayConvention
    fixingDays: float
    floatIndex: IborIndex
    fixedRate: float
    baseCPI: float
    fixedDayCount: DayCounter
    fixedSchedule: Schedule
    fixedRoll: BusinessDayConvention
    observationLag: Period
    fixedIndex: ZeroInflationIndex
    observationInterpolation: Optional[CPIInterpolationType] = None
    inflationNominal: Optional[float] = None


class FdG2SwaptionEngine(BaseModel):
    resource_name: Optional[Literal["FdG2SwaptionEngine"]] = "FdG2SwaptionEngine"
    model: G2
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    yGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    invEps: Optional[float] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class FdHullWhiteSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["FdHullWhiteSwaptionEngine"]
    ] = "FdHullWhiteSwaptionEngine"
    model: HullWhite
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    invEps: Optional[float] = None
    schemeDesc: Optional[FdmSchemeDesc] = None


class Bond0(BaseModel):
    resource_name: Optional[Literal["Bond"]] = "Bond"
    settlementDays: float
    calendar: Calendar
    issueDate: Optional[Date] = None
    coupons: Optional[Leg] = None


class Bond1(BaseModel):
    resource_name: Optional[Literal["Bond"]] = "Bond"
    settlementDays: float
    calendar: Calendar
    faceAmount: float
    maturityDate: Date
    issueDate: Optional[Date] = None
    cashflows: Optional[Leg] = None


class ZeroCouponBond(BaseModel):
    resource_name: Optional[Literal["ZeroCouponBond"]] = "ZeroCouponBond"
    settlementDays: float
    calendar: Calendar
    faceAmount: float
    maturityDate: Date
    paymentConvention: Optional[BusinessDayConvention] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None


class FixedRateBond0(BaseModel):
    resource_name: Optional[Literal["FixedRateBond"]] = "FixedRateBond"
    settlementDays: int
    couponCalendar: Calendar
    faceAmount: float
    startDate: Date
    maturityDate: Date
    tenor: Period
    coupons: List[float]
    accrualDayCounter: DayCounter
    accrualConvention: Optional[BusinessDayConvention] = None
    paymentConvention: Optional[BusinessDayConvention] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None
    stubDate: Optional[Date] = None
    rule: Optional[DateGenerationRule] = None
    endOfMonth: Optional[bool] = None
    paymentCalendar: Optional[Calendar] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None


class FixedRateBond1(BaseModel):
    resource_name: Optional[Literal["FixedRateBond"]] = "FixedRateBond"
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    coupons: List[InterestRate]
    paymentConvention: Optional[BusinessDayConvention] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None
    paymentCalendar: Optional[Calendar] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None


class FixedRateBond2(BaseModel):
    resource_name: Optional[Literal["FixedRateBond"]] = "FixedRateBond"
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    coupons: List[float]
    paymentDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None
    paymentCalendar: Optional[Calendar] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None


class AmortizingFixedRateBond0(BaseModel):
    resource_name: Optional[
        Literal["AmortizingFixedRateBond"]
    ] = "AmortizingFixedRateBond"
    settlementDays: int
    paymentCalendar: Calendar
    faceAmount: float
    startDate: Date
    bondTenor: Period
    sinkingFrequency: float
    coupon: float
    accrualDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    issueDate: Optional[Date] = None


class AmortizingFixedRateBond1(BaseModel):
    resource_name: Optional[
        Literal["AmortizingFixedRateBond"]
    ] = "AmortizingFixedRateBond"
    settlementDays: int
    notionals: List[float]
    schedule: Schedule
    coupons: List[float]
    accrualDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    issueDate: Optional[Date] = None


class AmortizingFloatingRateBond(BaseModel):
    resource_name: Optional[
        Literal["AmortizingFloatingRateBond"]
    ] = "AmortizingFloatingRateBond"
    settlementDays: int
    notional: List[float]
    schedule: Schedule
    index: IborIndex
    accrualDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    fixingDays: Optional[int] = None
    gearings: Optional[List[float]] = None
    spreads: Optional[List[float]] = None
    caps: Optional[List[float]] = None
    floors: Optional[List[float]] = None
    inArrears: Optional[bool] = None
    issueDate: Optional[Date] = None


class FloatingRateBond(BaseModel):
    resource_name: Optional[Literal["FloatingRateBond"]] = "FloatingRateBond"
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    index: IborIndex
    paymentDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    fixingDays: Optional[int] = None
    gearings: Optional[List[float]] = None
    spreads: Optional[List[float]] = None
    caps: Optional[List[float]] = None
    floors: Optional[List[float]] = None
    inArrears: Optional[bool] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None


class CmsRateBond(BaseModel):
    resource_name: Optional[Literal["CmsRateBond"]] = "CmsRateBond"
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    index: SwapIndex
    paymentDayCounter: DayCounter
    paymentConvention: BusinessDayConvention
    fixingDays: float
    gearings: List[float]
    spreads: List[float]
    caps: List[float]
    floors: List[float]
    inArrears: Optional[bool] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None


class CallableFixedRateBond(BaseModel):
    resource_name: Optional[Literal["CallableFixedRateBond"]] = "CallableFixedRateBond"
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    coupons: List[float]
    accrualDayCounter: DayCounter
    paymentConvention: BusinessDayConvention
    redemption: float
    issueDate: Date
    putCallSchedule: List[Callability]


class CPIBond(BaseModel):
    resource_name: Optional[Literal["CPIBond"]] = "CPIBond"
    settlementDays: float
    faceAmount: float
    growthOnly: bool
    baseCPI: float
    observationLag: Period
    cpiIndex: ZeroInflationIndex
    observationInterpolation: CPIInterpolationType
    schedule: Schedule
    coupons: List[float]
    accrualDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    issueDate: Optional[Date] = None
    paymentCalendar: Optional[Calendar] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None


class ConvertibleZeroCouponBond(BaseModel):
    resource_name: Optional[
        Literal["ConvertibleZeroCouponBond"]
    ] = "ConvertibleZeroCouponBond"
    exercise: Exercise
    conversionRatio: float
    dividends: List[Dividend]
    callability: List[Callability]
    creditSpread: QuoteHandle
    issueDate: Date
    settlementDays: int
    dayCounter: DayCounter
    schedule: Schedule
    redemption: Optional[float] = None


class ConvertibleFixedCouponBond(BaseModel):
    resource_name: Optional[
        Literal["ConvertibleFixedCouponBond"]
    ] = "ConvertibleFixedCouponBond"
    exercise: Exercise
    conversionRatio: float
    dividends: List[Dividend]
    callability: List[Callability]
    creditSpread: QuoteHandle
    issueDate: Date
    settlementDays: int
    coupons: List[float]
    dayCounter: DayCounter
    schedule: Schedule
    redemption: Optional[float] = None


class ConvertibleFloatingRateBond(BaseModel):
    resource_name: Optional[
        Literal["ConvertibleFloatingRateBond"]
    ] = "ConvertibleFloatingRateBond"
    exercise: Exercise
    conversionRatio: float
    dividends: List[Dividend]
    callability: List[Callability]
    creditSpread: QuoteHandle
    issueDate: Date
    settlementDays: int
    index: IborIndex
    fixingDays: int
    spreads: List[float]
    dayCounter: DayCounter
    schedule: Schedule
    redemption: Optional[float] = None


class DepositRateHelper0(BaseModel):
    resource_name: Optional[Literal["DepositRateHelper"]] = "DepositRateHelper"
    rate: Union[QuoteHandle, float]
    index: IborIndex


class DepositRateHelper1(BaseModel):
    resource_name: Optional[Literal["DepositRateHelper"]] = "DepositRateHelper"
    rate: Union[QuoteHandle, float]
    tenor: Period
    fixingDays: float
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    dayCounter: DayCounter


class FraRateHelper0(BaseModel):
    resource_name: Optional[Literal["FraRateHelper"]] = "FraRateHelper"
    rate: Union[float, QuoteHandle]
    monthsToStart: float
    monthsToEnd: float
    fixingDays: float
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    dayCounter: DayCounter
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None
    useIndexedCoupon: Optional[bool] = None


class FraRateHelper1(BaseModel):
    resource_name: Optional[Literal["FraRateHelper"]] = "FraRateHelper"
    rate: Union[float, QuoteHandle]
    monthsToStart: float
    index: IborIndex
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None
    useIndexedCoupon: Optional[bool] = None


class FraRateHelper2(BaseModel):
    resource_name: Optional[Literal["FraRateHelper"]] = "FraRateHelper"
    rate: Union[float, QuoteHandle]
    immOffsetStart: float
    immOffsetEnd: float
    iborIndex: IborIndex
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None
    useIndexedCoupon: Optional[bool] = None


class FuturesRateHelper0(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: float
    iborStartDate: Date
    index: IborIndex
    convexityAdjustment: Optional[float] = None
    type: Optional[FuturesType] = None


class FuturesRateHelper1(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: QuoteHandle
    iborStartDate: Date
    index: IborIndex
    convexityAdjustment: Optional[QuoteHandle] = None
    type: Optional[FuturesType] = None


class FuturesRateHelper2(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: float
    iborStartDate: Date
    iborEndDate: Date
    dayCounter: DayCounter
    convexityAdjustment: Optional[float] = None
    type: Optional[FuturesType] = None


class FuturesRateHelper3(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: QuoteHandle
    iborStartDate: Date
    iborEndDate: Date
    dayCounter: DayCounter
    convexityAdjustment: Optional[QuoteHandle] = None
    type: Optional[FuturesType] = None


class FuturesRateHelper4(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: float
    iborStartDate: Date
    nMonths: float
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    dayCounter: DayCounter
    convexityAdjustment: Optional[float] = None
    type: Optional[FuturesType] = None


class FuturesRateHelper5(BaseModel):
    resource_name: Optional[Literal["FuturesRateHelper"]] = "FuturesRateHelper"
    price: QuoteHandle
    iborStartDate: Date
    nMonths: float
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    dayCounter: DayCounter
    convexityAdjustment: Optional[QuoteHandle] = None
    type: Optional[FuturesType] = None


class SwapRateHelper0(BaseModel):
    resource_name: Optional[Literal["SwapRateHelper"]] = "SwapRateHelper"
    rate: Union[float, QuoteHandle]
    tenor: Period
    calendar: Calendar
    fixedFrequency: float
    fixedConvention: BusinessDayConvention
    fixedDayCount: DayCounter
    index: IborIndex
    spread: Optional[QuoteHandle] = None
    fwdStart: Optional[Period] = None
    discountingCurve: Optional[YieldTermStructureHandle] = None
    settlementDays: Optional[float] = None
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None


class SwapRateHelper1(BaseModel):
    resource_name: Optional[Literal["SwapRateHelper"]] = "SwapRateHelper"
    rate: Union[float, QuoteHandle]
    index: SwapIndex
    spread: Optional[QuoteHandle] = None
    fwdStart: Optional[Period] = None
    discountingCurve: Optional[YieldTermStructureHandle] = None
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None


class BondHelperBase(BaseModel):
    resource_name: Optional[Literal["BondHelper"]] = "BondHelper"
    cleanPrice: QuoteHandle
    bond: Bond
    useCleanPrice: Optional[bool] = None


class FixedRateBondHelper(BaseModel):
    resource_name: Optional[Literal["FixedRateBondHelper"]] = "FixedRateBondHelper"
    cleanPrice: QuoteHandle
    settlementDays: int
    faceAmount: float
    schedule: Schedule
    coupons: List[float]
    paymentDayCounter: DayCounter
    paymentConvention: Optional[BusinessDayConvention] = None
    redemption: Optional[float] = None
    issueDate: Optional[Date] = None
    paymentCalendar: Optional[Calendar] = None
    exCouponPeriod: Optional[Period] = None
    exCouponCalendar: Optional[Calendar] = None
    exCouponConvention: Optional[BusinessDayConvention] = None
    exCouponEndOfMonth: Optional[bool] = None
    useCleanPrice: Optional[bool] = None


class OISRateHelper(BaseModel):
    resource_name: Optional[Literal["OISRateHelper"]] = "OISRateHelper"
    settlementDays: float
    tenor: Period
    rate: QuoteHandle
    index: OvernightIndex
    discountingCurve: Optional[YieldTermStructureHandle] = None
    telescopicValueDates: Optional[bool] = None
    paymentLag: Optional[float] = None
    paymentConvention: Optional[BusinessDayConvention] = None
    paymentFrequency: Optional[float] = None
    paymentCalendar: Optional[Calendar] = None
    forwardStart: Optional[Period] = None
    overnightSpread: Optional[float] = None
    pillar: Optional[PillarChoice] = None
    customPillarDate: Optional[Date] = None


class FxSwapRateHelper(BaseModel):
    resource_name: Optional[Literal["FxSwapRateHelper"]] = "FxSwapRateHelper"
    fwdPoint: QuoteHandle
    spotFx: QuoteHandle
    tenor: Period
    fixingDays: float
    calendar: Calendar
    convention: BusinessDayConvention
    endOfMonth: bool
    isFxBaseCurrencyCollateralCurrency: bool
    collateralCurve: YieldTermStructureHandle
    tradingCalendar: Optional[Calendar] = None


class OvernightIndexFutureRateHelperBase(BaseModel):
    resource_name: Optional[
        Literal["OvernightIndexFutureRateHelper"]
    ] = "OvernightIndexFutureRateHelper"
    price: QuoteHandle
    valueDate: Date
    maturityDate: Date
    index: OvernightIndex
    convexityAdjustment: Optional[QuoteHandle] = None
    type: Optional[OvernightIndexFutureNettingType] = None


class SofrFutureRateHelper0(BaseModel):
    resource_name: Optional[Literal["SofrFutureRateHelper"]] = "SofrFutureRateHelper"
    price: float
    referenceMonth: conint(ge=1, le=12)  # type: ignore
    referenceYear: conint(ge=1900, le=2999)  # type: ignore
    referenceFreq: float
    index: OvernightIndex
    convexityAdjustment: Optional[float] = None
    type: Optional[OvernightIndexFutureNettingType] = None


class SofrFutureRateHelper1(BaseModel):
    resource_name: Optional[Literal["SofrFutureRateHelper"]] = "SofrFutureRateHelper"
    price: QuoteHandle
    referenceMonth: conint(ge=1, le=12)  # type: ignore
    referenceYear: conint(ge=1900, le=2999)  # type: ignore
    referenceFreq: float
    index: OvernightIndex
    convexityAdjustment: Optional[QuoteHandle] = None
    type: Optional[OvernightIndexFutureNettingType] = None


class SpreadCdsHelper(BaseModel):
    resource_name: Optional[Literal["SpreadCdsHelper"]] = "SpreadCdsHelper"
    spread: Union[float, QuoteHandle]
    tenor: Period
    settlementDays: int
    calendar: Calendar
    frequency: float
    convention: BusinessDayConvention
    rule: DateGenerationRule
    dayCounter: DayCounter
    recoveryRate: float
    discountCurve: YieldTermStructureHandle
    settlesAccrual: Optional[bool] = None
    paysAtDefaultTime: Optional[bool] = None


class UpfrontCdsHelper(BaseModel):
    resource_name: Optional[Literal["UpfrontCdsHelper"]] = "UpfrontCdsHelper"
    upfront: Union[float, QuoteHandle]
    spread: float
    tenor: Period
    settlementDays: int
    calendar: Calendar
    frequency: float
    convention: BusinessDayConvention
    rule: DateGenerationRule
    dayCounter: DayCounter
    recoveryRate: float
    discountCurve: YieldTermStructureHandle
    upfrontSettlementDays: Optional[float] = None
    settlesAccrual: Optional[bool] = None
    paysAtDefaultTime: Optional[bool] = None


class FaceValueAccrualClaim(BaseModel):
    resource_name: Optional[Literal["FaceValueAccrualClaim"]] = "FaceValueAccrualClaim"
    bond: Bond


class CreditDefaultSwap0(BaseModel):
    resource_name: Optional[Literal["CreditDefaultSwap"]] = "CreditDefaultSwap"
    side: ProtectionSide
    notional: float
    upfront: float
    spread: float
    schedule: Schedule
    paymentConvention: BusinessDayConvention
    dayCounter: DayCounter
    settlesAccrual: Optional[bool] = None
    paysAtDefaultTime: Optional[bool] = None
    protectionStart: Optional[Date] = None
    upfrontDate: Optional[Date] = None
    claim: Optional[Claim] = None
    lastPeriodDayCounter: Optional[DayCounter] = None
    rebatesAccrual: Optional[bool] = None


class CreditDefaultSwap1(BaseModel):
    resource_name: Optional[Literal["CreditDefaultSwap"]] = "CreditDefaultSwap"
    side: ProtectionSide
    notional: float
    spread: float
    schedule: Schedule
    paymentConvention: BusinessDayConvention
    dayCounter: DayCounter
    settlesAccrual: Optional[bool] = None
    paysAtDefaultTime: Optional[bool] = None
    protectionStart: Optional[Date] = None


class IntegralCdsEngine(BaseModel):
    resource_name: Optional[Literal["IntegralCdsEngine"]] = "IntegralCdsEngine"
    integrationStep: Period
    probability: DefaultProbabilityTermStructureHandle
    recoveryRate: float
    discountCurve: YieldTermStructureHandle
    includeSettlementDateFlows: Optional[bool] = None


class IsdaCdsEngine(BaseModel):
    resource_name: Optional[Literal["IsdaCdsEngine"]] = "IsdaCdsEngine"
    probability: DefaultProbabilityTermStructureHandle
    recoveryRate: float
    discountCurve: YieldTermStructureHandle
    includeSettlementDateFlows: Optional[bool] = None
    numericalFix: Optional[IsdaCdsEngineNumericalFix] = None
    accrualBias: Optional[IsdaCdsEngineAccrualBias] = None
    forwardsInCouponPeriod: Optional[IsdaCdsEngineForwardsInCouponPeriod] = None


class CdsOption(BaseModel):
    resource_name: Optional[Literal["CdsOption"]] = "CdsOption"
    swap: CreditDefaultSwap
    exercise: Exercise
    knocksOut: Optional[bool] = None


class FdmSimpleProcess1dMesher(BaseModel):
    resource_name: Optional[
        Literal["FdmSimpleProcess1dMesher"]
    ] = "FdmSimpleProcess1dMesher"
    size: int
    process: StochasticProcess1D
    maturity: float
    tAvgSteps: Optional[int] = None
    epsilon: Optional[float] = None
    mandatoryPoint: Optional[Optional[float]] = None


class FdmMesherComposite2(BaseModel):
    resource_name: Optional[Literal["FdmMesherComposite"]] = "FdmMesherComposite"
    layout: FdmLinearOpLayout
    mesher: List[Fdm1dMesher]


class FdmDirichletBoundary(BaseModel):
    resource_name: Optional[Literal["FdmDirichletBoundary"]] = "FdmDirichletBoundary"
    mesher: FdmMesher
    valueOnBoundary: float
    direction: int
    side: FdmDirichletBoundarySide


class FdmDiscountDirichletBoundary(BaseModel):
    resource_name: Optional[
        Literal["FdmDiscountDirichletBoundary"]
    ] = "FdmDiscountDirichletBoundary"
    mesher: FdmMesher
    rTS: YieldTermStructure
    maturityTime: float
    valueOnBoundary: float
    direction: int
    side: FdmDiscountDirichletBoundarySide


class FdmBatesOp(BaseModel):
    resource_name: Optional[Literal["FdmBatesOp"]] = "FdmBatesOp"
    mesher: FdmMesher
    batesProcess: BatesProcess
    bcSet: FdmBoundaryConditionSet
    integroIntegrationOrder: int
    quantoHelper: Optional[FdmQuantoHelper] = None


class FdmSquareRootFwdOp(BaseModel):
    resource_name: Optional[Literal["FdmSquareRootFwdOp"]] = "FdmSquareRootFwdOp"
    mesher: FdmMesher
    kappa: float
    theta: float
    sigma: float
    direction: int
    type: Optional[FdmSquareRootFwdOpTransformationType] = None


class FdmHestonFwdOp(BaseModel):
    resource_name: Optional[Literal["FdmHestonFwdOp"]] = "FdmHestonFwdOp"
    mesher: FdmMesher
    process: HestonProcess
    type: Optional[FdmSquareRootFwdOpTransformationType] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class CraigSneydScheme(BaseModel):
    resource_name: Optional[Literal["CraigSneydScheme"]] = "CraigSneydScheme"
    theta: float
    mu: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class ImplicitEulerScheme(BaseModel):
    resource_name: Optional[Literal["ImplicitEulerScheme"]] = "ImplicitEulerScheme"
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None
    relTol: Optional[float] = None
    solverType: Optional[ImplicitEulerSchemeSolverType] = None


class CrankNicolsonScheme(BaseModel):
    resource_name: Optional[Literal["CrankNicolsonScheme"]] = "CrankNicolsonScheme"
    theta: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None
    relTol: Optional[float] = None
    solverType: Optional[ImplicitEulerSchemeSolverType] = None


class DouglasScheme(BaseModel):
    resource_name: Optional[Literal["DouglasScheme"]] = "DouglasScheme"
    theta: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class ExplicitEulerScheme(BaseModel):
    resource_name: Optional[Literal["ExplicitEulerScheme"]] = "ExplicitEulerScheme"
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class HundsdorferScheme(BaseModel):
    resource_name: Optional[Literal["HundsdorferScheme"]] = "HundsdorferScheme"
    theta: float
    mu: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class MethodOfLinesScheme(BaseModel):
    resource_name: Optional[Literal["MethodOfLinesScheme"]] = "MethodOfLinesScheme"
    eps: float
    relInitStepSize: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class ModifiedCraigSneydScheme(BaseModel):
    resource_name: Optional[
        Literal["ModifiedCraigSneydScheme"]
    ] = "ModifiedCraigSneydScheme"
    theta: float
    mu: float
    map: FdmLinearOpComposite
    bcSet: Optional[FdmBoundaryConditionSet] = None


class Fdm1DimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm1DimSolver"]] = "Fdm1DimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class FdmBackwardSolver(BaseModel):
    resource_name: Optional[Literal["FdmBackwardSolver"]] = "FdmBackwardSolver"
    map: FdmLinearOpComposite
    bcSet: FdmBoundaryConditionSet
    condition: FdmStepConditionComposite
    schemeDesc: FdmSchemeDesc


class Fdm2DimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm2DimSolver"]] = "Fdm2DimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class Fdm3DimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm3DimSolver"]] = "Fdm3DimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class Fdm4dimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm4dimSolver"]] = "Fdm4dimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class Fdm5dimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm5dimSolver"]] = "Fdm5dimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class Fdm6dimSolver(BaseModel):
    resource_name: Optional[Literal["Fdm6dimSolver"]] = "Fdm6dimSolver"
    solverDesc: FdmSolverDesc
    schemeDesc: FdmSchemeDesc
    op: FdmLinearOpComposite


class FdmIndicesOnBoundary(BaseModel):
    resource_name: Optional[Literal["FdmIndicesOnBoundary"]] = "FdmIndicesOnBoundary"
    l: FdmLinearOpLayout
    direction: int
    side: FdmDirichletBoundarySide


class FittedBondDiscountCurve0(BaseModel):
    resource_name: Optional[
        Literal["FittedBondDiscountCurve"]
    ] = "FittedBondDiscountCurve"
    referenceDate: Date
    helpers: List[BondHelper]
    dayCounter: DayCounter
    fittingMethod: FittingMethod
    accuracy: Optional[float] = None
    maxEvaluations: Optional[int] = None
    guess: Optional[Array] = None
    simplexLambda: Optional[float] = None


class FittedBondDiscountCurve1(BaseModel):
    resource_name: Optional[
        Literal["FittedBondDiscountCurve"]
    ] = "FittedBondDiscountCurve"
    settlementDays: float
    calendar: Calendar
    helpers: List[BondHelper]
    dayCounter: DayCounter
    fittingMethod: FittingMethod
    accuracy: Optional[float] = None
    maxEvaluations: Optional[int] = None
    guess: Optional[Array] = None
    simplexLambda: Optional[float] = None


class FixedRateBondForward(BaseModel):
    resource_name: Optional[Literal["FixedRateBondForward"]] = "FixedRateBondForward"
    valueDate: Date
    maturityDate: Date
    type: PositionType
    strike: float
    settlementDays: float
    dayCounter: DayCounter
    calendar: Calendar
    businessDayConvention: BusinessDayConvention
    fixedBond: FixedRateBond
    discountCurve: Optional[YieldTermStructureHandle] = None
    incomeDiscountCurve: Optional[YieldTermStructureHandle] = None


class ForwardRateAgreement(BaseModel):
    resource_name: Optional[Literal["ForwardRateAgreement"]] = "ForwardRateAgreement"
    valueDate: Date
    maturityDate: Date
    type: PositionType
    strikeForwardRate: float
    notionalAmount: float
    index: IborIndex
    discountCurve: Optional[YieldTermStructureHandle] = None
    useIndexedCoupon: Optional[bool] = None


class MarkovFunctional0(BaseModel):
    resource_name: Optional[Literal["MarkovFunctional"]] = "MarkovFunctional"
    termStructure: YieldTermStructureHandle
    reversion: float
    volstepdates: List[Date]
    volatilities: List[float]
    capletVol: OptionletVolatilityStructureHandle
    capletExpiries: List[Date]
    iborIndex: IborIndex
    modelSettings: Optional[MarkovFunctionalModelSettings] = None


class MarkovFunctional1(BaseModel):
    resource_name: Optional[Literal["MarkovFunctional"]] = "MarkovFunctional"
    termStructure: YieldTermStructureHandle
    reversion: float
    volstepdates: List[Date]
    volatilities: List[float]
    swaptionVol: SwaptionVolatilityStructureHandle
    swaptionExpiries: List[Date]
    swaptionTenors: List[Period]
    swapIndexBase: SwapIndex
    modelSettings: Optional[MarkovFunctionalModelSettings] = None


class Gaussian1dSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["Gaussian1dSwaptionEngine"]
    ] = "Gaussian1dSwaptionEngine"
    model: Gaussian1dModel
    integrationPoints: Optional[int] = None
    stddevs: Optional[float] = None
    extrapolatePayoff: Optional[bool] = None
    flatPayoffExtrapolation: Optional[bool] = None
    discountCurve: Optional[YieldTermStructureHandle] = None
    probabilities: Optional[Gaussian1dSwaptionEngineProbabilities] = None


class Gaussian1dJamshidianSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["Gaussian1dJamshidianSwaptionEngine"]
    ] = "Gaussian1dJamshidianSwaptionEngine"
    model: Gaussian1dModel


class Gaussian1dNonstandardSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["Gaussian1dNonstandardSwaptionEngine"]
    ] = "Gaussian1dNonstandardSwaptionEngine"
    model: Gaussian1dModel
    integrationPoints: Optional[int] = None
    stddevs: Optional[float] = None
    extrapolatePayoff: Optional[bool] = None
    flatPayoffExtrapolation: Optional[bool] = None
    oas: Optional[QuoteHandle] = None
    discountCurve: Optional[YieldTermStructureHandle] = None
    probabilities: Optional[Gaussian1dNonstandardSwaptionEngineProbabilities] = None


class Gaussian1dFloatFloatSwaptionEngine(BaseModel):
    resource_name: Optional[
        Literal["Gaussian1dFloatFloatSwaptionEngine"]
    ] = "Gaussian1dFloatFloatSwaptionEngine"
    model: Gaussian1dModel
    integrationPoints: Optional[int] = None
    stddevs: Optional[float] = None
    extrapolatePayoff: Optional[bool] = None
    flatPayoffExtrapolation: Optional[bool] = None
    oas: Optional[QuoteHandle] = None
    discountCurve: Optional[YieldTermStructureHandle] = None
    includeTodaysExercise: Optional[bool] = None
    probabilities: Optional[Gaussian1dFloatFloatSwaptionEngineProbabilities] = None


class SobolRsg(BaseModel):
    resource_name: Optional[Literal["SobolRsg"]] = "SobolRsg"
    dimensionality: int
    seed: Optional[int] = None
    directionIntegers: Optional[SobolRsgDirectionIntegers] = None


class UniformLowDiscrepancySequenceGenerator(BaseModel):
    resource_name: Optional[
        Literal["UniformLowDiscrepancySequenceGenerator"]
    ] = "UniformLowDiscrepancySequenceGenerator"
    dimensionality: int
    seed: Optional[int] = None
    directionIntegers: Optional[SobolRsgDirectionIntegers] = None


class GaussianLowDiscrepancySequenceGenerator(BaseModel):
    resource_name: Optional[
        Literal["GaussianLowDiscrepancySequenceGenerator"]
    ] = "GaussianLowDiscrepancySequenceGenerator"
    u: UniformLowDiscrepancySequenceGenerator


class NeumannBC(BaseModel):
    resource_name: Optional[Literal["NeumannBC"]] = "NeumannBC"
    value: float
    side: DefaultBoundaryConditionSide


class DirichletBC(BaseModel):
    resource_name: Optional[Literal["DirichletBC"]] = "DirichletBC"
    value: float
    side: DefaultBoundaryConditionSide


class SobolBrownianGeneratorFactory(BaseModel):
    resource_name: Optional[
        Literal["SobolBrownianGeneratorFactory"]
    ] = "SobolBrownianGeneratorFactory"
    ordering: SobolBrownianGeneratorOrdering
    seed: Optional[int] = None
    directionIntegers: Optional[SobolRsgDirectionIntegers] = None


class FdHestonBarrierEngine(BaseModel):
    resource_name: Optional[Literal["FdHestonBarrierEngine"]] = "FdHestonBarrierEngine"
    model: HestonModel
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    vGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class FdHestonDoubleBarrierEngine(BaseModel):
    resource_name: Optional[
        Literal["FdHestonDoubleBarrierEngine"]
    ] = "FdHestonDoubleBarrierEngine"
    model: HestonModel
    tGrid: Optional[int] = None
    xGrid: Optional[int] = None
    vGrid: Optional[int] = None
    dampingSteps: Optional[int] = None
    schemeDesc: Optional[FdmSchemeDesc] = None
    leverageFct: Optional[LocalVolTermStructure] = None


class CapFloorTermVolCurve0(BaseModel):
    resource_name: Optional[Literal["CapFloorTermVolCurve"]] = "CapFloorTermVolCurve"
    settlementDays: float
    calendar: Calendar
    bdc: BusinessDayConvention
    lengths: List[Period]
    vols: List[float]
    dc: Optional[DayCounter] = None


class CapFloorTermVolCurve1(BaseModel):
    resource_name: Optional[Literal["CapFloorTermVolCurve"]] = "CapFloorTermVolCurve"
    referenceDate: Date
    calendar: Calendar
    bdc: BusinessDayConvention
    lengths: List[Period]
    vols: List[float]
    dc: Optional[DayCounter] = None


class CapFloorTermVolSurface0(BaseModel):
    resource_name: Optional[
        Literal["CapFloorTermVolSurface"]
    ] = "CapFloorTermVolSurface"
    settlementDays: float
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    strikes: List[float]
    volatilities: Matrix
    dc: Optional[DayCounter] = None


class CapFloorTermVolSurface1(BaseModel):
    resource_name: Optional[
        Literal["CapFloorTermVolSurface"]
    ] = "CapFloorTermVolSurface"
    settlementDate: Date
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    strikes: List[float]
    volatilities: Matrix
    dc: Optional[DayCounter] = None


class CapFloorTermVolSurface2(BaseModel):
    resource_name: Optional[
        Literal["CapFloorTermVolSurface"]
    ] = "CapFloorTermVolSurface"
    settlementDate: Date
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    strikes: List[float]
    quotes: List[List[QuoteHandle]]
    dc: Optional[DayCounter] = None


class CapFloorTermVolSurface3(BaseModel):
    resource_name: Optional[
        Literal["CapFloorTermVolSurface"]
    ] = "CapFloorTermVolSurface"
    settlementDays: float
    calendar: Calendar
    bdc: BusinessDayConvention
    optionTenors: List[Period]
    strikes: List[float]
    quotes: List[List[QuoteHandle]]
    dc: Optional[DayCounter] = None


class OptionletStripper1(BaseModel):
    resource_name: Optional[Literal["OptionletStripper"]] = "OptionletStripper"
    parVolSurface: CapFloorTermVolSurface
    index: IborIndex
    switchStrikes: Optional[float] = None
    accuracy: Optional[float] = None
    maxIter: Optional[float] = None
    discount: Optional[YieldTermStructureHandle] = None
    type: Optional[VolatilityType] = None
    displacement: Optional[float] = None
    dontThrow: Optional[bool] = None


class Swaption(BaseModel):
    resource_name: Optional[Literal["Swaption"]] = "Swaption"
    swap: VanillaSwap
    exercise: Exercise
    type: Optional[SettlementType] = None
    settlementMethod: Optional[SettlementMethod] = None


class NonstandardSwaption(BaseModel):
    resource_name: Optional[Literal["NonstandardSwaption"]] = "NonstandardSwaption"
    swap: NonstandardSwap
    exercise: Exercise
    type: Optional[SettlementType] = None
    settlementMethod: Optional[SettlementMethod] = None


class FloatFloatSwaption(BaseModel):
    resource_name: Optional[Literal["FloatFloatSwaption"]] = "FloatFloatSwaption"
    swap: FloatFloatSwap
    exercise: Exercise
    delivery: Optional[SettlementType] = None
    settlementMethod: Optional[SettlementMethod] = None


class ZeroCurve(BaseModel):
    resource_name: Optional[Literal["ZeroCurve"]] = "ZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[Linear] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class LogLinearInterpolatedZeroCurve(BaseModel):
    resource_name: Optional[
        Literal["LogLinearInterpolatedZeroCurve"]
    ] = "LogLinearInterpolatedZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[LogLinear] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class CubicInterpolatedZeroCurve(BaseModel):
    resource_name: Optional[
        Literal["CubicInterpolatedZeroCurve"]
    ] = "CubicInterpolatedZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[Cubic] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class SplineCubicInterpolatedZeroCurve(BaseModel):
    resource_name: Optional[
        Literal["SplineCubicInterpolatedZeroCurve"]
    ] = "SplineCubicInterpolatedZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[SplineCubic] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class DefaultLogCubicInterpolatedZeroCurve(BaseModel):
    resource_name: Optional[
        Literal["DefaultLogCubicInterpolatedZeroCurve"]
    ] = "DefaultLogCubicInterpolatedZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[DefaultLogCubic] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class MonotonicCubicInterpolatedZeroCurve(BaseModel):
    resource_name: Optional[
        Literal["MonotonicCubicInterpolatedZeroCurve"]
    ] = "MonotonicCubicInterpolatedZeroCurve"
    dates: List[Date]
    yields: List[float]
    dayCounter: DayCounter
    calendar: Optional[Calendar] = None
    i: Optional[MonotonicCubic] = None
    compounding: Optional[Compounding] = None
    frequency: Optional[float] = None


class ActualActual(BaseModel):
    resource_name: Optional[Literal["ActualActual"]] = "ActualActual"
    c: Optional[ActualActualConvention] = None
    schedule: Optional[Schedule] = None


class HestonBlackVolSurface(BaseModel):
    resource_name: Optional[Literal["HestonBlackVolSurface"]] = "HestonBlackVolSurface"
    hestonModel: HestonModelHandle
    cpxLogFormula: Optional[AnalyticHestonEngineComplexLogFormula] = None
    integration: Optional[AnalyticHestonEngineIntegration] = None


class AnalyticHestonEngine0(BaseModel):
    resource_name: Optional[Literal["AnalyticHestonEngine"]] = "AnalyticHestonEngine"
    model: HestonModel
    cpxLog: AnalyticHestonEngineComplexLogFormula
    itg: AnalyticHestonEngineIntegration
    andersenPiterbargEpsilon: Optional[float] = None


class AssetSwap(BaseModel):
    resource_name: Optional[Literal["AssetSwap"]] = "AssetSwap"
    payFixedRate: bool
    bond: Bond
    bondCleanPrice: float
    index: IborIndex
    spread: float
    floatSchedule: Optional[Schedule] = None
    floatingDayCount: Optional[DayCounter] = None
    parAssetSwap: Optional[bool] = None


GeneralizedBlackScholesProcess = Union[
    BlackProcess,
    BlackScholesMertonProcess,
    BlackScholesProcess,
    GarmanKohlagenProcess,
    GeneralizedBlackScholesProcess0,
    GeneralizedBlackScholesProcess1,
]
ConstantOptionletVolatility = Union[
    ConstantOptionletVolatility0, ConstantOptionletVolatility1
]
FuturesRateHelper = Union[
    FuturesRateHelper0,
    FuturesRateHelper1,
    FuturesRateHelper2,
    FuturesRateHelper3,
    FuturesRateHelper4,
    FuturesRateHelper5,
]
SofrFutureRateHelper = Union[SofrFutureRateHelper0, SofrFutureRateHelper1]
TreeCapFloorEngine = Union[TreeCapFloorEngine0, TreeCapFloorEngine1]
JointCalendar = Union[JointCalendar0, JointCalendar1, JointCalendar2]
BrownianBridge = Union[BrownianBridge0, BrownianBridge1, BrownianBridge2]
FdBlackScholesVanillaEngine = Union[
    FdBlackScholesVanillaEngine0, FdBlackScholesVanillaEngine1
]
FdmCellAveragingInnerValue = Union[FdmLogInnerValue]
SabrSmileSection = Union[SabrSmileSection0, SabrSmileSection1]
CmsSpreadCouponPricer = Union[LognormalCmsSpreadPricer]
EuriborSwapIsdaFixA = Union[EuriborSwapIsdaFixA0, EuriborSwapIsdaFixA1]
EurLiborSwapIfrFix = Union[EurLiborSwapIfrFix0, EurLiborSwapIfrFix1]
InflationTermStructure = Union[YoYInflationTermStructure, ZeroInflationTermStructure]
NinePointLinearOp = Union[NinePointLinearOpBase, SecondOrderMixedDerivativeOp]
LocalConstantVol = Union[LocalConstantVol0, LocalConstantVol1]
CapFloorTermVolSurface = Union[
    CapFloorTermVolSurface0,
    CapFloorTermVolSurface1,
    CapFloorTermVolSurface2,
    CapFloorTermVolSurface3,
]
FdmBoundaryCondition = Union[FdmDirichletBoundary, FdmDiscountDirichletBoundary]
SwaptionVolatilityMatrix = Union[
    SwaptionVolatilityMatrix0, SwaptionVolatilityMatrix1, SwaptionVolatilityMatrix2
]
JpyLiborSwapIsdaFixAm = Union[JpyLiborSwapIsdaFixAm0, JpyLiborSwapIsdaFixAm1]
DoubleBarrierOption = Union[DoubleBarrierOptionBase, QuantoDoubleBarrierOption]
SwaptionHelper = Union[SwaptionHelper0, SwaptionHelper1, SwaptionHelper2]
StrikedTypePayoff = Union[
    AssetOrNothingPayoff,
    CashOrNothingPayoff,
    GapPayoff,
    PercentageStrikePayoff,
    PlainVanillaPayoff,
    SuperSharePayoff,
    VanillaForwardPayoff,
]
Euribor365 = Union[
    Euribor365Base
]  # , Euribor365_10M, Euribor365_11M, Euribor365_1M, Euribor365_1Y, Euribor365_2M, Euribor365_2W, Euribor365_3M, Euribor365_3W, Euribor365_4M, Euribor365_5M, Euribor365_6M, Euribor365_7M, Euribor365_8M, Euribor365_9M, Euribor365_SW]
Money = Union[Money0, Money1]
ConstantParameter = Union[ConstantParameter0, ConstantParameter1]
FittingMethod = Union[
    CubicBSplinesFitting,
    ExponentialSplinesFitting,
    NelsonSiegelFitting,
    SimplePolynomialFitting,
    SvenssonFitting,
]
VanillaOption = Union[EuropeanOption, VanillaOptionBase]
ChfLiborSwapIsdaFix = Union[ChfLiborSwapIsdaFix0, ChfLiborSwapIsdaFix1]
IborCouponPricer = Union[BlackIborCouponPricer]
TridiagonalOperator = Union[DMinus, DPlus, DPlusDMinus, DZero, TridiagonalOperatorBase]
FdHestonVanillaEngine = Union[FdHestonVanillaEngine0, FdHestonVanillaEngine1]
FdmInnerValueCalculator = Union[FdmLogBasketInnerValue]
StrippedOptionletBase = Union[OptionletStripper1]
DailyTenorLibor = Union[CADLiborON, DailyTenorLiborBase, GBPLiborON, USDLiborON]
UsdLiborSwapIsdaFixAm = Union[UsdLiborSwapIsdaFixAm0, UsdLiborSwapIsdaFixAm1]
Bbsw = Union[Bbsw1M, Bbsw2M, Bbsw3M, Bbsw4M, Bbsw5M, Bbsw6M, BbswBase]
TreeCallableFixedRateBondEngine = Union[
    TreeCallableFixedRateBondEngine0, TreeCallableFixedRateBondEngine1
]
Claim = Union[FaceValueAccrualClaim, FaceValueClaim]
CreditDefaultSwap = Union[CreditDefaultSwap0, CreditDefaultSwap1]
TripleBandLinearOp = Union[
    FirstDerivativeOp, SecondDerivativeOp, TripleBandLinearOpBase
]
BlackSwaptionEngine = Union[BlackSwaptionEngine0, BlackSwaptionEngine1]
FlatHazardRate = Union[FlatHazardRate0, FlatHazardRate1]
AmortizingFixedRateBond = Union[AmortizingFixedRateBond0, AmortizingFixedRateBond1]
NoArbSabrInterpolatedSmileSection = Union[
    NoArbSabrInterpolatedSmileSection0, NoArbSabrInterpolatedSmileSection1
]
HestonModel = Union[BatesModel, HestonModelBase]
Period = Union[Period0, Period1]
Concentrating1dMesher = Union[Concentrating1dMesher0, Concentrating1dMesher1]
Exercise = Union[
    AmericanExercise,
    BermudanExercise,
    EuropeanExercise,
    ExerciseBase,
    RebatedExercise,
    SwingExercise,
]
CmsCouponPricer = Union[AnalyticHaganPricer, LinearTsrPricer, NumericHaganPricer]
EURLibor = Union[
    EURLibor10M,
    EURLibor11M,
    EURLibor1M,
    EURLibor1Y,
    EURLibor2M,
    EURLibor2W,
    EURLibor3M,
    EURLibor4M,
    EURLibor5M,
    EURLibor6M,
    EURLibor7M,
    EURLibor8M,
    EURLibor9M,
    EURLiborBase,
    EURLiborSW,
]
Euribor = Union[
    Euribor10M,
    Euribor11M,
    Euribor1M,
    Euribor1Y,
    Euribor2M,
    Euribor2W,
    Euribor3M,
    Euribor3W,
    Euribor4M,
    Euribor5M,
    Euribor6M,
    Euribor7M,
    Euribor8M,
    Euribor9M,
    EuriborBase,
    EuriborSW,
]
MarkovFunctional = Union[MarkovFunctional0, MarkovFunctional1]
GbpLiborSwapIsdaFix = Union[GbpLiborSwapIsdaFix0, GbpLiborSwapIsdaFix1]
Bibor = Union[Bibor1M, Bibor1Y, Bibor2M, Bibor3M, Bibor6M, Bibor9M, BiborBase, BiborSW]
CallableBond = Union[CallableFixedRateBond]
FdmLinearOpComposite = Union[
    Fdm2dBlackScholesOp,
    FdmBatesOp,
    FdmBlackScholesFwdOp,
    FdmBlackScholesOp,
    FdmCEVOp,
    FdmDupire1dOp,
    FdmG2Op,
    FdmHestonFwdOp,
    FdmHestonHullWhiteOp,
    FdmHestonOp,
    FdmHullWhiteOp,
    FdmLocalVolFwdOp,
    FdmOrnsteinUhlenbeckOp,
    FdmSabrOp,
    FdmSquareRootFwdOp,
    FdmZabrOp,
]
AverageBasketPayoff = Union[AverageBasketPayoff0, AverageBasketPayoff1]
HestonProcess = Union[BatesProcess, HestonProcessBase]
Currency = Union[
    ARSCurrency,
    ATSCurrency,
    AUDCurrency,
    BDTCurrency,
    BEFCurrency,
    BGLCurrency,
    BRLCurrency,
    BYRCurrency,
    CADCurrency,
    CHFCurrency,
    CLPCurrency,
    CNYCurrency,
    COPCurrency,
    CYPCurrency,
    CZKCurrency,
    DEMCurrency,
    DKKCurrency,
    EEKCurrency,
    ESPCurrency,
    EURCurrency,
    FIMCurrency,
    FRFCurrency,
    GBPCurrency,
    GRDCurrency,
    HKDCurrency,
    HUFCurrency,
    IDRCurrency,
    IEPCurrency,
    ILSCurrency,
    INRCurrency,
    IQDCurrency,
    IRRCurrency,
    ISKCurrency,
    ITLCurrency,
    JPYCurrency,
    KRWCurrency,
    KWDCurrency,
    LTLCurrency,
    LUFCurrency,
    LVLCurrency,
    MTLCurrency,
    MXNCurrency,
    MYRCurrency,
    NLGCurrency,
    NOKCurrency,
    NPRCurrency,
    NZDCurrency,
    PEHCurrency,
    PEICurrency,
    PENCurrency,
    PKRCurrency,
    PLNCurrency,
    PTECurrency,
    ROLCurrency,
    RONCurrency,
    RUBCurrency,
    SARCurrency,
    SEKCurrency,
    SGDCurrency,
    SITCurrency,
    SKKCurrency,
    THBCurrency,
    TRLCurrency,
    TRYCurrency,
    TTDCurrency,
    TWDCurrency,
    USDCurrency,
    VEBCurrency,
    VNDCurrency,
    ZARCurrency,
]
BrownianGeneratorFactory = Union[
    MTBrownianGeneratorFactory, SobolBrownianGeneratorFactory
]
FlatForward = Union[FlatForward0, FlatForward1]
TreeSwaptionEngine = Union[TreeSwaptionEngine0, TreeSwaptionEngine1]
DeltaVolQuote = Union[DeltaVolQuote0, DeltaVolQuote1]
FixedRateBond = Union[FixedRateBond0, FixedRateBond1, FixedRateBond2]
DefaultProbabilityHelper = Union[SpreadCdsHelper, UpfrontCdsHelper]
Region = Union[CustomRegion]
ForwardVanillaOption = Union[ForwardVanillaOptionBase, QuantoForwardVanillaOption]
FittedBondDiscountCurve = Union[FittedBondDiscountCurve0, FittedBondDiscountCurve1]
YoYInflationIndex = Union[YYEUHICP, YYEUHICPXT, YYFRHICP, YYUKRPI, YYUSCPI, YYZACPI]
Dividend = Union[FixedDividend, FractionalDividend]
EuriborSwapIfrFix = Union[EuriborSwapIfrFix0, EuriborSwapIfrFix1]
Rounding = Union[
    CeilingTruncation, ClosestRounding, DownRounding, FloorTruncation, UpRounding
]
Array = Union[Array0, Array1]
OvernightIndexedSwap = Union[OvernightIndexedSwap0, OvernightIndexedSwap1]
FlatSmileSection = Union[FlatSmileSection0, FlatSmileSection1]
NoArbSabrSmileSection = Union[NoArbSabrSmileSection0, NoArbSabrSmileSection1]
FraRateHelper = Union[FraRateHelper0, FraRateHelper1, FraRateHelper2]
DayCounter = Union[
    Actual360,
    Actual365Fixed,
    ActualActual,
    Business252,
    OneDayCounter,
    SimpleDayCounter,
    Thirty360,
]
Schedule = Union[Schedule0, Schedule1]
Matrix = Union[Matrix0, Matrix1]
BlackConstantVol = Union[BlackConstantVol0, BlackConstantVol1]
DefaultBoundaryCondition = Union[DirichletBC, NeumannBC]
Constraint = Union[
    BoundaryConstraint,
    CompositeConstraint,
    NoConstraint,
    NonhomogeneousBoundaryConstraint,
    PositiveConstraint,
]
BondHelper = Union[BondHelperBase, FixedRateBondHelper]
Callability = Union[CallabilityBase, SoftCallability]
OvernightIndex = Union[Aonia, Eonia, FedFunds, Nzocr, OvernightIndexBase, Sofr, Sonia]
OptimizationMethod = Union[
    BFGS,
    ConjugateGradient,
    DifferentialEvolution,
    GaussianSimulatedAnnealing,
    LevenbergMarquardt,
    LogNormalSimulatedAnnealing,
    MirrorGaussianSimulatedAnnealing,
    Simplex,
    SteepestDescent,
]
AnalyticPTDHestonEngine = Union[
    AnalyticPTDHestonEngine0, AnalyticPTDHestonEngine1, AnalyticPTDHestonEngine2
]
Seasonality = Union[MultiplicativePriceSeasonality]
Bkbm = Union[Bkbm1M, Bkbm2M, Bkbm3M, Bkbm4M, Bkbm5M, Bkbm6M, BkbmBase]
BachelierSwaptionEngine = Union[BachelierSwaptionEngine0, BachelierSwaptionEngine1]
DepositRateHelper = Union[DepositRateHelper0, DepositRateHelper1]
InflationCoupon = Union[CPICoupon]
RiskNeutralDensityCalculator = Union[
    BSMRNDCalculator,
    CEVRNDCalculator,
    GBSMRNDCalculator,
    HestonRNDCalculator,
    LocalVolRNDCalculator,
    SquareRootProcessRNDCalculator,
]
Forward = Union[FixedRateBondForward, ForwardRateAgreement]
JpyLiborSwapIsdaFixPm = Union[JpyLiborSwapIsdaFixPm0, JpyLiborSwapIsdaFixPm1]
CapFloor = Union[Cap, Collar, Floor]
CappedFlooredCoupon = Union[
    CappedFlooredCmsCoupon,
    CappedFlooredCmsSpreadCoupon,
    CappedFlooredCouponBase,
    CappedFlooredIborCoupon,
]
ConstantSwaptionVolatility = Union[
    ConstantSwaptionVolatility0, ConstantSwaptionVolatility1
]
FdmMesherComposite = Union[
    FdmMesherComposite0, FdmMesherComposite1, FdmMesherComposite2
]
CapFloorTermVolCurve = Union[CapFloorTermVolCurve0, CapFloorTermVolCurve1]
SwapRateHelper = Union[SwapRateHelper0, SwapRateHelper1]
ZeroInflationIndex = Union[
    EUHICP, EUHICPXT, FRHICP, UKRPI, USCPI, ZACPI, ZeroInflationIndexBase
]
YoYInflationCapFloor = Union[YoYInflationCap, YoYInflationCollar, YoYInflationFloor]
Vasicek = Union[HullWhite, VasicekBase]
MultiAssetOption = Union[BasketOption, EverestOption, HimalayaOption]
EurLiborSwapIsdaFixA = Union[EurLiborSwapIsdaFixA0, EurLiborSwapIsdaFixA1]
GlobalBootstrap = Union[GlobalBootstrap0, GlobalBootstrap1]
EuriborSwapIsdaFixB = Union[EuriborSwapIsdaFixB0, EuriborSwapIsdaFixB1]
Statistics = Union[RiskStatistics]
AnalyticHestonEngine = Union[
    AnalyticHestonEngine0, AnalyticHestonEngine1, AnalyticHestonEngine2
]
EurLiborSwapIsdaFixB = Union[EurLiborSwapIsdaFixB0, EurLiborSwapIsdaFixB1]
UsdLiborSwapIsdaFixPm = Union[UsdLiborSwapIsdaFixPm0, UsdLiborSwapIsdaFixPm1]
BatesEngine = Union[BatesEngine0, BatesEngine1]
SwapIndex = Union[
    ChfLiborSwapIsdaFix,
    EurLiborSwapIfrFix,
    EurLiborSwapIsdaFixA,
    EurLiborSwapIsdaFixB,
    EuriborSwapIfrFix,
    EuriborSwapIsdaFixA,
    EuriborSwapIsdaFixB,
    GbpLiborSwapIsdaFix,
    JpyLiborSwapIsdaFixAm,
    JpyLiborSwapIsdaFixPm,
    OvernightIndexedSwapIndex,
    SwapIndexBase,
    UsdLiborSwapIsdaFixAm,
    UsdLiborSwapIsdaFixPm,
]
SwaptionVolatilityDiscrete = Union[
    SwaptionVolCube1, SwaptionVolCube2, SwaptionVolatilityMatrix
]
FloatingRateCouponPricer = Union[
    CmsCouponPricer, CmsSpreadCouponPricer, IborCouponPricer
]
IborIndex = Union[
    AUDLibor,
    Bbsw,
    Bibor,
    Bkbm,
    CADLibor,
    CHFLibor,
    Cdor,
    DKKLibor,
    DailyTenorLibor,
    EURLibor,
    Euribor,
    Euribor365,
    GBPLibor,
    IborIndexBase,
    JPYLibor,
    Jibar,
    Libor,
    Mosprime,
    NZDLibor,
    OvernightIndex,
    Pribor,
    Robor,
    SEKLibor,
    Shibor,
    THBFIX,
    TRLibor,
    Tibor,
    USDLibor,
    Wibor,
    Zibor,
]
FloatingRateCoupon = Union[
    CappedFlooredCoupon, CmsCoupon, CmsSpreadCoupon, IborCoupon, OvernightIndexedCoupon
]
StochasticProcess = Union[
    ExtOUWithJumpsProcess,
    G2ForwardProcess,
    G2Process,
    GJRGARCHProcess,
    HestonProcess,
    HestonSLVProcess,
    KlugeExtOUProcess,
    StochasticProcessArray,
]
Swap = Union[
    AssetSwap,
    CPISwap,
    FloatFloatSwap,
    NonstandardSwap,
    OvernightIndexedSwap,
    SwapBase,
    VanillaSwap,
    YearOnYearInflationSwap,
    ZeroCouponInflationSwap,
]
Gaussian1dModel = Union[Gsr, MarkovFunctional]
DefaultProbabilityTermStructure = Union[FlatHazardRate]
InflationIndex = Union[YoYInflationIndex, ZeroInflationIndex]
FdmLinearOp = Union[
    FdmLinearOpComposite, NinePointLinearOp, NthOrderDerivativeOp, TripleBandLinearOp
]
YieldTermStructure = Union[
    CubicInterpolatedZeroCurve,
    DefaultLogCubicInterpolatedZeroCurve,
    FittedBondDiscountCurve,
    FlatForward,
    ForwardSpreadedTermStructure,
    ImpliedTermStructure,
    LogLinearInterpolatedZeroCurve,
    MonotonicCubicInterpolatedZeroCurve,
    SplineCubicInterpolatedZeroCurve,
    ZeroCurve,
    ZeroSpreadedTermStructure,
]
Calendar = Union[
    Argentina,
    Australia,
    BespokeCalendar,
    Brazil,
    Canada,
    China,
    CzechRepublic,
    Denmark,
    Finland,
    France,
    Germany,
    HongKong,
    Hungary,
    Iceland,
    India,
    Indonesia,
    Israel,
    Italy,
    Japan,
    JointCalendar,
    Mexico,
    NewZealand,
    Norway,
    NullCalendar,
    Poland,
    Romania,
    Russia,
    SaudiArabia,
    Singapore,
    Slovakia,
    SouthAfrica,
    SouthKorea,
    Sweden,
    Switzerland,
    TARGET,
    Taiwan,
    Thailand,
    Turkey,
    Ukraine,
    UnitedKingdom,
    UnitedStates,
    WeekendsOnly,
]
Parameter = Union[ConstantParameter, NullParameter, PiecewiseConstantParameter]
OvernightIndexFutureRateHelper = Union[
    OvernightIndexFutureRateHelperBase, SofrFutureRateHelper
]
StochasticProcess1D = Union[
    ExtendedOrnsteinUhlenbeckProcess,
    GeneralizedBlackScholesProcess,
    GeometricBrownianMotionProcess,
    GsrProcess,
    HullWhiteForwardProcess,
    HullWhiteProcess,
    Merton76Process,
    OrnsteinUhlenbeckProcess,
    VarianceGammaProcess,
]
Quote = Union[DeltaVolQuote, SimpleQuote]
BlackVolTermStructure = Union[
    AndreasenHugeVolatilityAdapter,
    BlackConstantVol,
    BlackVarianceCurve,
    HestonBlackVolSurface,
]
Fdm1dMesher = Union[
    Concentrating1dMesher,
    ExponentialJump1dMesher,
    Fdm1dMesherBase,
    FdmBlackScholesMesher,
    FdmCEV1dMesher,
    FdmHestonLocalVolatilityVarianceMesher,
    FdmHestonVarianceMesher,
    FdmSimpleProcess1dMesher,
    Glued1dMesher,
    Predefined1dMesher,
    Uniform1dMesher,
]
BlackCalibrationHelper = Union[CapHelper, HestonModelHelper, SwaptionHelper]
CapFloorTermVolatilityStructure = Union[CapFloorTermVolCurve, CapFloorTermVolSurface]
TypePayoff = Union[StrikedTypePayoff]
OneAssetOption = Union[
    BarrierOption,
    ContinuousAveragingAsianOption,
    DiscreteAveragingAsianOption,
    DividendVanillaOption,
    DoubleBarrierOption,
    ForwardVanillaOption,
    QuantoVanillaOption,
    VanillaOption,
    VanillaSwingOption,
]
FdmMesher = Union[FdmMesherComposite]
Bond = Union[
    AmortizingFixedRateBond,
    AmortizingFloatingRateBond,
    Bond0,
    Bond1,
    CPIBond,
    CallableBond,
    CmsRateBond,
    ConvertibleFixedCouponBond,
    ConvertibleFloatingRateBond,
    ConvertibleZeroCouponBond,
    FixedRateBond,
    FloatingRateBond,
    ZeroCouponBond,
]
OptionletVolatilityStructure = Union[
    ConstantOptionletVolatility, StrippedOptionletAdapter
]
PricingEngine = Union[
    AnalyticBarrierEngine,
    AnalyticBinaryBarrierEngine,
    AnalyticCEVEngine,
    AnalyticCapFloorEngine,
    AnalyticContinuousGeometricAveragePriceAsianEngine,
    AnalyticDigitalAmericanEngine,
    AnalyticDigitalAmericanKOEngine,
    AnalyticDiscreteGeometricAveragePriceAsianEngine,
    AnalyticDiscreteGeometricAverageStrikeAsianEngine,
    AnalyticDividendEuropeanEngine,
    AnalyticDoubleBarrierBinaryEngine,
    AnalyticDoubleBarrierEngine,
    AnalyticEuropeanEngine,
    AnalyticGJRGARCHEngine,
    AnalyticHestonEngine,
    AnalyticPTDHestonEngine,
    BachelierCapFloorEngine,
    BachelierSwaptionEngine,
    BaroneAdesiWhaleyApproximationEngine,
    BatesEngine,
    BinomialCRRConvertibleEngine,
    BinomialCRRVanillaEngine,
    BinomialJRConvertibleEngine,
    BinomialJRVanillaEngine,
    BinomialJoshi4ConvertibleEngine,
    BinomialJoshi4VanillaEngine,
    BinomialTianConvertibleEngine,
    BinomialTianVanillaEngine,
    BinomialTrigeorgisConvertibleEngine,
    BinomialTrigeorgisVanillaEngine,
    BjerksundStenslandApproximationEngine,
    BlackCallableFixedRateBondEngine,
    BlackCapFloorEngine,
    BlackCdsOptionEngine,
    BlackSwaptionEngine,
    COSHestonEngine,
    ContinuousArithmeticAsianLevyEngine,
    DiscountingBondEngine,
    DiscountingSwapEngine,
    FDAmericanEngine,
    FDBermudanEngine,
    FDEuropeanEngine,
    FDShoutEngine,
    FFTVarianceGammaEngine,
    Fd2dBlackScholesVanillaEngine,
    FdBatesVanillaEngine,
    FdBlackScholesAsianEngine,
    FdBlackScholesBarrierEngine,
    FdBlackScholesVanillaEngine,
    FdCEVVanillaEngine,
    FdG2SwaptionEngine,
    FdHestonBarrierEngine,
    FdHestonDoubleBarrierEngine,
    FdHestonVanillaEngine,
    FdHullWhiteSwaptionEngine,
    FdOrnsteinUhlenbeckVanillaEngine,
    FdSabrVanillaEngine,
    FdSimpleBSSwingEngine,
    ForwardEuropeanEngine,
    G2SwaptionEngine,
    Gaussian1dFloatFloatSwaptionEngine,
    Gaussian1dJamshidianSwaptionEngine,
    Gaussian1dNonstandardSwaptionEngine,
    Gaussian1dSwaptionEngine,
    IntegralCdsEngine,
    IntegralEngine,
    IsdaCdsEngine,
    JamshidianSwaptionEngine,
    JuQuadraticApproximationEngine,
    KirkEngine,
    MidPointCdsEngine,
    QuantoEuropeanEngine,
    QuantoForwardEuropeanEngine,
    StulzEngine,
    TreeCallableFixedRateBondEngine,
    TreeCapFloorEngine,
    TreeSwaptionEngine,
    VannaVolgaBarrierEngine,
    VarianceGammaEngine,
    WulinYongDoubleBarrierEngine,
]
BasketPayoff = Union[
    AverageBasketPayoff, MaxBasketPayoff, MinBasketPayoff, SpreadBasketPayoff
]
SmileSection = Union[
    FlatSmileSection,
    KahaleSmileSection,
    NoArbSabrInterpolatedSmileSection,
    NoArbSabrSmileSection,
    SabrSmileSection,
]
LocalVolTermStructure = Union[
    AndreasenHugeLocalVolAdapter, LocalConstantVol, LocalVolSurface
]
OneFactorAffineModel = Union[Vasicek]
Payoff = Union[BasketPayoff, TypePayoff]
Coupon = Union[FixedRateCoupon, FloatingRateCoupon, InflationCoupon]
CalibrationHelper = Union[BlackCalibrationHelper]
ShortRateModel = Union[BlackKarasinski, G2, OneFactorAffineModel]
SwaptionVolatilityStructure = Union[
    ConstantSwaptionVolatility, SwaptionVolatilityDiscrete
]
Option = Union[CdsOption, OneAssetOption, Swaption]
InterestRateIndex = Union[IborIndex, SwapIndex, SwapSpreadIndex]
RateHelper = Union[
    BondHelper,
    DatedOISRateHelper,
    DepositRateHelper,
    FraRateHelper,
    FuturesRateHelper,
    FxSwapRateHelper,
    OISRateHelper,
    OvernightIndexFutureRateHelper,
    SwapRateHelper,
]
VolatilityTermStructure = Union[
    BlackVolTermStructure,
    CapFloorTermVolatilityStructure,
    LocalVolTermStructure,
    OptionletVolatilityStructure,
    SwaptionVolatilityStructure,
]
Index = Union[InflationIndex, InterestRateIndex]
CashFlow = Union[AmortizingPayment, Coupon, Dividend, Redemption, SimpleCashFlow]
CalibratedModel = Union[
    GJRGARCHModel, HestonModel, PiecewiseTimeDependentHestonModel, ShortRateModel
]
Instrument = Union[
    Bond,
    CompositeInstrument,
    CreditDefaultSwap,
    FloatFloatSwaption,
    Forward,
    NonstandardSwaption,
    Option,
    Stock,
    Swap,
    YoYInflationCapFloor,
]
TermStructure = Union[
    DefaultProbabilityTermStructure,
    InflationTermStructure,
    VolatilityTermStructure,
    YieldTermStructure,
]
Observable = Union[
    AndreasenHugeVolatilityInterpl,
    CalibratedModel,
    CashFlow,
    DefaultProbabilityHelper,
    Index,
    Instrument,
    PricingEngine,
    Quote,
    RateHelper,
    SmileSection,
    StochasticProcess,
    TermStructure,
    TermStructureConsistentModel,
]


AUDLibor.update_forward_refs()
ActualActual.update_forward_refs()
AmericanExercise.update_forward_refs()
AmortizingFixedRateBond0.update_forward_refs()
AmortizingFixedRateBond1.update_forward_refs()
AmortizingFloatingRateBond.update_forward_refs()
AmortizingPayment.update_forward_refs()
AnalyticBarrierEngine.update_forward_refs()
AnalyticBinaryBarrierEngine.update_forward_refs()
AnalyticCapFloorEngine.update_forward_refs()
AnalyticContinuousGeometricAveragePriceAsianEngine.update_forward_refs()
AnalyticDigitalAmericanEngine.update_forward_refs()
AnalyticDigitalAmericanKOEngine.update_forward_refs()
AnalyticDiscreteGeometricAveragePriceAsianEngine.update_forward_refs()
AnalyticDiscreteGeometricAverageStrikeAsianEngine.update_forward_refs()
AnalyticDividendEuropeanEngine.update_forward_refs()
AnalyticDoubleBarrierBinaryEngine.update_forward_refs()
AnalyticDoubleBarrierEngine.update_forward_refs()
AnalyticEuropeanEngine.update_forward_refs()
AnalyticHestonEngine0.update_forward_refs()
AnalyticHestonEngine1.update_forward_refs()
AnalyticHestonEngine2.update_forward_refs()
AndreasenHugeVolatilityInterpl.update_forward_refs()
AssetSwap.update_forward_refs()
AverageBasketPayoff0.update_forward_refs()
AverageBasketPayoff1.update_forward_refs()
BSMRNDCalculator.update_forward_refs()
BachelierSwaptionEngine0.update_forward_refs()
BaroneAdesiWhaleyApproximationEngine.update_forward_refs()
BarrierOption.update_forward_refs()
BasketOption.update_forward_refs()
BbswBase.update_forward_refs()
BermudanExercise.update_forward_refs()
BiborBase.update_forward_refs()
BinomialCRRConvertibleEngine.update_forward_refs()
BinomialCRRVanillaEngine.update_forward_refs()
BinomialJRConvertibleEngine.update_forward_refs()
BinomialJRVanillaEngine.update_forward_refs()
BinomialJoshi4ConvertibleEngine.update_forward_refs()
BinomialJoshi4VanillaEngine.update_forward_refs()
BinomialTianConvertibleEngine.update_forward_refs()
BinomialTianVanillaEngine.update_forward_refs()
BinomialTrigeorgisConvertibleEngine.update_forward_refs()
BinomialTrigeorgisVanillaEngine.update_forward_refs()
BjerksundStenslandApproximationEngine.update_forward_refs()
BkbmBase.update_forward_refs()
BlackCalculator.update_forward_refs()
BlackConstantVol0.update_forward_refs()
BlackConstantVol1.update_forward_refs()
BlackSwaptionEngine0.update_forward_refs()
BlackVarianceCurve.update_forward_refs()
BlackVolTermStructureHandle.update_forward_refs()
Bond0.update_forward_refs()
Bond1.update_forward_refs()
BondHelperBase.update_forward_refs()
Business252.update_forward_refs()
CADLibor.update_forward_refs()
CHFLibor.update_forward_refs()
COSHestonEngine.update_forward_refs()
CPIBond.update_forward_refs()
CPISwap.update_forward_refs()
CalibratedModelHandle.update_forward_refs()
CallabilityBase.update_forward_refs()
CallableFixedRateBond.update_forward_refs()
Cap.update_forward_refs()
CapFloorTermVolCurve0.update_forward_refs()
CapFloorTermVolCurve1.update_forward_refs()
CapFloorTermVolSurface0.update_forward_refs()
CapFloorTermVolSurface1.update_forward_refs()
CapFloorTermVolSurface2.update_forward_refs()
CapFloorTermVolSurface3.update_forward_refs()
CapFloorTermVolatilityStructureHandle.update_forward_refs()
CapHelper.update_forward_refs()
CappedFlooredCmsCoupon.update_forward_refs()
CappedFlooredCmsSpreadCoupon.update_forward_refs()
CappedFlooredCouponBase.update_forward_refs()
CappedFlooredIborCoupon.update_forward_refs()
CashFlows.update_forward_refs()
Cdor.update_forward_refs()
CdsOption.update_forward_refs()
ChfLiborSwapIsdaFix0.update_forward_refs()
ChfLiborSwapIsdaFix1.update_forward_refs()
CmsCoupon.update_forward_refs()
CmsMarket.update_forward_refs()
CmsMarketCalibration.update_forward_refs()
CmsRateBond.update_forward_refs()
CmsSpreadCoupon.update_forward_refs()
Collar.update_forward_refs()
CompositeConstraint.update_forward_refs()
ConstantOptionletVolatility0.update_forward_refs()
ConstantOptionletVolatility1.update_forward_refs()
ConstantParameter0.update_forward_refs()
ConstantParameter1.update_forward_refs()
ConstantSwaptionVolatility0.update_forward_refs()
ConstantSwaptionVolatility1.update_forward_refs()
ContinuousArithmeticAsianLevyEngine.update_forward_refs()
ContinuousAveragingAsianOption.update_forward_refs()
ConvertibleFixedCouponBond.update_forward_refs()
ConvertibleFloatingRateBond.update_forward_refs()
ConvertibleZeroCouponBond.update_forward_refs()
CraigSneydScheme.update_forward_refs()
CrankNicolsonScheme.update_forward_refs()
CreditDefaultSwap0.update_forward_refs()
CreditDefaultSwap1.update_forward_refs()
CubicBSplinesFitting.update_forward_refs()
CubicInterpolatedZeroCurve.update_forward_refs()
DKKLibor.update_forward_refs()
DailyTenorLiborBase.update_forward_refs()
DatedOISRateHelper.update_forward_refs()
DefaultLogCubicInterpolatedZeroCurve.update_forward_refs()
DefaultProbabilityTermStructureHandle.update_forward_refs()
DeltaVolQuoteHandle.update_forward_refs()
DepositRateHelper0.update_forward_refs()
DepositRateHelper1.update_forward_refs()
DiscountingSwapEngine.update_forward_refs()
DiscreteAveragingAsianOption.update_forward_refs()
DividendVanillaOption.update_forward_refs()
DoubleBarrierOptionBase.update_forward_refs()
DouglasScheme.update_forward_refs()
EURLiborBase.update_forward_refs()
EurLiborSwapIfrFix0.update_forward_refs()
EurLiborSwapIfrFix1.update_forward_refs()
EurLiborSwapIsdaFixA0.update_forward_refs()
EurLiborSwapIsdaFixA1.update_forward_refs()
EurLiborSwapIsdaFixB0.update_forward_refs()
EurLiborSwapIsdaFixB1.update_forward_refs()
Euribor365Base.update_forward_refs()
EuriborBase.update_forward_refs()
EuriborSwapIfrFix0.update_forward_refs()
EuriborSwapIfrFix1.update_forward_refs()
EuriborSwapIsdaFixA0.update_forward_refs()
EuriborSwapIsdaFixA1.update_forward_refs()
EuriborSwapIsdaFixB0.update_forward_refs()
EuriborSwapIsdaFixB1.update_forward_refs()
EuropeanExercise.update_forward_refs()
EuropeanOption.update_forward_refs()
EverestOption.update_forward_refs()
ExchangeRate.update_forward_refs()
ExplicitEulerScheme.update_forward_refs()
ExponentialSplinesFitting.update_forward_refs()
FDAmericanEngine.update_forward_refs()
FDBermudanEngine.update_forward_refs()
FDEuropeanEngine.update_forward_refs()
FDShoutEngine.update_forward_refs()
FaceValueAccrualClaim.update_forward_refs()
Fd2dBlackScholesVanillaEngine.update_forward_refs()
FdBlackScholesAsianEngine.update_forward_refs()
FdBlackScholesBarrierEngine.update_forward_refs()
FdBlackScholesVanillaEngine0.update_forward_refs()
FdBlackScholesVanillaEngine1.update_forward_refs()
FdHestonBarrierEngine.update_forward_refs()
FdHestonDoubleBarrierEngine.update_forward_refs()
FdHestonVanillaEngine0.update_forward_refs()
FdHestonVanillaEngine1.update_forward_refs()
FdOrnsteinUhlenbeckVanillaEngine.update_forward_refs()
FdSimpleBSSwingEngine.update_forward_refs()
Fdm1DimSolver.update_forward_refs()
Fdm2DimSolver.update_forward_refs()
Fdm2dBlackScholesOp.update_forward_refs()
Fdm3DimSolver.update_forward_refs()
Fdm4dimSolver.update_forward_refs()
Fdm5dimSolver.update_forward_refs()
Fdm6dimSolver.update_forward_refs()
FdmAmericanStepCondition.update_forward_refs()
FdmArithmeticAverageCondition.update_forward_refs()
FdmBackwardSolver.update_forward_refs()
FdmBatesOp.update_forward_refs()
FdmBermudanStepCondition.update_forward_refs()
FdmBlackScholesFwdOp.update_forward_refs()
FdmBlackScholesMesher.update_forward_refs()
FdmBlackScholesOp.update_forward_refs()
FdmCEVOp.update_forward_refs()
FdmDirichletBoundary.update_forward_refs()
FdmDiscountDirichletBoundary.update_forward_refs()
FdmDividendHandler.update_forward_refs()
FdmDupire1dOp.update_forward_refs()
FdmG2Op.update_forward_refs()
FdmHestonFwdOp.update_forward_refs()
FdmHestonHullWhiteOp.update_forward_refs()
FdmHestonLocalVolatilityVarianceMesher.update_forward_refs()
FdmHestonOp.update_forward_refs()
FdmHestonVarianceMesher.update_forward_refs()
FdmHullWhiteOp.update_forward_refs()
FdmLocalVolFwdOp.update_forward_refs()
FdmLogBasketInnerValue.update_forward_refs()
FdmLogInnerValue.update_forward_refs()
FdmMesherComposite0.update_forward_refs()
FdmMesherComposite1.update_forward_refs()
FdmMesherComposite2.update_forward_refs()
FdmOrnsteinUhlenbeckOp.update_forward_refs()
FdmQuantoHelper.update_forward_refs()
FdmSabrOp.update_forward_refs()
FdmSimpleProcess1dMesher.update_forward_refs()
FdmSimpleStorageCondition.update_forward_refs()
FdmSimpleSwingCondition.update_forward_refs()
FdmSquareRootFwdOp.update_forward_refs()
FdmZabrOp.update_forward_refs()
FirstDerivativeOp.update_forward_refs()
FittedBondDiscountCurve0.update_forward_refs()
FittedBondDiscountCurve1.update_forward_refs()
FixedDividend.update_forward_refs()
FixedRateBond0.update_forward_refs()
FixedRateBond1.update_forward_refs()
FixedRateBond2.update_forward_refs()
FixedRateBondForward.update_forward_refs()
FixedRateBondHelper.update_forward_refs()
FixedRateCoupon.update_forward_refs()
FlatForward0.update_forward_refs()
FlatForward1.update_forward_refs()
FlatHazardRate0.update_forward_refs()
FlatHazardRate1.update_forward_refs()
FlatSmileSection0.update_forward_refs()
FlatSmileSection1.update_forward_refs()
FloatFloatSwap.update_forward_refs()
FloatFloatSwaption.update_forward_refs()
FloatingRateBond.update_forward_refs()
Floor.update_forward_refs()
ForwardEuropeanEngine.update_forward_refs()
ForwardRateAgreement.update_forward_refs()
ForwardVanillaOptionBase.update_forward_refs()
FraRateHelper0.update_forward_refs()
FraRateHelper1.update_forward_refs()
FraRateHelper2.update_forward_refs()
FractionalDividend.update_forward_refs()
FuturesRateHelper0.update_forward_refs()
FuturesRateHelper1.update_forward_refs()
FuturesRateHelper2.update_forward_refs()
FuturesRateHelper3.update_forward_refs()
FuturesRateHelper4.update_forward_refs()
FuturesRateHelper5.update_forward_refs()
FxSwapRateHelper.update_forward_refs()
GBPLibor.update_forward_refs()
GBSMRNDCalculator.update_forward_refs()
Gaussian1dFloatFloatSwaptionEngine.update_forward_refs()
Gaussian1dJamshidianSwaptionEngine.update_forward_refs()
Gaussian1dNonstandardSwaptionEngine.update_forward_refs()
Gaussian1dSwaptionEngine.update_forward_refs()
GbpLiborSwapIsdaFix0.update_forward_refs()
GbpLiborSwapIsdaFix1.update_forward_refs()
GlobalBootstrap0.update_forward_refs()
Glued1dMesher.update_forward_refs()
Gsr.update_forward_refs()
GsrProcess.update_forward_refs()
HestonModelBase.update_forward_refs()
HestonModelHandle.update_forward_refs()
HestonModelHelper.update_forward_refs()
HestonRNDCalculator.update_forward_refs()
HestonSLVProcess.update_forward_refs()
HimalayaOption.update_forward_refs()
HundsdorferScheme.update_forward_refs()
IborCoupon.update_forward_refs()
IborIndexBase.update_forward_refs()
ImplicitEulerScheme.update_forward_refs()
ImpliedTermStructure.update_forward_refs()
IntegralCdsEngine.update_forward_refs()
IntegralEngine.update_forward_refs()
InterestRate.update_forward_refs()
JPYLibor.update_forward_refs()
JamshidianSwaptionEngine.update_forward_refs()
Jibar.update_forward_refs()
JointCalendar0.update_forward_refs()
JointCalendar1.update_forward_refs()
JointCalendar2.update_forward_refs()
JpyLiborSwapIsdaFixAm0.update_forward_refs()
JpyLiborSwapIsdaFixAm1.update_forward_refs()
JpyLiborSwapIsdaFixPm0.update_forward_refs()
JpyLiborSwapIsdaFixPm1.update_forward_refs()
JuQuadraticApproximationEngine.update_forward_refs()
KahaleSmileSection.update_forward_refs()
Libor.update_forward_refs()
LocalConstantVol0.update_forward_refs()
LocalConstantVol1.update_forward_refs()
LocalVolRNDCalculator.update_forward_refs()
LocalVolTermStructureHandle.update_forward_refs()
LogLinearInterpolatedZeroCurve.update_forward_refs()
LognormalCmsSpreadPricer.update_forward_refs()
MakeOIS.update_forward_refs()
MakeVanillaSwap.update_forward_refs()
MarkovFunctional0.update_forward_refs()
MarkovFunctional1.update_forward_refs()
MaxBasketPayoff.update_forward_refs()
MethodOfLinesScheme.update_forward_refs()
MinBasketPayoff.update_forward_refs()
ModifiedCraigSneydScheme.update_forward_refs()
Money0.update_forward_refs()
Money1.update_forward_refs()
MonotonicCubicInterpolatedZeroCurve.update_forward_refs()
Mosprime.update_forward_refs()
MultiplicativePriceSeasonality.update_forward_refs()
NZDLibor.update_forward_refs()
NelsonSiegelFitting.update_forward_refs()
NinePointLinearOpBase.update_forward_refs()
NoArbSabrInterpolatedSmileSection0.update_forward_refs()
NoArbSabrInterpolatedSmileSection1.update_forward_refs()
NoArbSabrSmileSection0.update_forward_refs()
NonhomogeneousBoundaryConstraint.update_forward_refs()
NonstandardSwap.update_forward_refs()
NonstandardSwaption.update_forward_refs()
NthOrderDerivativeOp.update_forward_refs()
OISRateHelper.update_forward_refs()
OptionletStripper1.update_forward_refs()
OptionletVolatilityStructureHandle.update_forward_refs()
OvernightIndexBase.update_forward_refs()
OvernightIndexFutureRateHelperBase.update_forward_refs()
OvernightIndexedCoupon.update_forward_refs()
OvernightIndexedSwap0.update_forward_refs()
OvernightIndexedSwap1.update_forward_refs()
OvernightIndexedSwapIndex.update_forward_refs()
PiecewiseConstantParameter.update_forward_refs()
PiecewiseTimeDependentHestonModel.update_forward_refs()
Pribor.update_forward_refs()
QuantoDoubleBarrierOption.update_forward_refs()
QuantoEuropeanEngine.update_forward_refs()
QuantoForwardEuropeanEngine.update_forward_refs()
QuantoForwardVanillaOption.update_forward_refs()
QuantoVanillaOption.update_forward_refs()
QuoteHandle.update_forward_refs()
RebatedExercise.update_forward_refs()
Redemption.update_forward_refs()
RelinkableBlackVolTermStructureHandle.update_forward_refs()
RelinkableCalibratedModelHandle.update_forward_refs()
RelinkableCapFloorTermVolatilityStructureHandle.update_forward_refs()
RelinkableDefaultProbabilityTermStructureHandle.update_forward_refs()
RelinkableDeltaVolQuoteHandle.update_forward_refs()
RelinkableLocalVolTermStructureHandle.update_forward_refs()
RelinkableOptionletVolatilityStructureHandle.update_forward_refs()
RelinkableQuoteHandle.update_forward_refs()
RelinkableShortRateModelHandle.update_forward_refs()
RelinkableSwaptionVolatilityStructureHandle.update_forward_refs()
RelinkableYieldTermStructureHandle.update_forward_refs()
Robor.update_forward_refs()
SEKLibor.update_forward_refs()
SVD.update_forward_refs()
SabrSmileSection1.update_forward_refs()
SafeBackwardFlatInterpolation.update_forward_refs()
SafeBicubicSpline.update_forward_refs()
SafeBilinearInterpolation.update_forward_refs()
SafeConvexMonotoneInterpolation.update_forward_refs()
SafeCubicNaturalSpline.update_forward_refs()
SafeForwardFlatInterpolation.update_forward_refs()
SafeFritschButlandCubic.update_forward_refs()
SafeFritschButlandLogCubic.update_forward_refs()
SafeKrugerCubic.update_forward_refs()
SafeKrugerLogCubic.update_forward_refs()
SafeLinearInterpolation.update_forward_refs()
SafeLogCubicNaturalSpline.update_forward_refs()
SafeLogLinearInterpolation.update_forward_refs()
SafeLogParabolic.update_forward_refs()
SafeMonotonicCubicNaturalSpline.update_forward_refs()
SafeMonotonicLogCubicNaturalSpline.update_forward_refs()
SafeMonotonicLogParabolic.update_forward_refs()
SafeMonotonicParabolic.update_forward_refs()
SafeParabolic.update_forward_refs()
SampledCurve.update_forward_refs()
SamplerMirrorGaussian.update_forward_refs()
Schedule0.update_forward_refs()
Schedule1.update_forward_refs()
SecondDerivativeOp.update_forward_refs()
SecondOrderMixedDerivativeOp.update_forward_refs()
Shibor.update_forward_refs()
ShortRateModelHandle.update_forward_refs()
SimpleCashFlow.update_forward_refs()
SimplePolynomialFitting.update_forward_refs()
SofrFutureRateHelper0.update_forward_refs()
SofrFutureRateHelper1.update_forward_refs()
SoftCallability.update_forward_refs()
SplineCubicInterpolatedZeroCurve.update_forward_refs()
SpreadBasketPayoff.update_forward_refs()
StochasticProcessArray.update_forward_refs()
StrippedOptionletAdapter.update_forward_refs()
StulzEngine.update_forward_refs()
SvenssonFitting.update_forward_refs()
SwapBase.update_forward_refs()
SwapIndexBase.update_forward_refs()
SwapRateHelper0.update_forward_refs()
SwapRateHelper1.update_forward_refs()
SwapSpreadIndex.update_forward_refs()
Swaption.update_forward_refs()
SwaptionHelper0.update_forward_refs()
SwaptionHelper1.update_forward_refs()
SwaptionHelper2.update_forward_refs()
SwaptionVolCube1.update_forward_refs()
SwaptionVolCube2.update_forward_refs()
SwaptionVolatilityMatrix0.update_forward_refs()
SwaptionVolatilityMatrix1.update_forward_refs()
SwaptionVolatilityMatrix2.update_forward_refs()
SwaptionVolatilityStructureHandle.update_forward_refs()
SwingExercise.update_forward_refs()
THBFIX.update_forward_refs()
TRLibor.update_forward_refs()
Tibor.update_forward_refs()
TimeBasket.update_forward_refs()
TreeCallableFixedRateBondEngine0.update_forward_refs()
TreeCallableFixedRateBondEngine1.update_forward_refs()
TreeCapFloorEngine0.update_forward_refs()
TreeCapFloorEngine1.update_forward_refs()
TreeSwaptionEngine1.update_forward_refs()
TridiagonalOperatorBase.update_forward_refs()
TripleBandLinearOpBase.update_forward_refs()
USDLibor.update_forward_refs()
UsdLiborSwapIsdaFixAm0.update_forward_refs()
UsdLiborSwapIsdaFixAm1.update_forward_refs()
UsdLiborSwapIsdaFixPm0.update_forward_refs()
UsdLiborSwapIsdaFixPm1.update_forward_refs()
VanillaOptionBase.update_forward_refs()
VanillaSwap.update_forward_refs()
VanillaSwingOption.update_forward_refs()
Wibor.update_forward_refs()
WulinYongDoubleBarrierEngine.update_forward_refs()
YearOnYearInflationSwap.update_forward_refs()
YieldTermStructureHandle.update_forward_refs()
YoYInflationCap.update_forward_refs()
YoYInflationCollar.update_forward_refs()
YoYInflationFloor.update_forward_refs()
ZeroCouponBond.update_forward_refs()
ZeroCouponInflationSwap.update_forward_refs()
ZeroCurve.update_forward_refs()
ZeroInflationIndexBase.update_forward_refs()
ZeroSpreadedTermStructure.update_forward_refs()
Zibor.update_forward_refs()
