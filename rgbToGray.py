import os
import cv2
import sys


def resize(img):
    resized_img = cv2.resize(img, (300, 300))
    print("The image resize is complete and the rest of the program is progressing...")
    return resized_img


def check_size(img):
    height, width, _ = img.shape

    # Check if the size is 300x300
    if width == 300 and height == 300:
        print("Image size is 300x300.")
    else:
        print("Image size is not 300x300.")
        answer = input("Do you want to convert it to 300x300? (yes/no): ").lower()
        if answer == "yes":
            # Resize the image to 300x300
            return resize(img)
        else:
            print("Program closed.")
            sys.exit()


def rgb_to_other_color_spaces(input_image_path, output_dir):
    # Load the RGB image
    img = cv2.imread(input_image_path)

    # Check image size
    img = check_size(img)

    # Convert to Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to CIE XYZ color space
    xyz_img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

    # Convert to YCrCb color space
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Convert to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Convert to HLS color space
    hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # Convert to CIE L*a*b color space
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

    # Convert to CIE L*u*v color space
    luv_img = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the converted images in the output directory
    cv2.imwrite(os.path.join(output_dir, "gray_image.jpg"), gray_img)
    cv2.imwrite(os.path.join(output_dir, "xyz_image.jpg"), xyz_img)
    cv2.imwrite(os.path.join(output_dir, "ycrcb_image.jpg"), ycrcb_img)
    cv2.imwrite(os.path.join(output_dir, "hsv_image.jpg"), hsv_img)
    cv2.imwrite(os.path.join(output_dir, "hls_image.jpg"), hls_img)
    cv2.imwrite(os.path.join(output_dir, "lab_image.jpg"), lab_img)
    cv2.imwrite(os.path.join(output_dir, "luv_image.jpg"), luv_img)


if __name__ == "__main__":
    # The 'output_image' folder will be created in the same directory as the script
    rgb_to_other_color_spaces("input_rgb_image.jpeg", "output_image")
    print("Image saved in 'output_image' directory.")
