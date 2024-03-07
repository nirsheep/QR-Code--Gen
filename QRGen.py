import qrcode

# Function to generate QR code from URL and save as PNG
def generate_qr_code(url, file_path='qr_code.png'):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save it somewhere, change the path as needed
    img.save(file_path)

    return f"QR code generated and saved as {file_path}"

# Example usage
url = "https://www.alto.com"  # Replace with the URL you want
output_file = "output_qr.png"    # The file path where the QR code will be saved
generate_qr_code(url, output_file)
