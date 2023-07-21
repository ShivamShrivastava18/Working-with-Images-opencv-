import time
from PIL import Image
import numpy as np

start_time = time.time()

img = np.array(Image.open(r'D:\\Omdena\\image.png'))

img_bgr = img[:, :, ::-1]

Image.fromarray(img_bgr).save('image_bgr.png')

end_time = time.time()

print("Execution time:", end_time - start_time, "seconds")