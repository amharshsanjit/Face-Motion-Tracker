# Face-Motion-Tracker
Real-time face movement detection system using OpenCV that tracks direction (left, right, up, down) and visualizes it with animated arrows.
# 🎯 Face Direction Detection with Animated Arrow

A real-time computer vision project using **OpenCV** that detects face movement direction (LEFT, RIGHT, UP, DOWN) and displays an animated arrow accordingly.

---

## 🚀 Features

- 📸 Real-time webcam face detection  
- 🧠 Movement tracking using face center points  
- 🔄 Direction detection (Left, Right, Up, Down)  
- 🎯 Animated arrow visualization  
- ⚡ Lightweight and fast execution  

---

## 🛠️ Tech Stack

- Python 🐍  
- OpenCV 👁️  

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/face-direction-tracker.git
cd face-direction-tracker
```

2. Install dependencies:

```bash
pip install opencv-python
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

- Your webcam will open 📷  
- Move your face in different directions  
- Direction + animated arrow will be displayed  

Press **`q`** to exit.

---

## 🧠 How It Works

1. Uses Haar Cascade for face detection  
2. Calculates center point of detected face  
3. Compares current position with previous frame  
4. Determines movement direction  
5. Displays animated arrow based on direction  

---

## 📸 Output Preview

```
![ face_dection_output ]
Direction: RIGHT ➡️
(Arrow animating in real-time)
```

---

## ⚙️ Future Improvements

- 🖐️ Add hand gesture support  
- 🤖 Use MediaPipe for better accuracy  
- 🎮 Integrate with games (face-controlled input)  
- 📊 Add movement sensitivity controls  


---

## 💡 Author

**Harsh Sanjit**  
AI & ML Enthusiast 🚀  
