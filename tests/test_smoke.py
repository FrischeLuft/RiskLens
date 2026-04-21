from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risklens.config import Settings


class SettingsTests(unittest.TestCase):
    def test_defaults_are_loaded(self) -> None:
        settings = Settings.from_env()

        self.assertEqual(settings.environment, "dev")
        self.assertEqual(settings.db_host, "localhost")
        self.assertEqual(settings.db_port, 5432)
        self.assertEqual(settings.db_schema, "core")


if __name__ == "__main__":
    unittest.main()
