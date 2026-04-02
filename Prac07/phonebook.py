import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    
    # Кестені құру
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        );
    """)
    
    # Кестеде UNIQUE шектеуі бар-жоғын тексеру және жоқ болса қосу
    try:
        cur.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint WHERE conname = 'contacts_phone_number_key'
                ) THEN
                    ALTER TABLE contacts ADD CONSTRAINT contacts_phone_number_key UNIQUE (phone_number);
                END IF;
            END $$;
        """)
    except Exception as e:
        print(f"Ескерту (Constraint): {e}")
        
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # UNIQUE шектеуі істеп тұрғандықтан, ON CONFLICT қате бермейді
                cur.execute(
                    """
                    INSERT INTO contacts (username, phone_number)
                    VALUES (%s, %s)
                    ON CONFLICT (phone_number) DO NOTHING
                    """,
                    (row["first_name"].strip(), row["phone"].strip())
                )
        conn.commit()
        print("Contacts inserted from CSV.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error during CSV insert: {e}")
        conn.rollback()
        
    cur.close()
    conn.close()

def insert_from_console():
    conn = get_connection()
    cur = conn.cursor()
    
    print("\n--- Енгізуді тоқтату үшін атына ештеңе жазбай Enter басыңыз ---")
    
    while True:
        name = input("Enter name: ").strip()
        if not name:  # Ат бос қалса цикл тоқтайды
            break
            
        phone = input("Enter phone: ").strip()
        
        try:
            cur.execute(
                "INSERT INTO contacts (username, phone_number) VALUES (%s, %s)",
                (name, phone)
            )
            conn.commit()
            print(f"Contact '{name}' inserted.")
        except Exception as e:
            print(f"Error inserting contact: {e}")
            conn.rollback()
            
    cur.close()
    conn.close()
    print("Console input completed.")

def update_contact():
    value = input("Enter existing name or phone of contact to update: ")
    field = input("What do you want to update? (name/phone): ").strip().lower()
    new_value = input("Enter new value: ")
    conn = get_connection()
    cur = conn.cursor()

    if field == "name":
        cur.execute(
            "UPDATE contacts SET username = %s WHERE username = %s OR phone_number = %s",
            (new_value, value, value)
        )
    elif field == "phone":
        cur.execute(
            "UPDATE contacts SET phone_number = %s WHERE username = %s OR phone_number = %s",
            (new_value, value, value)
        )
    else:
        print("Invalid field.")
        cur.close()
        conn.close()
        return

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated.")

def query_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    if rows:
        print("\n--- All Contacts ---")
        for row in rows:
            print(row)
    else:
        print("No contacts found.")
    cur.close()
    conn.close()

def query_by_name():
    name = input("Enter name filter: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM contacts WHERE username ILIKE %s ORDER BY id",
        (f"%{name}%",)
    )
    rows = cur.fetchall()
    if rows:
        print("\n--- Found Contacts ---")
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")
    cur.close()
    conn.close()

def query_by_phone_prefix():
    prefix = input("Enter phone prefix: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM contacts WHERE phone_number LIKE %s ORDER BY id",
        (f"{prefix}%",)
    )
    rows = cur.fetchall()
    if rows:
        print("\n--- Found Contacts ---")
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")
    cur.close()
    conn.close()

def delete_contact():
    value = input("Enter username or phone number to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM contacts WHERE username = %s OR phone_number = %s",
        (value, value)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted if it existed.")

def menu():
    create_table()
    while True:
        print("\n--- PhoneBook Menu (Practice 7) ---")
        print("1. Insert data from CSV")
        print("2. Insert data from console")
        print("3. Update contact name or phone")
        print("4. Query all contacts")
        print("5. Query by name")
        print("6. Query by phone prefix")
        print("7. Delete by username or phone")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_all()
        elif choice == "5":
            query_by_name()
        elif choice == "6":
            query_by_phone_prefix()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()