# Object Recognition Project

## Project Overview
This project explores object recognition using a single base model trained under different conditions.
The goal was to perform object detection on three videos as thuroughly as possible.
The videos were construction themed and accent was set on safety.  

Multiple experimental versions were implemented to compare results and identify which version worked best.

---

## Problem Definition
**Input:** Videos  
**Output:** Videos where object class predictions with bounding boxes are shown  
**Task:** Detect and localize target objects in real-world scenes  

**Constraints:**
- Limited training time
- Limited dataset size
- Fixed base model architecture

**Success Criteria:**
- Stable detections
- Acceptable inference speed
- Reasonable generalization to unseen data

---

## Model & Approach
- **Base model:** YOLOv8
- **Reason for selection:** Good trade-off between speed and accuracy, suitable for real-time use
- The same model architecture was trained multiple times using different datasets and configurations

---

## Experiments
### Version 1 – Initial Attempt
**Goal:** Establish a working baseline  
**Description:**  
- Fine tuned the YOLOv8 trained on COCO dataset with the dataset that I found on construction theme
- Compared results to YOLOv8 trained only on the dataset
- Focused on achieving stable detections
- For better results I upscaled the third video because the CCTV footage had low quality which seemed to disturb good detection 


**Outcome:**  
- Reasonable performance on validation data  
- Poor generalization in some real-world scenarios  

---



## Results Summary
| Experiment | Training Time | Performance (Qualitative / Metrics) |
|----------|--------------|-------------------------------------|
| Version 1 | Already trained(came with dataset) | Moderate accuracy |
| Version 2 | ~1 hour     | Better accuracy |


## Observed Issues & Limitations
- Inconsistent detections in complex scenes
- Not very relevant detections in non-construction scenes
- Limited dataset diversity

---

## Analysis & Hypotheses
The main issues are believed to be caused by:
- Dataset bias and limited variability

These factors likely contributed more to performance limitations than the model architecture itself.

---

## Potential Improvements
If more time were available, the following steps would be prioritized:
- Additional data collection
- More extensive hyperparameter tuning
- Longer training with better validation monitoring

---

## Future Work / Next Steps
- Evaluate alternative model architectures
- Improve evaluation metrics and benchmarking

---

## Lessons Learned
- Dataset quality has a major impact on detection performance
- Iterative experimentation is critical
- Even incomplete experiments can provide valuable insights


