from enum_tools.documentation import document_enum

from cybsi.api.enum import CybsiAPIEnum


@document_enum
class ShareLevels(CybsiAPIEnum):
    """Information share level, according to Traffic Light Protocol."""

    White = "White"  # doc: Disclosure is not limited.
    Green = "Green"  # doc: Limited disclosure, restricted to the community.
    Amber = "Amber"  # noqa: E501 # doc: Limited disclosure, restricted to participants’ organizations.
    Red = "Red"  # doc: Not for disclosure, restricted to participants only.


@document_enum
class EntityTypes(CybsiAPIEnum):
    """Entity types."""

    IPAddress = "IPAddress"  # doc: IPv4 or IPv6 address.
    DomainName = "DomainName"  # doc: Domain name.
    File = "File"  # doc: File.
    EmailAddress = "EmailAddress"  # doc: Email address.
    PhoneNumber = "PhoneNumber"  # doc: Phone number.
    Identity = "Identity"  # doc: Identity.
    URL = "URL"  # doc: URL.


@document_enum
class EntityKeyTypes(CybsiAPIEnum):
    """Natural entity key types."""

    String = "String"  # doc: String identifying entity.
    MD5 = "MD5Hash"  # doc: File MD5 hash.
    SHA1 = "SHA1Hash"  # doc: File SHA1 hash.
    SHA256 = "SHA256Hash"  # doc: File SHA256 hash.
    IANAID = "IANAID"  # doc: Identity identifier in IANA registry.
    RIPEID = "RIPEID"  # doc: Identity identifier in RIPE database.
    NICHandle = "NICHandle"  # doc: Identity identifier in NIC database.


@document_enum
class AttributeNames(CybsiAPIEnum):
    """Entity attribute names.

    See Also:
        See :ref:`attributes`
        for complete information about available attributes.
    """

    Class = "Class"  # doc: Identity class.
    DisplayNames = "DisplayNames"  # doc: Email address display names.
    IsIoC = "IsIoC"  # doc: The entity is indicator of compromise.
    IsTrusted = "IsTrusted"  # doc: The entity is trusted.
    MalwareFamilyAliases = (
        "MalwareFamilyAliases"  # noqa: E501 # doc: Aliases of malware family.
    )
    Names = "Names"  # doc: Names of the entity.
    NodeRoles = "NodeRoles"  # doc: The role of the node in a network.
    Sectors = "Sectors"  # doc: Identity industry sector.
    Size = "Size"  # doc: Entity size.
    IsMalicious = "IsMalicious"  # doc: The entity is malicious.
    IsDGA = "IsDGA"  # doc: The domain was generated by algorithm.


@document_enum
class RelationshipKinds(CybsiAPIEnum):
    """Kind of a relationship between entities.

    See Also:
        See :ref:`relationships`
        for complete information about available relationships.
    """

    Has = "Has"
    Contains = "Contains"
    BelongsTo = "BelongsTo"  # doc: Deprecated.
    ConnectsTo = "ConnectsTo"
    Drops = "Drops"
    Uses = "Uses"
    Owns = "Owns"
    Supports = "Supports"
    ResolvesTo = "ResolvesTo"
    VariantOf = "VariantOf"  # doc: Deprecated.
    Targets = "Targets"
    Exploits = "Exploits"
    Hosts = "Hosts"
    Serves = "Serves"
    Locates = "Locates"


@document_enum
class EntityAggregateSections(CybsiAPIEnum):
    """Entity aggregation section."""

    AssociatedAttributes = "AssociatedAttributes"
    NaturalAttributes = "NaturalAttributes"
    Threat = "Threat"
    AVScanStatistics = "AVScanStatistics"
    GeoIP = "GeoIP"
    Labels = "Labels"


@document_enum
class ThreatStatus(CybsiAPIEnum):
    """Threat status."""

    Unknown = "Unknown"
    Malicious = "Malicious"
    NonMalicious = "NonMalicious"


@document_enum
class LinkDirection(CybsiAPIEnum):
    """Direction of links."""

    Forward = "Forward"
    Reverse = "Reverse"
