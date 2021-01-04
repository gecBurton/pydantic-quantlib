from enum import Enum


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


class CzechMarket(Enum):
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
