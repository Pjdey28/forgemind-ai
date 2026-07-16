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
You are an Industrial Information Extraction engine.
Extract relationships between the entities mentioned in the text.

IMPORTANT: You may ONLY use the following Entity IDs as your source and target. Do not invent new IDs.
VALID ENTITY IDS: {entity_list}

Return JSON only using this EXACT schema:
[
    {
        "source": "MUST BE FROM VALID ENTITY IDS",
        "relation": "RELATIONSHIP_TYPE_UPPERCASE",
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
UNIFIED_INDUSTRIAL_PROMPT = """
You are an expert Industrial Information Ingestion Engine.
Analyze the provided text fragment and extract Entities, Relationships, and measurable Facts.

1. ENTITIES: Extract equipment, components, catalysts, chemicals, or valves. Assign a standardized, clean uppercase string as the ID.
2. RELATIONSHIPS: Connect the extracted entities. The source and target strings MUST exactly match the normalized uppercase IDs you defined in the entities section.
3. FACTS: Extract property conditions or setpoints.

Return ONLY a valid JSON object matching this exact structural layout:
{
    "entities": [
        {"id": "REACTOR-R101", "label": "Equipment", "name": "Reactor-R101"},
        {"id": "TS-1", "label": "Catalyst", "name": "Titanium Silicate-1"}
    ],
    "relationships": [
        {"source": "REACTOR-R101", "relation": "CONTAINS", "target": "TS-1"}
    ],
    "facts": [
        {"key": "MAX_TEMPERATURE", "value": "180°C", "confidence": 0.95}
    ]
}
Do not include conversational filler, markdown formatting blocks, or extra text wrapper objects.
"""