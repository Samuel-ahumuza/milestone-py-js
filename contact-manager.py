import json
import os

# Define the file name for storing contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Loads contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as f:
                # Load the dictionary from the file
                return json.load(f)
        except json.JSONDecodeError:
            # Handles case where file is empty or corrupted
            return {}
    return {}

def save_contacts(contacts):
    """Saves the current contacts dictionary to the JSON file."""
    with open(CONTACTS_FILE, 'w') as f:
        # Write the dictionary to the file in a readable format
        json.dump(contacts, f, indent=4)
    print("✅ Contacts saved successfully.")

# --- Core Functions ---

def add_contact(contacts):
    """Prompts user for contact details and adds them."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip().title()
    if not name:
        print("❌ Name cannot be empty.")
        return

    # Check for duplicate names
    if name in contacts:
        print(f"⚠️ Contact '{name}' already exists. Please choose a unique name or update the existing one.")
        return

    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()
    
    # Store contact using name as the key and a dictionary of details as the value
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"⭐ Contact '{name}' added!")

def view_contacts(contacts):
    """Displays all stored contacts."""
    print("\n--- Your Contacts ---")
    if not contacts:
        print("😔 Your contact book is empty.")
        return

    # Sort contacts alphabetically by name
    for name, details in sorted(contacts.items()):
        print("-" * 30)
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email'] if details['email'] else 'N/A'}")
    print("-" * 30)

def delete_contact(contacts):
    """Prompts user for a name and deletes the corresponding contact."""
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the Name of the contact to delete: ").strip().title()

    if name_to_delete in contacts:
        # Use pop() to remove the key-value pair and retrieve the details
        del contacts[name_to_delete]
        print(f"🗑️ Contact '{name_to_delete}' deleted.")
    else:
        print(f"❌ Contact '{name_to_delete}' not found.")

# --- Main Program Loop ---

def main():
    """The main function to run the Contact Manager."""
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Save & Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            save_contacts(contacts)
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
