from os import name
import cv2
import numpy as np
import datetime
from pyzbar.pyzbar import decode


data = '8904130855498'
data2 = '8906126352479'
name1 = "Red headphones"
name2 = "Black Headphones"
detections = []
# invalid = []

def forever(start=0):
    count = start
    while True:
        yield count
        count += 1

def read_barcodes(frame):

    barcodes =decode(frame)

    for barcode in barcodes:
        x, y , w, h = barcode.rect
        
        # print(count)
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        # count = 1
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        
        
            
        if(barcode_info == data):
            # print (count)
            detections.append(barcode_info)

            cv2.putText(frame,"                "+name1, (1950,490), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            cv2.putText(frame,"                    "+barcode_info, (1950,310), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            cv2.putText(frame,"                      "+"Valid ", (1950,340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            # for i in barcode_info:
            #     with open(f"barcode_result{i}.txt", mode ='w') as file:
            #         file.write("Recognized Barcode:" + barcode_info)

        elif(barcode_info==data2):
            detections.append(barcode_info)
            cv2.putText(frame,"                "+name2, (1950,490), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            cv2.putText(frame,"                    "+barcode_info, (1950,310), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            cv2.putText(frame,"                      "+"Valid ", (1950,340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)

        if(barcode_info!=data and barcode_info!=data2):
            cv2.putText(frame,"                    "+barcode_info, (1950,310), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            cv2.putText(frame,"                      "+"Invalid ", (1950,340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            # new_ele = detections[0]
            # print(new_ele)
        # with open("barcode_result.txt", mode ='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
    return frame

    
def main():
    #1


    cap = cv2.VideoCapture('data4.wmv')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('slow_motion.mp4', fourcc, 20, (1450,680))

    img = cv2.imread('ri.jpg')
    logo = cv2.resize(img, (550,100))

    # Create a mask of logo
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  

    ret, frame = cap.read()
    #2
    while ret:
        ret, frame = cap.read()



        black_area = np.zeros([1080, 700, 3], dtype=np.uint8)
        black_area.fill(175)
        frame = np.concatenate((frame, black_area), axis=1)
        frame[0:logo.shape[0], frame.shape[1] - logo.shape[1] -100 :frame.shape[1]-100] = logo
        frame = read_barcodes(frame)
        time = datetime.datetime.now().strftime("%H:%M:%S")   
        cv2.putText(frame,"Current Status:", (1950,150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame,"Date:"+" "+"Jun 29", (1950,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Time:"+" "+str(time), (1950,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Area:"+" "+"Sticer Pasting Activity", (1950,220), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"----------------------------------------------------", (1950,245), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
        cv2.putText(frame,"Activity Analytics:", (1950,270), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame,"----------------------------------------------------", (1950,430), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
        cv2.putText(frame,"Boxes Passed:", (1950,370), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Boxes Remaining:", (1950,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Bar/QR code Data:", (1950,310), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Box Validation:", (1950,340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        
        cv2.putText(frame,"Box Details:", (1950,460), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame,"Product Name:", (1950,490), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Client Name: XYZ Electronics", (1950,520), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
        cv2.putText(frame,"Production no : A45786", (1950,550), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)


        
        

        for i in range(len(detections)):
            if detections !=[]:
                
                box = len(set(detections))
                remaining = 5-box
                cv2.putText(frame,"                      "+str(box), (1950,370), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                cv2.putText(frame,"                      "+str(remaining), (1950,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2) 
                # invalid.append(set(detections))
                

                # print(detections[i])
                # i+=1
    
                
            #     cv2.putText(frame,op, (1950,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            # if detections[i] == 3:

            #     cv2.putText(frame,op, (1950,290), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            #     i+=1

         
        frame1 =cv2.resize(frame,(1450,680))
        # scale_percent = 60  # percent of original size
        # width = int(frame.shape[1] * scale_percent / 100)
        # height = int(frame.shape[0] * scale_percent / 100)
        # dim = (width, height)
        # frame1= cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        cv2.imshow('Barcode/QR code reader', frame1)
        # out.write(frame1)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    cap.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()