from script import process_csv_and_send_emails

def main():
    
    csv_file = input("Please enter the path to your CSV file: ").strip()
    
    process_csv_and_send_emails(csv_file)

if __name__ == "__main__":
    main()
