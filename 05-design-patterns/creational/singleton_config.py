import json
from pathlib import Path


class ConfigManager:
    _instance: "ConfigManager | None" = None

    def __init__(self, config_path: str | Path = Path(__file__).with_name("config.json")) -> None:
        # TODO: Load JSON once and store data
        raise NotImplementedError

    @classmethod
    def get_instance(cls) -> "ConfigManager":
        # TODO: Return singleton instance, creating it once if needed
        raise NotImplementedError

    def get(self, key_path: str, default=None):
        # TODO: Traverse dot-separated keys like "database.host"
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for singleton_config.py")
