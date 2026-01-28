# cv_ndt_project

## Project Overview
- Topic: Industrial surface defect detection
- Dataset: NEU-DET
- Model: YOLOv8n (Baseline)
- Environment: Windows 11 + WSL2 (Ubuntu), Python, PyTorch

## Session 3 (Baseline)
- YOLOv8n baseline training (100 epochs)
- mAP50: 0.753
- mAP50-95: 0.395
- ONNX export completed
- ONNX inference verified (≈10.8 ms per image)
- Baseline artifacts fixed under `artifacts/baseline_v1/`

## Notes
- Baseline results are fixed and used as reference for all future experiments.
- Next step: Knowledge Distillation (YOLOv8m → YOLOv8n).
