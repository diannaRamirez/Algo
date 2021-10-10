import numpy as np
from PIL import Image


def rgb2gray(rgb: np.array) -> np.array:
    """
    Return gray image from rgb image
    >>> rgb2gray(np.array([[[127, 255, 0]]]))
    array([[187.6453]])
    >>> rgb2gray(np.array([[[0, 0, 0]]]))
    array([[0.]])
    >>> rgb2gray(np.array([[[2,  4,  1]]]))
    array([[3.0598]])
    >>> rgb2gray(np.array([[[26,  255,  14], [ 5,  147, 20], [ 1,  200,  0]]]))
    array([[159.0524,  90.0635, 117.6989]])
    """
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def gray2binary(gray: np.array) -> np.array:
    """
    Return binary image from gray image
    >>> gray2binary(np.array([[127, 255, 0]]))
    array([[False,  True, False]])
    >>> gray2binary(np.array([[0]]))
    array([[False]])
    >>> gray2binary(np.array([[26.2409,  4.9315,  1.4729]]))
    array([[False, False, False]])
    >>> gray2binary(np.array([[26,  255,  14], [ 5,  147, 20], [ 1,  200,  0]]))
    array([[False,  True, False],
           [False,  True, False],
           [False,  True, False]])
    """
    return (127 < gray) & (gray <= 255)


def erosion(image: np.array, kernel: np.array) -> np.array:
    """
    Return eroded image
    >>> erosion(np.array([[True, True, False]]), np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
    array([[False, False, False]])
    >>> erosion(np.array([[True, False, False]]), np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
    array([[False, False, False]])
    """
    output = np.zeros_like(image)
    image_padded = np.zeros(
        (image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1)
    )

    # Copy image to padded image
    image_padded[kernel.shape[0] - 2 : -1 :, kernel.shape[1] - 2 : -1 :] = image

    # Iterate over image & apply kernel
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            summation = (
                kernel * image_padded[y : y + kernel.shape[0], x : x + kernel.shape[1]]
            ).sum()
            if summation == 5:
                output[y, x] = 1
            else:
                output[y, x] = 0
    return output


# kernel to be applied
structuring_element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

if __name__ == "__main__":
    # read original image
    image = np.array(Image.open(r"..\image_data\lena.jpg"))
    # convert it into binary image
    binary = gray2binary(rgb2gray(image))
    # Apply erosion operation
    output = erosion(binary, structuring_element)
    # Save the output image
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_erosion.png")
