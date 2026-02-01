# Teacher Model Validation Results (NEU-DET)

## Experimental Setup
- Dataset: NEU-DET
- Input size: 640 × 640
- Evaluation mode: Validation only
- Metric: mAP@0.5 and mAP@0.5:0.95

---

## Quantitative Results

| Teacher Model | Parameters | GFLOPs | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| YOLOv8m | 25.8M | 78.7 | **0.743** | 0.398 |
| YOLOv8l | 43.6M | 164.8 | **0.743** | **0.402** |
| YOLOv8x | 68.1M | 257.4 | 0.732 | 0.379 |

---

## Discussion
- YOLOv8m and YOLOv8l achieve identical mAP50 scores.
- YOLOv8l achieves the highest mAP50-95 among all teacher models.
- YOLOv8x does not provide additional performance gains despite significantly higher computational cost.

Based on these results, **YOLOv8l is considered the most effective teacher candidate** for subsequent knowledge distillation experiments.

---

## Notes
- Teacher validation results are reported as reference upper bounds.
- These results are not logged to W&B by design, as they are used only for final comparison and decision making.
