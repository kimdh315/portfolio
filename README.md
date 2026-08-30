# Donghyun Kim

**Digital Design & Verification Engineer**

> I develop FPGA and embedded systems with a focus on RTL design and UVM-based verification.  
> My work centers on digital circuit design, functional verification, and hardware/software integration.

---

## Education

#### Kwangwoon University - Bachelor, Electronic Engineering  
2020.03 - 2026.02
- Relevant coursework : Digital Logic Design, Computer Architecture, Semiconductor Engineering
- GPA : 4.36 / 4.5 (Major GPA : 4.5 / 4.5)
- Project : 
  1. 10MHz 10bits Monotonic SAR ADC circuit design
  2. Snapshot Digital PLL circuit design
- Club : ROLAB / Trick

#### On-Device AI System Semiconductor Design Education
2026.03 - Current
- Project :
  1. SoC based on AXI
  2. RV32I Single-Cycle CPU
  3. UART / FIFO Design & Verification

---

## Skills

| Area | Details |
|------|---------|
| **RTL Design** | SystemVerilog, Verilog |
| **Verification** | UVM, SystemVerilog Assertions (SVA), Functional Coverage |
| **FPGA** | Xilinx Artix-7 (Basys3), Vivado |
| **Embedded** | MicroBlaze, Embedded C |
| **Tools** | Git, GTKWave, Vivado Simulator |

---

## Featured Projects

### [OV7670 Camera with VGA](https://github.com/kimdh315/vga_camera.git)
1. Get image from ov7670 camera and display it by VGA connect
2. SCCB is designed based on FSM to setup ov7670 camera module
3. Gray and Binary filter is added and controlled by switch on Basys3 board

`OV7670` `SCCB` `VGA` `Verilog`

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

`Verilog` `RISC-V` `Basys3`

### [RV32I Single-Cycle CPU](https://github.com/kimdh315/rv32i_single_cycle)
1. Single cycle CPU supporting the RISC-V RV32I instruction set
2. Verification with assembly code - Bubble sort algorithm

`Verilog` `RISC-V` `Basys3`

### [UART & FIFO with UVM](https://github.com/kimdh315/uart_fifo_uvm)
1. RTL design of 8-N-1 UART protocol controller and 8 bit width synchronous FIFO
2. Verification with UVM

`Verilog` `SystemVerilog` `UART` `FIFO` `UVM`

---

## AI Utilization

### [UVM Auto Generation](https://github.com/kimdh315/auto_uvm_gen.git)
- Automated generation of UVM boilerplate with Python, minimizing repetitive coding unrelated to verification logic

---

## Contact

- Email: kimdh01315@gmail.com
- github: https://github.com/kimdh315/portfolio

---

<sub>Simulation waveforms and FPGA resource reports for each project are available in the respective repository README files.</sub>
