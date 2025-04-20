#pip install matplotlib

import matplotlib.pyplot as plt
import os
import re

# Read lines from the file
with open("variants.txt", "r", encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

# Output folder
os.makedirs("latex_images", exist_ok=True)

question_number = 0
current_steps = []

for line in lines:
    if re.match(r'^\d+\.', line):  # This is a new question
        # Save previous steps if any
        if current_steps:
            fig, ax = plt.subplots(figsize=(14, 2 + 0.5 * len(current_steps)))
            ax.axis('off')
            ax.text(0.01, 0.5, '\n'.join(current_steps), fontsize=18, va='center', wrap=True)
            plt.savefig(f"latex_images/Q{question_number}_steps.png", dpi=150, bbox_inches='tight', pad_inches=0.3)
            plt.close()
            current_steps = []

        # Start new question
        question_number = int(line.split('.')[0])
        question_text = line

        # Render question image
        fig, ax = plt.subplots(figsize=(14, 2))
        ax.axis('off')
        ax.text(0.01, 0.5, question_text, fontsize=18, va='center', wrap=True)
        plt.savefig(f"latex_images/Q{question_number}.png", dpi=150, bbox_inches='tight', pad_inches=0.3)
        plt.close()

    elif line.startswith('='):
        current_steps.append(line)

# Save the final steps
if current_steps:
    fig, ax = plt.subplots(figsize=(14, 2 + 0.5 * len(current_steps)))
    ax.axis('off')
    ax.text(0.01, 0.5, '\n'.join(current_steps), fontsize=18, va='center', wrap=True)
    plt.savefig(f"latex_images/Q{question_number}_steps.png", dpi=150, bbox_inches='tight', pad_inches=0.3)
    plt.close()

print("✅ All question and step images have been successfully generated.")
