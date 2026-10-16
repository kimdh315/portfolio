<div align="center">

# 김동현

### RTL Design & Verification Engineer

<a href="mailto:kimdh01315@gmail.com"><img src="https://img.shields.io/badge/Email-kimdh01315@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>
<a href="https://github.com/kimdh315"><img src="https://img.shields.io/badge/GitHub-kimdh315-181717?style=flat-square&logo=github&logoColor=white"/></a>

RTL 설계와 UVM 기반 검증을 중심으로 FPGA 및 임베디드 시스템을 개발합니다.<br/>
디지털 및 아날로그 회로 설계, 기능 검증, 하드웨어/소프트웨어 통합에 집중하고 있습니다.

</div>

---

## 🎓 학력 및 교육

**광운대학교** 전자공학과 학사 &nbsp;|&nbsp; `2020.03 – 2026.02`

- **학점** : 4.36 / 4.5 &nbsp;(전공 **4.5 / 4.5**)
- **관련 과목** : 디지털공학, 컴퓨터구조, 회로이론
- **프로젝트** : 10MHz 10bit Monotonic SAR ADC 설계 · Snapshot Digital PLL 설계
- **동아리** : ROLAB / Trick

**온디바이스 AI 시스템반도체 설계 교육** &nbsp;|&nbsp; `2026.03 – 2026.10`

- **프로젝트** : CNN 가속기 설계 · RV32I CPU · AXI 기반 SoC · UART / FIFO 설계 및 UVM 검증

---

## 🛠 기술 스택

| 분야 | 내용 |
|:--|:--|
| **RTL 설계** | ![SystemVerilog](https://img.shields.io/badge/SystemVerilog-1A4D8F?style=flat-square) ![Verilog](https://img.shields.io/badge/Verilog-2E7D32?style=flat-square) |
| **검증** | ![UVM](https://img.shields.io/badge/UVM-6A1B9A?style=flat-square) ![Functional Coverage](https://img.shields.io/badge/Functional_Coverage-8E24AA?style=flat-square) |
| **FPGA** | ![Artix-7](https://img.shields.io/badge/Artix--7_(Basys3)-ED1C24?style=flat-square) ![Zynq-7020](https://img.shields.io/badge/Zynq--7020_(Zybo_Z7--20)-ED1C24?style=flat-square) ![Vivado](https://img.shields.io/badge/Vivado-F57C00?style=flat-square) |
| **임베디드** | ![MicroBlaze](https://img.shields.io/badge/MicroBlaze-455A64?style=flat-square) ![C](https://img.shields.io/badge/Embedded_C-00599C?style=flat-square&logo=c&logoColor=white) |
| **툴** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![Vivado Simulator](https://img.shields.io/badge/Vivado_Simulator-F57C00?style=flat-square) ![Virtuoso](https://img.shields.io/badge/Virtuoso-0277BD?style=flat-square) ![PSpice](https://img.shields.io/badge/PSpice-0277BD?style=flat-square) |

---

<div style="page-break-after: always;"></div>

## 🚀 주요 프로젝트

<table>
  <tr>
    <td><a href="https://github.com/mumallaeng/LightLetter"><img src="images/cards/lightletter.svg" width="400"/></a></td>
    <td><a href="https://github.com/kimdh315/rv32i_pipeline"><img src="images/cards/rv32i_pipeline.svg" width="400"/></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/kimdh315/uart_fifo_uvm"><img src="images/cards/uart_fifo_uvm.svg" width="400"/></a></td>
    <td><a href="https://github.com/kimdh315/soc_axi_microblaze"><img src="images/cards/axi_soc.svg" width="400"/></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/kimdh315/vga_camera"><img src="images/cards/ov7670_vga.svg" width="400"/></a></td>
    <td><a href="https://github.com/kimdh315/body_and_workout_check"><img src="images/cards/workout_check.svg" width="400"/></a></td>
  </tr>
</table>

<sub>카드를 클릭하면 해당 저장소로 이동합니다.</sub>

---

<div style="page-break-after: always;"></div>

## 📝 프로젝트 상세

### 🔦 [LightLetter](https://github.com/mumallaeng/LightLetter.git) — 손글씨 인식 광통신용 CNN 가속기

> **CPU 대비 6.22× 빠른 연산 · 전력 소모 57.7% 감소**

<!-- <img src="images/lightletter.png" width="600"/> -->

- EMNIST 손글씨를 인식해 광통신을 수행하는 시스템에서, 연산을 빠르고 효율적으로 처리하는 CNN 가속기 설계
- 입력이 0이면 연산을 건너뛰는 **Zero gating** 기법 적용
- 기존 가속기 대비 **연산 시간 12.3% 단축**, **전력 소모 5% 감소**

`CNN 가속기` `Verilog`

### ⚙️ [RV32I Pipeline CPU](https://github.com/kimdh315/rv32i_pipeline) — 5단 파이프라인 RISC-V 프로세서

> **Critical path delay 14.391 ns → 9.736 ns (32.3% 단축)**

<!-- <img src="images/rv32i_pipeline.png" width="600"/> -->

- RISC-V RV32I 명령어 세트를 지원하는 5단 파이프라인 CPU 설계
- Single-Cycle CPU에서 발생한 setup time violation을 해결하기 위해 파이프라인 구조로 재설계
- 어셈블리 코드(Bubble sort 알고리즘)로 검증

`Verilog` `RISC-V` `Basys3`

### ✅ [UVM 기반 UART & FIFO](https://github.com/kimdh315/uart_fifo_uvm) — 통신 IP 설계 및 검증

- 8-N-1 UART 프로토콜 컨트롤러 및 8bit 폭 동기식 FIFO RTL 설계
- UVM 테스트벤치로 동작 검증

`Verilog` `SystemVerilog` `UART` `FIFO` `UVM`

<!-- ### [UVM 기반 I2C / SPI 컨트롤러](https://github.com/kimdh315/spi_i2c_uvm)
1. SPI 및 I2C 컨트롤러 RTL 설계
2. UVM으로 검증

`SystemVerilog` `UVM` `SVA` -->

### 🧩 [AXI 기반 SoC](https://github.com/kimdh315/soc_axi_microblaze) — MicroBlaze + Custom IP

- Basys3 보드에 MicroBlaze를 이용한 AXI4-Lite 기반 SoC 구현
- RTL로 직접 설계한 Custom IP 적용 : **Timer, UART, SPI, I2C, GPIO**
- Vitis C 코드로 검증

`AXI` `Custom IP` `Vivado` `Vitis` `C`

### 📷 [OV7670 카메라 & VGA 출력](https://github.com/kimdh315/vga_camera.git) — 영상 입출력 파이프라인

- OV7670 카메라로 영상을 받아 VGA로 화면에 출력
- 카메라 모듈 설정을 위한 SCCB 인터페이스를 FSM 기반으로 설계
- Gray / Binary 필터를 추가하고 Basys3 보드의 스위치로 제어

`OV7670` `SCCB` `VGA` `Verilog`

### 🏋️ [AI 기반 운동 자세 체크 및 추천 시스템](https://github.com/kimdh315/body_and_workout_check.git) — 엣지 AI

> **판단 윈도우 30 → 10 프레임 최적화로 실시간성 확보**

- 사용자의 체형을 바탕으로 운동을 추천하고, 운동 자세를 체크하는 시스템 구현
- Mediapipe 및 LSTM으로 자세를 판별하는 프로그램 작성
- Jetson Orin Nano 환경에서 실시간으로 동작하도록 최적화

`AI` `LSTM` `Mediapipe` `Jetson Orin Nano` `Python`

---

<div style="page-break-after: always;"></div>

<!-- ## AI 활용

### [UVM 자동 생성](https://github.com/kimdh315/auto_uvm_gen.git)
- Python으로 UVM 보일러플레이트 코드를 자동 생성하여, 검증 로직과 무관한 반복 코딩 최소화

--- -->

## 📫 연락처

- **Email** : kimdh01315@gmail.com
- **GitHub** : https://github.com/kimdh315

---

<sub>각 프로젝트의 시뮬레이션 파형과 FPGA 리소스 리포트는 해당 저장소의 README에서 확인할 수 있습니다.</sub>
