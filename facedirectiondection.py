import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
direction = ""
offset = 0  # arrow animation

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cx = x + w // 2
        cy = y + h // 2

        if prev_x != 0 and prev_y != 0:
            if cx > prev_x + 10:
                direction = "RIGHT"
            elif cx < prev_x - 10:
                direction = "LEFT"
            elif cy > prev_y + 10:
                direction = "DOWN"
            elif cy < prev_y - 10:
                direction = "UP"

        prev_x, prev_y = cx, cy

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 🔥 Animation offset update
    offset = (offset + 5) % 40

    # 📍 Base position (top-left)
    base_x, base_y = 20, 40

    # 🔤 Show direction text
    cv2.putText(frame, direction, (base_x, base_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 🎯 Draw animated arrow
    if direction == "RIGHT":
        cv2.arrowedLine(frame, (base_x + 120, base_y - 10),
                        (base_x + 120 + offset, base_y - 10),
                        (0, 255, 0), 3)

    elif direction == "LEFT":
        cv2.arrowedLine(frame, (base_x + 120, base_y - 10),
                        (base_x + 120 - offset, base_y - 10),
                        (0, 255, 0), 3)

    elif direction == "UP":
        cv2.arrowedLine(frame, (base_x + 120, base_y + 10),
                        (base_x + 120, base_y + 10 - offset),
                        (0, 255, 0), 3)

    elif direction == "DOWN":
        cv2.arrowedLine(frame, (base_x + 120, base_y - 10),
                        (base_x + 120, base_y - 10 + offset),
                        (0, 255, 0), 3)

    cv2.imshow("Face Direction + Arrow", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
