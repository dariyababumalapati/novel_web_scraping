import pywhatkit as kit

book_number = '901-905'
# Path to the file you want to send
file_path = f"C:/Users/91833/Downloads/{book_number}_cleaned.epub"

# WhatsApp number of the contact (include country code without '+' or '00')
contact_number = "+19135485129"

# Send the file
kit.send_file_via_whatsapp(contact_number,file_path)