import cv2
import os
import time

camera = cv2.VideoCapture(0)
slouch = True # True: take slouched photos, False: take non slouched photos
path = './data/slouched' if slouch else './data/not-slouched'


# create directories to store data
def create_dirs():
    if not os.path.isdir('./data/slouched'):
        os.makedirs('./data/slouched')
        print('directory for slouched created')

    if not os.path.isdir('./data/not-slouched'):
        os.mkdir('./data/not-slouched')
        print('directory for not-slouched created')


def countdown(count, curr):
    time.sleep(1)
    print(f'Taking picture {curr} in...')
    time.sleep(1)
    for i in range(count):
        print(f'{count - i}...')
        time.sleep(1)
    print('SMILE :)')

# capture images
def capture_images():
    MAX_IMAGES = 5 # number of images to be taken
    img_name = 0 # images will be named 0-n
    img_count = 0 # keep track of current image count
    delay = 3 # countdown delay in seconds
    while(img_count < MAX_IMAGES):
        countdown(delay, img_count)
        ret, img = camera.read() # capture current frame
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert img to grayscale
        cv2.imwrite(os.path.join(path, f'{img_name}.jpg'), gray_img) # save img to dir
        img_name += 1
        img_count += 1

    # close camera
    camera.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    create_dirs()
    capture_images()
