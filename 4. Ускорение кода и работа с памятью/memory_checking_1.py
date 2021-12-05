import numpy as np


def make_big_array():
    return np.zeros((1024, 1024, 50))


def make_two_arrays():
    arr1 = np.zeros((1024, 1024, 10))
    arr2 = np.ones((1024, 1024, 10))
    return arr1, arr2


def stack_images(iterable, n_pixels):
    """stack the images in the iterable on a (n_pixel x n_pixel) canvas"""

    canvas = np.zeros((n_pixels,n_pixels))

    for item in iterable:
        canvas += item

    return canvas


def get_random_image(n_pixels):
    """create a random 2D image with n_pixels on the side"""

    return np.random.rand(n_pixels, n_pixels)


def stack_using_list(n_images, n_pixels):
    """iterate through a list and stack the objects"""

    iterable = [get_random_image(n_pixels) for _ in range(n_images)]
    stack_images(iterable, n_pixels)


def stack_using_generator(n_images, n_pixels):
    iterable = (get_random_image(n_pixels) for _ in range(n_images))
    stack_images(iterable, n_pixels)


from parallel import if_prime