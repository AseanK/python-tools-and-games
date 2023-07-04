import qrcode

def create(data):
    qr = qrcode.make(data)
    qr.save('qrcode.png')

def create_custom(data, size=10, border=2, bg='white', fill='black'):
    qr = qrcode.QRCode(
            box_size=size,
            border=border
        )
    qr.add_data(data)
    qr.make(fit=True)
    res = qr.make_image(fill_color=fill,back_color=bg)
    res.save('qrcode.png')

if __name__ == '__main__':
    while True:
        cont = input('Press Enter to continue or (Q) to Quit\n')
        data = input('Enter the data you want to generate\n')
        custom = input('Would you like to custom your qrcode? (Yes or No) \n').lower()
        if custom == 'yes' or custom == 'y':
            size = input('Enter the size of the qrcode (Enter for default)\n')
            border = input('Enter the border width (Enter for default)\n')
            bg = input('Enter the background color (Enter for default)\n')
            fill = input('Enter the fill color (Enter for default)\n')

            create_custom(data, size, border, bg, fill)

        elif custom == 'no' or custom == 'n':
            create(data)

        else:
            print('Please enter "Yes" or "No"')
