# Bed Calibration PWA

## Overview
This project is a **Progressive Web App (PWA) with Flask** designed to assist in **the bed calibration of Flashforge Adventurer 3/4 Series 3d Printer**. The app allows users to **input Z-height measurements**, **detect outliers**, and **generate adjustment recommendations** for manual calibration. It also **visualizes the bed leveling data** with a heatmap to help users identify uneven spots.

The app is designed to be **offline-friendly**, meaning users can add it to their **Android home screen** and use it without needing an internet connection.

## Features
✅ **Enter 9-point Z-height calibration data** (used for manual bed leveling)
✅ **Detect outliers** based on standard deviation thresholds
✅ **Provide adjustment recommendations** (using 0.05, 0.1, or 0.5 mm increments, except for the center point which uses 0.02 mm increments)
✅ **Generate a heatmap** to visualize bed unevenness
✅ **Works offline as a PWA** (installed on Android or PC)
✅ **Mobile-friendly interface**

## Project Structure
```
📂 bed_calibration_pwa
 ├── 📂 static        # Contains CSS, JavaScript, and images
 │   ├── 📂 images
 │   ├── style.css    # Stylesheet
 │   ├── script.js    # JavaScript logic
 │   ├── service-worker.js  # Enables Offline Mode
 │   ├── manifest.json  # PWA Settings (name, icons, etc.)
 ├── 📂 templates     # HTML templates for the app
 │   ├── index.html   # Main UI
 ├── app.py          # Flask Backend (Runs Python)
 ├── requirements.txt # Python dependencies
 ├── README.md       # Project Guide
```

## Installation
### **1️⃣ Install Dependencies**
Ensure you have **Python 3+** installed, then install dependencies:
```sh
pip install flask numpy matplotlib seaborn
```

### **2️⃣ Run the Flask App**
```sh
python app.py
```

### **3️⃣ Access the App on Your Phone or PC**
- Open **Chrome or Edge**
- Go to **`http://127.0.0.1:5000/`**
- To install on **Android**, click **"Add to Home Screen"**

## How It Works
1. Enter **Z-height values** from your **3D printer's manual bed leveling process**.
2. Click **"Analyze"** to:
   - Detect **outliers** that are too high or too low.
   - Suggest **adjustments** based on the center point.
   - Generate a **heatmap** for visualization.
3. Follow the **recommended adjustments** to improve bed leveling.

## Goal
The goal of this project is to **make Flashforge Adventurer 3/4 Series 3d Printer easier** by providing a **simple, visual tool** for manual leveling. Many 3D printers lack built-in mesh leveling, and this tool helps users achieve a more level print surface manually.

## Current Status
This is still in preliminary stage. 2 python script were developped. 
- Bed_calibration.py create a web interface accessible over the local network from any device but has to run continuously on a pc or a server.
- calibration.py is a standalone app running only on the device on which it is loaded. In order to be truly functional, the PC would need to be located near the printer.

Will need to adapt the scripts to make them work on a phone as standalone apps. 

## Potential Future Improvements
🚀 **Save previous calibration results** for comparison
🚀 **Export calibration reports** as PDFs
🚀 **Support for multiple printer profiles**

## Contributing
If you’d like to contribute, feel free to fork this repository and submit pull requests!

## License
This project is licensed under the GNU GPL License.

---

### **💡 Need help?**
If you run into any issues, feel free to open an **issue on GitHub** or reach out. Happy printing! 🎉

