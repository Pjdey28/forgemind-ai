ENTITY_EXTRACTION_PROMPT = """
You are an Industrial Information Extraction engine.

Extract every industrial entity.

Possible entities include

Equipment
Asset
Machine
Catalyst
Component
Material
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

Return JSON only using this EXACT schema:
{
    "CategoryName": [
        {
            "id": "STANDARDIZED_ID_IN_UPPERCASE (e.g., REACTOR-R101, TS-1, VALVE-V404)",
            "name": "Original Text Name"
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

Return JSON only using this EXACT schema:
[
    {
        "key": "Property Name (e.g., Pressure, Temperature)",
        "value": "Measured Value (e.g., 180°C, 100 psi)",
        "confidence": 0.95
    }
]
"""