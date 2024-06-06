import time
import pyautogui as pgui
import pytesseract
from PIL import Image, ImageOps, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

match_timer_crop_values = [186, 65, 260, 87]

character_crop_values = [[342, 613, 402, 673], [342, 675, 402, 735], [342, 737, 402, 797], [342, 799, 402, 859],
                         [342, 861, 402, 921]]

dmg_crop_values = [[853, 613, 961, 673], [853, 675, 961, 735], [853, 737, 961, 797], [853, 799, 961, 859],
                   [853, 861, 961, 921]]

heal_crop_values = [[961, 613, 1066, 673], [961, 675, 1066, 735], [961, 737, 1066, 797], [961, 799, 1066, 859],
                    [961, 861, 1066, 921]]

match_time = 0

player_damage_dealt = []

player_healing_done = []


def enhanceImage(image):
    # Resize the image to double its size
    resized_image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)

    # Enhance the sharpness of the image
    enhancer = ImageEnhance.Sharpness(resized_image)
    sharpened_image = enhancer.enhance(2.0)
    return sharpened_image


def main():
    time.sleep(0.1)
    ss = pgui.screenshot()
    grey_scale_image = ImageOps.grayscale(ss)
    ss.save('temp.png')
    grey_scale_image.save('temp_grey.png')

    # Get the value of the match timer
    cropped_image = grey_scale_image.crop((match_timer_crop_values[0], match_timer_crop_values[1],
                                           match_timer_crop_values[2], match_timer_crop_values[3]))
    text = pytesseract.image_to_string(enhanceImage(cropped_image), config='--psm 6')
    minutes, seconds = text.split(':')
    minutes = int(minutes)
    seconds = int(seconds)
    match_time = minutes * 60 + seconds
    print("The match time is ", match_time, "seconds")

    # Get the damage dealt value for each player
    for i in range(5):
        cropped_image = grey_scale_image.crop(
            (dmg_crop_values[i][0], dmg_crop_values[i][1], dmg_crop_values[i][2], dmg_crop_values[i][3]))
        text = pytesseract.image_to_string(enhanceImage(cropped_image), config='--psm 6')
        text = text.replace(',', '')
        player_damage_dealt.append(int(text))
        print("The damage is ", text)

    # Get the healing done value for each player
    for i in range(5):
        cropped_image = grey_scale_image.crop(
            (heal_crop_values[i][0], heal_crop_values[i][1], heal_crop_values[i][2], heal_crop_values[i][3]))
        text = pytesseract.image_to_string(enhanceImage(cropped_image), config='--psm 6')
        text = text.replace(',', '')
        player_healing_done.append(int(text))
        print("The healing is ", text)


if __name__ == '__main__':
    main()
