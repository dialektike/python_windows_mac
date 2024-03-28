# python windows mac linux

파이썬에서 파일을 읽거나 쓰거나 또는 폴더를 다룰 때 상이한 OS에서 처리하는 사례

만약 가상 환경을 만들지 않고 이 프로젝트를 연습하고자 하시는 분은 `pandas`라는 패키지를 설치해주세요.

## 가상 환경 만들기

이 프로젝트에서 사용할 가장 환경을 만들겠습니다. 여기서는 `conda`를 이용해서 `monthly`이라는 이름으로 만들겠습니다. 그리고 나서 만든 가상환경을 활성화하겠습니다. 참고로 저는 맥에서 `miniforge`를 이용해서 `conda`를 사용하고 있습니다. 추가로 이 프로젝트를 가지고 연습하기 위해서는 `pandas`라는 패키지가 필요합니다. 가상환경에 이 패키지를 추가합니다.

```bash
conda create -n monthly python=3.11
conda activate monthly
conda install pandas
```

만약 앞에서 만든 가상환경에서 나가고 제거하려고 한다면 다음과 같이 하시면 됩니다.

```bash
conda deactivate
conda remove -n monthly --all
```
