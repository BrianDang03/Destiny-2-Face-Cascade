# Destiny 2 Face Detection with OpenCV Haar Cascade 

Created a Haar Cascade to detect my Destiny 2 charater's face.

## Table of Contents
<details>
  <summary>Click Me!</summary>
  
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Acknowledgments](#acknowledgments)

</details>

---

## Overview
This project aims to detect the face of my Destiny 2 character in video frames, allowing me to explore the capabilities of OpenCV in a fun and engaging way. I created a custom Haar Cascade for face detection, using a third-party application to generate the cascade model. For training, I provided both positive and negative samples, automating data preparation by converting all sample images to grayscale and resizing the positive samples to improve accuracy during training. The custom Haar Cascade scans each video frame to identify the character's face.     
![image](https://github.com/user-attachments/assets/2ce41da6-8c15-4264-836b-3a627c2fe187)
![Screenshot 2024-11-08 120939](https://github.com/user-attachments/assets/4e13d20f-8c9a-41da-8eaf-7c111f6d0289)

---

## Installation
1. Create a new directory or folder.
2. Use Github Desktop or git clone to pull the repository to the new directory or folder.
```
git clone https://github.com/BrianDang03/Destiny-2-Face-Cascade.git
```
3. Use the terminal and change to the Destiny-2-Face-Cascade directory. 
```
cd Destiny-2-Face-Cascade
```  
4. Use and activate venv or local machine to pip install dependencies.
```
pip install -r requirements.txt
```

## Usage

1. After successfully installing dependencies, change to the src directory.
```
cd Destiny-2-Face-Cascade/src
```

2.  Run the main.py file.
```
python main.py
```

---

## Scripts
1. main.py: Driver of the program.
2. grayscale_converter.py: Converts all negative and postive samples under the assets/negative_sample and assets/positive_sample folder into grey scale images.
3. resize_images.py: Converts all positive grey scaled images under the destiny_face_cascade/p folder to desired size.
    
---

## Acknowledgments

