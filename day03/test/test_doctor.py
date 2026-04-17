# add project root and source root to python path
import os
import sys
import pytest
import csv





project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# src_root = os.path.join(project_root, 'src')
# sys.path.insert(0, src_root)
sys.path.insert(0, project_root)

from src.models.doctor import Doctor

"""
This module contains contract tests for the Doctor model and DoctorStore.
"""
def test_doctor_model():
    """Test the Doctor model's basic functionality."""
    doctor = Doctor(1, 'Dr. Smith', 'Cardiology')
    assert doctor.id == 1
    assert doctor.name == 'Dr. Smith'
    assert doctor.specialty == 'Cardiology'

def read_doctor_test_data():
    """Read doctor test data from a CSV file."""
    doctor_data = []
    csv_path = os.path.join(project_root, 'test', 'doctors.csv')
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or all(cell.strip() == '' for cell in row):
                continue
            if row[0].strip().lower() == 'id':
                continue
            doctor_data.append((int(row[0]), row[1], row[2]))
    return doctor_data


@pytest.mark.parametrize("doctor_id, expected_name, expected_specialty", read_doctor_test_data())
def test_doctor_creation_parameterized(doctor_id, expected_name, expected_specialty):
    """Test creating Doctor instances with different parameters."""
    doctor = Doctor(doctor_id, expected_name, expected_specialty)
    assert doctor.id == doctor_id
    assert doctor.name == expected_name
    assert doctor.specialty == expected_specialty
