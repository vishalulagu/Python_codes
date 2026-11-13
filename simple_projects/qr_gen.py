# requirement ;
# qrcode[pil]


from qrcode import QRCode
qr = QRCode()
url = input("Enter URL: ")
name = input("Enter the name of the QR: ")
save_path = input("Enter Path to Save: ")


def qr_gen(url, name="unknown", save_path=""):
    if not save_path:
        save_path = r"C:\Users\VISHAL\Desktop\python-code\qrimgs"

    full_path = save_path + "\\" + name + ".png"

    qr.add_data(url)
    img = qr.make_image()
    img.save(full_path)
    return f"QR Saved in {full_path}"

print(qr_gen(url, name, save_path))
