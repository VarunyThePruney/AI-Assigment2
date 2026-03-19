import os
from PIL import Image

# ===== CONFIGURATION =====
CAPTCHA_PATH = "TTandCaptcha/captchaimage.png"
CORRECT_ANSWER = "smwn"

def show_captcha():
    """Opens the CAPTCHA image."""
    if not os.path.exists(CAPTCHA_PATH):
        print("Captcha image not found at:", CAPTCHA_PATH)
        return False

    img = Image.open(CAPTCHA_PATH)
    img.show()
    return True


def verify_captcha():
    """Handles user verification."""
    user_input = input("Enter the text shown in the CAPTCHA: ")
    user_input = user_input.strip().lower()

    if user_input == CORRECT_ANSWER:
        print("CAPTCHA Verified. You are human.")
        return True
    else:
        print("Incorrect.CAPTCHA Failed. Access denied.")

    print("")
    return False


def main():
    if show_captcha():
        verify_captcha()


if __name__ == "__main__":
    main()