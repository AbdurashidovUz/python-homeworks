import numpy as np
from PIL import Image

def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype='uint8')
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, value=40):
    return np.clip(image_array + value, 0, 255)

def apply_mask(image_array):
    mask = image_array.copy()
    center_x, center_y = mask.shape[1] // 2, mask.shape[0] // 2
    mask[center_y-50:center_y+50, center_x-50:center_x+50] = 0
    return mask


image = Image.open('D:\python-homeworks\lesson-14\images\'birds.jpg')
image_array = np.array(image)


flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)
Image.fromarray(flipped_image).save('images/birds_flipped.jpg')
Image.fromarray(noisy_image).save('images/birds_noisy.jpg')
Image.fromarray(brightened_image).save('images/birds_brightened.jpg')
Image.fromarray(masked_image).save('images/birds_masked.jpg')