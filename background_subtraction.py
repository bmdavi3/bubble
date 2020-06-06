import cv2
import numpy as np
import psycopg2
import simpleaudio

drip = simpleaudio.WaveObject.from_wave_file("drip.wav")

frames_to_track = 200
non_zeros = [0 for x in range(frames_to_track)]
frame_num = 0
hit_most_of_high_water_mark = False
jug_id = 1

conn = psycopg2.connect('')
conn.autocommit=True
cursor = conn.cursor()


def high_water(values):
    return max(values)


# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('example.avi')

# fgbg = cv2.createBackgroundSubtractorKNN(10, 5000, False)
fgbg = cv2.createBackgroundSubtractorMOG2(50, 500, False)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    index = frame_num % frames_to_track
    non_zeros[index] = cv2.countNonZero(fgmask)

    high_water_mark = high_water(non_zeros)

    bubble_text = ''

    if hit_most_of_high_water_mark == False:
        if non_zeros[index] / float(high_water_mark) >= 0.666:
            hit_most_of_high_water_mark = True
            bubble_text = ' BUBBLE!!!!! '
            drip.play()
            cursor.execute("INSERT INTO bubble (jug_id) VALUES (%s)", (jug_id,))
    else:
        if non_zeros[index] == 0:
            hit_most_of_high_water_mark = False

    print("frame: {0} non_zeros: {1} high water mark: {2}{3}".format(str(frame_num).rjust(4), str(non_zeros[index]).rjust(4), str(high_water_mark).rjust(4), bubble_text))


    # Highest number of last X frames

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(33) & 0xff
    if k == 27:
        break

    frame_num += 1








cap.release()
cv2.destroyAllWindows()
