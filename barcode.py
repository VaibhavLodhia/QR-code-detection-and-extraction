import cv2
import numpy as np
import datetime
from pyzbar.pyzbar import decode

data = '8904130855498'
detections = []
invalid = []
def read_barcodes(frame):
    barcodes =decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        cv2.putText(frame,barcode_info, (1950,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        #3
        # cv2.putText(frame,data, (1950,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        # print(type(barcode_info))
        if(barcode_info == data):
            
            
            print('')



        else:
            detections.append(3)
        # with open("barcode_result.txt", mode ='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
    return frame

    
def main():
    #1


    cap = cv2.VideoCapture('data3.mp4')


    img = cv2.imread('ri.jpg')
    logo = cv2.resize(img, (550,100))

    # Create a mask of logo
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  

    ret, frame = cap.read()
    frametime = 1
    #2
    while ret:
        ret, frame = cap.read()
        frame = read_barcodes(frame)

        black_area = np.zeros([1080, 700, 3], dtype=np.uint8)
        black_area.fill(175)
        frame = np.concatenate((frame, black_area), axis=1)
        frame[0:logo.shape[0], frame.shape[1] - logo.shape[1] -100 :frame.shape[1]-100] = logo
        
        time = datetime.datetime.now().strftime("%H:%M:%S")   
        cv2.putText(frame,"Current Status:", (1950,150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame,"Date:"+" "+"Jun 29", (1950,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Time:"+" "+str(time), (1950,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Area:"+" "+"Sticer Pasting Activity", (1950,220), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"----------------------------------------------------", (1950,235), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
        cv2.putText(frame,"Activity Analytics:", (1950,250), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame,"----------------------------------------------------", (1950,300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
        
        

        for i in range(len(detections)):
            if detections !=[]:
                
                op=detections[0]
                # print(detections[i])
                # i+=1
    
                
            #     cv2.putText(frame,op, (1950,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            # if detections[i] == 3:

            #     cv2.putText(frame,op, (1950,290), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            #     i+=1

         
        frame1 =cv2.resize(frame,(1500,680))
        cv2.imshow('Barcode/QR code reader', frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #3
    cap.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()