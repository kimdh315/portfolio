# 김동현

**회로 설계 및 검증 엔지니어**

> RTL 설계와 UVM 기반 검증을 중심으로 FPGA 및 임베디드 시스템을 개발합니다.  
> 디지털 및 아날로그 회로 설계, 기능 검증, 하드웨어/소프트웨어 통합에 집중하고 있습니다.

---

## 학력 및 교육

#### 광운대학교 - 전자공학과 학사  
2020.03 - 2026.02
- 관련 과목 : 디지털공학, 컴퓨터구조, 회로이론
- 학점 : 4.36 / 4.5 (전공 학점 : 4.5 / 4.5)
- 프로젝트 : 
  1. 10MHz 10bit Monotonic SAR ADC 회로 설계
  2. Snapshot Digital PLL 회로 설계
- 동아리 : ROLAB / Trick

#### 온디바이스 AI 시스템반도체 설계 교육
2026.03 - 2026.10
- 프로젝트 :
  1. AXI 기반 SoC
  2. RV32I Single-Cycle CPU
  3. UART / FIFO 설계 및 검증
  4. CNN 가속기 설계

---

## 기술 스택

| 분야 | 내용 |
|------|---------|
| **RTL 설계** | SystemVerilog, Verilog |
| **검증** | UVM, Functional Coverage |
| **FPGA** | Xilinx Artix-7 (Basys3), Xilinx Zynq-7020 (Zybo z7-20), Vivado |
| **임베디드** | MicroBlaze, Embedded C |
| **툴** | Git, Vivado Simulator, Virtuoso, PSpice |

---

<div style="page-break-after: always;"></div>

## 주요 프로젝트

### [LightLetter](https://github.com/mumallaeng/LightLetter.git)
1. 손글씨를 인식해 광통신을 수행하는 LightLetter 프로젝트 수행
2. 손글씨를 인식하기 위해 EMNIST 데이터 셋 사용 및 연산을 효율적이고 빠르게 하기 위한 CNN 가속기 설계
3. 전력 효율을 높이기 위해 입력이 0인 경우 연산을 하지 않는 Zero gating 기법 적용
4. CPU대비 10배의 연산속도, 40%의 전력 소모 감소 달성

`CNN 가속기` `Verilog`

### [OV7670 카메라 & VGA 출력](https://github.com/kimdh315/vga_camera.git)
1. OV7670 카메라로 영상을 받아 VGA로 화면에 출력
2. OV7670 카메라 모듈 설정을 위한 SCCB를 FSM 기반으로 설계
3. Gray / Binary 필터를 추가하고 Basys3 보드의 스위치로 제어

`OV7670` `SCCB` `VGA` `Verilog`

### [AI기반 운동 자세 체크 및 추천 시스템](https://github.com/kimdh315/body_and_workout_check.git)
1. AI를 기반으로 사용자의 체형을 바탕으로 운동을 추천하고, 운동의 자세를 체크하는 시스템 구현
2. Mediapipe 및 LSTM을 통해 자세 확인하는 프로그램 작성
3. Jetson Orin Nano 환경의 실시간성 확보를 위해 판단 윈도우를 30프레임에서 10프레임으로 최적화

`AI` `LSTM` `Mediapipe` `Jetson Orin Nano` `Python`

### [AXI 기반 SoC](https://github.com/kimdh315/soc_axi_microblaze)
1. Basys3 보드에 MicroBlaze를 이용한 AXI4-Lite 기반 SoC 구현
2. RTL로 직접 설계한 Custom IP 적용 - Timer, UART, SPI, I2C, GPIO
3. Vitis C 코드로 검증

`AXI` `Custom IP` `Vivado` `Vitis` `C`

<!-- ### [UVM 기반 I2C / SPI 컨트롤러](https://github.com/kimdh315/spi_i2c_uvm)
1. SPI 및 I2C 컨트롤러 RTL 설계
2. UVM으로 검증

`SystemVerilog` `UVM` `SVA` -->

### [RV32I Pipeline CPU](https://github.com/kimdh315/rv32i_pipeline)
1. RISC-V RV32I 명령어 세트를 지원하는 5단 파이프라인 CPU
2. Single-Cycle CPU에서 발생한 setup time violation을 해결하기 위해 설계
3. Single-Cycle 설계 대비 critical path delay를 14.391 ns에서 9.736 ns로 32.3% 단축
4. 어셈블리 코드(Bubble sort 알고리즘)로 검증

`Verilog` `RISC-V` `Basys3`

### [UVM 기반 UART & FIFO](https://github.com/kimdh315/uart_fifo_uvm)
1. 8-N-1 UART 프로토콜 컨트롤러 및 8bit 폭 동기식 FIFO RTL 설계
2. UVM을 통해 동작 검증

`Verilog` `SystemVerilog` `UART` `FIFO` `UVM`

---

<div style="page-break-after: always;"></div>

## AI 활용

### [UVM 자동 생성](https://github.com/kimdh315/auto_uvm_gen.git)
- Python으로 UVM 보일러플레이트 코드를 자동 생성하여, 검증 로직과 무관한 반복 코딩 최소화

---

## 연락처

- Email: kimdh01315@gmail.com
- GitHub: https://github.com/kimdh315/portfolio

---

<sub>각 프로젝트의 시뮬레이션 파형과 FPGA 리소스 리포트는 해당 저장소의 README에서 확인할 수 있습니다.</sub>
