# hl7
Statically typed HL7 python builder & parser library 

# Quickstart
```
uv pip install "git+ssh://git@github.com/AccuCodeAI/hl7.git[v2_5_1]"
```

```py
from hl7.v2_5_1.segments import MSH
from hl7.v2_5_1.data_types import ST, HD, IS, TS, DSM

msh = MSH(
field_separator=ST(x),
encoding_characters=ST(x),
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
)
)
```

- See sample temporal trigger event builder temporal workflows in `./examples`
- Check available versions to install in `./src/hl7`
