import subprocess
import cv2

input = "ressources/test.png"
width = 1280
quality = 20
resampling = 8
output = "ressources/test.jxl"

# Resize image
image = cv2.imread(input)
ratio = width / image.shape[1]
image = cv2.resize(image, (0, 0), fx = ratio, fy = ratio)

cv2.imwrite("ressources/test_resized.png", image)

# Convert to JPEG XL
process = subprocess.run(["cjxl", input, "-q", str(quality), f"--resampling={resampling}", output], capture_output=True)

print(process.returncode) # Should be zero
print(process.stdout)
print(process.stderr)
