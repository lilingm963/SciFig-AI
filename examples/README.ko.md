# 세 가지 예제 따라 하기

[English](README.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

입력은 학습용 합성 예제로 실험적 근거가 아닙니다. 튜토리얼 미리보기는 별도의 제품 작업 흐름을 보여 주며 이 예제 입력으로 생성한 결과가 아닙니다.

## 개념적인 시료 준비 · Illustration

### 입력

‘시료 채취’, ‘시료 준비’, ‘시료 관찰’의 라벨이 있는 세 패널로 개념 일러스트를 만드세요. 흰 배경, 청록색 계열, 왼쪽에서 오른쪽으로 명확한 화살표를 사용하세요. 장비, 수치, 생물학적 기전을 임의로 추가하지 말고 ‘개념적인 학습용 예제’라고 표시하세요.

### 단계 및 확인 사항

Illustration에서 프롬프트를 사용하세요. 라벨과 화살표 방향을 확인하고 튜토리얼의 편집 도구 하나를 시도하세요. 이 예제는 실제 실험 절차를 제시하지 않습니다.

[전체 작업 흐름 보기](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-illustration-tutorial.mp4)

## 합성 시계열 측정 데이터 · DataChart

### 입력

[synthetic-timeseries.csv](datachart/synthetic-timeseries.csv)

### 단계 및 확인 사항

DataChart에 CSV를 올리고 time_min에 대한 signal_a와 signal_b를 두 계열로 그립니다. 세로축에 ‘임의 단위’를 표시하고 각 점을 CSV와 대조하세요. 범례를 확인한 뒤 제공되는 옵션으로 내보내세요.

[전체 작업 흐름 보기](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-datachart-tutorial.mp4)

## 학습용 데이터 검토 흐름 · FlowChart

### 입력

학습용 흐름을 만드세요: 합성 데이터 수신 → 열 이름과 단위 검증 → 결측값 검토 → 요약 → 차트 검토 → 공유. 검증에 실패하면 입력 단계로 돌아갑니다. 분기에 라벨을 표시하고 공유 전에 검토 단계를 유지하세요.

### 단계 및 확인 사항

FlowChart에서 흐름 텍스트를 사용하세요. 각 노드, 검증 반복 경로, 판단 라벨을 확인하세요. 편집기에서 노드 하나를 수정하고 관계가 여전히 입력과 일치하는지 확인하세요.

[전체 작업 흐름 보기](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-flowchart-tutorial.mp4)

공유 전에 과학적 의미, 라벨, 출처를 검토하세요. 편집 및 내보내기 옵션은 작업 공간과 작업 흐름에 따라 다르며 튜토리얼에서 구체적인 예를 확인할 수 있습니다.

SciFig는 상용 플랫폼입니다. 이 저장소는 공개 리소스 모음이며 제품 소스 코드는 아닙니다. 자료, 템플릿, MIT 라이선스 Skill에는 각각 별도 약관이 적용되며 다른 콘텐츠에 자동으로 확대 적용되지 않습니다.

[라이선스 및 사용](../docs/example-usage.ko.md)
