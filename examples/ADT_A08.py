import asyncio

from temporalio import activity, workflow
from functools import partial
from datetime import timedelta

# fmt: off
from hl7.v2_5_1.trigger_events import (
    ADT_A08
)
from hl7.v2_5_1.segment_groups import (
    ADT_A08_PROCEDURE_GROUP, ADT_A08_INSURANCE_GROUP
)
from hl7.v2_5_1.segments import (
    EVN, MSH, SFT, PV2, OBX, DB1, PD1, NK1, PID, UB2, ACC, PV1, AL1, ROL, DG1, IN3, DRG, IN1, PR1, IN2, PDA, UB1, GT1
)
from hl7.v2_5_1.data_types import (
    DTN, PL, DR, DLD, CE, DT, DLN, IS, TX, AUI, XPN, SI, TS, FC, CX, RMC, DTM, VARIES, DDI, UVC, PT, SAD, XTN, HD, XCN, VID, XAD, CNE, MO, JCC, ICD, XON, OSP, CWE, ST, NM, MSG, MOP, PTA, CP, EI, FN, ID, OCD
)
from hl7.v2_5_1.tables import (
    NameType, CoverageType, StudentStatus, InsuranceCompanyContactReason, AdmissionType, RecreationalDrugUseCode, ProcessingId, AllergySeverity, DiagnosisPriority, SegmentActionCode, NatureOfAbnormalTesting, DayType, Religion, Precision, ContactRole, Race, ProcedureFunctionalType, VisitIndicator, DiagnosisClassification, EligibilitySource, AmbulatoryStatus, TelecommunicationEquipmentType, ObservationResultStatusCodesInterpretation, ZipCode, Lastname, PriceType, VisitUserCode, PatientConditionCode, MailClaimParty, PersonLocationType, CountryCode, OrganizationalNameType, OrganDonorCode, RoomType, DegreeOrLicenseOrCertificate, AlternateCharacterSets, ReAdmissionIndicator, AcceptOrApplicationAcknowledgmentConditions, ProblemOrGoalActionCode, MessageType, PublicityCode, PatientStatusCode, NameOrAddressRepresentation, Relationship, YesOrNoIndicator, AdministrativeSex, ValueType, DischargeDisposition, State, MoneyOrPercentageIndicator, ProcessingMode, HospitalService, CpRangeType, City, DrgTransferType, LivingWillCode, PatientSRelationshipToInsured, CheckDigitScheme, TissueTypeCode, EthnicGroup, PurgeStatusCode, LivingDependency, SpecialProgramCode, TelecommunicationUseCode, ProcedureDrgType, FirstName, PolicyType, ModeOfArrivalCode, BedStatus, CertificationPatientType, MilitaryStatus, AdvanceDirectiveCode, CurrencyCodes, NotifyClergyCode, IdentityReliabilityCode, AddressType, JobStatus, EmploymentStatus, AdmitSource, StateOrProvince, UniversalIdType, MilitaryRankOrGrade, NameAssemblyOrder, PatientClass, EventType, MaritalStatus, PrecautionCode, ProductionClassCode, LivingArrangement, DisabledPersonCode, ImmunizationRegistryStatus, ProcedurePriority, AmountClass, CodingSystem, DrgPayor, AmountType, OutlierType, ReleaseInformation, CoordinationOfBenefits, MessageStructure, IdentifierType, MilitaryService, AllergenType, EventReason, AdmissionLevelOfCareCode, ProviderRole, AlternateCharacterSetHandlingScheme, OrganizationUnitType, VersionId, SignatureCode, TypeOfAgreement, DiagnosisType, AbnormalFlags, AssignmentOfBenefits, VisitPriorityCode
)
# fmt: on

# sample enum parser for tables (implements base.EnumParser(Protocol))
def llm_parser(raw_input: str, choices: list[str], descriptions: list[str]) -> str:
    return choices[-1]

class UpstreamInput(str):
    """SAMPLE INPUT: Replace me with refactor > rename function with target input model"""
    iterable: list
    ...

@activity.defn(name="build :: ADT_A08 => MSH")
async def msh_1(x: UpstreamInput) -> MSH:
    """
    The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.
    """
    msh = MSH(
        sending_application=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        sending_facility=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        receiving_application=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        receiving_facility=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        date_or_time_of_message=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        security=ST(x),
        message_type=MSG(
            message_code=MessageType.parse(
                x, using=llm_parser
            ),
            trigger_event=EventType.parse(
                x, using=llm_parser
            ),
            message_structure=MessageStructure.parse(
                x, using=llm_parser
            )
        ),
        message_control_id=ST(x),
        processing_id=PT(
            processing_id=ProcessingId.parse(
                x, using=llm_parser
            ),
            processing_mode=ProcessingMode.parse(
                x, using=llm_parser
            )
        ),
        version_id=VID(
            version_id=VersionId.parse(
                x, using=llm_parser
            ),
            internationalization_code=CountryCode.parse(
                x, using=llm_parser
            ),
            international_version_id=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            )
        ),
        sequence_number=NM(x),
        continuation_pointer=ST(x),
        accept_acknowledgment_type=AcceptOrApplicationAcknowledgmentConditions.parse(
            x, using=llm_parser
        ),
        application_acknowledgment_type=AcceptOrApplicationAcknowledgmentConditions.parse(
            x, using=llm_parser
        ),
        country_code=CountryCode.parse(
            x, using=llm_parser
        ),
        character_set=AlternateCharacterSets.parse(
            x, using=llm_parser
        ),
        principal_language_of_message=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        alternate_character_set_handling_scheme=AlternateCharacterSetHandlingScheme.parse(
            x, using=llm_parser
        ),
        message_profile_identifier=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
    )

    return msh

@activity.defn(name="build :: ADT_A08 => SFT")
async def sft_2(x: UpstreamInput) -> SFT:
    """
    This segment provides additional information about the software product(s) used as a Sending Application. The primary purpose of this segment is for diagnostic use. There may be additional uses per site-specific agreements.

Example: MSH [{ SFT }] ….. 
    """
    sft = SFT(
        software_vendor_organization=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        software_certified_version_or_release_number=ST(x),
        software_product_name=ST(x),
        software_binary_id=ST(x),
        software_product_information=TX(x),
        software_install_date=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
    )

    return sft

@activity.defn(name="build :: ADT_A08 => EVN")
async def evn_3(x: UpstreamInput) -> EVN:
    """
    The EVN segment is used to communicate necessary trigger event information to receiving applications. Valid event types for all chapters are contained in HL7 Table 0003 - Event Type .
    """
    evn = EVN(
        event_type_code=EventType.parse(
            x, using=llm_parser
        ),
        recorded_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        date_or_time_planned_event=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        event_reason_code=EventReason.parse(
            x, using=llm_parser
        ),
        operator_id=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        event_occurred=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        event_facility=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
    )

    return evn

@activity.defn(name="build :: ADT_A08 => PID")
async def pid_4(x: UpstreamInput) -> PID:
    """
    The PID segment is used by all applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying and demographic information that, for the most part, is not likely to change frequently.
    """
    pid = PID(
        set_id_pid=SI(x),
        patient_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        patient_identifier_list=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        alternate_patient_id_pid=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        patient_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        mothers_maiden_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        date_or_time_of_birth=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        administrative_sex=AdministrativeSex.parse(
            x, using=llm_parser
        ),
        patient_alias=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        race=Race.parse(
            x, using=llm_parser
        ),
        patient_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        county_code=IS(x),
        phone_number_home=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        phone_number_business=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        primary_language=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        marital_status=MaritalStatus.parse(
            x, using=llm_parser
        ),
        religion=Religion.parse(
            x, using=llm_parser
        ),
        patient_account_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        ssn_number_patient=ST(x),
        drivers_license_number_patient=DLN(
            license_number=ST(x),
            issuing_state_province_country=IS(x),
            expiration_date=DT(x)
        ),
        mothers_identifier=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        ethnic_group=EthnicGroup.parse(
            x, using=llm_parser
        ),
        birth_place=ST(x),
        multiple_birth_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        birth_order=NM(x),
        citizenship=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        veterans_military_status=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        nationality=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        patient_death_date_and_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        patient_death_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        identity_unknown_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        identity_reliability_code=IdentityReliabilityCode.parse(
            x, using=llm_parser
        ),
        last_update_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        last_update_facility=HD(
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        species_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        breed_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        strain=ST(x),
        production_class_code=ProductionClassCode.parse(
            x, using=llm_parser
        ),
        tribal_citizenship=CWE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            coding_system_version_id=ST(x),
            alternate_coding_system_version_id=ST(x),
            original_text=ST(x)
        ),
    )

    return pid

@activity.defn(name="build :: ADT_A08 => PD1")
async def pd1_5(x: UpstreamInput) -> PD1:
    """
    The patient additional demographic segment contains demographic information that is likely to change about the patient.
    """
    pd1 = PD1(
        living_dependency=LivingDependency.parse(
            x, using=llm_parser
        ),
        living_arrangement=LivingArrangement.parse(
            x, using=llm_parser
        ),
        patient_primary_facility=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        patient_primary_care_provider_name_and_id_no=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        student_indicator=StudentStatus.parse(
            x, using=llm_parser
        ),
        handicap=IS(x),
        living_will_code=LivingWillCode.parse(
            x, using=llm_parser
        ),
        organ_donor_code=OrganDonorCode.parse(
            x, using=llm_parser
        ),
        separate_bill=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        duplicate_patient=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        publicity_code=PublicityCode.parse(
            x, using=llm_parser
        ),
        protection_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        protection_indicator_effective_date=DT(x),
        place_of_worship=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        advance_directive_code=AdvanceDirectiveCode.parse(
            x, using=llm_parser
        ),
        immunization_registry_status=ImmunizationRegistryStatus.parse(
            x, using=llm_parser
        ),
        immunization_registry_status_effective_date=DT(x),
        publicity_code_effective_date=DT(x),
        military_branch=MilitaryService.parse(
            x, using=llm_parser
        ),
        military_rank_or_grade=MilitaryRankOrGrade.parse(
            x, using=llm_parser
        ),
        military_status=MilitaryStatus.parse(
            x, using=llm_parser
        ),
    )

    return pd1

@activity.defn(name="build :: ADT_A08 => ROL")
async def rol_6(x: UpstreamInput) -> ROL:
    """
    The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted.
    """
    rol = ROL(
        role_instance_id=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        action_code=ProblemOrGoalActionCode.parse(
            x, using=llm_parser
        ),
        role_rol=ProviderRole.parse(
            x, using=llm_parser
        ),
        role_person=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        role_begin_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_end_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_duration=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        role_action_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        provider_type=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        organization_unit_type=OrganizationUnitType.parse(
            x, using=llm_parser
        ),
        office_or_home_address_or_birthplace=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        phone=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
    )

    return rol

@activity.defn(name="build :: ADT_A08 => NK1")
async def nk1_7(x: UpstreamInput) -> NK1:
    """
    The NK1 segment contains information about the patients other related parties. Any associated parties may be identified. Utilizing NK1-1 - set ID, multiple NK1 segments can be sent to patient accounts.
    """
    nk1 = NK1(
        set_id_nk1=SI(x),
        nk_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        relationship=Relationship.parse(
            x, using=llm_parser
        ),
        address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        business_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        contact_role=ContactRole.parse(
            x, using=llm_parser
        ),
        start_date=DT(x),
        end_date=DT(x),
        next_of_kin_or_associated_parties_job_title=ST(x),
        next_of_kin_or_associated_parties_job_code_or_class=JCC(
            job_code=IS(x),
            job_class=IS(x),
            job_description_text=TX(x)
        ),
        next_of_kin_or_associated_parties_employee_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        organization_name_nk1=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        marital_status=MaritalStatus.parse(
            x, using=llm_parser
        ),
        administrative_sex=AdministrativeSex.parse(
            x, using=llm_parser
        ),
        date_or_time_of_birth=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        living_dependency=LivingDependency.parse(
            x, using=llm_parser
        ),
        ambulatory_status=AmbulatoryStatus.parse(
            x, using=llm_parser
        ),
        citizenship=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        primary_language=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        living_arrangement=LivingArrangement.parse(
            x, using=llm_parser
        ),
        publicity_code=PublicityCode.parse(
            x, using=llm_parser
        ),
        protection_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        student_indicator=StudentStatus.parse(
            x, using=llm_parser
        ),
        religion=Religion.parse(
            x, using=llm_parser
        ),
        mothers_maiden_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        nationality=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        ethnic_group=EthnicGroup.parse(
            x, using=llm_parser
        ),
        contact_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        contact_persons_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        contact_persons_telephone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        contact_persons_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        next_of_kin_or_associated_partys_identifiers=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        job_status=JobStatus.parse(
            x, using=llm_parser
        ),
        race=Race.parse(
            x, using=llm_parser
        ),
        handicap=IS(x),
        contact_person_social_security_number=ST(x),
        next_of_kin_birth_place=ST(x),
        vip_indicator=IS(x),
    )

    return nk1

@activity.defn(name="build :: ADT_A08 => PV1")
async def pv1_8(x: UpstreamInput) -> PV1:
    """
    The PV1 segment is used by Registration/Patient Administration applications to communicate information on an account or visit-specific basis. The default is to send account level data. To use this segment for visit level data PV1-51 - Visit Indicator must be valued to V. The value of PV-51 affects the level of data being sent on the PV1, PV2, and any other segments that are part of the associated PV1 hierarchy (e.g. ROL, DG1, or OBX).
    """
    pv1 = PV1(
        set_id_pv1=SI(x),
        patient_class=PatientClass.parse(
            x, using=llm_parser
        ),
        assigned_patient_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        admission_type=AdmissionType.parse(
            x, using=llm_parser
        ),
        preadmit_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        prior_patient_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        attending_doctor=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        referring_doctor=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        consulting_doctor=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        hospital_service=HospitalService.parse(
            x, using=llm_parser
        ),
        temporary_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        preadmit_test_indicator=IS(x),
        re_admission_indicator=ReAdmissionIndicator.parse(
            x, using=llm_parser
        ),
        admit_source=AdmitSource.parse(
            x, using=llm_parser
        ),
        ambulatory_status=AmbulatoryStatus.parse(
            x, using=llm_parser
        ),
        vip_indicator=IS(x),
        admitting_doctor=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        patient_type=IS(x),
        visit_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        financial_class=FC(
            financial_class_code=IS(x),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        charge_price_indicator=IS(x),
        courtesy_code=IS(x),
        credit_rating=IS(x),
        contract_code=IS(x),
        contract_effective_date=DT(x),
        contract_amount=NM(x),
        contract_period=NM(x),
        interest_code=IS(x),
        transfer_to_bad_debt_code=IS(x),
        transfer_to_bad_debt_date=DT(x),
        bad_debt_agency_code=IS(x),
        bad_debt_transfer_amount=NM(x),
        bad_debt_recovery_amount=NM(x),
        delete_account_indicator=IS(x),
        delete_account_date=DT(x),
        discharge_disposition=DischargeDisposition.parse(
            x, using=llm_parser
        ),
        discharged_to_location=DLD(
            discharge_location=IS(x),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        diet_type=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        servicing_facility=IS(x),
        bed_status=BedStatus.parse(
            x, using=llm_parser
        ),
        account_status=IS(x),
        pending_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        prior_temporary_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        admit_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        discharge_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        current_patient_balance=NM(x),
        total_charges=NM(x),
        total_adjustments=NM(x),
        total_payments=NM(x),
        alternate_visit_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        visit_indicator=VisitIndicator.parse(
            x, using=llm_parser
        ),
        other_healthcare_provider=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
    )

    return pv1

@activity.defn(name="build :: ADT_A08 => PV2")
async def pv2_9(x: UpstreamInput) -> PV2:
    """
    The PV2 segment is a continuation of information contained on the PV1 segment.
    """
    pv2 = PV2(
        prior_pending_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        accommodation_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        admit_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        transfer_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        patient_valuables=ST(x),
        patient_valuables_location=ST(x),
        visit_user_code=VisitUserCode.parse(
            x, using=llm_parser
        ),
        expected_admit_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        expected_discharge_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        estimated_length_of_inpatient_stay=NM(x),
        actual_length_of_inpatient_stay=NM(x),
        visit_description=ST(x),
        referral_source_code=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        previous_service_date=DT(x),
        employment_illness_related_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        purge_status_code=PurgeStatusCode.parse(
            x, using=llm_parser
        ),
        purge_status_date=DT(x),
        special_program_code=SpecialProgramCode.parse(
            x, using=llm_parser
        ),
        retention_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        expected_number_of_insurance_plans=NM(x),
        visit_publicity_code=PublicityCode.parse(
            x, using=llm_parser
        ),
        visit_protection_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        clinic_organization_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        patient_status_code=PatientStatusCode.parse(
            x, using=llm_parser
        ),
        visit_priority_code=VisitPriorityCode.parse(
            x, using=llm_parser
        ),
        previous_treatment_date=DT(x),
        expected_discharge_disposition=DischargeDisposition.parse(
            x, using=llm_parser
        ),
        signature_on_file_date=DT(x),
        first_similar_illness_date=DT(x),
        patient_charge_adjustment_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        recurring_service_code=IS(x),
        billing_media_code=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        expected_surgery_date_and_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        military_partnership_code=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        military_non_availability_code=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        newborn_baby_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        baby_detained_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        mode_of_arrival_code=ModeOfArrivalCode.parse(
            x, using=llm_parser
        ),
        recreational_drug_use_code=RecreationalDrugUseCode.parse(
            x, using=llm_parser
        ),
        admission_level_of_care_code=AdmissionLevelOfCareCode.parse(
            x, using=llm_parser
        ),
        precaution_code=PrecautionCode.parse(
            x, using=llm_parser
        ),
        patient_condition_code=PatientConditionCode.parse(
            x, using=llm_parser
        ),
        living_will_code=LivingWillCode.parse(
            x, using=llm_parser
        ),
        organ_donor_code=OrganDonorCode.parse(
            x, using=llm_parser
        ),
        advance_directive_code=AdvanceDirectiveCode.parse(
            x, using=llm_parser
        ),
        patient_status_effective_date=DT(x),
        expected_loa_return_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        expected_pre_admission_testing_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        notify_clergy_code=NotifyClergyCode.parse(
            x, using=llm_parser
        ),
    )

    return pv2

@activity.defn(name="build :: ADT_A08 => ROL")
async def rol_10(x: UpstreamInput) -> ROL:
    """
    The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted.
    """
    rol = ROL(
        role_instance_id=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        action_code=ProblemOrGoalActionCode.parse(
            x, using=llm_parser
        ),
        role_rol=ProviderRole.parse(
            x, using=llm_parser
        ),
        role_person=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        role_begin_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_end_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_duration=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        role_action_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        provider_type=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        organization_unit_type=OrganizationUnitType.parse(
            x, using=llm_parser
        ),
        office_or_home_address_or_birthplace=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        phone=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
    )

    return rol

@activity.defn(name="build :: ADT_A08 => DB1")
async def db1_11(x: UpstreamInput) -> DB1:
    """
    The disability segment contains information related to the disability of a person. This segment was created instead of adding disability attributes to each segment that contains a person (to which disability may apply). This is an optional segment that can be used to send disability information about a person already defined by the Patient Administration Chapter. The disabled person code and identifier allow for the association of the disability information to the person.
    """
    db1 = DB1(
        set_id_db1=SI(x),
        disabled_person_code=DisabledPersonCode.parse(
            x, using=llm_parser
        ),
        disabled_person_identifier=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        disabled_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        disability_start_date=DT(x),
        disability_end_date=DT(x),
        disability_return_to_work_date=DT(x),
        disability_unable_to_work_date=DT(x),
    )

    return db1

@activity.defn(name="build :: ADT_A08 => OBX")
async def obx_12(x: UpstreamInput) -> OBX:
    """
    The OBX segment is used to transmit a single observation or observation fragment. It represents the smallest indivisible unit of a report. The OBX segment can also contain encapsulated data, e.g., a CDA document or a DICOM image.

Its principal mission is to carry information about observations in report messages.  But the OBX can also be part of an observation order.  In this case, the OBX carries clinical information needed by the filler to interpret the observation the filler makes.  For example, an OBX is needed to report the inspired oxygen on an order for a blood oxygen to a blood gas lab, or to report the menstrual phase information which should be included on an order for a pap smear to a cytology lab.  Appendix 7A includes codes for identifying many of pieces of information needed by observation producing services to properly interpret a test result.  OBX is also found in other HL7 messages that need to include patient clinical information. 
    """
    obx = OBX(
        set_id_obx=SI(x),
        value_type=ValueType.parse(
            x, using=llm_parser
        ),
        observation_identifier=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        observation_sub_id=ST(x),
        observation_value=VARIES(x),
        units=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        references_range=ST(x),
        abnormal_flags=AbnormalFlags.parse(
            x, using=llm_parser
        ),
        probability=NM(x),
        nature_of_abnormal_test=NatureOfAbnormalTesting.parse(
            x, using=llm_parser
        ),
        observation_result_status=ObservationResultStatusCodesInterpretation.parse(
            x, using=llm_parser
        ),
        effective_date_of_reference_range=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        user_defined_access_checks=ST(x),
        date_or_time_of_the_observation=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        producers_id=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        responsible_observer=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        observation_method=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        equipment_instance_identifier=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        date_or_time_of_the_analysis=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        reserved_for_harmonization_with_v2_6=ST(x),
        reserved_for_harmonization_with_v2_6_20=ST(x),
        reserved_for_harmonization_with_v2_6_21=ST(x),
        performing_organization_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        performing_organization_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        performing_organization_medical_director=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
    )

    return obx

@activity.defn(name="build :: ADT_A08 => AL1")
async def al1_13(x: UpstreamInput) -> AL1:
    """
    The AL1 segment contains patient allergy information of various types. Most of this information will be derived from user-defined tables. Each AL1 segment describes a single patient allergy.
    """
    al1 = AL1(
        set_id_al1=SI(x),
        allergen_type_code=AllergenType.parse(
            x, using=llm_parser
        ),
        allergen_code_or_mnemonic_or_description=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        allergy_severity_code=AllergySeverity.parse(
            x, using=llm_parser
        ),
        allergy_reaction_code=ST(x),
        identification_date=DT(x),
    )

    return al1

@activity.defn(name="build :: ADT_A08 => DG1")
async def dg1_14(x: UpstreamInput) -> DG1:
    """
    The DG1 segment contains patient diagnosis information of various types, for example, admitting, primary, etc. The DG1 segment is used to send multiple diagnoses (for example, for medical records encoding). It is also used when the FT1-19 - Diagnosis Code - FT1 does not provide sufficient information for a billing system. This diagnosis coding should be distinguished from the clinical problem segment used by caregivers to manage the patient (see Chapter 12, Patient Care). Coding methodologies are also defined.
    """
    dg1 = DG1(
        set_id_dg1=SI(x),
        diagnosis_coding_method=ID(x),
        diagnosis_code_dg1=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        diagnosis_description=ST(x),
        diagnosis_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        diagnosis_type=DiagnosisType.parse(
            x, using=llm_parser
        ),
        major_diagnostic_category=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        diagnostic_related_group=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        drg_approval_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        drg_grouper_review_code=IS(x),
        outlier_type=OutlierType.parse(
            x, using=llm_parser
        ),
        outlier_days=NM(x),
        outlier_cost=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        grouper_version_and_type=ST(x),
        diagnosis_priority=DiagnosisPriority.parse(
            x, using=llm_parser
        ),
        diagnosing_clinician=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        diagnosis_classification=DiagnosisClassification.parse(
            x, using=llm_parser
        ),
        confidential_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        attestation_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        diagnosis_identifier=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        diagnosis_action_code=SegmentActionCode.parse(
            x, using=llm_parser
        ),
    )

    return dg1

@activity.defn(name="build :: ADT_A08 => DRG")
async def drg_15(x: UpstreamInput) -> DRG:
    """
    The DRG segment contains diagnoses-related grouping information of various types. The DRG segment is used to send the DRG information, for example, for billing and medical records encoding.
    """
    drg = DRG(
        diagnostic_related_group=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        drg_assigned_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        drg_approval_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        drg_grouper_review_code=IS(x),
        outlier_type=OutlierType.parse(
            x, using=llm_parser
        ),
        outlier_days=NM(x),
        outlier_cost=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        drg_payor=DrgPayor.parse(
            x, using=llm_parser
        ),
        outlier_reimbursement=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        confidential_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        drg_transfer_type=DrgTransferType.parse(
            x, using=llm_parser
        ),
    )

    return drg

@activity.defn(name="build :: ADT_A08 => PR1")
async def pr1_16(x: UpstreamInput) -> PR1:
    """
    The PR1 segment contains information relative to various types of procedures that can be performed on a patient. The PR1 segment can be used to send procedure information, for example: Surgical, Nuclear Medicine, X-ray with contrast, etc. The PR1 segment is used to send multiple procedures, for example, for medical records encoding or for billing systems.
    """
    pr1 = PR1(
        set_id_pr1=SI(x),
        procedure_coding_method=IS(x),
        procedure_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        procedure_description=ST(x),
        procedure_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        procedure_functional_type=ProcedureFunctionalType.parse(
            x, using=llm_parser
        ),
        procedure_minutes=NM(x),
        anesthesiologist=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        anesthesia_code=IS(x),
        anesthesia_minutes=NM(x),
        surgeon=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        procedure_practitioner=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        consent_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        procedure_priority=ProcedurePriority.parse(
            x, using=llm_parser
        ),
        associated_diagnosis_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        procedure_code_modifier=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        procedure_drg_type=ProcedureDrgType.parse(
            x, using=llm_parser
        ),
        tissue_type_code=TissueTypeCode.parse(
            x, using=llm_parser
        ),
        procedure_identifier=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        procedure_action_code=SegmentActionCode.parse(
            x, using=llm_parser
        ),
    )

    return pr1

@activity.defn(name="build :: ADT_A08 => ROL")
async def rol_17(x: UpstreamInput) -> ROL:
    """
    The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted.
    """
    rol = ROL(
        role_instance_id=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        action_code=ProblemOrGoalActionCode.parse(
            x, using=llm_parser
        ),
        role_rol=ProviderRole.parse(
            x, using=llm_parser
        ),
        role_person=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        role_begin_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_end_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_duration=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        role_action_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        provider_type=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        organization_unit_type=OrganizationUnitType.parse(
            x, using=llm_parser
        ),
        office_or_home_address_or_birthplace=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        phone=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
    )

    return rol

@activity.defn(name="build :: ADT_A08 => GT1")
async def gt1_18(x: UpstreamInput) -> GT1:
    """
    The GT1 segment contains guarantor (e.g., the person or the organization with financial responsibility for payment of a patient account) data for patient and insurance billing applications.
    """
    gt1 = GT1(
        set_id_gt1=SI(x),
        guarantor_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        guarantor_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        guarantor_spouse_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        guarantor_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        guarantor_ph_num_home=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        guarantor_ph_num_business=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        guarantor_date_or_time_of_birth=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        guarantor_administrative_sex=AdministrativeSex.parse(
            x, using=llm_parser
        ),
        guarantor_type=IS(x),
        guarantor_relationship=Relationship.parse(
            x, using=llm_parser
        ),
        guarantor_ssn=ST(x),
        guarantor_date_begin=DT(x),
        guarantor_date_end=DT(x),
        guarantor_priority=NM(x),
        guarantor_employer_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        guarantor_employer_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        guarantor_employer_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        guarantor_employee_id_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        guarantor_employment_status=EmploymentStatus.parse(
            x, using=llm_parser
        ),
        guarantor_organization_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        guarantor_billing_hold_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        guarantor_credit_rating_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        guarantor_death_date_and_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        guarantor_death_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        guarantor_charge_adjustment_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        guarantor_household_annual_income=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        guarantor_household_size=NM(x),
        guarantor_employer_id_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        guarantor_marital_status_code=MaritalStatus.parse(
            x, using=llm_parser
        ),
        guarantor_hire_effective_date=DT(x),
        employment_stop_date=DT(x),
        living_dependency=LivingDependency.parse(
            x, using=llm_parser
        ),
        ambulatory_status=AmbulatoryStatus.parse(
            x, using=llm_parser
        ),
        citizenship=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        primary_language=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        living_arrangement=LivingArrangement.parse(
            x, using=llm_parser
        ),
        publicity_code=PublicityCode.parse(
            x, using=llm_parser
        ),
        protection_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        student_indicator=StudentStatus.parse(
            x, using=llm_parser
        ),
        religion=Religion.parse(
            x, using=llm_parser
        ),
        mothers_maiden_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        nationality=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        ethnic_group=EthnicGroup.parse(
            x, using=llm_parser
        ),
        contact_persons_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        contact_persons_telephone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        contact_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        contact_relationship=Relationship.parse(
            x, using=llm_parser
        ),
        job_title=ST(x),
        job_code_or_class=JCC(
            job_code=IS(x),
            job_class=IS(x),
            job_description_text=TX(x)
        ),
        guarantor_employers_organization_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        handicap=IS(x),
        job_status=JobStatus.parse(
            x, using=llm_parser
        ),
        guarantor_financial_class=FC(
            financial_class_code=IS(x),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        guarantor_race=Race.parse(
            x, using=llm_parser
        ),
        guarantor_birth_place=ST(x),
        vip_indicator=IS(x),
    )

    return gt1

@activity.defn(name="build :: ADT_A08 => IN1")
async def in1_19(x: UpstreamInput) -> IN1:
    """
    The IN1 segment contains insurance policy coverage information necessary to produce properly pro-rated and patient and insurance bills.
    """
    in1 = IN1(
        set_id_in1=SI(x),
        insurance_plan_id=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        insurance_company_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        insurance_company_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        insurance_company_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        insurance_co_contact_person=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        insurance_co_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        group_number=ST(x),
        group_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        insureds_group_emp_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        insureds_group_emp_name=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        plan_effective_date=DT(x),
        plan_expiration_date=DT(x),
        authorization_information=AUI(
            authorization_number=ST(x),
            date=DT(x),
            source=ST(x)
        ),
        plan_type=IS(x),
        name_of_insured=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        insureds_relationship_to_patient=Relationship.parse(
            x, using=llm_parser
        ),
        insureds_date_of_birth=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        insureds_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        assignment_of_benefits=AssignmentOfBenefits.parse(
            x, using=llm_parser
        ),
        coordination_of_benefits=CoordinationOfBenefits.parse(
            x, using=llm_parser
        ),
        coord_of_ben_priority=ST(x),
        notice_of_admission_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        notice_of_admission_date=DT(x),
        report_of_eligibility_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        report_of_eligibility_date=DT(x),
        release_information_code=ReleaseInformation.parse(
            x, using=llm_parser
        ),
        pre_admit_cert=ST(x),
        verification_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        verification_by=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        type_of_agreement_code=TypeOfAgreement.parse(
            x, using=llm_parser
        ),
        billing_status=IS(x),
        lifetime_reserve_days=NM(x),
        delay_before_l_r_day=NM(x),
        company_plan_code=IS(x),
        policy_number=ST(x),
        policy_deductible=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        policy_limit_amount=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        policy_limit_days=NM(x),
        room_rate_semi_private=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        room_rate_private=CP(
            price=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            price_type=PriceType.parse(
                x, using=llm_parser
            ),
            from_value=NM(x),
            to_value=NM(x),
            range_units=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            range_type=CpRangeType.parse(
                x, using=llm_parser
            )
        ),
        insureds_employment_status=EmploymentStatus.parse(
            x, using=llm_parser
        ),
        insureds_administrative_sex=AdministrativeSex.parse(
            x, using=llm_parser
        ),
        insureds_employers_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        verification_status=ST(x),
        prior_insurance_plan_id=IS(x),
        coverage_type=CoverageType.parse(
            x, using=llm_parser
        ),
        handicap=IS(x),
        insureds_id_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        signature_code=SignatureCode.parse(
            x, using=llm_parser
        ),
        signature_code_date=DT(x),
        insureds_birth_place=ST(x),
        vip_indicator=IS(x),
    )

    return in1

@activity.defn(name="build :: ADT_A08 => IN2")
async def in2_20(x: UpstreamInput) -> IN2:
    """
    The IN2 segment contains additional insurance policy coverage and benefit information necessary for proper billing and reimbursement. Fields used by this segment are defined by CMS or other regulatory agencies.
    """
    in2 = IN2(
        insureds_employee_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        insureds_social_security_number=ST(x),
        insureds_employers_name_and_id=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        employer_information_data=IS(x),
        mail_claim_party=MailClaimParty.parse(
            x, using=llm_parser
        ),
        medicare_health_ins_card_number=ST(x),
        medicaid_case_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        medicaid_case_number=ST(x),
        military_sponsor_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        military_id_number=ST(x),
        dependent_of_military_recipient=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        military_organization=ST(x),
        military_station=ST(x),
        military_service=MilitaryService.parse(
            x, using=llm_parser
        ),
        military_rank_or_grade=MilitaryRankOrGrade.parse(
            x, using=llm_parser
        ),
        military_status=MilitaryStatus.parse(
            x, using=llm_parser
        ),
        military_retire_date=DT(x),
        military_non_avail_cert_on_file=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        baby_coverage=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        combine_baby_bill=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        blood_deductible=ST(x),
        special_coverage_approval_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        special_coverage_approval_title=ST(x),
        non_covered_insurance_code=IS(x),
        payor_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        payor_subscriber_id=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        eligibility_source=EligibilitySource.parse(
            x, using=llm_parser
        ),
        room_coverage_type_or_amount=RMC(
            room_type=RoomType.parse(
                x, using=llm_parser
            ),
            amount_type=AmountType.parse(
                x, using=llm_parser
            ),
            coverage_amount=NM(x),
            money_or_percentage=MOP(
                money_or_percentage_indicator=MoneyOrPercentageIndicator.parse(
                    x, using=llm_parser
                ),
                money_or_percentage_quantity=NM(x),
                currency_denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            )
        ),
        policy_type_or_amount=PTA(
            policy_type=PolicyType.parse(
                x, using=llm_parser
            ),
            amount_class=AmountClass.parse(
                x, using=llm_parser
            ),
            money_or_percentage_quantity=NM(x),
            money_or_percentage=MOP(
                money_or_percentage_indicator=MoneyOrPercentageIndicator.parse(
                    x, using=llm_parser
                ),
                money_or_percentage_quantity=NM(x),
                currency_denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            )
        ),
        daily_deductible=DDI(
            delay_days=NM(x),
            monetary_amount=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            ),
            number_of_days=NM(x)
        ),
        living_dependency=LivingDependency.parse(
            x, using=llm_parser
        ),
        ambulatory_status=AmbulatoryStatus.parse(
            x, using=llm_parser
        ),
        citizenship=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        primary_language=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        living_arrangement=LivingArrangement.parse(
            x, using=llm_parser
        ),
        publicity_code=PublicityCode.parse(
            x, using=llm_parser
        ),
        protection_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        student_indicator=StudentStatus.parse(
            x, using=llm_parser
        ),
        religion=Religion.parse(
            x, using=llm_parser
        ),
        mothers_maiden_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        nationality=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        ethnic_group=EthnicGroup.parse(
            x, using=llm_parser
        ),
        marital_status=MaritalStatus.parse(
            x, using=llm_parser
        ),
        insureds_employment_start_date=DT(x),
        employment_stop_date=DT(x),
        job_title=ST(x),
        job_code_or_class=JCC(
            job_code=IS(x),
            job_class=IS(x),
            job_description_text=TX(x)
        ),
        job_status=JobStatus.parse(
            x, using=llm_parser
        ),
        employer_contact_person_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        employer_contact_person_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        employer_contact_reason=IS(x),
        insureds_contact_persons_name=XPN(
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x)
        ),
        insureds_contact_person_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        insureds_contact_person_reason=IS(x),
        relationship_to_the_patient_start_date=DT(x),
        relationship_to_the_patient_stop_date=DT(x),
        insurance_co_contact_reason=InsuranceCompanyContactReason.parse(
            x, using=llm_parser
        ),
        insurance_co_contact_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        policy_scope=IS(x),
        policy_source=IS(x),
        patient_member_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        guarantors_relationship_to_insured=Relationship.parse(
            x, using=llm_parser
        ),
        insureds_phone_number_home=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        insureds_employer_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        military_handicapped_program=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        suspend_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        copay_limit_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        stoploss_limit_flag=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        insured_organization_name_and_id=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        insured_employer_organization_name_and_id=XON(
            organization_name=ST(x),
            organization_name_type_code=OrganizationalNameType.parse(
                x, using=llm_parser
            ),
            id_number=NM(x),
            check_digit=NM(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            organization_identifier=ST(x)
        ),
        race=Race.parse(
            x, using=llm_parser
        ),
        cms_patients_relationship_to_insured=PatientSRelationshipToInsured.parse(
            x, using=llm_parser
        ),
    )

    return in2

@activity.defn(name="build :: ADT_A08 => IN3")
async def in3_21(x: UpstreamInput) -> IN3:
    """
    The IN3 segment contains additional insurance information for certifying the need for patient care. Fields used by this segment are defined by CMS, or other regulatory agencies.
    """
    in3 = IN3(
        set_id_in3=SI(x),
        certification_number=CX(
            id_number=ST(x),
            check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            effective_date=DT(x),
            expiration_date=DT(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        certified_by=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        certification_required=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        penalty=MOP(
            money_or_percentage_indicator=MoneyOrPercentageIndicator.parse(
                x, using=llm_parser
            ),
            money_or_percentage_quantity=NM(x),
            currency_denomination=CurrencyCodes.parse(
                x, using=llm_parser
            )
        ),
        certification_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        certification_modify_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        operator=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        certification_begin_date=DT(x),
        certification_end_date=DT(x),
        days=DTN(
            day_type=DayType.parse(
                x, using=llm_parser
            ),
            number_of_days=NM(x)
        ),
        non_concur_code_or_description=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        non_concur_effective_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        physician_reviewer=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        certification_contact=ST(x),
        certification_contact_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        appeal_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        certification_agency=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        certification_agency_phone_number=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
        pre_certification_requirement=ICD(
            certification_patient_type=CertificationPatientType.parse(
                x, using=llm_parser
            ),
            certification_required=YesOrNoIndicator.parse(
                x, using=llm_parser
            ),
            date_or_time_certification_required=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        case_manager=ST(x),
        second_opinion_date=DT(x),
        second_opinion_status=IS(x),
        second_opinion_documentation_received=IS(x),
        second_opinion_physician=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
    )

    return in3

@activity.defn(name="build :: ADT_A08 => ROL")
async def rol_22(x: UpstreamInput) -> ROL:
    """
    The role segment contains the data necessary to add, update, correct, and delete from the record persons involved, as well as their functional involvement with the activity being transmitted.
    """
    rol = ROL(
        role_instance_id=EI(
            entity_identifier=ST(x),
            namespace_id=IS(x),
            universal_id=ST(x),
            universal_id_type=UniversalIdType.parse(
                x, using=llm_parser
            )
        ),
        action_code=ProblemOrGoalActionCode.parse(
            x, using=llm_parser
        ),
        role_rol=ProviderRole.parse(
            x, using=llm_parser
        ),
        role_person=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        role_begin_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_end_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        role_duration=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        role_action_reason=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        provider_type=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        organization_unit_type=OrganizationUnitType.parse(
            x, using=llm_parser
        ),
        office_or_home_address_or_birthplace=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        phone=XTN(
            telephone_number=ST(x),
            telecommunication_use_code=TelecommunicationUseCode.parse(
                x, using=llm_parser
            ),
            telecommunication_equipment_type=TelecommunicationEquipmentType.parse(
                x, using=llm_parser
            ),
            email_address=ST(x),
            country_code=NM(x),
            area_or_city_code=NM(x),
            local_number=NM(x),
            extension=NM(x),
            any_text=ST(x),
            extension_prefix=ST(x),
            speed_dial_code=ST(x),
            unformatted_telephone_number=ST(x)
        ),
    )

    return rol

@activity.defn(name="build :: ADT_A08 => ACC")
async def acc_23(x: UpstreamInput) -> ACC:
    """
    The ACC segment contains patient information relative to an accident in which the patient has been involved.
    """
    acc = ACC(
        accident_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        accident_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        accident_location=ST(x),
        auto_accident_state=StateOrProvince.parse(
            x, using=llm_parser
        ),
        accident_job_related_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        accident_death_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        entered_by=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        accident_description=ST(x),
        brought_in_by=ST(x),
        police_notified_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        accident_address=XAD(
            street_address=SAD(
                street_or_mailing_address=ST(x),
                street_name=ST(x),
                dwelling_number=ST(x)
            ),
            other_designation=ST(x),
            city=City.parse(
                x, using=llm_parser
            ),
            state_or_province=State.parse(
                x, using=llm_parser
            ),
            zip_or_postal_code=ZipCode.parse(
                x, using=llm_parser
            ),
            country=CountryCode.parse(
                x, using=llm_parser
            ),
            address_type=AddressType.parse(
                x, using=llm_parser
            ),
            other_geographic_designation=ST(x),
            county_or_parish_code=IS(x),
            census_tract=IS(x),
            address_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            address_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
    )

    return acc

@activity.defn(name="build :: ADT_A08 => UB1")
async def ub1_24(x: UpstreamInput) -> UB1:
    """
    The UB1 segment contains the data necessary to complete UB82 bills specific to the United States; other realms may choose to implement using regional code sets. Only UB82 fields that do not exist in other HL7 defined segments appear in this segment. Patient Name and Date of Birth are required for UB82 billing; however, they are included in the PID segment and therefore do not appear here. The UB codes listed as examples are not an exhaustive or current list. Refer to a UB specification for additional information.

The Uniform Billing segments are specific to the US and may not be implemented in non-US systems. 
    """
    ub1 = UB1(
        set_id_ub1=SI(x),
        blood_deductible=NM(x),
        blood_furnished_pints_of=NM(x),
        blood_replaced_pints=NM(x),
        blood_not_replaced_pints=NM(x),
        co_insurance_days=NM(x),
        condition_code=IS(x),
        covered_days=NM(x),
        non_covered_days=NM(x),
        value_amount_and_code=UVC(
            value_code=CNE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            value_amount=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            )
        ),
        number_of_grace_days=NM(x),
        special_program_indicator=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        psro_or_ur_approval_indicator=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        psro_or_ur_approved_stay_fm=DT(x),
        psro_or_ur_approved_stay_to=DT(x),
        occurrence=OCD(
            occurrence_code=CNE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            occurrence_date=DT(x)
        ),
        occurrence_span=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        occur_span_start_date=DT(x),
        occur_span_end_date=DT(x),
        ub_82_locator_2=ST(x),
        ub_82_locator_9=ST(x),
        ub_82_locator_27=ST(x),
        ub_82_locator_45=ST(x),
    )

    return ub1

@activity.defn(name="build :: ADT_A08 => UB2")
async def ub2_25(x: UpstreamInput) -> UB2:
    """
    The UB2 segment contains data necessary to complete UB92 bills specific to the United States; other realms may choose to implement using regional code sets. Only UB82 and UB92 fields that do not exist in other HL7 defined segments appear in this segment.  Just as with the UB82 billing, Patient Name and Date of Birth are required; they are included in the PID segment and therefore do not appear here. When the field locators are different on the UB92, as compared to the UB82, the element is listed with its new location in parentheses ( ). The UB codes listed as examples are not an exhaustive or current list; refer to a UB specification for additional information.

The Uniform Billing segments are specific to the US and may not be implemented in non-US systems.
    """
    ub2 = UB2(
        set_id_ub2=SI(x),
        co_insurance_days=ST(x),
        condition_code=IS(x),
        covered_days=ST(x),
        non_covered_days=ST(x),
        value_amount_and_code=UVC(
            value_code=CNE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            value_amount=MO(
                quantity=NM(x),
                denomination=CurrencyCodes.parse(
                    x, using=llm_parser
                )
            )
        ),
        occurrence_code_and_date=OCD(
            occurrence_code=CNE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            occurrence_date=DT(x)
        ),
        occurrence_span_code_or_dates=OSP(
            occurrence_span_code=CNE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            occurrence_span_start_date=DT(x),
            occurrence_span_stop_date=DT(x)
        ),
        ub92_locator_2=ST(x),
        ub92_locator_11=ST(x),
        ub92_locator_31=ST(x),
        document_control_number=ST(x),
        ub92_locator_49=ST(x),
        ub92_locator_56=ST(x),
        ub92_locator_57=ST(x),
        ub92_locator_78=ST(x),
        special_visit_count=NM(x),
    )

    return ub2

@activity.defn(name="build :: ADT_A08 => PDA")
async def pda_26(x: UpstreamInput) -> PDA:
    """
    This segment carries information on a patients death and possible autopsy.
    """
    pda = PDA(
        death_cause_code=CE(
            identifier=ST(x),
            text=ST(x),
            name_of_coding_system=CodingSystem.parse(
                x, using=llm_parser
            ),
            alternate_identifier=ST(x),
            alternate_text=ST(x),
            name_of_alternate_coding_system=CodingSystem.parse(
                x, using=llm_parser
            )
        ),
        death_location=PL(
            point_of_care=IS(x),
            room=IS(x),
            bed=IS(x),
            facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            location_status=IS(x),
            person_location_type=PersonLocationType.parse(
                x, using=llm_parser
            ),
            building=IS(x),
            floor=IS(x),
            location_description=ST(x),
            comprehensive_location_identifier=EI(
                entity_identifier=ST(x),
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            assigning_authority_for_location=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            )
        ),
        death_certified_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        death_certificate_signed_date_or_time=TS(
            time=DTM(x),
            degree_of_precision=Precision.parse(
                x, using=llm_parser
            )
        ),
        death_certified_by=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        autopsy_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
        autopsy_start_and_end_date_or_time=DR(
            range_start_date_or_time=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            range_end_date_or_time=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            )
        ),
        autopsy_performed_by=XCN(
            id_number=ST(x),
            family_name=FN(
                surname=Lastname.parse(
                    x, using=llm_parser
                ),
                own_surname_prefix=ST(x),
                own_surname=ST(x),
                surname_prefix_from_partner_or_spouse=ST(x),
                surname_from_partner_or_spouse=ST(x)
            ),
            given_name=FirstName.parse(
                x, using=llm_parser
            ),
            second_and_further_given_names_or_initials_thereof=ST(x),
            suffix=ST(x),
            prefix=ST(x),
            degree=DegreeOrLicenseOrCertificate.parse(
                x, using=llm_parser
            ),
            source_table=IS(x),
            assigning_authority=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_type_code=NameType.parse(
                x, using=llm_parser
            ),
            identifier_check_digit=ST(x),
            check_digit_scheme=CheckDigitScheme.parse(
                x, using=llm_parser
            ),
            identifier_type_code=IdentifierType.parse(
                x, using=llm_parser
            ),
            assigning_facility=HD(
                namespace_id=IS(x),
                universal_id=ST(x),
                universal_id_type=UniversalIdType.parse(
                    x, using=llm_parser
                )
            ),
            name_representation_code=NameOrAddressRepresentation.parse(
                x, using=llm_parser
            ),
            name_context=CE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                )
            ),
            name_validity_range=DR(
                range_start_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                ),
                range_end_date_or_time=TS(
                    time=DTM(x),
                    degree_of_precision=Precision.parse(
                        x, using=llm_parser
                    )
                )
            ),
            name_assembly_order=NameAssemblyOrder.parse(
                x, using=llm_parser
            ),
            effective_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            expiration_date=TS(
                time=DTM(x),
                degree_of_precision=Precision.parse(
                    x, using=llm_parser
                )
            ),
            professional_suffix=ST(x),
            assigning_jurisdiction=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            ),
            assigning_agency_or_department=CWE(
                identifier=ST(x),
                text=ST(x),
                name_of_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                alternate_identifier=ST(x),
                alternate_text=ST(x),
                name_of_alternate_coding_system=CodingSystem.parse(
                    x, using=llm_parser
                ),
                coding_system_version_id=ST(x),
                alternate_coding_system_version_id=ST(x),
                original_text=ST(x)
            )
        ),
        coroner_indicator=YesOrNoIndicator.parse(
            x, using=llm_parser
        ),
    )

    return pda



@workflow.defn
class Build_ADT_A08:
    """
    HL7v2.5.1
    This trigger event is used when any patient information has changed but when no other trigger event has occurred.  For example, an A08 event can be used to notify the receiving systems of a change of address or a name change.  We strongly recommend that the A08 transaction be used to update fields that are not updated by any of the other trigger events.  If there are specific trigger events for this update, these trigger events should be used. For example, if a patient's address and location are to be changed, then an A08 is used to change the patient address and the appropriate patient location trigger event is used to change the patient location. The A08 event can include information specific to an episode of care, but it can also be used for demographic information only.
    """
    @workflow.run
    async def run(self, x: UpstreamInput) -> str:
        # build = partial(
        #     workflow.execute_local_activity,
        #     arg=x,
        #     start_to_close_timeout=timedelta(seconds=10),
        #     # other temporal activity args go here
        # )
        build = lambda f: f(x)

        adt_a08 = ADT_A08(
            message_header=await build(msh_1),
            software_segment=(                                                   # rpt:*            
                await build(sft_2),
            ),
            event_type=await build(evn_3),
            patient_identification=await build(pid_4),
            patient_additional_demographic=await build(pd1_5),
            role=(                                                               # rpt:*            
                await build(rol_6),
            ),
            next_of_kin_or_associated_parties=(                                  # rpt:*            
                await build(nk1_7),
            ),
            patient_visit=await build(pv1_8),
            patient_visit_additional_information=await build(pv2_9),
            role_10=(                                                            # rpt:*            
                await build(rol_10),
            ),
            disability=(                                                         # rpt:*            
                await build(db1_11),
            ),
            observation_or_result=(                                              # rpt:*            
                await build(obx_12),
            ),
            patient_allergy_information=(                                        # rpt:*            
                await build(al1_13),
            ),
            diagnosis=(                                                          # rpt:*            
                await build(dg1_14),
            ),
            diagnosis_related_group=await build(drg_15),
            procedure=(                                                          # rpt:*            
                ADT_A08_PROCEDURE_GROUP(
                    procedures=await build(pr1_16),
                    role=await build(rol_17),
                ),
                ADT_A08_PROCEDURE_GROUP(
                    procedures=await build(pr1_16),
                    role=await build(rol_17),
                ),
            ),
            guarantor=(                                                          # rpt:*            
                await build(gt1_18),
            ),
            insurance=(                                                          # rpt:*            
                ADT_A08_INSURANCE_GROUP(
                    insurance=await build(in1_19),
                    insurance_additional_information=await build(in2_20),
                    insurance_additional_information_certification=await build(in3_21),
                    role=await build(rol_22),
                ),
                ADT_A08_INSURANCE_GROUP(
                    insurance=await build(in1_19),
                    insurance_additional_information=await build(in2_20),
                    insurance_additional_information_certification=await build(in3_21),
                    role=await build(rol_22),
                ),
            ),
            accident=await build(acc_23),
            ub82_data=await build(ub1_24),
            ub92_data=await build(ub2_25),
            patient_death_and_autopsy=await build(pda_26),
        )

        return adt_a08.to_hl7()

async def main():
    x = UpstreamInput("1")
    xx = await Build_ADT_A08().run(x)
    print(xx)

if __name__ == "__main__":
    asyncio.run(main())