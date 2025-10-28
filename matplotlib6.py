from PIL import Image
import matplotlib.pyplot as plt

#images and saving in matplotlib 

#images
img = Image.open("ironman.webp")   # use Pillow
plt.imshow(img)
plt.axis("off")
plt.show()

#saving
plt.savefig("plot.png", dpi=300, bbox_inches="tight")