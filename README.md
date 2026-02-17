# Awais Cheema - CIO Programming Test: Rice Grain Counting
# My Solution 

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
```bash    
git clone https://github.com/dbe-cio/cio-Awais123-creator
cd cio-Awais123-creator
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
