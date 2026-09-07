# 🛡️ AI-Based Proctoring System

An AI-powered online examination proctoring system designed to monitor candidates during exams, detect suspicious activities, and improve the security and integrity of online assessments.

## 📌 Overview

The **AI-Based Proctoring System** uses computer vision and real-time monitoring to automatically supervise online examinations.

The system analyzes the candidate's webcam feed and detects activities such as:

* 👤 Face detection and monitoring
* 📱 Suspicious object detection
* 👀 Multiple-person detection
* 🚨 Unusual or suspicious activities
* 🔔 Real-time alerts and notifications

This reduces the need for continuous human supervision and provides a more secure online examination environment.

## ✨ Features

* **Face Detection** – Detects and monitors the candidate's face during the examination.
* **Multiple Face Detection** – Identifies the presence of additional people.
* **Object Detection** – Detects potentially prohibited objects such as mobile phones.
* **Real-Time Monitoring** – Processes webcam video continuously.
* **Suspicious Activity Detection** – Identifies predefined suspicious behaviors.
* **Real-Time Alerts** – Sends alerts when suspicious activity is detected.
* **WebSocket Communication** – Enables real-time communication between the client and server.
* **Automated Proctoring** – Minimizes the need for manual supervision.

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     Candidate       │
                    │      Webcam         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    React Frontend   │
                    │  Exam + Live Video  │
                    └──────────┬──────────┘
                               │
                         WebSocket
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Node.js / Express  │
                    │       Backend       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Proctoring     │
                    │       Engine        │
                    │ Python + OpenCV     │
                    │       + YOLO        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Suspicious Activity │
                    │ Detection & Alerts  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      MongoDB        │
                    │   Logs & Records    │
                    └─────────────────────┘
```

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* React.js

### Backend

* Node.js
* Express.js
* WebSockets

### AI / Computer Vision

* Python
* OpenCV
* YOLO
* TensorFlow / PyTorch

### Database

* MongoDB

## 📂 Project Structure

```text
AI-Proctoring-System/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── assets/
│   └── App.js
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── server.js
│   └── websocket/
│
├── ai-engine/
│   ├── face_detection/
│   ├── object_detection/
│   ├── proctor.py
│   └── models/
│
├── database/
│   └── models/
│
├── requirements.txt
├── package.json
└── README.md
```

## ⚙️ How It Works

1. The candidate logs into the online examination system.
2. The system requests access to the candidate's webcam.
3. The webcam continuously captures video frames.
4. OpenCV processes the video stream.
5. The AI models detect faces and objects.
6. Suspicious activities are identified based on predefined rules.
7. Alerts are generated when suspicious behavior is detected.
8. Monitoring information and relevant logs are stored in the database.

## 🚨 Example Suspicious Activities

| Activity                     | Detection     |
| ---------------------------- | ------------- |
| No face detected             | ⚠️ Alert      |
| Multiple faces               | 🚨 High Alert |
| Mobile phone detected        | 🚨 High Alert |
| Candidate leaves camera view | ⚠️ Alert      |
| Unauthorized object detected | ⚠️ Alert      |

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Proctoring-System.git
cd AI-Proctoring-System
```

### 2. Install Backend Dependencies

```bash
cd backend
npm install
```

### 3. Install AI Dependencies

```bash
cd ../ai-engine
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
PORT=5000
MONGODB_URI=your_mongodb_connection_string
```

### 5. Start the Backend

```bash
npm start
```

### 6. Start the Frontend

```bash
cd frontend
npm install
npm start
```

## 🎯 Use Cases

* Online examinations
* College/university assessments
* Recruitment tests
* Certification examinations
* Remote assessments
* Competitive examinations

## 🔮 Future Enhancements

* Voice activity detection
* Eye and gaze tracking
* Head-pose estimation
* Browser/tab-switch detection
* Audio monitoring
* AI-generated examination reports
* Advanced behavioral analysis
* Cloud-based deployment
* Admin dashboard with real-time analytics

## 🔐 Privacy & Security

The system should process candidate data responsibly. Webcam and examination data should only be collected with appropriate consent and should be protected using suitable security and data-retention practices.

## 📊 Benefits

* Reduces manual proctoring effort
* Enables real-time monitoring
* Improves examination security
* Detects suspicious activities automatically
* Supports scalable online examinations

## 👨‍💻 Author

**Varun Suthar**

B.Tech Computer Science Engineering | 2026

---

⭐ If you find this project useful, consider giving the repository a star!
