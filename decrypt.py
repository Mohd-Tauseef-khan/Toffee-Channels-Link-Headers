import pyzipper,os

def unzip_password_protected_zip(zip_file_path, output_path, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as z:
            z.extractall(output_path, pwd=password.encode('utf-8'))
        print("Extraction successful.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
zip_file_path = 'main.zip'
output_path = ''
password = os.environ["password"]
#
unzip_password_protected_zip(zip_file_path, output_path, password)

if password:
    # Save the password to a file
    with open("password.txt", "w") as file:
        file.write(password)
    print("Password saved to password.txt")
else:
    print("Password not found in environment variables.")


os.system("python main.py")
os.remove("main.py")
