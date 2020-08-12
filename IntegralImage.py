from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

sum

def rowSum(currentRow, currentColumn, imagepath):
    image = Image.open(imagepath)
    inputPixels = np.array(image)
    global sum
    sum = 0
    for colm in range(currentColumn):
        sum += inputPixels[currentRow, colm]

    return sum

def integralImageNormalized(imagePath):
    image = Image.open(imagePath)
    inputPixels = np.array(image)
    row = image.size[0]
    col = image.size[1]
    outputPixels = np.zeros((row, col))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if i == 0 and j == 0:
                outputPixels[i, j] = inputPixels[i, j]
                print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j}  if 1")
            elif i >= 0 and j >= 0:

                if i == 0 and j > 0:
                    outputPixels[i, j] = inputPixels[i, j] + rowSum(i, j, imagePath)
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 2")

                elif i > 0 and j == 0:
                    outputPixels[i, j] = inputPixels[i, j] + outputPixels[i - 1, j]
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 3")

                else:
                    outputPixels[i, j] = inputPixels[i, j] + rowSum(i, j, imagePath) + outputPixels[i - 1, j]
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 4")

    maxInt = np.amax(outputPixels)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if outputPixels[i, j] > 255:
                outputPixels[i, j] /= maxInt / 255.0
                outputPixels[i, j] = int(outputPixels[i, j])
    Image.fromarray(outputPixels).show()
    plt.imsave("/Users/amrabuelfadl/Desktop/Camera_Integ.jpg", outputPixels, cmap="gray")
    return outputPixels

def integralImage(imagePath):
    image = Image.open(imagePath)
    inputPixels = np.array(image)
    row = image.size[0]
    col = image.size[1]
    outputPixels = np.zeros((row, col))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if i == 0 and j == 0:
                outputPixels[i, j] = inputPixels[i, j]
                print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j}  if 1")
            elif i >= 0 and j >= 0:

                if i == 0 and j > 0:
                    outputPixels[i, j] = inputPixels[i, j] + rowSum(i, j, imagePath)
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 2")

                elif i > 0 and j == 0:
                    outputPixels[i, j] = inputPixels[i, j] + outputPixels[i - 1, j]
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 3")

                else:
                    outputPixels[i, j] = inputPixels[i, j] + rowSum(i, j, imagePath) + outputPixels[i - 1, j]
                    print(f"Input: {inputPixels[i, j]} Output: {outputPixels[i, j]}  row: {i}  col: {j} if 4")


    return outputPixels

def filteringImage(image, s):
    OriginalImage = Image.open(image)
    original_ImagePixels = np.array(OriginalImage)
    row = OriginalImage.size[0]
    col = OriginalImage.size[1]
    med = int((s-1)/2)
    integral_ImagePixels = integralImage(image)
    for i in range(med + 1, row - med - 2):
        for j in range(med + 1, col - med - 2):
            original_ImagePixels[i, j] = (integral_ImagePixels[i + med, j + med] - integral_ImagePixels[i - med - 1, j + med] - integral_ImagePixels[i + med, j - med - 1] + integral_ImagePixels[i - med - 1, j - med - 1]) / (s*s)

    plt.imsave(f"/Users/amrabuelfadl/Desktop/Camera_Filt_{s}.jpg", original_ImagePixels, cmap="gray")
    return original_ImagePixels

Image.fromarray(filteringImage("/Users/amrabuelfadl/Desktop/ComputerVision/Assignment 1_30408/Cameraman_noise.bmp", 5)).show()
integralImageNormalized("/Users/amrabuelfadl/Desktop/ComputerVision/Assignment 1_30408/Cameraman_noise.bmp")