from ...base import HL7Table

"""
HL7 Version: 2.5.1
Degree/license/certificate - 0360
Table Type: User
"""


class DegreeOrLicenseOrCertificate(HL7Table):
    """
    Degree/license/certificate - 0360 // User table type
    - ASSOCIATE_OF_ARTS
    - ASSOCIATE_OF_APPLIED_SCIENCE
    - ASSOCIATE_OF_BUSINESS_ADMINISTRATION
    - ASSOCIATE_OF_ENGINEERING
    - ASSOCIATE_OF_SCIENCE
    - BACHELOR_OF_ARTS
    - BACHELOR_OF_BUSINESS_ADMINISTRATION
    - BACHELOR_OR_ENGINEERING
    - BACHELOR_OF_FINE_ARTS
    - BACHELOR_OF_NURSING
    - BACHELOR_OF_SCIENCE
    - BACHELOR_OF_SCIENCE_LAW
    - BACHELOR_ON_SCIENCE_NURSING
    - BACHELOR_OF_THEOLOGY
    - CERTIFIED_ADULT_NURSE_PRACTITIONER
    - CERTIFICATE
    - CERTIFIED_MEDICAL_ASSISTANT
    - CERTIFIED_NURSE_MIDWIFE
    - CERTIFIED_NURSE_PRACTITIONER
    - CERTIFIED_NURSE_SPECIALIST
    - CERTIFIED_PEDIATRIC_NURSE_PRACTITIONER
    - CERTIFIED_REGISTERED_NURSE
    - DOCTOR_OF_BUSINESS_ADMINISTRATION
    - DOCTOR_OF_EDUCATION
    - DIPLOMA
    - DOCTOR_OF_OSTEOPATHY
    - EMERGENCY_MEDICAL_TECHNICIAN
    - EMERGENCY_MEDICAL_TECHNICIAN_PARAMEDIC
    - FAMILY_PRACTICE_NURSE_PRACTITIONER
    - HIGH_SCHOOL_GRADUATE
    - JURIS_DOCTOR
    - MASTER_OF_ARTS
    - MASTER_OF_BUSINESS_ADMINISTRATION
    - MASTER_OF_CIVIL_ENGINEERING
    - DOCTOR_OF_MEDICINE
    - MEDICAL_ASSISTANT
    - MASTER_OF_DIVINITY
    - MASTER_OF_ENGINEERING
    - MASTER_OF_EDUCATION
    - MASTER_OF_ELECTRICAL_ENGINEERING
    - MASTER_OF_FINE_ARTS
    - MASTER_OF_MECHANICAL_ENGINEERING
    - MASTER_OF_SCIENCE
    - MASTER_OF_SCIENCE_LAW
    - MASTER_OF_SCIENCE_NURSING
    - MASTER_OF_THEOLOGY
    - MEDICAL_TECHNICIAN
    - NON_GRADUATE
    - NURSE_PRACTITIONER
    - PHYSICIAN_ASSISTANT
    - DOCTOR_OF_PHARMACY
    - DOCTOR_OF_PHILOSOPHY
    - DOCTOR_OF_ENGINEERING
    - DOCTOR_OF_SCIENCE
    - ADVANCED_PRACTICE_NURSE
    - REGISTERED_MEDICAL_ASSISTANT
    - REGISTERED_PHARMACIST
    - SECRETARIAL_CERTIFICATE
    - TRADE_SCHOOL_GRADUATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0360
    """

    ASSOCIATE_OF_ARTS = "AA"
    """Associate of Arts"""
    ASSOCIATE_OF_APPLIED_SCIENCE = "AAS"
    """Associate of Applied Science"""
    ASSOCIATE_OF_BUSINESS_ADMINISTRATION = "ABA"
    """Associate of Business Administration"""
    ASSOCIATE_OF_ENGINEERING = "AE"
    """Associate of Engineering"""
    ASSOCIATE_OF_SCIENCE = "AS"
    """Associate of Science"""
    BACHELOR_OF_ARTS = "BA"
    """Bachelor of Arts"""
    BACHELOR_OF_BUSINESS_ADMINISTRATION = "BBA"
    """Bachelor of Business Administration"""
    BACHELOR_OR_ENGINEERING = "BE"
    """Bachelor or Engineering"""
    BACHELOR_OF_FINE_ARTS = "BFA"
    """Bachelor of Fine Arts"""
    BACHELOR_OF_NURSING = "BN"
    """Bachelor of Nursing"""
    BACHELOR_OF_SCIENCE = "BS"
    """Bachelor of Science"""
    BACHELOR_OF_SCIENCE_LAW = "BSL"
    """Bachelor of Science - Law"""
    BACHELOR_ON_SCIENCE_NURSING = "BSN"
    """Bachelor on Science - Nursing"""
    BACHELOR_OF_THEOLOGY = "BT"
    """Bachelor of Theology"""
    CERTIFIED_ADULT_NURSE_PRACTITIONER = "CANP"
    """Certified Adult Nurse Practitioner"""
    CERTIFICATE = "CER"
    """Certificate"""
    CERTIFIED_MEDICAL_ASSISTANT = "CMA"
    """Certified Medical Assistant"""
    CERTIFIED_NURSE_MIDWIFE = "CNM"
    """Certified Nurse Midwife"""
    CERTIFIED_NURSE_PRACTITIONER = "CNP"
    """Certified Nurse Practitioner"""
    CERTIFIED_NURSE_SPECIALIST = "CNS"
    """Certified Nurse Specialist"""
    CERTIFIED_PEDIATRIC_NURSE_PRACTITIONER = "CPNP"
    """Certified Pediatric Nurse Practitioner"""
    CERTIFIED_REGISTERED_NURSE = "CRN"
    """Certified Registered Nurse"""
    DOCTOR_OF_BUSINESS_ADMINISTRATION = "DBA"
    """Doctor of Business Administration"""
    DOCTOR_OF_EDUCATION = "DED"
    """Doctor of Education"""
    DIPLOMA = "DIP"
    """Diploma"""
    DOCTOR_OF_OSTEOPATHY = "DO"
    """Doctor of Osteopathy"""
    EMERGENCY_MEDICAL_TECHNICIAN = "EMT"
    """Emergency Medical Technician"""
    EMERGENCY_MEDICAL_TECHNICIAN_PARAMEDIC = "EMTP"
    """Emergency Medical Technician - Paramedic"""
    FAMILY_PRACTICE_NURSE_PRACTITIONER = "FPNP"
    """Family Practice Nurse Practitioner"""
    HIGH_SCHOOL_GRADUATE = "HS"
    """High School Graduate"""
    JURIS_DOCTOR = "JD"
    """Juris Doctor"""
    MASTER_OF_ARTS = "MA"
    """Master of Arts"""
    MASTER_OF_BUSINESS_ADMINISTRATION = "MBA"
    """Master of Business Administration"""
    MASTER_OF_CIVIL_ENGINEERING = "MCE"
    """Master of Civil Engineering"""
    DOCTOR_OF_MEDICINE = "MD"
    """Doctor of Medicine"""
    MEDICAL_ASSISTANT = "MDA"
    """Medical Assistant"""
    MASTER_OF_DIVINITY = "MDI"
    """Master of Divinity"""
    MASTER_OF_ENGINEERING = "ME"
    """Master of Engineering"""
    MASTER_OF_EDUCATION = "MED"
    """Master of Education"""
    MASTER_OF_ELECTRICAL_ENGINEERING = "MEE"
    """Master of Electrical Engineering"""
    MASTER_OF_FINE_ARTS = "MFA"
    """Master of Fine Arts"""
    MASTER_OF_MECHANICAL_ENGINEERING = "MME"
    """Master of Mechanical Engineering"""
    MASTER_OF_SCIENCE = "MS"
    """Master of Science"""
    MASTER_OF_SCIENCE_LAW = "MSL"
    """Master of Science - Law"""
    MASTER_OF_SCIENCE_NURSING = "MSN"
    """Master of Science - Nursing"""
    MASTER_OF_THEOLOGY = "MT"
    """Master of Theology"""
    MEDICAL_TECHNICIAN = "MT"
    """Medical Technician"""
    NON_GRADUATE = "NG"
    """Non-Graduate"""
    NURSE_PRACTITIONER = "NP"
    """Nurse Practitioner"""
    PHYSICIAN_ASSISTANT = "PA"
    """Physician Assistant"""
    DOCTOR_OF_PHARMACY = "PharmD"
    """Doctor of Pharmacy"""
    DOCTOR_OF_PHILOSOPHY = "PHD"
    """Doctor of Philosophy"""
    DOCTOR_OF_ENGINEERING = "PHE"
    """Doctor of Engineering"""
    DOCTOR_OF_SCIENCE = "PHS"
    """Doctor of Science"""
    ADVANCED_PRACTICE_NURSE = "PN"
    """Advanced Practice Nurse"""
    REGISTERED_MEDICAL_ASSISTANT = "RMA"
    """Registered Medical Assistant"""
    REGISTERED_PHARMACIST = "RPH"
    """Registered Pharmacist"""
    SECRETARIAL_CERTIFICATE = "SEC"
    """Secretarial Certificate"""
    TRADE_SCHOOL_GRADUATE = "TS"
    """Trade School Graduate"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DegreeOrLicenseOrCertificate.ASSOCIATE_OF_ARTS: "Associate of Arts",
    DegreeOrLicenseOrCertificate.ASSOCIATE_OF_APPLIED_SCIENCE: "Associate of Applied Science",
    DegreeOrLicenseOrCertificate.ASSOCIATE_OF_BUSINESS_ADMINISTRATION: "Associate of Business Administration",
    DegreeOrLicenseOrCertificate.ASSOCIATE_OF_ENGINEERING: "Associate of Engineering",
    DegreeOrLicenseOrCertificate.ASSOCIATE_OF_SCIENCE: "Associate of Science",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_ARTS: "Bachelor of Arts",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_BUSINESS_ADMINISTRATION: "Bachelor of Business Administration",
    DegreeOrLicenseOrCertificate.BACHELOR_OR_ENGINEERING: "Bachelor or Engineering",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_FINE_ARTS: "Bachelor of Fine Arts",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_NURSING: "Bachelor of Nursing",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_SCIENCE: "Bachelor of Science",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_SCIENCE_LAW: "Bachelor of Science - Law",
    DegreeOrLicenseOrCertificate.BACHELOR_ON_SCIENCE_NURSING: "Bachelor on Science - Nursing",
    DegreeOrLicenseOrCertificate.BACHELOR_OF_THEOLOGY: "Bachelor of Theology",
    DegreeOrLicenseOrCertificate.CERTIFIED_ADULT_NURSE_PRACTITIONER: "Certified Adult Nurse Practitioner",
    DegreeOrLicenseOrCertificate.CERTIFICATE: "Certificate",
    DegreeOrLicenseOrCertificate.CERTIFIED_MEDICAL_ASSISTANT: "Certified Medical Assistant",
    DegreeOrLicenseOrCertificate.CERTIFIED_NURSE_MIDWIFE: "Certified Nurse Midwife",
    DegreeOrLicenseOrCertificate.CERTIFIED_NURSE_PRACTITIONER: "Certified Nurse Practitioner",
    DegreeOrLicenseOrCertificate.CERTIFIED_NURSE_SPECIALIST: "Certified Nurse Specialist",
    DegreeOrLicenseOrCertificate.CERTIFIED_PEDIATRIC_NURSE_PRACTITIONER: "Certified Pediatric Nurse Practitioner",
    DegreeOrLicenseOrCertificate.CERTIFIED_REGISTERED_NURSE: "Certified Registered Nurse",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_BUSINESS_ADMINISTRATION: "Doctor of Business Administration",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_EDUCATION: "Doctor of Education",
    DegreeOrLicenseOrCertificate.DIPLOMA: "Diploma",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_OSTEOPATHY: "Doctor of Osteopathy",
    DegreeOrLicenseOrCertificate.EMERGENCY_MEDICAL_TECHNICIAN: "Emergency Medical Technician",
    DegreeOrLicenseOrCertificate.EMERGENCY_MEDICAL_TECHNICIAN_PARAMEDIC: "Emergency Medical Technician - Paramedic",
    DegreeOrLicenseOrCertificate.FAMILY_PRACTICE_NURSE_PRACTITIONER: "Family Practice Nurse Practitioner",
    DegreeOrLicenseOrCertificate.HIGH_SCHOOL_GRADUATE: "High School Graduate",
    DegreeOrLicenseOrCertificate.JURIS_DOCTOR: "Juris Doctor",
    DegreeOrLicenseOrCertificate.MASTER_OF_ARTS: "Master of Arts",
    DegreeOrLicenseOrCertificate.MASTER_OF_BUSINESS_ADMINISTRATION: "Master of Business Administration",
    DegreeOrLicenseOrCertificate.MASTER_OF_CIVIL_ENGINEERING: "Master of Civil Engineering",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_MEDICINE: "Doctor of Medicine",
    DegreeOrLicenseOrCertificate.MEDICAL_ASSISTANT: "Medical Assistant",
    DegreeOrLicenseOrCertificate.MASTER_OF_DIVINITY: "Master of Divinity",
    DegreeOrLicenseOrCertificate.MASTER_OF_ENGINEERING: "Master of Engineering",
    DegreeOrLicenseOrCertificate.MASTER_OF_EDUCATION: "Master of Education",
    DegreeOrLicenseOrCertificate.MASTER_OF_ELECTRICAL_ENGINEERING: "Master of Electrical Engineering",
    DegreeOrLicenseOrCertificate.MASTER_OF_FINE_ARTS: "Master of Fine Arts",
    DegreeOrLicenseOrCertificate.MASTER_OF_MECHANICAL_ENGINEERING: "Master of Mechanical Engineering",
    DegreeOrLicenseOrCertificate.MASTER_OF_SCIENCE: "Master of Science",
    DegreeOrLicenseOrCertificate.MASTER_OF_SCIENCE_LAW: "Master of Science - Law",
    DegreeOrLicenseOrCertificate.MASTER_OF_SCIENCE_NURSING: "Master of Science - Nursing",
    DegreeOrLicenseOrCertificate.MASTER_OF_THEOLOGY: "Master of Theology",
    DegreeOrLicenseOrCertificate.MEDICAL_TECHNICIAN: "Medical Technician",
    DegreeOrLicenseOrCertificate.NON_GRADUATE: "Non-Graduate",
    DegreeOrLicenseOrCertificate.NURSE_PRACTITIONER: "Nurse Practitioner",
    DegreeOrLicenseOrCertificate.PHYSICIAN_ASSISTANT: "Physician Assistant",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_PHARMACY: "Doctor of Pharmacy",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_PHILOSOPHY: "Doctor of Philosophy",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_ENGINEERING: "Doctor of Engineering",
    DegreeOrLicenseOrCertificate.DOCTOR_OF_SCIENCE: "Doctor of Science",
    DegreeOrLicenseOrCertificate.ADVANCED_PRACTICE_NURSE: "Advanced Practice Nurse",
    DegreeOrLicenseOrCertificate.REGISTERED_MEDICAL_ASSISTANT: "Registered Medical Assistant",
    DegreeOrLicenseOrCertificate.REGISTERED_PHARMACIST: "Registered Pharmacist",
    DegreeOrLicenseOrCertificate.SECRETARIAL_CERTIFICATE: "Secretarial Certificate",
    DegreeOrLicenseOrCertificate.TRADE_SCHOOL_GRADUATE: "Trade School Graduate",
}
