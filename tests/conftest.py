import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    table.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table.metadata.drop_all(engine)
