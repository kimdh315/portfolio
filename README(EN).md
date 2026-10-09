# Donghyun Kim

**Circuit Design & Verification Engineer**

> I develop FPGA and embedded systems with a focus on RTL design and UVM-based verification.  
> My work centers on digital and analog circuit design, functional verification, and hardware/software integration.

---

## Education

#### Kwangwoon University - Bachelor, Electronic Engineering  
2020.03 - 2026.02
- Relevant coursework : Digital Engineering, Computer Architecture, Circuit Theory
- GPA : 4.36 / 4.5 (Major GPA : 4.5 / 4.5)
- Project : 
  1. 10MHz 10bits Monotonic SAR ADC circuit design
  2. Snapshot Digital PLL circuit design
- Club : ROLAB / Trick

#### On-Device AI System Semiconductor Design Education
2026.03 - 2026.10
- Project :
  1. SoC based on AXI
  2. RV32I Single-Cycle CPU
  3. UART / FIFO Design & Verification
  4. CNN Accelerator Design

---

## Skills

| Area | Details |
|------|---------|
| **RTL Design** | SystemVerilog, Verilog |
| **Verification** | UVM, Functional Coverage |
| **FPGA** | Xilinx Artix-7 (Basys3), Xilinx Zynq-7020 (Zybo Z7-20), Vivado |
| **Embedded** | MicroBlaze, Embedded C |
| **Tools** | Git, Vivado Simulator, Virtuoso, PSpice |

---

<div style="page-break-after: always;"></div>

## Featured Projects

### [LightLetter](https://github.com/mumallaeng/LightLetter.git)
1. LightLetter project that recognizes handwriting and transmits it through optical communication
2. Used the EMNIST dataset for handwriting recognition and designed a CNN accelerator for fast and efficient computation
3. Applied zero gating, which skips computation when the input is zero, to improve power efficiency
4. Achieved 10x faster computation and 40% lower power consumption compared to the CPU

`CNN Accelerator` `Verilog`

### [OV7670 Camera with VGA](https://github.com/kimdh315/vga_camera.git)
1. Get image from ov7670 camera and display it by VGA connect
2. SCCB is designed based on FSM to setup ov7670 camera module
3. Gray and Binary filter is added and controlled by switch on Basys3 board

`OV7670` `SCCB` `VGA` `Verilog`

### [AI-based Workout Posture Check & Recommendation System](https://github.com/kimdh315/body_and_workout_check.git)
1. AI-based system that recommends workouts based on the user's body type and checks workout posture
2. Developed a posture checking program using Mediapipe and LSTM
3. Optimized the decision window from 30 frames to 10 frames to secure real-time performance on Jetson Orin Nano

`AI` `LSTM` `Mediapipe` `Jetson Orin Nano` `Python`

### [SoC based on AXI](https://github.com/kimdh315/soc_axi_microblaze)
1. AXI4-Lite based SoC implemented on the Basys3 with MicroBlaze
2. RTL design custom IP is used - Timer, UART, SPI, I2C, GPIO
3. Verification with Vitis C code

`AXI` `Custom IP` `Vivado` `Vitis` `C`

<!-- ### [I2C / SPI Controller with UVM](https://github.com/kimdh315/spi_i2c_uvm)
1. RTL design of SPI and I2C controller
2. Verification with UVM

`SystemVerilog` `UVM` `SVA` -->

### [RV32I Pipeline CPU](https://github.com/kimdh315/rv32i_pipeline)
1. 5 stage pipeline CPU supporting the RISC-V RV32I instruction set
2. Designed to resolve setup time violation at single cycle CPU
3. Achieved a 32.3% reduction in critical path delay compared to the single-cycle design, improving from 14.391 ns to 9.736 ns
4. Verification with assembly code - Bubble sort algorithm

`Verilog` `RISC-V` `Basys3`

### [UART & FIFO with UVM](https://github.com/kimdh315/uart_fifo_uvm)
1. RTL design of 8-N-1 UART protocol controller and 8 bit width synchronous FIFO
2. Functional verification with UVM

`Verilog` `SystemVerilog` `UART` `FIFO` `UVM`

---

<div style="page-break-after: always;"></div>

## AI Utilization

### [UVM Auto Generation](https://github.com/kimdh315/auto_uvm_gen.git)
- Automated generation of UVM boilerplate with Python, minimizing repetitive coding unrelated to verification logic

---

## Contact

- Email: kimdh01315@gmail.com
- GitHub: https://github.com/kimdh315/portfolio

---

<sub>Simulation waveforms and FPGA resource reports for each project are available in the respective repository README files.</sub>
