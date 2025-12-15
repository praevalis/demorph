from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ConfigDto(BaseModel):
    """Base configuration for all DTOs."""

    model_config = ConfigDict(
        use_enum_values=True,  # Directly serializes the enum's values rather than variables
        alias_generator=to_camel,  # Generates camelCase alias for fields, allows cleaner code on client.
        populate_by_name=True,
    )


class RequestDto(ConfigDto):
    """Base API request DTO."""

    model_config = ConfigDict(
        extra='forbid'  # Prevent misformed payloads in request bodies
    )


class ResponseDto(ConfigDto):
    """Base API response DTO."""

    model_config = ConfigDict(
        from_attributes=True,  # Maps ORM objects to DTO
        extra='ignore',  # Excludes extra fields
    )
