import pytest
# Sample message from HL7 Normative Edition
# http://healthinfo.med.dal.ca/hl7intro/CDA_R2_normativewebedition/help/v3guide/v3guide.htm#v3gexamples


def assert_hl7_equal(actual: str, expected: str):
    """
    Asserts that two HL7 messages are equal, providing detailed difference information if they're not.

    Args:
        actual: The actual HL7 message produced
        expected: The expected HL7 message to compare against

    Raises:
        AssertionError: If messages don't match, with detailed difference information
    """
    if actual == expected:
        return

    # Split both messages into fields
    actual_fields = actual.split("|")
    expected_fields = expected.split("|")

    # Get segment names
    actual_segment = actual_fields[0]
    expected_segment = expected_fields[0]

    if actual_segment != expected_segment:
        raise AssertionError(
            f"Segment mismatch: expected '{expected_segment}', got '{actual_segment}'"
        )

    # Compare lengths
    if len(actual_fields) != len(expected_fields):
        raise AssertionError(
            f"Field count mismatch: expected {len(expected_fields)} fields, got {len(actual_fields)}\n"
            f"Expected: {expected}\n"
            f"Actual  : {actual}"
        )

    # Compare each field
    differences = []
    for i, (exp_field, act_field) in enumerate(zip(expected_fields, actual_fields)):
        if exp_field != act_field:
            differences.append(f"Field {i}: expected '{exp_field}', got '{act_field}'")

    if differences:
        # Create a visual difference display
        visual_diff = "\n".join(
            [
                "Expected: " + expected,
                "Actual  : " + actual,
                "",
                "Differences found:",
                "\n".join(differences),
            ]
        )
        raise AssertionError("\n" + visual_diff)


# Usage:
# assert_hl7_equal(msh.to_hl7(), expected)


# Example with difference highlighting:
def highlight_differences(actual: str, expected: str) -> tuple[str, str]:
    """
    Returns a tuple of (expected, actual) with differences highlighted using >>> <<<

    Example:
        expected = "MSH|^~\\&|GHH LAB"
        actual = "MSH|^~\\&|GHH LAB2"
        highlight_differences(actual, expected)
        # Returns:
        # ("MSH|^~\\&|>>>GHH LAB<<<", "MSH|^~\\&|>>>GHH LAB2<<<")
    """
    if actual == expected:
        return expected, actual

    actual_fields = actual.split("|")
    expected_fields = expected.split("|")

    highlighted_expected = []
    highlighted_actual = []

    for i in range(max(len(actual_fields), len(expected_fields))):
        exp_field = expected_fields[i] if i < len(expected_fields) else ""
        act_field = actual_fields[i] if i < len(actual_fields) else ""

        if exp_field != act_field:
            highlighted_expected.append(f">>>{exp_field}<<<")
            highlighted_actual.append(f">>>{act_field}<<<")
        else:
            highlighted_expected.append(exp_field)
            highlighted_actual.append(act_field)

    return ("|".join(highlighted_expected), "|".join(highlighted_actual))


def test_serialize_msh1():
    from hl7.v2_5_1.segments import MSH
    from hl7.v2_5_1.data_types import ST, HD, IS, TS, DTM, MSG, PT
    from hl7.v2_5_1.tables import MessageType, EventType, MessageStructure, ProcessingId

    msh = MSH(
        sending_application=ST("GHH LAB"),
        sending_facility=HD(namespace_id=IS("ELAB-3")),
        receiving_application=HD(namespace_id=IS("GHH OE")),
        receiving_facility=HD(namespace_id=IS("BLDG4")),
        date_or_time_of_message=TS(time=DTM("200202150930")),
        message_type=MSG(
            message_code=MessageType.UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE,  # ORU
            trigger_event=EventType.LOG_EVENT,  # LOG
            message_structure=MessageStructure.R01,  # ORU_R01
        ),
        message_control_id=ST("CNTRL-3456"),
        processing_id=PT(
            processing_id=ProcessingId.PRODUCTION  # P
        ),
        version_id=ST("2.5.1"),
    )
    expected = "MSH|^~\\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^LOG^ORU_R01|CNTRL-3456|P|2.5.1"
    assert_hl7_equal(msh.to_hl7(), expected)


def test_deserialize_msh1():
    from hl7.v2_5_1.segments import MSH
    from hl7.v2_5_1.data_types import MSG
    from hl7.v2_5_1.tables import MessageType, EventType, MessageStructure, ProcessingId

    target = "MSH|^~\\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^LOG^ORU_R01|CNTRL-3456|P|2.5.1"
    msh = MSH.from_hl7(target)
    assert msh.sending_application == "GHH LAB"
    assert msh.sending_facility == "ELAB-3"
    assert msh.receiving_application == "GHH OE"
    assert msh.receiving_facility == "BLDG4"
    assert msh.date_or_time_of_message == "200202150930"
    assert (
        msh.message_type
        == MSG(
            message_code=MessageType.UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE,  # ORU
            trigger_event=EventType.LOG_EVENT,  # LOG
            message_structure=MessageStructure.R01,  # ORU_R01
        )
    )


def test_msh1_alt_encoding_chars():
    from hl7.v2_5_1.segments import MSH
    from hl7.v2_5_1.data_types import ST, HD, IS, TS, DTM, MSG, PT
    from hl7.v2_5_1.tables import MessageType, EventType, MessageStructure, ProcessingId

    msh = MSH(
        field_separator=ST("*"),
        encoding_characters=ST("!~\\&"),
        sending_application=ST("GHH LAB"),
        sending_facility=HD(namespace_id=IS("ELAB-3")),
        receiving_application=HD(namespace_id=IS("GHH OE")),
        receiving_facility=HD(namespace_id=IS("BLDG4")),
        date_or_time_of_message=TS(time=DTM("200202150930")),
        message_type=MSG(
            message_code=MessageType.UNSOLICITED_TRANSMISSION_OF_AN_OBSERVATION_MESSAGE,  # ORU
            trigger_event=EventType.LOG_EVENT,  # LOG
            message_structure=MessageStructure.R01,  # ORU_R01
        ),
        message_control_id=ST("CNTRL-3456"),
        processing_id=PT(
            processing_id=ProcessingId.PRODUCTION  # P
        ),
        version_id=ST("2.5.1"),
    )
    expected = "MSH*!~\\&*GHH LAB*ELAB-3*GHH OE*BLDG4*200202150930**ORU!LOG!ORU_R01*CNTRL-3456*P*2.5.1"
    assert_hl7_equal(msh.to_hl7(), expected)
