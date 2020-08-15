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
    # print(r)
    # print(g)
    # print(b)
    return [r, g, b]

cap = cv2.VideoCapture('giphy.mp4')
cap = cv2.VideoCapture('lick.mp4')

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

resolution = 200
data = np.zeros((resolution, resolution, 3), dtype=np.uint8)
mean_array = np.array([[0, 0, 0]])
while True:
    i += 1
    # print(i)
    ret, frame = cap.read()
    if ret == True:
        # print(np.mean(frame))
        cv2.imshow('original video', frame)
        blurred = cv2.GaussianBlur(frame, (7,7), 0)
        # black_and_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        array = np.array(blurred)
        # mean = np.mean(array)
        mean_pixel = calculate_mean_pixel(array)
        for pixel in range(resolution):
            # print(pixel)
            data[pixel] = mean_pixel
        result = Image.fromarray(data, 'RGB')
        result_name = 'resized_image.png'
        result.save(result_name)
        average_frame = cv2.imread(result_name)
        # cv2.imshow('Video', blurred)
        cv2.imshow('modified video', average_frame)
        # print(mean_pixel)
        mean_array = np.append(mean_array, mean_pixel)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

#save the new resized image in the same directory
# data = np.zeros((h, w, 3), dtype=np.uint8)
mean_array = np.reshape(mean_array, (-1, 3))
# print(mean_array)

# max_width = 1000
# width = mean_array.shape[0]%max_width+max_width
# height = round(max_width/4)

width = mean_array.shape[0]
height = round(width/4)

print(height, width)
data = np.zeros((height, width, 3), dtype=np.uint8)
# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
for pixel in range(0, width):
    data[:,pixel] = mean_array[pixel]



img = Image.fromarray(data, 'RGB')

max_width = 1000
width = round(max_width/4)
height = mean_array.shape[0]%max_width+max_width
img = img.resize((height, width))
img.save('The Art From the Video.jpg')
img.show()

cap.release()
cv2.destroyAllWindows()

