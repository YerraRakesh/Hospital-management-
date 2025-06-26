
import json
import os

filename = "patients.json"

def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_data(patients):
    with open(filename, "w") as f:
        json.dump(patients, f, indent=4)

def add_patient():
    patients = load_data()
    patient = {
        "id": len(patients) + 1,
        "name": input("Enter name: "),
        "age": input("Enter age: "),
        "gender": input("Enter gender: "),
        "disease": input("Enter disease: "),
        "contact": input("Enter contact number: "),
        "admit_date": input("Enter admission date: ")
    }
    patients.append(patient)
    save_data(patients)
    print("Patient added successfully.\n")

def view_patients():
    patients = load_data()
    for p in patients:
        print(p)

def search_patient():
    name = input("Enter name to search: ").lower()
    patients = load_data()
    found = [p for p in patients if p["name"].lower() == name]
    print(found if found else "No patient found.")

def update_patient():
    pid = int(input("Enter patient ID to update: "))
    patients = load_data()
    for p in patients:
        if p["id"] == pid:
            print(f"\nUpdating record for: {p['name']}")
            while True:
                print("\nWhat would you like to update?")
                print("1. Name")
                print("2. Age")
                print("3. Gender")
                print("4. Disease")
                print("5. Contact")
                print("6. Admission Date")
                print("7. Exit Update")

                choice = input("Enter choice: ")

                if choice == '1':
                    p["name"] = input("Enter new name: ")
                elif choice == '2':
                    p["age"] = input("Enter new age: ")
                elif choice == '3':
                    p["gender"] = input("Enter new gender: ")
                elif choice == '4':
                    p["disease"] = input("Enter new disease: ")
                elif choice == '5':
                    p["contact"] = input("Enter new contact number: ")
                elif choice == '6':
                    p["admit_date"] = input("Enter new admission date: ")
                elif choice == '7':
                    break
                else:
                    print("Invalid option.")

            save_data(patients)
            print("✅ Record updated.\n")
            return
    print("❌ Patient not found.\n")

def delete_patient():
    pid = int(input("Enter patient ID to delete: "))
    patients = load_data()
    patients = [p for p in patients if p["id"] != pid]
    save_data(patients)
    print("Record deleted.\n")

def menu():
    while True:
        print("\n--- Hospital Management ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()
