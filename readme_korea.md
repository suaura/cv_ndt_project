## 프로젝트 개요 (Korean)

### 프로젝트 주제
- 산업 표면 결함 검출(Industrial Surface Defect Detection)

### 사용 데이터셋
- NEU-DET (철강 표면 결함 데이터셋)

### 사용 모델
- YOLOv8n (Baseline 모델)

### 개발 환경
- Windows 11 + WSL2 (Ubuntu)
- Python / PyTorch
- GPU: NVIDIA RTX 5080

---

## Session 3: Baseline 학습 요약

- YOLOv8n 모델을 사용한 Baseline 학습 수행 (100 epochs)
- 성능 지표:
  - mAP@0.5: **0.753**
  - mAP@0.5:0.95: **0.395**
- 학습 완료 후 ONNX 포맷으로 모델 변환
- ONNX Runtime 기반 추론 검증 완료
  - 추론 속도: 약 **10.8 ms / image**
- Baseline 관련 산출물은 `artifacts/baseline_v1/`에 고정 저장

---

## 참고 사항

- 본 Baseline 결과는 이후 모든 실험(Knowledge Distillation, Pruning, INT8 Quantization)의 기준선으로 사용됨
- 이후 단계에서는 YOLOv8m을 Teacher로 사용하는 지식 증류를 수행할 예정
