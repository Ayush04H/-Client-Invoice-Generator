from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from docxtpl import DocxTemplate
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Invoice Automation")

frame = Frame(root)
frame.pack()

# 0. invoice and date info
date_and_invoice_info = LabelFrame(frame, text="Date & Invoice details:")
date_and_invoice_info.grid(row=0, column=0, sticky="news", padx=10, pady=10)

# contents of date label frame
beginning_date = Label(date_and_invoice_info, text="Beginning Date")
beginning_date.grid(row=0, column=0)
beginning_date_entry = DateEntry(date_and_invoice_info, selectmode='day', date_pattern='dd-MM-yyyy')
beginning_date_entry.grid(row=1, column=0, padx=5, pady=5)

end_date = Label(date_and_invoice_info, text="End Date")
end_date.grid(row=0, column=1)
end_date_entry = DateEntry(date_and_invoice_info, selectmode='day', date_pattern='dd-MM-yyyy')
end_date_entry.grid(row=1, column=1, padx=5, pady=5)

date_label = Label(date_and_invoice_info, text="Invoice Date")
date_label.grid(row=2, column=0)
date_entry = DateEntry(date_and_invoice_info, selectmode='day', date_pattern='dd-MM-yyyy')
date_entry.grid(row=3, column=0, padx=5, pady=5)

# contents of invoice label frame
invoice_label = Label(date_and_invoice_info, text="Invoice No.")
invoice_label.grid(row=2, column=1)
invoice_entry = Entry(date_and_invoice_info)
invoice_entry.grid(row=3, column=1, padx=15, pady=5)

def next_step():
    if invoice_entry.get():
        # the user entered data in the mandatory entry: proceed to next step
        # print("next step")
        root.destroy()
    else:
        # the mandatory field is empty
        print("KINDLY FILL INVOICE NUMBER")
        invoice_entry.focus_set()

    print("\n---------\n")


# --------------------------------------------------#
client_info = LabelFrame(frame, text="Client's Address:")
client_info.grid(row=1, column=0, sticky="news", padx=10, pady=10)


comp_name_label = Label(client_info, text="Company's Name:")
comp_name_label.grid(row=0, column=0)
comp_name_label_entry = Entry(client_info)
comp_name_label_entry.grid(row=0, column=1)

comp_addr_label = Label(client_info, text="Company's Address")
comp_addr_label.grid(row=1, column=0)
comp_addr_label_entry = Entry(client_info)
comp_addr_label_entry.grid(row=1, column=1)

comp_gst_label = Label(client_info, text="GST No.")
comp_gst_label.grid(row=2, column=0)
comp_gst_label_entry = Entry(client_info)
comp_gst_label_entry.grid(row=2, column=1)

comp_pan_label = Label(client_info, text="PAN No.")
comp_pan_label.grid(row=3, column=0)
comp_pan_label_entry = Entry(client_info)
comp_pan_label_entry.grid(row=3, column=1)










# --------------------------------------------------#
# B. PERSONAL BRANDING INFO
personal_branding_info = LabelFrame(frame, text="Personal Branding:")
personal_branding_info.grid(row=2, column=0, sticky="news", padx=10, pady=10)

method_1 = StringVar(value="Personal Branding")
personal_branding_choices = {
    "LinkedIn Profile Audit and Update": 1000,
    "Market Research": 2000,
    "Market Strategy": 5000
}

# Create a list to store selected services
service_1 = []

# Function to calculate the subtotal and update the list of selected services
def calculate_first_subtotal():
    first_subtotal = 0
    service_1.clear()  # Clear the list before updating it
    for idx, (choice, value) in enumerate(personal_branding_choices.items()):
        is_checked = var_list[idx].get()
        if is_checked:
            service_1.append(choice)
            first_subtotal += value

    first_subtotal_textbox.delete(1.0, END)
    first_subtotal_textbox.insert(END, str(first_subtotal))

    print(service_1)

    return first_subtotal


# Create Checkbuttons for personal branding choices
var_list = []  # List to store IntVar for each Checkbutton
for idx, (choice, value) in enumerate(personal_branding_choices.items()):
    var = IntVar()
    var_list.append(var)
    check_button = Checkbutton(personal_branding_info, text=choice, variable=var)
    check_button.grid(row=idx, column=0, padx=5, pady=5)

# Button to calculate subtotal
first_total_button = Button(personal_branding_info, text="Calculate Subtotal", command=calculate_first_subtotal)
first_total_button.grid(row=len(personal_branding_choices), column=0, columnspan=2, pady=10)

# Textbox for displaying the subtotal
first_subtotal_textbox = Text(personal_branding_info, height=1, width=10)
first_subtotal_textbox.grid(row=len(personal_branding_choices), column=2, padx=5, pady=5)


# C. CONTENT MARKETING INFO
content_marketing_info = LabelFrame(frame, text="Content Marketing:")
content_marketing_info.grid(row=2, column=1, sticky="news", padx=10, pady=10)

method_2 = StringVar(value="Content Marketing")
content_marketing_choices = {
    "Content Writing": 1000,
    "Content Designing": 2000,
    "Video Editing": 3000,
    "Content Calendar Prep": 7000,
    "Social Media Management": 4000
}

# Create a list to store selected services
service_2 = []

# Function to calculate the subtotal and update the list of selected services
def calculate_second_subtotal():
    second_subtotal = 0
    service_2.clear()  # Clear the list before updating it
    for idx, (choice, value) in enumerate(content_marketing_choices.items()):
        is_checked = var_list[idx].get()
        if is_checked:
            service_2.append(choice)
            second_subtotal += value

    second_subtotal_textbox.delete(1.0, END)
    second_subtotal_textbox.insert(END, str(second_subtotal))

    print(service_2)

    return second_subtotal


# Create Checkbuttons for content marketing choices
var_list = []  # List to store IntVar for each Checkbutton
for idx, (choice, value) in enumerate(content_marketing_choices.items()):
    var = IntVar()
    var_list.append(var)
    check_button = Checkbutton(content_marketing_info, text=choice, variable=var)
    check_button.grid(row=idx, column=0, padx=5, pady=5)

# Button to calculate subtotal
second_total_button = Button(content_marketing_info, text="Calculate Subtotal", command=calculate_second_subtotal)
second_total_button.grid(row=len(content_marketing_choices), column=0, columnspan=2, pady=10)

# Textbox for displaying the subtotal
second_subtotal_textbox = Text(content_marketing_info, height=1, width=10)
second_subtotal_textbox.grid(row=len(content_marketing_choices), column=2, padx=5, pady=5)

# D. LEAD GENERATION INFO
lead_generation_info = LabelFrame(frame, text="Lead Generation:")
lead_generation_info.grid(row=0, column=0, sticky="news", padx=10, pady=10)

method_3 = StringVar(value="Lead Generation")
lead_generation_choices = {
    "Lead Scraping and Filtering": 1000,
    "Comment Engine": 8000,
    "DM Marketing": 9000,
    "Email Marketing": 3000
}

# Create a list to store selected services
service_3 = []

# Function to calculate the subtotal and update the list of selected services
def calculate_third_subtotal():
    third_subtotal = 0
    service_3.clear()  # Clear the list before updating it
    for idx, (choice, value) in enumerate(lead_generation_choices.items()):
        is_checked = var_list[idx].get()
        if is_checked:
            service_3.append(choice)
            third_subtotal += value

    third_subtotal_textbox.delete(1.0, END)
    third_subtotal_textbox.insert(END, str(third_subtotal))

    print(service_3)

    return float(third_subtotal)



# Create Checkbuttons for lead generation choices
var_list = []  # List to store IntVar for each Checkbutton
for idx, (choice, value) in enumerate(lead_generation_choices.items()):
    var = IntVar()
    var_list.append(var)
    check_button = Checkbutton(lead_generation_info, text=choice, variable=var)
    check_button.grid(row=idx, column=0, padx=5, pady=5)

# Button to calculate subtotal
third_total_button = Button(lead_generation_info, text="Calculate Subtotal", command=calculate_third_subtotal)
third_total_button.grid(row=len(lead_generation_choices), column=0, columnspan=2, pady=10)

# Textbox for displaying the subtotal
third_subtotal_textbox = Text(lead_generation_info, height=1, width=10)
third_subtotal_textbox.grid(row=len(lead_generation_choices), column=2, padx=5, pady=5)




# E. WEB DEV INFO
web_dev_info = LabelFrame(frame, text="Web Development:")
web_dev_info.grid(row=3, column=1, sticky="news", padx=10, pady=10)

method_4 = StringVar(value="Web Development")
web_development_choices = {
    "UI/UX Design": 1000,
    "Copywriting": 1000,
    "Launch and Post Launch Support": 1000
}

# Create a list to store selected services
service_4 = []

# Function to calculate the subtotal and update the list of selected services
def calculate_fourth_subtotal():
    fourth_subtotal = 0
    service_4.clear()  # Clear the list before updating it
    for idx, (choice, value) in enumerate(web_development_choices.items()):
        is_checked = var_list[idx].get()
        if is_checked:
            service_4.append(choice)
            fourth_subtotal += value

    fourth_subtotal_textbox.delete(1.0, END)
    fourth_subtotal_textbox.insert(END, str(fourth_subtotal))

    print(service_4)

    return fourth_subtotal


# Create Checkbuttons for web development choices
var_list = []  # List to store IntVar for each Checkbutton
for idx, (choice, value) in enumerate(web_development_choices.items()):
    var = IntVar()
    var_list.append(var)
    check_button = Checkbutton(web_dev_info, text=choice, variable=var)
    check_button.grid(row=idx, column=0, padx=5, pady=5)

# Button to calculate subtotal
fourth_total_button = Button(web_dev_info, text="Calculate Subtotal", command=calculate_fourth_subtotal)
fourth_total_button.grid(row=len(web_development_choices), column=0, columnspan=2, pady=10)

# Textbox for displaying the subtotal
fourth_subtotal_textbox = Text(web_dev_info, height=1, width=10)
fourth_subtotal_textbox.grid(row=len(web_development_choices), column=2, padx=5, pady=5)




def enter_data():
    doc=DocxTemplate("Sample Invoice_1.docx")
    beg_date = beginning_date_entry.get()
    end_date = end_date_entry.get()
    date = date_entry.get()
    invoice_no = invoice_entry.get()
    comp_name = comp_name_label_entry.get()
    comp_add = comp_addr_label_entry.get()
    comp_gst = comp_gst_label_entry.get()
    comp_pan = comp_pan_label_entry.get()
    subtotal=subtotal_textbox.get("1.0", END)
    gsttotal=gst_textbox.get("1.0", END)
    total=total_textbox.get("1.0", END)
    doc.render({"name_company":comp_name,"address":comp_add,"pan":comp_pan,"gst_no":comp_gst,
            "end_date":end_date,"beginning_date":beg_date,
            "inv_no":invoice_no,"inv_date":date,
            "sum_total":subtotal,
            "gst_val":gsttotal,
            "total":total})
    doc.save("Final.docx")
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
# C. Billing
def calculate_subtotal():
    subtotal = 0
    first_subtotal = float(first_subtotal_textbox.get("1.0", END))
    second_subtotal = float(second_subtotal_textbox.get("1.0", END))
    third_subtotal = float(third_subtotal_textbox.get("1.0", END))
    fourth_subtotal = float(fourth_subtotal_textbox.get("1.0", END))

    subtotal = first_subtotal + second_subtotal + third_subtotal + fourth_subtotal


    subtotal_textbox.delete(1.0, END)
    subtotal_textbox.insert(END, str(subtotal))
    return subtotal

def calculate_gst():
    subtotal = float(subtotal_textbox.get("1.0", END))
    if subtotal is not None:
        gst = subtotal * 0.18

    gst_textbox.delete(1.0, END)
    gst_textbox.insert(END, str(gst))

    return gst

def calculate_total():
    subtotal = float(subtotal_textbox.get("1.0", END))
    gst = float(gst_textbox.get("1.0", END))
    total = subtotal + gst
    total_textbox.delete(1.0, END)
    total_textbox.insert(END, str(total))



billing_info = LabelFrame(frame, text="Billing:")
billing_info.grid(row=6, column=0, sticky="news", padx=10, pady=10)

# Textbox for Subtotal
subtotal_textbox_label = Label(billing_info, text="Subtotal")
subtotal_textbox_label.grid(row=0, column=0)
subtotal_textbox = Text(billing_info, height=1, width=10)
subtotal_textbox.grid(row=0, column=1, padx=5, pady=5)

calculate_subtotal_button = Button(billing_info, text="Calculate Subtotal", command=calculate_subtotal)
calculate_subtotal_button.grid(row=0, column=2, padx=5, pady=5)

# Textbox for gst
gst_textbox_label = Label(billing_info, text="GST")
gst_textbox_label.grid(row=1, column=0)
gst_textbox = Text(billing_info, height=1, width=10)
gst_textbox.grid(row=1, column=1, padx=5, pady=5)

calculate_gst_button = Button(billing_info, text="Calculate GST", command=calculate_gst)
calculate_gst_button.grid(row=1, column=2, padx=5, pady=5)

# Textbox for TOTAL
total_label = Label(billing_info, text="Total")
total_label.grid(row=2, column=0)
total_textbox = Text(billing_info, height=1, width=10)
total_textbox.grid(row=2, column=1, padx=5, pady=5)

calculate_total_button = Button(billing_info, text="Calculate Total", command=calculate_total)
calculate_total_button.grid(row=2, column=2, padx=5, pady=5)

# FINAL BUTTON
button = Button(frame, text="Enter Data", command=enter_data)
button.grid(row=7, column=0)

# --------------------------------------#
mainloop()