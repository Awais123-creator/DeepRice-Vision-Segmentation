# DeepRice-Vision: Automated Grain Segmentation & Counting
**Developed by Awais Cheema** 
This repository features an end-to-end Computer Vision pipeline designed to detect, segment, and uniquely label individual objects (rice grains) in high-noise environments. It utilizes advanced morphological processing and the Watershed algorithm to resolve complex clusters of overlapping grains.

---

## Key Technical Features
* **Adaptive Semantic Masking:** Leverages **Otsu’s Thresholding** and Gaussian filtering to eliminate sensor noise and isolate the foreground with high precision.
* **Instance Segmentation (Watershed):** Implements a **Euclidean Distance Transform** to identify the "centroid" of each grain. This allows the model to separate touching objects that traditional edge-detection methods fail to resolve.
* **Morphological Optimization:** Uses **Mathematical Morphology** (Binary Closing and Small Object Removal) to refine grain boundaries and ensure structural integrity.
* **HSV Color Mapping:** A custom algorithm that assigns a unique, high-contrast hue to every identified instance, ensuring 100% distinct visualization for all detected grains.

---

## Results
* **Final Grain Count:** 70 rice grains
* **Visual Output:** Each grain is uniquely color-mapped to verify segmentation accuracy.

![Final Result](figrice_coloured.png)

---

1) **What I did**
- I loaded the file 'figs/rice.png'
- Then I turned it into a grayscale and blurred it slightly, so that tiny specks could be removed
- I built a clean black/white mask: Keeps grains, removes dust, fills tiny holes, closes small gaps 
- Find one center (seed) per each grain and then I used watershed to split touching grains
- I gave each grain a unique color (evenly spaced hues) and saved the result as figs/rice_coloured.png
- **Final Grain Count:70 rice grains**
- **Completeness note: I tuned parameters to avoid over splitting and to keep small true grains. The result looks complete for this image, but there maybe a few edge cases where tiny touching grains could be missed. the settings are easy to adjust**
---
  

## 2) How to run the code from GitHub
### Get the code and open the folder
### 1. Clone the Repository
```bash    
git clone [https://github.com/Awais123-creator/DeepRice-Vision-Segmentation](https://github.com/Awais123-creator/DeepRice-Vision-Segmentation)
cd DeepRice-Vision-Segmentation
```
You should see:
- README.md
- awais code task.ipynb
- count_and_colour_rice.py (to directly run it on python)
- requirements.txt
- figs/rice.png

# Instructions to create and activate conda environment
```bash
conda create -n awais-code-task python=3.10 -y
conda activate awais-code-task
```

# Instructions for installing all dependencies (make all the imports in Cell 1)
- Option A: 'requirements.txt' is in the repo, then use 
```bash
pip install -r requirements.txt
```
- Option B :
```bash
pip install numpy scipy scikit-image opencv-python-headless matplotlib
```

# Run the notebook
```bash 
jupyter lab
```

- Open the notebook in jupyter lab
- Select awais-code-task kernel
- Run all the cells from top to bottom (chronological order)
- Output is saved to : figs/rice_coloured.png
- The final line prints: final grains counted:70

**To run as a script**
```bash
python count_and_colour_rice.py
```

# Reproducibility
I used:
- python 3.10
- numpy
- scipy
- scikit-image
- opencv-python-headless
- matplotlib

- A **requirements.txt** has been provided so you can install everything with:
```bash
pip install -r requirements.txt
```

  
---

If you paste that in, you fully satisfy Step 2 (unique colour per grain + saved output + final number + completeness note) and Step 3 (clear set up, env creation), dependency install, run instructions.
