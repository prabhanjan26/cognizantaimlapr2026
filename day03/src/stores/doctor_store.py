"""Create doctor crud operations."""

import logging
from models.doctor import Doctor
from exceptions.doctor_not_found_exception import DoctorNotFoundException

logger = logging.getLogger(__name__)


class DoctorStore:
    """A store for managing doctor records."""

    def __init__(self):
        """Initialize the doctor store."""
        self.doctors = {}

    def add_doctor(self, doctor):
        """Add a doctor to the store."""
        logger.info(f"Adding doctor with id {doctor.id} to the store.")
        if doctor.id in self.doctors:
            raise ValueError(f"Doctor with id {doctor.id} already exists.")
        self.doctors[doctor.id] = doctor

    def get_doctor(self, doctor_id):
        """Get a doctor by id."""
        logger.info(f"Retrieving doctor with id {doctor_id} from the store.")
        if doctor_id in self.doctors:
            return self.doctors[doctor_id]
        raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found.")

    def update_doctor(self, doctor_id, name=None, specialty=None):
        """Update a doctor's information."""
        logger.info(f"Updating doctor with id {doctor_id}.")
        doctor = self.get_doctor(doctor_id)
        if not doctor:
            raise ValueError(f"Doctor with id {doctor_id} does not exist.")
        if name:
            doctor.name = name
        if specialty:
            doctor.specialty = specialty

    def delete_doctor(self, doctor_id):
        """Delete a doctor from the store."""
        logger.info(f"Deleting doctor with id {doctor_id} from the store.")
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]
            