import os
import sys
from datetime import date

import pytest
import csv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.models.patient import Patient


def test_patient_model():
    """Test the Patient model's basic functionality."""
    patient = Patient(1, 'Rahul Menon', date(1990, 5, 14), 'Diabetes')
    assert patient.id == 1
    assert patient.name == 'Rahul Menon'
    assert patient.dob == date(1990, 5, 14)
    assert patient.ailment == 'Diabetes'


def read_patient_test_data():
    """Read patient test data from a CSV file."""
    patient_data = []
    csv_path = os.path.join(project_root, 'test', 'patient.csv')
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or all(cell.strip() == '' for cell in row):
                continue
            if row[0].strip().lower() == 'id':
                continue
            patient_data.append((int(row[0]), row[1], date.fromisoformat(row[2]), row[3]))
    return patient_data


@pytest.mark.parametrize("patient_id, expected_name, expected_dob, expected_ailment", read_patient_test_data())
def test_patient_creation_parameterized(patient_id, expected_name, expected_dob, expected_ailment):
    """Test creating Patient instances with different parameters."""
    patient = Patient(patient_id, expected_name, expected_dob, expected_ailment)
    assert patient.id == patient_id
    assert patient.name == expected_name
    assert patient.dob == expected_dob
    assert patient.ailment == expected_ailment

