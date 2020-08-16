import cv2
import numpy as np
from PIL import Image

def calculate_mean_pixel(img):    
    img = img.transpose()
    r = round(np.mean(img[0,:]))
    g = round(np.mean(img[1,:]))
    b = round(np.mean(img[2,:]))
    return [r, g, b]

#input video (change it!)
video_name = 'only-man.mp4'
cap = cv2.VideoCapture(video_name)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

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
demo_frame_color = np.zeros((resolution, resolution, 3), dtype=np.uint8)
mean_array = np.array([[0, 0, 0]])

frame_index = 0
while True:
    frame_index += 1
    ret, frame = cap.read()
    if ret == True:
        # original video
        cv2.imshow('original-video', frame)

        # calculating mean pixel
        blurred = cv2.GaussianBlur(frame, (7,7), 0)
        array = np.array(blurred)
        mean_pixel = calculate_mean_pixel(array)
        mean_array = np.append(mean_array, mean_pixel)

        # frame color
        for pixel in range(resolution):
            demo_frame_color[pixel] = mean_pixel
        result = Image.fromarray(demo_frame_color, 'RGB')
        result_name = 'frame-color.png'
        result.save(result_name)
        average_frame = cv2.imread(result_name)

        font = cv2.FONT_HERSHEY_PLAIN 
        org = (20, 100) 
        fontScale = 0.8
        color = (255, 255, 255) 
        thickness = 1
        average_frame = cv2.putText(average_frame, 'frame #' + str(frame_index) + ': (' + str(int(mean_pixel[0])) + ',' + str(int(mean_pixel[1])) + ',' + str(int(mean_pixel[2])) + ')', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.imshow('frame-color', average_frame)

        #timeline        
        demo_array[:,frame_index - 1] = mean_array[frame_index]
        demo_image = Image.fromarray(demo_array, 'RGB')
        demo_image_resized = demo_image.resize((image_height, image_width))
        result_name = 'timeline.png'
        demo_image_resized.save(result_name)
        timeline = cv2.imread(result_name)
        percentage = str(100 * frame_index / total_frames) + '%'
        font = cv2.FONT_HERSHEY_PLAIN 
        org = (int(image_height / 2)-100, int(image_width / 2)) 
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
mean_array = np.reshape(mean_array, (-1, 3))
width = mean_array.shape[0]
height = round(width/4)
data = np.zeros((height, width, 3), dtype=np.uint8)
for pixel in range(0, width):
    data[:,pixel] = mean_array[pixel]
result_image = Image.fromarray(data, 'RGB')
result_image = result_image.resize((image_height, image_width))
result_image.save('VID-ART.jpg')
result_image.show()

cap.release()
cv2.destroyAllWindows()

