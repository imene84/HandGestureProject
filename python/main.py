import cv2
import mediapipe as mp
import time
import serial
arduino = serial.Serial('/dev/cu.usbmodem11201', 9600)
time.sleep(2)
def count_fingers(landmarks, handedness):

    fingers = 0

    if landmarks[8].y < landmarks[6].y:
        fingers += 1

    if landmarks[12].y < landmarks[10].y:
        fingers += 1

    if landmarks[16].y < landmarks[14].y:
        fingers += 1

    if landmarks[20].y < landmarks[18].y:
        fingers += 1

    if handedness == "Left":
        if landmarks[4].x < landmarks[3].x:
            fingers += 1
    else:
        if landmarks[4].x > landmarks[3].x:
            fingers += 1

    return fingers

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)

camera = cv2.VideoCapture(0)
start_time = time.monotonic()
previous_count = -1
stable_frames = 0
current_count = -1

with HandLandmarker.create_from_options(options) as landmarker:

    while True:
        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        timestamp = int((time.monotonic() - start_time) * 1000)

        result = landmarker.detect_for_video(mp_image, timestamp)

        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:

                hand_label = result.handedness[0][0].category_name

                fingers = count_fingers(hand_landmarks, hand_label)

                if fingers == previous_count:
                    stable_frames += 1
                else:
                    stable_frames = 1

                previous_count = fingers

                if stable_frames >= 5 and fingers != current_count:
                   current_count = fingers
                   print("Sending:", current_count)
                   arduino.write(f"{current_count}\n".encode())

                cv2.putText(
                     frame,
                     f"{hand_label} hand | Fingers: {current_count}",
                     (20, 50),
                     cv2.FONT_HERSHEY_SIMPLEX,
                     1,
                     (0, 255, 0),
                     2
                )
                for landmark in hand_landmarks:
                    height, width, _ = frame.shape
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)

                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        cv2.imshow("Hand Detection", frame)

        if cv2.waitKey(1) == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()