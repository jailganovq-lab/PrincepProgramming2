import sys
import csv
from connect import get_connection

# 1. Implement inserting data from a CSV file
def import_from_csv(filename="contacts.csv"):
    conn = get_connection()
    if not conn: return
    
    try:
        count = 0
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("""
                        INSERT INTO contacts (username, phone_number)
                        VALUES (%s, %s)
                        ON CONFLICT (username) DO NOTHING;
                    """, (row['username'], row['phone_number']))
                    if cur.rowcount > 0:
                        count += 1
                conn.commit()
        print(f"Successfully imported {count} new contacts from CSV.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please create it first.")
    except Exception as e:
        print(f"Error importing CSV: {e}")
        conn.rollback()
    finally:
        conn.close()

# 2. Implement inserting data entered from the console
def add_contact():
    username = input("Enter username: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if not username or not phone:
        print("Username and phone number cannot be empty.")
        return
        
    conn = get_connection()
    if not conn: return
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO contacts (username, phone_number)
                VALUES (%s, %s)
                ON CONFLICT (username) 
                DO UPDATE SET phone_number = EXCLUDED.phone_number;
            """, (username, phone))
            conn.commit()
            print(f"Contact '{username}' saved.")
    except Exception as e:
        print(f"Error adding contact: {e}")
        conn.rollback()
    finally:
        conn.close()

# 3. Implement updating a contact's first name or phone number
def update_contact():
    username = input("Enter the username of the contact to update: ").strip()
    print("What do you want to update?")
    print("1. Change Username")
    print("2. Change Phone Number")
    choice = input("Select an option (1-2): ").strip()
    
    conn = get_connection()
    if not conn: return
    
    try:
        with conn.cursor() as cur:
            if choice == '1':
                new_username = input("Enter new username: ").strip()
                cur.execute("UPDATE contacts SET username = %s WHERE username = %s;", (new_username, username))
            elif choice == '2':
                new_phone = input("Enter new phone number: ").strip()
                cur.execute("UPDATE contacts SET phone_number = %s WHERE username = %s;", (new_phone, username))
            else:
                print("Invalid choice.")
                return
                
            if cur.rowcount > 0:
                conn.commit()
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
    except Exception as e:
        print(f"Error updating contact: {e}")
        conn.rollback()
    finally:
        conn.close()

# 4. Implement querying contacts with different filters
def query_contacts():
    print("\nQuery Options:")
    print("1. Show all contacts")
    print("2. Search by exact username")
    print("3. Search by username prefix (starts with)")
    print("4. Search by phone prefix (starts with)")
    choice = input("Select an option (1-4): ").strip()
    
    conn = get_connection()
    if not conn: return
    
    try:
        with conn.cursor() as cur:
            if choice == '1':
                cur.execute("SELECT username, phone_number FROM contacts;")
            elif choice == '2':
                val = input("Enter username: ").strip()
                cur.execute("SELECT username, phone_number FROM contacts WHERE username = %s;", (val,))
            elif choice == '3':
                val = input("Enter username prefix: ").strip()
                cur.execute("SELECT username, phone_number FROM contacts WHERE username LIKE %s;", (val + '%',))
            elif choice == '4':
                val = input("Enter phone prefix: ").strip()
                cur.execute("SELECT username, phone_number FROM contacts WHERE phone_number LIKE %s;", (val + '%',))
            else:
                print("Invalid choice.")
                return
            
            results = cur.fetchall()
            if not results:
                print("No contacts found.")
            else:
                print("\n--- CONTACTS ---")
                for row in results:
                    print(f"User: {row[0]} | Phone: {row[1]}")
                print("----------------")
    except Exception as e:
        print(f"Error querying contacts: {e}")
    finally:
        conn.close()

# 5. Implement deleting a contact by username or phone number
def delete_contact():
    print("\nDelete Options:")
    print("1. Delete by username")
    print("2. Delete by phone number")
    choice = input("Select an option (1-2): ").strip()
    
    conn = get_connection()
    if not conn: return
    
    try:
        with conn.cursor() as cur:
            if choice == '1':
                val = input("Enter username to delete: ").strip()
                cur.execute("DELETE FROM contacts WHERE username = %s;", (val,))
            elif choice == '2':
                val = input("Enter phone number to delete: ").strip()
                cur.execute("DELETE FROM contacts WHERE phone_number = %s;", (val,))
            else:
                print("Invalid choice.")
                return
                
            if cur.rowcount > 0:
                conn.commit()
                print("Contact deleted successfully.")
            else:
                print("No matching contact found to delete.")
    except Exception as e:
        print(f"Error deleting contact: {e}")
        conn.rollback()
    finally:
        conn.close()

# Console Interface
def main():
    # Attempt to build the table before running the program
    from connect import initialize_database
    initialize_database()
    
    while True:
        print("\n===== PhoneBook Menu =====")
        print("1. Import contacts from CSV")
        print("2. Add/Insert new contact")
        print("3. Update a contact")
        print("4. Query/Search contacts")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            import_from_csv("contacts.csv")
        elif choice == '2':
            add_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting PhoneBook. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()