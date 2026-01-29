# sclearn-est15th

이 저장소는 **Scikit-learn**을 활용한 머신러닝 학습 예제와 실전 프로젝트 코드를 포함하고 있습니다.
기초적인 머신러닝 개념부터 고급 알고리즘, 그리고 실제 데이터셋을 활용한 프로젝트(타이타닉, 와인 품질 예측 등)까지 다양한 내용을 다룹니다.

## 📂 프로젝트 구조 (Project Structure)

주요 학습 내용은 Jupyter Notebook 파일(`.ipynb`)로 구성되어 있으며, 주제별로 다음과 같이 나뉩니다.

### 📚 기초 및 데이터 전처리 (Basics & Preprocessing)
- **Scikit-learn 시작하기**: `1_sklearn_start.ipynb`
- **모델 선택 (Model Selection)**: `2_ModelSelection.ipynb`
- **데이터 전처리 (Preprocessing)**: `4_sklearn_PreProcess.ipynb`
- **다항 특성 (Polynomial Features)**: `8_polynominal_Feature.ipynb`

### 🤖 지도 학습 (Supervised Learning)

#### 분류 (Classification)
- **분류 모델 기초**: `5_sklearn_classification.ipynb`
- **서포트 벡터 머신 (SVM)**: `3_SVM.ipynb`
- **분류 모델 튜닝 (Optuna)**: `6_classification_Optuna.ipynb`

#### 회귀 (Regression)
- **선형 회귀 모델**: `9_LinearRegressionModel.ipynb`
- **선형 회귀 심화**: `Plus_6_LinearRegressionModel.ipynb`

#### 앙상블 (Ensemble)
- **앙상블 기법**: `10_ensemble.ipynb`
- **앙상블 모델 튜닝 (Optuna)**: `11_ensemble_Optuna.ipynb`

### 🧠 비지도 학습 (Unsupervised Learning)
- **비지도 학습 기초**: `13_unsupervisedLearning.ipynb`

### 🚀 실전 프로젝트 (Projects)

#### 🚢 타이타닉 생존자 예측 (Titanic Survivor Prediction)
- `7_Titanic.ipynb`: 타이타닉 데이터 분석 및 기본 모델링
- `TitanicProject.ipynb`: 심화 프로젝트 코드
- `colab_titanic-a-beginner-friendly-approach-to-top-3.ipynb`: Colab 연동 및 입문자용 가이드

#### 🍷 와인 품질 분류 (Wine Quality Classification)
- `Plus_1_sklearn_wine_classification.ipynb`

#### 🔢 손글씨 숫자 인식 (Digits Recognition)
- `Plus_3_sklearn_digits.ipynb`

### 📂 기타 폴더 (Directories)
- `AutoML/`: AutoML 관련 실험 코드
- `webML/`: 웹 애플리케이션 및 배포 관련 코드
- `data/`: 프로젝트에 사용되는 데이터셋 폴더

## 💻 설치 및 실행 (Installation & Usage)

이 프로젝트는 Python 3.x 환경에서 실행됩니다. 아래 명령어로 필요한 라이브러리를 설치할 수 있습니다.

```bash
pip install -r requirements.txt
# 또는 주요 라이브러리 직접 설치
pip install scikit-learn pandas numpy matplotlib seaborn optuna jupyter
```

Jupyter Notebook을 실행하여 각 파일을 열어볼 수 있습니다.

```bash
jupyter notebook
```

---
*Created for sclearn-est15th curriculum.*
