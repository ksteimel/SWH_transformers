import pytest
from pathlib import Path


@pytest.fixture
def project_root_dir_path() -> Path:
    return Path(".")


@pytest.fixture
def fixtures_dir_path(project_root_dir_path: Path) -> Path:
    return project_root_dir_path / "test_fixtures"


@pytest.fixture
def sample_sentence_level_data_path(fixtures_dir_path: Path):
    return fixtures_dir_path / "sample_sentence_level_data.txt"
