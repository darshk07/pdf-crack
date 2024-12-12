from PyPDF2 import PdfReader

def check_pdf_password(pdf_path, password):
    try:
        reader = PdfReader(pdf_path)
        if reader.decrypt(password):
            print("Password is correct!")
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
pdf_path = "./path_to_pdf.pdf"
password = "abcd0000"
num = 0

def make_length_4(num):
		if num < 10:
				return "000" + str(num)
		if num < 100:
				return "00" + str(num)
		if num < 1000:
				return "0" + str(num)
		return str(num)


while (1):
		if (num > 9999): 
			break
		newPass = password + make_length_4(num)
		print(newPass)
		if check_pdf_password(pdf_path, newPass):
			print("PDF unlocked successfully.")
			print("Password is: " + newPass)
			break
		num +=1
    
            
    