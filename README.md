
# 📐 LaTeXTestBench – Automated Math Model Testing with LaTeX

LaTeXTestBench is a two-part automation pipeline built to **test AI/ML math solvers** like [Mr. Math](https://metamersive-math-dse.vercel.app/) by:

1. Converting LaTeX questions and solution steps into images.
2. Uploading each image to the solver and capturing a screenshot of the returned solution.

This setup is designed for **stress testing**, **benchmarking**, and **evaluating math model accuracy** at scale.

---

## 🚀 Features

- 📄 Convert `.txt` LaTeX-based questions to PNG images using `matplotlib`
- 🤖 Automate solver interaction using `selenium` and Chrome
- 🔁 Repeat uploads (default: 9 times/question) to assess consistency
- 📸 Auto-save screenshots of each solution response
- 🗂️ Organized folder structure by question and attempt

---

## 📁 Directory Structure

```
LaTeXTestBench/
├── latex_images/           # Auto-generated question & step images (Q1.png, Q1_steps.png, etc.)
├── screenshots/            # Solution screenshots organized by question
│   └── Q1/
│       ├── Q1.1_solution.png
│       ├── Q1.2_solution.png
│       └── ...
├── variantswithdollarsign.txt  # Input LaTeX questions and steps
├── latexToImg.py           # Script 1: Converts LaTeX text to images
├── testSolverBot.py        # Script 2: Uploads images & captures solver output
└── README.md               # You're here!
```

---

## 🔧 Setup

### 1. Install Requirements

```bash
pip install matplotlib selenium
```

Also, ensure you have [Google Chrome](https://www.google.com/chrome/) installed and compatible [ChromeDriver](https://chromedriver.chromium.org/downloads) available in your `PATH`.

---

## 📝 Input Format (variants.txt)

Each question and its steps must be formatted like:

```text
1. Simplify $\frac{a^{3} a^{7}}{b^{-5}}$ and express your answer with positive indices.
= $\frac{a^{10}}{b^{-5}}$
= $a^{10} b^{5}$
```

---

## 📌 Script 1: Convert LaTeX to Images

### `latexToImg.py`

This script:
- Parses the `.txt` file.
- Generates:
  - `Q1.png` for question.
  - `Q1_steps.png` for steps.

📤 **Input:** `variants.txt`  
📥 **Output:** images in `latex_images/`

---

## 🤖 Script 2: Upload & Screenshot Solver Responses

### `testSolverBot.py`

This script:
- Uploads question images to Mr. Math (https://metamersive-math-dse.vercel.app/)
- Waits for console message `"Solution Response"`
- Takes a screenshot and saves it.

🔁 Each image is uploaded **9 times by default** for robustness testing.

🧠 **Target URL is customizable** in the script.

---

## ✅ Example

**Input Question Image:** `Q1.png`  
**Input Steps Image:** `Q1_steps.png`  
**Captured Solution Screenshot:** `Q1.1_solution.png`
---
## Output:

### Q1.png
![Q1](https://github.com/user-attachments/assets/956a7eaa-e02e-4a79-97d1-8f877f87fabf)

### Q1_steps.png
![Q1_steps](https://github.com/user-attachments/assets/7ab8de52-a9b0-4993-a0bd-b0731e8b298c)

### Q1.1_solution.png
![Q1 1_solution](https://github.com/user-attachments/assets/28ae5592-eae6-436c-a188-205e0184f7a4)



## 🛠️ Future Ideas

- Add image comparison (OCR or pixel-based) to auto-grade solutions
- Generate detailed success/failure reports
- Integrate with other math solvers (Symbolab, Wolfram Alpha, etc.)
- Save solution text (via `driver.find_element`) for deeper analysis

---

## 💡 Inspiration

Built for testing [Mr. Math](https://metamersive-math-dse.vercel.app/), but can be extended to **any UI-based math solver** that accepts image uploads.

---

## 📬 Contribute

Want to add error-checking, visual difference detection, or analytics? Pull requests are welcome!
