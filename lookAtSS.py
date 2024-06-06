import time

import pyautogui as pgui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

match_timer = [[186, 65], [260, 65], [186, 87], [260, 87]]

chars = [[342, 613, 402, 673], [342, 675, 402, 735], [342, 737, 402, 797], [342, 799, 402, 859], [342, 861, 402, 921]]

dmg = [[853, 613, 961, 673], [853, 675, 961, 735], [853, 737, 961, 797], [853, 799, 961, 859], [853, 861, 961, 921]]

heal = [[961, 613, 1066, 673], [961, 675, 1066, 735], [961, 737, 1066, 797], [961, 799, 1066, 859],
        [961, 861, 1066, 921]]


def main():
    time.sleep(0.5)
    ss = pgui.screenshot()
    ss.save('temp.png')
    for i in range(5):
        cropped_image = ss.crop((dmg[i][0], dmg[i][1], dmg[i][2], dmg[i][3]))
        cropped_image.show()
        text = pytesseract.image_to_string(cropped_image)
        print("The damage is ", text)

    for i in range(5):
        cropped_image = ss.crop((heal[i][0], heal[i][1], heal[i][2], heal[i][3]))
        cropped_image.show()
        text = pytesseract.image_to_string(cropped_image)
        print("The healing is ", text)


#  ss.show()


if __name__ == '__main__':
    main()
