# NeuralBee – A Beehive Health Monitoring System 🐝

NeuralBee is an AI-powered beehive health monitoring system that leverages **computer vision** and **audio analysis** to detect **Varroa mite infestations** and assess the overall health of beehives. The solution provides an intuitive **Flask web application** that allows users to upload images and audio files for real-time hive diagnostics.

---

## 🚀 Features

- **Varroa Mite Detection** using YOLO-based object detection models.
- **Beehive Audio Analysis** to classify hive strength ("StrongHive" or "WeakHive").
- **User-Friendly Web Interface** built with Flask.
- **Real-time Inference** for both image and audio inputs.
- **Docker Support** for seamless deployment.

---

## 📖 Abstract

Bees are essential as they are responsible for pollinating one-third of the world’s food. Without them, global ecosystems and food supplies would face significant challenges. NeuralBee proposes a system that:

- Detects **Varroa mite infestation** using computer vision models like YOLOv5, YOLOv7, YOLOv8, and SSD.
- Classifies beehive audio using **Mel spectrograms** and **MFCCs** to distinguish between strong and weak hives.

**Key Results:**
- 🐝 Varroa Mite Detection Precision: **0.962**  
- 🎧 Audio Classification Accuracy: **0.998**  

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

git clone https://github.com/deepmehta27/NeuralBee.git
cd NeuralBee


### 2️⃣ Create and Activate a Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

### 3️⃣ Install Dependencies

- pip install -r requirements.txt

### 4️⃣ Run the Application

- python webapp.py --port=5000


### 5️⃣ Access the Web App

Open your browser and navigate to:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 🐝 Usage

### 🌸 Varroa Mite Detection

1. Upload an image of bees on the homepage.  
2. The YOLO model detects Varroa mites and displays an annotated image with bounding boxes.  
3. Check the **Varroa Report** page to view previously processed images.  

### 🎧 Beehive Audio Classification

1. Navigate to the **Audio Analysis** page.  
2. Upload a hive audio recording (`.wav` or `.mp3`).  
3. The model predicts the hive state: **StrongHive** or **WeakHive**.

---

## 🧪 Methodology

### 📷 Varroa Mite Detection

- Models evaluated: YOLOv5, YOLOv7, YOLOv8, SSD.  
- Dataset: 10,000+ images of healthy and Varroa-infested bees.  
- Achieved **0.962** precision using the optimized model (`best1.pt`).  

### 🎶 Beehive Audio Analysis

- Features: **Mel spectrograms** and **MFCCs** extracted with `librosa`.  
- Dataset: Over 2 hours of recordings from both strong and weak hives.  
- Model: Deep neural network trained using TensorFlow/Keras.  
- Achieved **0.998** accuracy with the final model (`model.h5`).  

---

## 🧷 Docker Deployment

To run the application in a Docker container:

1. **Build the Docker image:**

   ```bash
   docker build -t neuralbee .
   ```

2. **Run the container:**

   ```bash
   docker run -p 5000:5000 neuralbee
   ```

3. **Access the app** at: [http://localhost:5000](http://localhost:5000)  

---

## 📝 Experimental Results

| Task                      | Metric    | Value  |
|---------------------------|-----------|--------|
| Varroa Mite Detection     | Precision | 0.962  |
| Beehive Audio Classification | Accuracy | 0.998  |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repo 🍴  
2. Create a new branch: `git checkout -b feature/your-feature` 🌱  
3. Commit your changes: `git commit -m "Add your feature"` 💬  
4. Push to the branch: `git push origin feature/your-feature` 🚀  
5. Submit a pull request 📩  

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 📫 Contact

- **Author:** Deep Mehta  
- **GitHub:** [@YourUsername](https://github.com/deepmehta27)  

---

## 🌻 Acknowledgments

- YOLO models from [Ultralytics](https://github.com/ultralytics/yolov5)  
- Audio processing with [librosa](https://librosa.org/)  
- Inspiration from the global beekeeping community 🐝💛  

---

*Help protect our pollinators!* 🌎🐝🌼  
