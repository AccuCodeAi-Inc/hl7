from ...base import HL7Table

"""
HL7 Version: 2.5.1
Kind of quantity - 0254
Table Type: HL7
"""


class KindOfQuantity(HL7Table):
    """
    Kind of quantity - 0254 // HL7 table type
    - ABSORBANCE
    - CONCENTRATION_ARBITRARY_SUBSTANCE
    - STAR_ACTIVITY
    - APPEARANCE
    - STAR_ARBITRARY
    - AREA
    - ASPECT
    - STAR_CATALYTIC_ACTIVITY
    - STAR_CATALYTIC_CONTENT
    - CATALYTIC_CONCENTRATION_RATIO
    - STAR_CATALYTIC_FRACTION
    - CLASS
    - STAR_CATALYTIC_CONCENTRATION
    - STAR_CONSTANT
    - STAR_COEFFICIENT
    - COLOR
    - CONSISTENCY
    - STAR_CATALYTIC_RATE
    - CATALYTIC_RATIO
    - DENSITY
    - DEVICE
    - STAR_DIFFERENCE
    - ELASTICITY
    - ELECTRICAL_POTENTIAL
    - ELECTRICAL_CURRENT
    - ELECTRICAL_RESISTANCE
    - ENERGY
    - STAR_ENTITIC
    - STAR_ENTITIC_CATALYTIC_ACTIVITY
    - STAR_ENTITIC_NUMBER
    - STAR_ENTITIC_SUBSTANCE_OF_AMOUNT
    - STAR_ENTITIC_VOLUME
    - EQUILIBRIUM
    - MECHANICAL_FORCE
    - FREQUENCY
    - IMPRESSION_OR_INTERPRETATION_OF_STUDY
    - STAR_KINEMATIC_VISCOSITY
    - LENGTH
    - STAR_LENGTH_INCREMENT
    - STAR_LIQUEFACTION
    - STAR_MASS
    - STAR_MASS_CONCENTRATION
    - MASS_CONTENT
    - STAR_MASS_CONCENTRATION_RATIO
    - STAR_MASS_FRACTION
    - MAGNETIC_FLUX
    - STAR_MASS_INCREMENT
    - MORPHOLOGY
    - MOTILITY
    - STAR_MASS_RATE
    - STAR_MASS_RATIO
    - STAR_NUMBER_CONCENTRATION
    - STAR_NUMBER_CONTENT
    - STAR_NUMBER_FRACTION
    - STAR_NUMBER_RATIO
    - STAR_NUMBER
    - OPTICAL_DENSITY
    - STAR_OSMOLALITY
    - STAR_PRESSURE
    - PRESENCE_OR_IDENTITY_OR_EXISTENCE
    - POWER
    - STAR_RANGES
    - STAR_RATIOS
    - STAR_RECIPROCAL_RELATIVE_TIME
    - STAR_RELATIVE_DENSITY
    - STAR_RELATIVE
    - STAR_RELATIVE_MASS_CONCENTRATION
    - STAR_RELATIVE_SUBSTANCE_CONCENTRATION
    - STAR_RELATIVE_TIME
    - STAR_SATURATION_FRACTION
    - STAR_SUBSTANCE_CONCENTRATION
    - STAR_SUBSTANCE_CONCENTRATION_INCREMENT
    - STAR_SUBSTANCE_CONTENT
    - STAR_SUBSTANCE_CONTENT_RATE
    - STAR_SUBSTANCE_CONCENTRATION_RATIO
    - STAR_SUBSTANCE_FRACTION
    - SHAPE
    - SMELL
    - STAR_SUBSTANCE_RATE
    - STAR_SUBSTANCE_RATIO
    - STAR_SUBSTANCE_AMOUNT
    - STAR_SUSCEPTIBILITY
    - TASTE
    - STAR_TEMPERATURE
    - STAR_TEMPERATURE_DIFFERENCE
    - STAR_TEMPERATURE_INCREMENT
    - STAR_THRESHOLD_MASS_CONCENTRATION
    - STAR_THRESHOLD_SUBSTANCE_CONCENTRATION
    - STAR_TIME
    - STAR_DILUTION_FACTOR
    - STAR_TIME_DIFFERENCE
    - STAR_TIME_STAMP_DATE_AND_TIME
    - STAR_TIME_RATIO
    - STAR_TYPE
    - STAR_VOLUME_CONTENT
    - STAR_VELOCITY
    - STAR_VELOCITY_RATIO
    - STAR_VOLUME_FRACTION
    - STAR_VISCOSITY
    - STAR_VOLUME
    - STAR_VOLUME_RATE
    - STAR_VOLUME_RATIO
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0254
    """

    ABSORBANCE = "ABS"
    """Absorbance"""
    CONCENTRATION_ARBITRARY_SUBSTANCE = "ACNC"
    """Concentration, Arbitrary Substance"""
    STAR_ACTIVITY = "ACT"
    """*Activity"""
    APPEARANCE = "APER"
    """Appearance"""
    STAR_ARBITRARY = "ARB"
    """*Arbitrary"""
    AREA = "AREA"
    """Area"""
    ASPECT = "ASPECT"
    """Aspect"""
    STAR_CATALYTIC_ACTIVITY = "CACT"
    """*Catalytic Activity"""
    STAR_CATALYTIC_CONTENT = "CCNT"
    """*Catalytic Content"""
    CATALYTIC_CONCENTRATION_RATIO = "CCRTO"
    """Catalytic Concentration Ratio"""
    STAR_CATALYTIC_FRACTION = "CFR"
    """*Catalytic Fraction"""
    CLASS = "CLAS"
    """Class"""
    STAR_CATALYTIC_CONCENTRATION = "CNC"
    """*Catalytic Concentration"""
    STAR_CONSTANT = "CNST"
    """*Constant"""
    STAR_COEFFICIENT = "COEF"
    """*Coefficient"""
    COLOR = "COLOR"
    """Color"""
    CONSISTENCY = "CONS"
    """Consistency"""
    STAR_CATALYTIC_RATE = "CRAT"
    """*Catalytic Rate"""
    CATALYTIC_RATIO = "CRTO"
    """Catalytic Ratio"""
    DENSITY = "DEN"
    """Density"""
    DEVICE = "DEV"
    """Device"""
    STAR_DIFFERENCE = "DIFF"
    """*Difference"""
    ELASTICITY = "ELAS"
    """Elasticity"""
    ELECTRICAL_POTENTIAL = "ELPOT"
    """Electrical Potential (Voltage)"""
    ELECTRICAL_CURRENT = "ELRAT"
    """Electrical current (amperage)"""
    ELECTRICAL_RESISTANCE = "ELRES"
    """Electrical Resistance"""
    ENERGY = "ENGR"
    """Energy"""
    STAR_ENTITIC = "ENT"
    """*Entitic"""
    STAR_ENTITIC_CATALYTIC_ACTIVITY = "ENTCAT"
    """*Entitic Catalytic Activity"""
    STAR_ENTITIC_NUMBER = "ENTNUM"
    """*Entitic Number"""
    STAR_ENTITIC_SUBSTANCE_OF_AMOUNT = "ENTSUB"
    """*Entitic Substance of Amount"""
    STAR_ENTITIC_VOLUME = "ENTVOL"
    """*Entitic Volume"""
    EQUILIBRIUM = "EQL"
    """Equilibrium"""
    MECHANICAL_FORCE = "FORCE"
    """Mechanical force"""
    FREQUENCY = "FREQ"
    """Frequency"""
    IMPRESSION_OR_INTERPRETATION_OF_STUDY = "IMP"
    """Impression/ interpretation of study"""
    STAR_KINEMATIC_VISCOSITY = "KINV"
    """*Kinematic Viscosity"""
    LENGTH = "LEN"
    """Length"""
    STAR_LENGTH_INCREMENT = "LINC"
    """*Length Increment"""
    STAR_LIQUEFACTION = "LIQ"
    """*Liquefaction"""
    STAR_MASS = "MASS"
    """*Mass"""
    STAR_MASS_CONCENTRATION = "MCNC"
    """*Mass Concentration"""
    MASS_CONTENT = "MCNT"
    """Mass Content"""
    STAR_MASS_CONCENTRATION_RATIO = "MCRTO"
    """*Mass Concentration Ratio"""
    STAR_MASS_FRACTION = "MFR"
    """*Mass Fraction"""
    MAGNETIC_FLUX = "MGFLUX"
    """Magnetic flux"""
    STAR_MASS_INCREMENT = "MINC"
    """*Mass Increment"""
    MORPHOLOGY = "MORPH"
    """Morphology"""
    MOTILITY = "MOTIL"
    """Motility"""
    STAR_MASS_RATE = "MRAT"
    """*Mass Rate"""
    STAR_MASS_RATIO = "MRTO"
    """*Mass Ratio"""
    STAR_NUMBER_CONCENTRATION = "NCNC"
    """*Number Concentration"""
    STAR_NUMBER_CONTENT = "NCNT"
    """*Number Content"""
    STAR_NUMBER_FRACTION = "NFR"
    """*Number Fraction"""
    STAR_NUMBER_RATIO = "NRTO"
    """*Number Ratio"""
    STAR_NUMBER = "NUM"
    """*Number"""
    OPTICAL_DENSITY = "OD"
    """Optical density"""
    STAR_OSMOLALITY = "OSMOL"
    """*Osmolality"""
    STAR_PRESSURE = "PRES"
    """*Pressure (Partial)"""
    PRESENCE_OR_IDENTITY_OR_EXISTENCE = "PRID"
    """Presence/Identity/Existence"""
    POWER = "PWR"
    """Power (wattage)"""
    STAR_RANGES = "RANGE"
    """*Ranges"""
    STAR_RATIOS = "RATIO"
    """*Ratios"""
    STAR_RECIPROCAL_RELATIVE_TIME = "RCRLTM"
    """*Reciprocal Relative Time"""
    STAR_RELATIVE_DENSITY = "RDEN"
    """*Relative Density"""
    STAR_RELATIVE = "REL"
    """*Relative"""
    STAR_RELATIVE_MASS_CONCENTRATION = "RLMCNC"
    """*Relative Mass Concentration"""
    STAR_RELATIVE_SUBSTANCE_CONCENTRATION = "RLSCNC"
    """*Relative Substance Concentration"""
    STAR_RELATIVE_TIME = "RLTM"
    """*Relative Time"""
    STAR_SATURATION_FRACTION = "SATFR"
    """*Saturation Fraction"""
    STAR_SUBSTANCE_CONCENTRATION = "SCNC"
    """*Substance Concentration"""
    STAR_SUBSTANCE_CONCENTRATION_INCREMENT = "SCNCIN"
    """*Substance Concentration Increment"""
    STAR_SUBSTANCE_CONTENT = "SCNT"
    """*Substance Content"""
    STAR_SUBSTANCE_CONTENT_RATE = "SCNTR"
    """*Substance Content Rate"""
    STAR_SUBSTANCE_CONCENTRATION_RATIO = "SCRTO"
    """*Substance Concentration Ratio"""
    STAR_SUBSTANCE_FRACTION = "SFR"
    """*Substance Fraction"""
    SHAPE = "SHAPE"
    """Shape"""
    SMELL = "SMELL"
    """Smell"""
    STAR_SUBSTANCE_RATE = "SRAT"
    """*Substance Rate"""
    STAR_SUBSTANCE_RATIO = "SRTO"
    """*Substance Ratio"""
    STAR_SUBSTANCE_AMOUNT = "SUB"
    """*Substance Amount"""
    STAR_SUSCEPTIBILITY = "SUSC"
    """*Susceptibility"""
    TASTE = "TASTE"
    """Taste"""
    STAR_TEMPERATURE = "TEMP"
    """*Temperature"""
    STAR_TEMPERATURE_DIFFERENCE = "TEMPDF"
    """*Temperature Difference"""
    STAR_TEMPERATURE_INCREMENT = "TEMPIN"
    """*Temperature Increment"""
    STAR_THRESHOLD_MASS_CONCENTRATION = "THRMCNC"
    """*Threshold Mass Concentration"""
    STAR_THRESHOLD_SUBSTANCE_CONCENTRATION = "THRSCNC"
    """*Threshold Substance Concentration"""
    STAR_TIME = "TIME"
    """*Time (e.g. seconds)"""
    STAR_DILUTION_FACTOR = "TITR"
    """*Dilution Factor (Titer)"""
    STAR_TIME_DIFFERENCE = "TMDF"
    """*Time Difference"""
    STAR_TIME_STAMP_DATE_AND_TIME = "TMSTP"
    """*Time Stamp -- Date and Time"""
    STAR_TIME_RATIO = "TRTO"
    """*Time Ratio"""
    STAR_TYPE = "TYPE"
    """*Type"""
    STAR_VOLUME_CONTENT = "VCNT"
    """*Volume Content"""
    STAR_VELOCITY = "VEL"
    """*Velocity"""
    STAR_VELOCITY_RATIO = "VELRT"
    """*Velocity Ratio"""
    STAR_VOLUME_FRACTION = "VFR"
    """*Volume Fraction"""
    STAR_VISCOSITY = "VISC"
    """*Viscosity"""
    STAR_VOLUME = "VOL"
    """*Volume"""
    STAR_VOLUME_RATE = "VRAT"
    """*Volume Rate"""
    STAR_VOLUME_RATIO = "VRTO"
    """*Volume Ratio"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    KindOfQuantity.ABSORBANCE: "Absorbance",
    KindOfQuantity.CONCENTRATION_ARBITRARY_SUBSTANCE: "Concentration, Arbitrary Substance",
    KindOfQuantity.STAR_ACTIVITY: "*Activity",
    KindOfQuantity.APPEARANCE: "Appearance",
    KindOfQuantity.STAR_ARBITRARY: "*Arbitrary",
    KindOfQuantity.AREA: "Area",
    KindOfQuantity.ASPECT: "Aspect",
    KindOfQuantity.STAR_CATALYTIC_ACTIVITY: "*Catalytic Activity",
    KindOfQuantity.STAR_CATALYTIC_CONTENT: "*Catalytic Content",
    KindOfQuantity.CATALYTIC_CONCENTRATION_RATIO: "Catalytic Concentration Ratio",
    KindOfQuantity.STAR_CATALYTIC_FRACTION: "*Catalytic Fraction",
    KindOfQuantity.CLASS: "Class",
    KindOfQuantity.STAR_CATALYTIC_CONCENTRATION: "*Catalytic Concentration",
    KindOfQuantity.STAR_CONSTANT: "*Constant",
    KindOfQuantity.STAR_COEFFICIENT: "*Coefficient",
    KindOfQuantity.COLOR: "Color",
    KindOfQuantity.CONSISTENCY: "Consistency",
    KindOfQuantity.STAR_CATALYTIC_RATE: "*Catalytic Rate",
    KindOfQuantity.CATALYTIC_RATIO: "Catalytic Ratio",
    KindOfQuantity.DENSITY: "Density",
    KindOfQuantity.DEVICE: "Device",
    KindOfQuantity.STAR_DIFFERENCE: "*Difference",
    KindOfQuantity.ELASTICITY: "Elasticity",
    KindOfQuantity.ELECTRICAL_POTENTIAL: "Electrical Potential (Voltage)",
    KindOfQuantity.ELECTRICAL_CURRENT: "Electrical current (amperage)",
    KindOfQuantity.ELECTRICAL_RESISTANCE: "Electrical Resistance",
    KindOfQuantity.ENERGY: "Energy",
    KindOfQuantity.STAR_ENTITIC: "*Entitic",
    KindOfQuantity.STAR_ENTITIC_CATALYTIC_ACTIVITY: "*Entitic Catalytic Activity",
    KindOfQuantity.STAR_ENTITIC_NUMBER: "*Entitic Number",
    KindOfQuantity.STAR_ENTITIC_SUBSTANCE_OF_AMOUNT: "*Entitic Substance of Amount",
    KindOfQuantity.STAR_ENTITIC_VOLUME: "*Entitic Volume",
    KindOfQuantity.EQUILIBRIUM: "Equilibrium",
    KindOfQuantity.MECHANICAL_FORCE: "Mechanical force",
    KindOfQuantity.FREQUENCY: "Frequency",
    KindOfQuantity.IMPRESSION_OR_INTERPRETATION_OF_STUDY: "Impression/ interpretation of study",
    KindOfQuantity.STAR_KINEMATIC_VISCOSITY: "*Kinematic Viscosity",
    KindOfQuantity.LENGTH: "Length",
    KindOfQuantity.STAR_LENGTH_INCREMENT: "*Length Increment",
    KindOfQuantity.STAR_LIQUEFACTION: "*Liquefaction",
    KindOfQuantity.STAR_MASS: "*Mass",
    KindOfQuantity.STAR_MASS_CONCENTRATION: "*Mass Concentration",
    KindOfQuantity.MASS_CONTENT: "Mass Content",
    KindOfQuantity.STAR_MASS_CONCENTRATION_RATIO: "*Mass Concentration Ratio",
    KindOfQuantity.STAR_MASS_FRACTION: "*Mass Fraction",
    KindOfQuantity.MAGNETIC_FLUX: "Magnetic flux",
    KindOfQuantity.STAR_MASS_INCREMENT: "*Mass Increment",
    KindOfQuantity.MORPHOLOGY: "Morphology",
    KindOfQuantity.MOTILITY: "Motility",
    KindOfQuantity.STAR_MASS_RATE: "*Mass Rate",
    KindOfQuantity.STAR_MASS_RATIO: "*Mass Ratio",
    KindOfQuantity.STAR_NUMBER_CONCENTRATION: "*Number Concentration",
    KindOfQuantity.STAR_NUMBER_CONTENT: "*Number Content",
    KindOfQuantity.STAR_NUMBER_FRACTION: "*Number Fraction",
    KindOfQuantity.STAR_NUMBER_RATIO: "*Number Ratio",
    KindOfQuantity.STAR_NUMBER: "*Number",
    KindOfQuantity.OPTICAL_DENSITY: "Optical density",
    KindOfQuantity.STAR_OSMOLALITY: "*Osmolality",
    KindOfQuantity.STAR_PRESSURE: "*Pressure (Partial)",
    KindOfQuantity.PRESENCE_OR_IDENTITY_OR_EXISTENCE: "Presence/Identity/Existence",
    KindOfQuantity.POWER: "Power (wattage)",
    KindOfQuantity.STAR_RANGES: "*Ranges",
    KindOfQuantity.STAR_RATIOS: "*Ratios",
    KindOfQuantity.STAR_RECIPROCAL_RELATIVE_TIME: "*Reciprocal Relative Time",
    KindOfQuantity.STAR_RELATIVE_DENSITY: "*Relative Density",
    KindOfQuantity.STAR_RELATIVE: "*Relative",
    KindOfQuantity.STAR_RELATIVE_MASS_CONCENTRATION: "*Relative Mass Concentration",
    KindOfQuantity.STAR_RELATIVE_SUBSTANCE_CONCENTRATION: "*Relative Substance Concentration",
    KindOfQuantity.STAR_RELATIVE_TIME: "*Relative Time",
    KindOfQuantity.STAR_SATURATION_FRACTION: "*Saturation Fraction",
    KindOfQuantity.STAR_SUBSTANCE_CONCENTRATION: "*Substance Concentration",
    KindOfQuantity.STAR_SUBSTANCE_CONCENTRATION_INCREMENT: "*Substance Concentration Increment",
    KindOfQuantity.STAR_SUBSTANCE_CONTENT: "*Substance Content",
    KindOfQuantity.STAR_SUBSTANCE_CONTENT_RATE: "*Substance Content Rate",
    KindOfQuantity.STAR_SUBSTANCE_CONCENTRATION_RATIO: "*Substance Concentration Ratio",
    KindOfQuantity.STAR_SUBSTANCE_FRACTION: "*Substance Fraction",
    KindOfQuantity.SHAPE: "Shape",
    KindOfQuantity.SMELL: "Smell",
    KindOfQuantity.STAR_SUBSTANCE_RATE: "*Substance Rate",
    KindOfQuantity.STAR_SUBSTANCE_RATIO: "*Substance Ratio",
    KindOfQuantity.STAR_SUBSTANCE_AMOUNT: "*Substance Amount",
    KindOfQuantity.STAR_SUSCEPTIBILITY: "*Susceptibility",
    KindOfQuantity.TASTE: "Taste",
    KindOfQuantity.STAR_TEMPERATURE: "*Temperature",
    KindOfQuantity.STAR_TEMPERATURE_DIFFERENCE: "*Temperature Difference",
    KindOfQuantity.STAR_TEMPERATURE_INCREMENT: "*Temperature Increment",
    KindOfQuantity.STAR_THRESHOLD_MASS_CONCENTRATION: "*Threshold Mass Concentration",
    KindOfQuantity.STAR_THRESHOLD_SUBSTANCE_CONCENTRATION: "*Threshold Substance Concentration",
    KindOfQuantity.STAR_TIME: "*Time (e.g. seconds)",
    KindOfQuantity.STAR_DILUTION_FACTOR: "*Dilution Factor (Titer)",
    KindOfQuantity.STAR_TIME_DIFFERENCE: "*Time Difference",
    KindOfQuantity.STAR_TIME_STAMP_DATE_AND_TIME: "*Time Stamp -- Date and Time",
    KindOfQuantity.STAR_TIME_RATIO: "*Time Ratio",
    KindOfQuantity.STAR_TYPE: "*Type",
    KindOfQuantity.STAR_VOLUME_CONTENT: "*Volume Content",
    KindOfQuantity.STAR_VELOCITY: "*Velocity",
    KindOfQuantity.STAR_VELOCITY_RATIO: "*Velocity Ratio",
    KindOfQuantity.STAR_VOLUME_FRACTION: "*Volume Fraction",
    KindOfQuantity.STAR_VISCOSITY: "*Viscosity",
    KindOfQuantity.STAR_VOLUME: "*Volume",
    KindOfQuantity.STAR_VOLUME_RATE: "*Volume Rate",
    KindOfQuantity.STAR_VOLUME_RATIO: "*Volume Ratio",
}
