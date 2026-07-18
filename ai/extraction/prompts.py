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
You are an Industrial Ontology Extraction engine.
Extract structural relationships between the entities mentioned in the text.

IMPORTANT: You may ONLY use the following Entity IDs as your source and target.
VALID ENTITY IDS: {entity_list}

Return JSON only using this EXACT schema:
[
    {
        "source": "MUST BE FROM VALID ENTITY IDS",
        "relation": "MUST BE STRICTLY ONE OF THESE EXACT STRINGS: FEEDS_INTO, REGULATED_BY, MAINTAINED_BY, BYPASSES, POWERED_BY, MONITORES, CONTAINS, CONNECTED_TO, TRIGGERED_BY",
        "target": "MUST BE FROM VALID ENTITY IDS"
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