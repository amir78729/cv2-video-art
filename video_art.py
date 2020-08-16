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

cap = cv2.VideoCapture('only-man.mp4')
# cap = cv2.VideoCapture('giphy.mp4')
# cap = cv2.VideoCapture('IMG_4998.MOV')
# cap = cv2.VideoCapture('video_2020-08-16_00-37-23.mp4')
# cap = cv2.VideoCapture('video_2020-08-16_00-42-02.mp4')
# cap = cv2.VideoCapture('Family.Guy.S11E04.Yug.Ylimaf.720p.WEB-DL.x264-DLHA_www.Downloadha.com_.mkv')




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
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(total_frames)

width = total_frames
height = round(width/4)
max_width = 1000
image_width = round(max_width/4)
image_height = total_frames%max_width+max_width

demo_array = np.zeros((height, width, 3), dtype=np.uint8)

demo_array[:,:] = [0,0,0]
demo_image = Image.fromarray(demo_array, 'RGB')
demo_image_resized = demo_image.resize((image_height, image_width))
# demo_image_resized.show()

resolution = 200
data = np.zeros((resolution, resolution, 3), dtype=np.uint8)
mean_array = np.array([[0, 0, 0]])

while True:
    i += 1
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('original video', frame)
        blurred = cv2.GaussianBlur(frame, (7,7), 0)
        # black_and_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           


        array = np.array(blurred)
        mean_pixel = calculate_mean_pixel(array)
        for pixel in range(resolution):
            data[pixel] = mean_pixel
        result = Image.fromarray(data, 'RGB')
        result_name = 'frame-color.png'
        result.save(result_name)
        average_frame = cv2.imread(result_name)
        # print color on frame
        font = cv2.FONT_HERSHEY_PLAIN 
        org = (20, 100) 
        fontScale = 0.8
        color = (255, 255, 255) 
        thickness = 1
        average_frame = cv2.putText(average_frame, 'frame #' + str(i) + ': (' + str(int(mean_pixel[0])) + ',' + str(int(mean_pixel[1])) + ',' + str(int(mean_pixel[2])) + ')', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.imshow('modified video', average_frame)

        mean_array = np.append(mean_array, mean_pixel)

        #timeline
        # demo_image = Image.fromarray(demo_array, 'RGB')

        # result.save('timeline.jpg')#
        # timeline = cv2.imread('timeline.jpg')#

        # demo_image_resized = demo_image.resize((image_height, image_width))#
        # demo_array[:,i - 1] = mean_array[i]#
        # open_cv_image = np.array(demo_image_resized) 


        
        demo_array[:,i - 1] = mean_array[i]
        demo_image = Image.fromarray(demo_array, 'RGB')
        demo_image_resized = demo_image.resize((image_height, image_width))
        result_name = 'timeline.png'
        demo_image_resized.save(result_name)
        timeline = cv2.imread(result_name)
        # open_cv_image = np.array(demo_image_resized) 
        # timeline = timeline[:, :, ::-1].copy() 
        percentage = str(100*i/total_frames) + '%'
        font = cv2.FONT_HERSHEY_PLAIN 
        org = (int(image_height/2)-100, int(image_width/2)) 
        fontScale = 2
        color = (255, 255, 255) 
        thickness = 1
        timeline = cv2.putText(timeline, percentage, org, font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.imshow('timeline', timeline)

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

print(mean_array.shape[0])

# print(height, width)
data = np.zeros((height, width, 3), dtype=np.uint8)
# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
for pixel in range(0, width):
    data[:,pixel] = mean_array[pixel]

img = Image.fromarray(data, 'RGB')

img = img.resize((image_height, image_width))
img.save('The Art From the Video.jpg')
img.show()

cap.release()
cv2.destroyAllWindows()

