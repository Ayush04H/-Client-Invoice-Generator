from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from docxtpl import DocxTemplate
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta 

root = Tk()
root.geometry("1500x600")
root.title("Invoice Automation")

frame = Frame(root)
frame.pack()

# 0. invoice and date info
date_and_invoice_info = LabelFrame(frame, text="Date & Invoice details:")
date_and_invoice_info.grid(row=0, column=1, sticky="news", padx=10, pady=10)

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
client_info.grid(row=0, column=2, sticky="news", padx=10, pady=10)

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
personal_branding_info.grid(row=1, column=0, sticky="news", padx=10, pady=10)

# contents of personal branding info
method_1 = StringVar(value="Personal Branding")
personal_branding_choices = {
    "LinkedIn Profile Audit and Update": 1000,
    "Market Research": 2000,
    "Market Strategy": 5000
}
# personal_branding_label = Label(personal_branding_info, text="Personal Branding:")
# personal_branding_label.grid(row=0, column=0)
personal_branding_listbox = Listbox(personal_branding_info, selectmode=EXTENDED, width=40, height=3)
for choice in personal_branding_choices.keys():
    personal_branding_listbox.insert(END, choice)
personal_branding_listbox.grid(row=0, column=0, padx=5, pady=10)

list1=[]
def calculate_first_subtotal():
    global list1
    first_subtotal = 0
    first_list = []
    # for listbox in [personal_branding_listbox, content_marketing_listbox, lead_generation_listbox, web_development_listbox]:
    for listbox in [personal_branding_listbox]:
        selected_indices = listbox.curselection()
        if selected_indices:
            for idx in selected_indices:
                choice_1 = listbox.get(idx)
                if choice_1 in personal_branding_choices:
                    first_subtotal += personal_branding_choices[choice_1]
                    first_list.append(choice_1)

    first_subtotal_textbox.delete(1.0, END)
    first_subtotal_textbox.insert(END, str(first_subtotal))

    first_list_text.delete(1.0, END)
    first_list_text.insert(END, str(first_list))

    # print(choice_1)
    list1=first_list.copy()
    return first_subtotal


first_list_text = Text(personal_branding_info, height=5, width=40)
first_list_text.grid(row=1, column=0, padx=5, pady=5)

first_subtotal_textbox = Text(personal_branding_info, height=1, width=40)
# first_subtotal_textbox.grid(row=2, column=0, padx=5, pady=5)

first_total_button = Button(personal_branding_info, text="Enter", command=calculate_first_subtotal)
first_total_button.grid(row=2, column=0, padx=5, pady=5)

#----------------------------------------------------------------------------#


# C. CONTENT MARKETING INFO
content_marketing_info = LabelFrame(frame, text="Content Marketing:")
content_marketing_info.grid(row=1, column=1, sticky="news", padx=10, pady=10)

method_2 = StringVar(value="Content Marketing")
content_marketing_choices = {
    "Content Writing": 1000,
    "Content Designing": 2000,
    "Video Editing": 3000,
    "Content Calendar Prep": 7000,
    "Social Media Management": 4000
}
content_marketing_listbox = Listbox(content_marketing_info, selectmode=EXTENDED, width=40, height=3)
for choice in content_marketing_choices.keys():
    content_marketing_listbox.insert(END, choice)
content_marketing_listbox.grid(row=0, column=0, padx=5, pady=10)

list2=[]
def calculate_second_subtotal():
    global list2
    second_subtotal = 0
    second_list = []
    # for listbox in [personal_branding_listbox, content_marketing_listbox, lead_generation_listbox, web_development_listbox]:
    for listbox in [content_marketing_listbox]:
        selected_indices = listbox.curselection()
        if selected_indices:
            for idx in selected_indices:
                choice_2 = listbox.get(idx)
                if choice_2 in content_marketing_choices:
                    second_subtotal += content_marketing_choices[choice_2]
                    second_list.append(choice_2)
    second_subtotal_textbox.delete(1.0, END)
    second_subtotal_textbox.insert(END, str(second_subtotal))
    second_list_text.delete(1.0, END)
    second_list_text.insert(END, str(second_list))
    list2=second_list.copy()
    return second_subtotal

second_list_text = Text(content_marketing_info, height=5, width=40)
second_list_text.grid(row=1, column=0, padx=5, pady=5)

second_subtotal_textbox = Text(content_marketing_info, height=1, width=10)
# second_subtotal_textbox.grid(row=0, column=1, padx=5, pady=5)

second_total_button = Button(content_marketing_info, text="Enter", command=calculate_second_subtotal)
second_total_button.grid(row=2, column=0, padx=5, pady=5)

#----------------------------------------------------------------------------------

# D. LEAD GENERATION INFO
lead_generation_info = LabelFrame(frame, text="Lead Generation:")
lead_generation_info.grid(row=1, column=2, sticky="news", padx=10, pady=10)

method_3 = StringVar(value="Lead Generation")
lead_generation_choices = {
    "Lead Scraping and Filtering": 1000,
    "Comment Engine": 8000,
    "DM Marketing": 9000,
    "Email Marketing": 3000
}
lead_generation_listbox = Listbox(lead_generation_info, selectmode=EXTENDED, width=40, height=3)
for choice in lead_generation_choices.keys():
    lead_generation_listbox.insert(END, choice)
lead_generation_listbox.grid(row=0, column=0, padx=5, pady=10)

list3=[]
def calculate_third_subtotal():
    global list3
    third_subtotal = 0
    third_list = []
    # for listbox in [personal_branding_listbox, content_marketing_listbox, lead_generation_listbox, web_development_listbox]:
    for listbox in [lead_generation_listbox]:
        selected_indices = listbox.curselection()
        if selected_indices:
            for idx in selected_indices:
                choice_3 = listbox.get(idx)
                if choice_3 in lead_generation_choices:
                    third_subtotal += lead_generation_choices[choice_3]
                    third_list.append(choice_3)

    third_subtotal_textbox.delete(1.0, END)
    third_subtotal_textbox.insert(END, str(third_subtotal))

    third_list_text.delete(1.0, END)
    third_list_text.insert(END, str(third_list))
    list3=third_list.copy()
    return third_subtotal


third_list_text = Text(lead_generation_info, height=5, width=40)
third_list_text.grid(row=1, column=0, padx=5, pady=5)

third_subtotal_textbox = Text(lead_generation_info, height=1, width=10)
# third_subtotal_textbox.grid(row=0, column=1, padx=5, pady=5)

third_total_button = Button(lead_generation_info, text="Enter", command=calculate_third_subtotal)
third_total_button.grid(row=2, column=0, padx=5, pady=5)

#------------------------------------------------------------------------------------#

# E. WEB DEV INFO
web_dev_info = LabelFrame(frame, text="Web Development:")
web_dev_info.grid(row=1, column=3, sticky="news", padx=10, pady=10)

method_4 = StringVar(value="Web Development")
web_development_choices = {
    "UI/UX Design": 1000,
    "Copywriting": 1000,
    "Launch and Post Launch Support": 1000
}
web_development_listbox = Listbox(web_dev_info, selectmode=EXTENDED, width=40, height=3)
for choice in web_development_choices.keys():
    web_development_listbox.insert(END, choice)
web_development_listbox.grid(row=0, column=0, padx=5, pady=10)

list4=[]
def calculate_fourth_subtotal():
    global list4
    fourth_subtotal = 0
    fourth_list = []
    # for listbox in [personal_branding_listbox, content_marketing_listbox, lead_generation_listbox, web_development_listbox]:
    for listbox in [web_development_listbox]:
        selected_indices = listbox.curselection()
        if selected_indices:
            for idx in selected_indices:
                choice_4 = listbox.get(idx)
                if choice_4 in web_development_choices:
                    fourth_subtotal += web_development_choices[choice_4]
                    fourth_list.append(choice_4)

    fourth_subtotal_textbox.delete(1.0, END)
    fourth_subtotal_textbox.insert(END, str(fourth_subtotal))

    fourth_list_text.delete(1.0, END)
    fourth_list_text.insert(END, str(fourth_list))
    list4=fourth_list.copy()
    return fourth_subtotal


fourth_list_text = Text(web_dev_info, height=5, width=40)
fourth_list_text.grid(row=1, column=0, padx=5, pady=5)

fourth_subtotal_textbox = Text(web_dev_info, height=1, width=10)
# fourth_subtotal_textbox.grid(row=0, column=1, padx=5, pady=5)

fourth_total_button = Button(web_dev_info, text="Enter", command=calculate_fourth_subtotal)
fourth_total_button.grid(row=2, column=0, padx=5, pady=5)


#--------------------------------------------------------------------------#

def enter_data():
    doc = DocxTemplate("Sample Invoice_1.docx")
    beg_date = beginning_date_entry.get_date().strftime('%d-%m-%Y')
    end_date = end_date_entry.get_date().strftime('%d-%m-%Y')
    date = date_entry.get_date().strftime('%d-%m-%Y')
    invoice_no = invoice_entry.get()
    comp_name = comp_name_label_entry.get()
    comp_add = comp_addr_label_entry.get()
    comp_gst = comp_gst_label_entry.get()
    comp_pan = comp_pan_label_entry.get()
    subtotal = subtotal_textbox.get("1.0", END)
    gsttotal = gst_textbox.get("1.0", END)
    total = total_textbox.get("1.0", END)

    context={"name_company": comp_name, "address": comp_add, "pan": comp_pan, "gst_no": comp_gst,
                 "beginning_date": beg_date,"end_date": end_date,
                "inv_no": "1", "inv_date": date,
                "services": [
            {
                "title": "Personal Branding (1 Account)",
                "details": list1
            },
            {
                "title": "Content Marketing (30 pieces of content)",
                "details": list2
            },
            {
                "title": "Content writing",
                "details": list3
            },
            {
                "title": "Web Development",
                "details": list4
            }
              ],
                "sum_total": subtotal_glob,
                "gst_val": gsttotal,
                "total": total,
                "amt_payable": total}
                #"web_lists":web,"lead_list":lead,"cont_list":cont,"per_list":per}
    doc.render(context)
    selected_service_title = "Content Marketing (30 pieces of content)"

# Filter the services list to only include the selected service
    context["services"] = [service for service in context["services"] if service["title"] == selected_service_title]

    beg_date_con=datetime.strptime(beg_date, '%d-%m-%Y')
    end_date_con=datetime.strptime(end_date,'%d-%m-%Y')
    date_con=datetime.strptime(date,'%d-%m-%Y')
    doc_name = comp_name + " - 1 dated from " + beg_date_con.date().strftime('%d-%m-%Y') + ' - ' + end_date_con.date().strftime('%d-%m-%Y') + " .docx"
    doc.save(doc_name)
   
    for x in range(2,7,1):
        
        beg_date_con=beg_date_con+timedelta(days=15) 
        end_date_con=end_date_con+timedelta(days=15)
        date_con=date_con+timedelta(days=15)
        context={"name_company": comp_name, "address": comp_add, "pan": comp_pan, "gst_no": comp_gst,
                 "beginning_date": beg_date_con.date().strftime('%d-%m-%Y'),"end_date": end_date_con.date().strftime('%d-%m-%Y'),
                "inv_no": str(x), "inv_date": date_con.date().strftime('%d-%m-%Y'),
                "services": [
                        {
                        "title": "Personal Branding (1 Account)",
                        "details": list1
                        },
                        {
                        "title": "Content Marketing (30 pieces of content)",
                        "details": list2
                        },
                        {
                        "title": "Content writing",
                        "details": list3
                        },
                        {
                        "title": "Web Development",
                        "details": list4
                        }
           
              ],
                "sum_total": subtotal_glob,
                "gst_val": gsttotal,
                "total": total,
                "amt_payable": total}
               # "web_lists":web,"lead_list":lead,"cont_list":cont,"per_list":per}
        doc.render(context)
        context["services"] = [service for service in context["services"] if service["title"] == selected_service_title]
        doc_name = comp_name +  " - " + str(x) + " dated from " + beg_date_con.date().strftime('%d-%m-%Y') + ' - ' + end_date_con.date().strftime('%d-%m-%Y') + " .docx"

        doc.save(doc_name)
    messagebox.showinfo("Invoice Complete", "Invoice Complete")




# C. Billing
subtotal_glob=0
def calculate_subtotal():
    global subtotal_glob
    subtotal = 0
    first_subtotal = float(first_subtotal_textbox.get("1.0", END)) if first_subtotal_textbox.get("1.0",
                                                                                                 END).strip() else 0.0
    second_subtotal = float(second_subtotal_textbox.get("1.0", END)) if second_subtotal_textbox.get("1.0",
                                                                                                    END).strip() else 0.0
    third_subtotal = float(third_subtotal_textbox.get("1.0", END)) if third_subtotal_textbox.get("1.0",
                                                                                                 END).strip() else 0.0
    fourth_subtotal = float(fourth_subtotal_textbox.get("1.0", END)) if fourth_subtotal_textbox.get("1.0",
                                                                                                    END).strip() else 0.0

    subtotal = first_subtotal + second_subtotal + third_subtotal + fourth_subtotal

    subtotal_textbox.delete(1.0, END)
    subtotal_textbox.insert(END, str(subtotal))
    subtotal_glob=subtotal
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

def setup_scrollbar(parent_frame, listbox):
    scrollbar = Scrollbar(parent_frame, orient=VERTICAL)
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")
    listbox.grid(row=0, column=0, sticky="nsew")

# Setup scrollbars for each listbox
setup_scrollbar(personal_branding_info, personal_branding_listbox)
setup_scrollbar(content_marketing_info, content_marketing_listbox)
setup_scrollbar(lead_generation_info, lead_generation_listbox)
setup_scrollbar(web_dev_info, web_development_listbox)



billing_info = LabelFrame(frame, text="Billing:")
billing_info.grid(row=2, column=1, sticky="news", padx=10, pady=10)

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
button.grid(row=3, column=1)
print(list2)
# --------------------------------------#
mainloop()
