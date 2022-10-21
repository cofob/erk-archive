from enum import Enum, unique


@unique
class WebAppTypes(Enum):
    """Enum for WebView status update types."""

    TEST = 0
    """Test type."""
