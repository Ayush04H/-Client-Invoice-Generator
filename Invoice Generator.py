from datetime import datetime, timedelta

# Define your functions here

# Initialize the date
date = datetime.now()

# Call your functions
# Combine the text from each function to form the complete invoice
for i in range(1, 6):
    # Save the invoice_text in a .docx file
    with open(f"Invoice_{i}.docx", "w") as file:
        file.write(invoice_text)

    # Add 15 days to the date
    date += timedelta(days=15)
