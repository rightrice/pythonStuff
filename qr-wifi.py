import os
import qrcode

os.system('cls')
ssid = input("\nWhat is your WiFi Network name?\n")
security = input("What type of network security do you have?\nEx: WPA, WEP, None.\n")
password = input(f"\nWhat is the password for {ssid}?\nIf there is no password, please press return.")

wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )

qr.add_data(wifi_data)
qr.make(fit=True)

img = qr.make_image(fill_color="#54ff8d", back_color="black")
img.save(f"{ssid}-qr-code.png")
img.show