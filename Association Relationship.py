class Doctor:
    def __init__(self, name: str):
        self.name = name
        self.patients = []  # Keeps track of patients

class Patient:
    def __init__(self, patient_id: int, doctor: Doctor):
        self.patient_id = patient_id
        self.doctor = doctor  # Establishes a standard reference link
        doctor.patients.append(self)


# --- Running the code ---
# 1. Instantiate the doctor
dr_smith = Doctor("Dr. Smith")

# 2. Instantiate individual patients and pass the doctor object
patient_1 = Patient(501, dr_smith)
patient_2 = Patient(502, dr_smith)

# 3. Verify the cross-referencing capabilities
print(f"Doctor Profile: {dr_smith.name}")
print("Linked patients tracked inside Doctor array:")
for p in dr_smith.patients:
    print(f"  - Patient ID: {p.patient_id}")

print(f"\nPatient #501 lookup -> Assigned to doctor: {patient_1.doctor.name}")
