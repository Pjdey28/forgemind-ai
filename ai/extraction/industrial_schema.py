from pydantic import BaseModel, Field


class Equipment(BaseModel):
    id: str
    type: str


class Incident(BaseModel):
    name: str
    severity: str | None = None


class Maintenance(BaseModel):
    activity: str


class Measurement(BaseModel):
    parameter: str
    value: str


class IndustrialEntities(BaseModel):

    equipment: list[Equipment] = Field(default_factory=list)

    incidents: list[Incident] = Field(default_factory=list)

    maintenance: list[Maintenance] = Field(default_factory=list)

    measurements: list[Measurement] = Field(default_factory=list)

    departments: list[str] = Field(default_factory=list)

    operators: list[str] = Field(default_factory=list)

    regulations: list[str] = Field(default_factory=list)

    dates: list[str] = Field(default_factory=list)