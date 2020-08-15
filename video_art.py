import cv2
import numpy as np
from PIL import Image

def calculate_mean_pixel(img):
    # mean =[[.0 , .0 , .0]]
    # for pixel in range(img.shape[0]):
    #     mean = mean + img[pixel]
    # mean = mean / img.shape[0]
    # return mean
    
    img = img.transpose()

    # r = np.mean(img[:,0])
    # g = np.mean(img[:,1])
    # b = np.mean(img[:,2])



    r = round(np.mean(img[0,:]))
    g = round(np.mean(img[1,:]))
    b = round(np.mean(img[2,:]))
    print(r)
    print(g)
    print(b)
    return [r, g, b]

cap = cv2.VideoCapture('giphy.mp4')
i = 0


# red = Image.open('red.png')
# green = Image.open('green.png')
# blue = Image.open('blue.png')
# bw = Image.open('bw.jpg')

# r = np.array(red)
# g = np.array(green)
# b = np.array(blue)
# bw = np.array(bw)

# print(calculate_mean_pixel(r))
# print(calculate_mean_pixel(g))
# print(calculate_mean_pixel(b))
# print(calculate_mean_pixel(bw))

# cv2.imshow('kjkj', calculate_mean_pixel(bw))


data = np.zeros((100, 100, 3), dtype=np.uint8)


while True:
    i += 1
    # print(i)
    ret, frame = cap.read()
    if ret == True:
        # print(np.mean(frame))
        blurred = cv2.GaussianBlur(frame, (7,7), 0)
        # black_and_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        array = np.array(blurred)
        # mean = np.mean(array)
        mean_pixel = calculate_mean_pixel(array)

        # print(mean)

        for pixel in range(100):
            print(pixel)
            data[pixel] = mean_pixel
        result = Image.fromarray(data, 'RGB')
        result_name = 'resized_image.png'
        result.save(result_name)
        im = cv2.imread(result_name)


        # cv2.imshow('Video', blurred)
        cv2.imshow('color', im)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

#save the new resized image in the same directory
# data = np.zeros((h, w, 3), dtype=np.uint8)


cap.release()
cv2.destroyAllWindows()

