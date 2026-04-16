from models.doctor import Doctor
from models.patient import Patient
from services.mapper import map_patient_to_doctor


def main():
    doctors = [
        Doctor("Dr. Smith", "Cardiology"),
        Doctor("Dr. Alice", "Neurology"),
        Doctor("Dr. John", "Orthopedics"),
    ]

    patient = Patient("Ramesh", "Cardiology")

    doctor = map_patient_to_doctor(patient, doctors)

    print("Patient Details:")
    print(patient)

    if doctor:
        print(f"Assigned Doctor: {doctor.name}")
    else:
        print("No suitable doctor found")


if __name__ == "__main__":
    main()
