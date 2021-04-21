
import os
import cv2
import numpy as np

## If edited file_list_txt in GatheringPath.py, then you need to edit in below
file_list_txt = "filePath.txt"

def check_path(path_list):
    a_list = []
    for member in path_list:
        if os.path.isfile(member):
            a_list.append(member)
    return a_list

def print_list(a_list):
    for member in a_list:
        print(member)

def path_to_filename(a_list):
    currentPath = os.path.abspath(__file__)
    b_list = []
    for member in a_list:
        if os.path.isfile(member):
            relPath = os.path.relpath(member , currentPath)
            relPath = relPath.replace('..\\','.\\')
            img_path = relPath[:-4]
            if not os.path.isdir(img_path):
                os.makedirs(img_path)
            b_list.append(os.path.join(img_path,relPath.replace('.\\','').replace('\\','_').replace('.','_')))
    
    return b_list

def Video(openpath, savepath = None):
    frame_number = 0
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    
    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            cv2.imwrite("{}_{}.png".format(savepath, str(frame_number)), frame)
            # Display the resulting frame
            cv2.imshow("Input", frame)
            frame_number += 1
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return


    
def main():
    file_path = np.loadtxt(file_list_txt, str, delimiter='\t')
    file_path = check_path(file_path)
    print_list(file_path)
    main_name_list = path_to_filename(file_path)
    print_list(main_name_list)
    for i in range(len(main_name_list)):
        Video(file_path[i], main_name_list[i])

if __name__=="__main__":
    main()
