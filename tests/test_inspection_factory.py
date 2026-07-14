import pytest

from core.inspection_factory import InspectionFactory
from inspection_person import PersonInspection

def test_factory_creates_person_inspection():
    inspection = InspectionFactory.create("person")

    assert isinstance(inspection, PersonInspection)

def test_factory_rejects_unknown_inspection():
    with pytest.raises(ValueError):
        InspectionFactory.create("unkown")
