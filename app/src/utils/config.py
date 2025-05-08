import os

def load_config(key, default=None):
    """Load environment variables with a fallback default."""
    return os.getenv(key, default)

