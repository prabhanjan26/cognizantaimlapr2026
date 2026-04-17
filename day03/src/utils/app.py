import sys
import os
from datetime import date

# add project root and source root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
src_root = os.path.join(project_root, 'src')
sys.path.insert(0, src_root)
sys.path.insert(0, project_root)

from config.logger_config import setup_logger
from models.doctor import Doctor
from models.patient import Patient
from stores.doctor_store import DoctorStore
from stores.patient_store import PatientStore

"""run the healthcare application. Also the entry point of the application."""
logger = setup_logger()

def run():
    """Run CRUD operations for doctors and patients and log each step."""
    doctor_store = DoctorStore()
    patient_store = PatientStore()

    # Doctor CRUD
    dr_smith = Doctor(1, 'Dr. Smith', 'Cardiology')
    dr_jones = Doctor(2, 'Dr. Jones', 'Neurology')

    doctor_store.add_doctor(dr_smith)
    doctor_store.add_doctor(dr_jones)

    try:
        fetched_doctor = doctor_store.get_doctor(1)
        logger.info('Fetched doctor: %s', fetched_doctor)
    except Exception as exc:
        logger.error('Could not fetch doctor: %s', exc)

    doctor_store.update_doctor(2, name='Dr. Amy Jones', specialty='Pediatrics')
    logger.info('Updated doctor id 2 to: %s', doctor_store.get_doctor(2))

    doctor_store.delete_doctor(1)
    logger.info('Deleted doctor with id 1')

    try:
        doctor_store.get_doctor(1)
    except Exception as exc:
        logger.warning('Expected missing doctor: %s', exc)

    # Patient CRUD
    patient_1 = Patient(1, 'John Doe', date(1990, 5, 10), 'Flu')
    patient_2 = Patient(2, 'Jane Doe', date(1985, 8, 20), 'Migraine')

    patient_store.add_patient(patient_1)
    patient_store.add_patient(patient_2)

    try:
        fetched_patient = patient_store.get_patient_by_id(1)
        logger.info('Fetched patient: %s', fetched_patient)
    except Exception as exc:
        logger.error('Could not fetch patient: %s', exc)

    patient_store.update_patient(2, name='Jane Smith', ailment='Tension Headache')
    logger.info('Updated patient id 2 to: %s', patient_store.get_patient_by_id(2))

    patient_store.delete_patient(1)
    logger.info('Deleted patient with id 1')

    try:
        patient_store.get_patient_by_id(1)
    except Exception as exc:
        logger.warning('Expected missing patient: %s', exc)


if __name__ == '__main__':
    run()
