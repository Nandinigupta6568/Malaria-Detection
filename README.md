# MalariaAI 

A simple tool that uses AI to check blood images for Malaria.

## What does it do?
Malaria is caused by a tiny parasite called **Plasmodium**. This AI looks at a picture of blood through a microscope and tells you if the parasite is there or not.

### How it helps:
* **Fast Results:** It gives a result in seconds.
* **Easy to Understand:** If it finds a parasite, the screen turns **RED**. If the blood is clean, the screen turns **GREEN**.


---

## 🔬 The Science (Simplified)
The parasite has a "life cycle." It starts in the liver and then moves to your **red blood cells**. This is called the **Blood Stage**.
* Our AI is trained to find the parasite in this specific stage.
* This is when people get sick with **high fever and shaking chills**.

---

## How to start the project

### 1. Get the files ready

Make sure you have all your files in one folder:
* `main.html` (The website part)
* `app.py` (The AI part)
* `malaria_model.h5` (The AI's brain)
* `requirements.txt` (The list of tools needed)


### 2. Install the tools
Open your computer's terminal (cmd) and type:
```bash
pip install -r requirements.txt
```
or install all the things given in requirements.txt


### 3. Run the AI
Type this in your terminal:
``` bash
python app.py
```


### 4. Open the website
Double-click main.html file to open it in Chrome. Upload an image and click Analyze!