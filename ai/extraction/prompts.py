ENTITY_EXTRACTION_PROMPT = """
You are an Industrial Information Extraction engine.

Extract every industrial entity.

Possible entities include

Equipment
Asset
Machine
Pump
Valve
Motor
Department
Person
Team
Document
Inspection
Failure
Incident
Maintenance
Location
Plant
Sensor
Work Order
Manual

Return JSON only.

{
    "Equipment":[
        {
            "id":"",
            "name":""
        }
    ]
}
"""
RELATIONSHIP_EXTRACTION_PROMPT = """
Extract relationships.

Examples

Pump P101
MAINTAINED_BY
Mechanical Team

Pump P101
LOCATED_IN
Plant A

Motor M2
PART_OF
Pump P101

Return JSON only.

[
    {
        "source":"",
        "relation":"",
        "target":""
    }
]
"""

FACT_EXTRACTION_PROMPT = """
Extract measurable industrial facts.

Examples

Pressure

Temperature

Inspection Date

Failure Date

Running Hours

Downtime

Manufacturer

Return JSON only.
"""