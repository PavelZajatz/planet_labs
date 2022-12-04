class SearchFilters:
    DateRangeFilter = {
        "type": "DateRangeFilter",
        "field_name": "acquired",
        "config": {
            "gt": "2019-12-31T00:00:00Z",
            "lte": "2020-01-31T00:00:00Z"
        }
    }

    GeometryFilter = {
        "type": "GeometryFilter",
        "field_name": "geometry",
        "config": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -120.27282714843749,
                        38.348118547988065
                    ],
                    [
                        -120.27282714843749,
                        38.74337300148126
                    ],
                    [
                        -119.761962890625,
                        38.74337300148126
                    ],
                    [
                        -119.761962890625,
                        38.348118547988065
                    ],
                    [
                        -120.27282714843749,
                        38.348118547988065
                    ]
                ]
            ]
        }
    }

    NumberInFilter = {
        "type": "NumberInFilter",
        "field_name": "gsd",
        "config": [
            3
        ]
    }

    RangeFilter = {
        "type": "RangeFilter",
        "field_name": "cloud_cover",
        "config": {
            "lte": 0.1
        }
    }

    StringInFilter = {
        "type": "StringInFilter",
        "field_name": "quality_category",
        "config": [
            "standard",
            "test"
        ]
    }

    UpdateFilter = {
        "type": "UpdateFilter",
        "field_name": "ground_control",
        "config": {
            "gt": "2020-04-15T00:00:00Z"
        }
    }

    AssetFilter = {
        "type": "AndFilter",
        "config": [
            {
                "type": "AssetFilter",
                "config": [
                    "analytic_sr"
                ]
            },
            {
                "type": "AssetFilter",
                "config": [
                    "udm2"
                ]
            }
        ]
    }

    PermissionFilter = {
        "type": "PermissionFilter",
        "config": [
            "assets:download"
        ]
    }

    AndFilter = {
        "type": "AndFilter",
        "config": [
            {
                "type": "DateRangeFilter",
                "field_name": "acquired",
                "config": {
                    "gte": "2020-01-01T00:00:00Z",
                    "lte": "2020-01-31T00:00:00Z"
                }
            },
            {
                "type": "StringInFilter",
                "field_name": "ground_control",
                "config": [
                    "true"
                ]
            },
            {
                "type": "AssetFilter",
                "config": [
                    "analytic_sr"
                ]
            },
            {
                "type": "PermissionFilter",
                "config": [
                    "assets:download"
                ]
            }
        ]
    }

    OrFilter = {
        "type": "OrFilter",
        "config": [
            {
                "type": "RangeFilter",
                "field_name": "visible_percent",
                "config": {
                    "gte": 90
                }
            },
            {
                "type": "RangeFilter",
                "field_name": "usable_data",
                "config": {
                    "gte": 0.90
                }
            }
        ]
    }

    NotFilter = {
        "type": "NotFilter",
        "config": {
            "type": "StringInFilter",
            "field_name": "quality_category",
            "config": [
                "test"
            ]
        }
    }
