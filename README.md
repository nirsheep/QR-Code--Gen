# QR Code Generator

This project contains a Python script that generates QR codes from URLs. The generated QR codes are saved as PNG files. This functionality is encapsulated in the `generate_qr_code` function.

## Functionality

The `generate_qr_code` function takes two parameters:
1. `url`: The URL to be encoded into a QR code.
2. `file_path`: The file path where the generated QR code should be saved. This parameter is optional and defaults to 'qr_code.png'.

The function uses the `qrcode` Python library to create and save the QR code. The generated QR code is saved as a PNG file at the specified `file_path`.

## Requirements

To run this script, you'll need Python 3 and the `qrcode` library. You can install the required library using pip:

```bash
pip install qrcode[pil]
