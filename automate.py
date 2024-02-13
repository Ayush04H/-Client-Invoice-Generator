from docxtpl import DocxTemplate

doc=DocxTemplate("Sample Invoice_1.docx")
doc.render({"name_company":"FC BARCELONA","address":"Bengaluru,India","pan":"UTR88965231513212","gst_no":"45698712",
            "end_date":"31th September, 2023","beginning_date":"20th September, 2023",
            "inv_no":"1","inv_date":"13th September,2024"})
            
doc.save("final_invoice.docx")