# ***WinkWatch-with-Wazowski***


## Introduction

WinkWatch with Wazowski is a delightful UI and **Qt application** that leverages real EEG, we delve into the world of signal processing to refine raw data, removing noise and enhancing its quality. With machine learning models at its core, the application seamlessly classifies the user's ongoing EEG signals to determine if the user's eye state is open or closed. 

Inspired by Mike Wazowski from Monsters Inc., this project combines cutting-edge technology with a touch of whimsy. With a user-friendly interface, it provides real-time feedback on eye states, opening up exciting possibilities for interactive applications. Join us in exploring the fascinating world of brain-computer interfaces with a touch of Pixar magic!

## About

In the dynamic landscape of medical challenges, our project introduces a novel approach: **EEG-based Eye State Detection**. Imagine a system that can instantaneously classify whether a patient's eyes are open or closed by analyzing their brain's electrical activity. That's precisely what WinkWatch with Wazowski does!

## Why EEG?

Electroencephalography (EEG) has long been a hero in neuroscience. Traditionally used for epilepsy studies, we're flipping the script by integrating EEG technology to monitor ocular activity. This paradigm shift opens doors to real-time insights, particularly valuable for ensuring optimal sedation levels during critical medical interventions.

## How It Works

1. **Data Collection:** Using a top-notch EEG setup, we recorded brain activity from willing participants, capturing both eyes-open and eyes-closed conditions.

2. **Data Description:**
    - **Format:** EEG data is stored in .mat files.
    - **Structure:** Each file is a 2D matrix, with rows representing observations at each time sample. Columns 2 to 17 contain recordings from 16 EEG electrodes, while the first column represents timestamps. Columns 18 and 19 hold triggers indicating experimental conditions.

3. **Data Magic:** Our team worked its magic on the EEG data. We filtered it to isolate the intriguing alpha wave activity (8-12 Hz), denoised it with Independent Component Analysis (ICA), and then resampled for consistency.

4. **Feature Extravaganza:** We dived into Power Spectral Density, extracting features like frequency bands' power intensities and statistical measures. Think of it as capturing the unique fingerprints of brain activity.

5. **Model Mastery:** Armed with these features, we trained three powerful models – Support Vector Machine (SVM), Random Forest, and XGBoost. Each aimed to be the brainiac in distinguishing between eyes open and closed states.


## Contributors

Gratitude goes out to all team members for their valuable contributions to this project.

<div align="left">
  <a href="https://github.com/joyou159">
    <img src="https://github.com/joyou159.png" width="100px" alt="@joyou159">
  </a>
  <a href="https://github.com/hagersamir">
    <img src="https://github.com/hagersamir.png" width="100px" alt="@hagersamir">
  </a>
  <a href="https://github.com/MohamedSayedDiab">
    <img src="https://github.com/MohamedSayedDiab.png" width="100px" alt="@MohamedSayedDiab">
  </a>
  <a href="https://github.com/Medo072">
    <img src="https://github.com/Medo072.png" width="100px" alt="@Medo072">
  </a>
 
  <a href="https://github.com/raghdaneiazyy6">
    <img src="https://github.com/raghdaneiazyy6.png" width="100px" alt="@raghdaneiazy6">
  </a>
</div>

## Acknowledgments

**This project was supervised by Dr. Sherif H. Elgohary & Eng. Amira Omar, who provided invaluable guidance and expertise throughout its development as a part of the Medical Instrumentation course at Cairo University Faculty of Engineering.**

<div style="text-align: right">
    <img src="https://imgur.com/Wk4nR0m.png" alt="Cairo University Logo" width="100" style="border-radius: 50%;"/>
</div>


---
Step into a world where advanced tech meets playful creativity. Join us in the WinkWatch with Wazowski project and let's explore the exciting realm of EEG-based applications!

