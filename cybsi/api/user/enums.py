from enum_tools import document_enum

from cybsi.api.enum import CybsiAPIEnum


@document_enum
class RoleName(CybsiAPIEnum):
    """Role name.

    Role means a list of permissions.
    Each permission is Resource:Action pair.
    See :class:`ResourceName`.
    """

    Administrator = "Administrator"  # noqa: E501 doc: Administrator's role permissions: DataSources:rw,EnrichmentConfig:r,Users:r
    ConfigReader = "ConfigReader"  # noqa: E501 doc: ConfigReader's role permissions: [DataSources:r, EnrichmentConfig:r]
    FeedAdministrator = "FeedAdministrator"  # noqa: E501 doc: FeedAdministrator's role permissions: [DataSources:r, Feeds:rw, FeedsData:r, Observable:r, ReputationLists:rw, ReputationListsContent:r, Search:r, SearchFilters:rw, StoredQuery:rw, Users:r]
    FeedDataReader = "FeedDataReader"  # noqa: E501 doc: FeedDataReader's role permissions: [DataSources:r, Feeds:r, FeedsData:r, ReputationLists:r, ReputationListsContent:r, SearchFilters:r, StoredQuery:r, Users:r]
    EnrichmentRunner = "EnrichmentRunner"  # noqa: E501 doc: EnrichmentRunner's role permissions: [DataSources:r, EnrichmentTasks:rw]
    EnrichmentTaskReader = "EnrichmentTaskReader"  # noqa: E501 doc: EnrichmentTaskReader's role permissions: [DataSources:r, EnrichmentTasks:r]
    ReportRegistrant = "ReportRegistrant"  # noqa: E501 doc: ReportRegistrant's role permissions: [Observations:w, Reports:w]
    ReportReader = "ReportReader"  # noqa: E501 doc: ReportReader's role permissions: [DataSources:r, Observations:r, RawReports:r, Reports:r]
    EntityRegistrant = "EntityRegistrant"  # noqa: E501 doc: EntityRegistrant's role permissions: [Observable:w]
    EntityReader = "EntityReader"  # noqa: E501 doc: EntityReader's role permissions: [DataSources:r, Observable:r]
    ArtifactReader = "ArtifactReader"  # noqa: E501 doc: ArtifactReader's role permissions: [Artifacts:r, DataSources:r]
    ArtifactRegistrant = "ArtifactRegistrant"  # noqa: E501 doc: ArtifactRegistrant's role permissions: [Artifacts:w]
    ArtifactContentReader = "ArtifactContentReader"  # noqa: E501 doc: ArtifactContentReader's role permissions: [Artifacts:r, ArtifactsContent:r]
    Searcher = "Searcher"  # noqa: E501 doc: Searcher's role permissions: [DataSources:r, Observable:r, Search:r, SearchFilters:rw]
    UserAdministrator = "UserAdministrator"  # noqa: E501 doc: UserAdministrator's role permissions: [APIKeys:rw, Users:rw]


@document_enum
class ResourceName(CybsiAPIEnum):
    """Resource name.

    Permission can be with read/write action for almost all resources.
    Exclusion resources:
    ArtifactsContent, RawReports, Search, ReputationListsContent.
    """

    Artifacts = "Artifacts"  # doc: Samples.
    ArtifactsContent = "ArtifactsContent"  # noqa: E501 doc: Sample contents. Permission can be only with reading action.
    DataSources = "DataSources"  # doc: Data sources.
    EnrichmentConfig = "EnrichmentConfig"  # doc: Enrichment configs.
    EnrichmentTasks = "EnrichmentTasks"  # doc: Enrichment tasks.
    Feeds = "Feeds"  # doc: Feeds.
    FeedsData = "FeedsData"  # noqa: E501 doc: Feed contents. Permission can be only with reading action.
    Observable = "Observable"  # doc: Observable entities.
    Observations = "Observations"  # doc: Observations.
    RawReports = "RawReports"  # noqa: E501 doc: Initial data of reports and observations. Permission can be only with reading action.
    Reports = "Reports"  # doc: Reports.
    Search = "Search"  # doc: Search. Permission can be only with reading action.
    SearchFilters = "SearchFilters"  # doc: Search filters.
    Users = "Users"  # doc: Users.
    APIKeys = "APIKeys"  # doc: Access keys.
    ReputationLists = "ReputationLists"  # doc: Reputation lists.
    ReputationListsContent = "ReputationListsContent"  # noqa: E501 doc: Reputation list contents. Permission can be only with reading action.
    StoredQuery = "StoredQuery"  # doc: Stored queries.
