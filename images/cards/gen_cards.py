# Generates project card SVGs for README.md
# Usage: python images/cards/gen_cards.py
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
W, H = 420, 236
FONT = "Pretendard, 'Apple SD Gothic Neo', 'Malgun Gothic', 'Noto Sans KR', sans-serif"

CARDS = [
    dict(file="lightletter", accent="#4F46E5", category="CNN ACCELERATOR",
         title="LightLetter", subtitle="손글씨 인식 광통신용 CNN 가속기",
         stats=[("6.22×", "CPU 대비 연산 속도"), ("-57.7%", "CPU 대비 전력 소모")],
         tags=["Verilog", "CNN", "Zero gating"]),
    dict(file="rv32i_pipeline", accent="#0284C7", category="PROCESSOR",
         title="RV32I Pipeline CPU", subtitle="5단 파이프라인 RISC-V 프로세서",
         stats=[("-32.3%", "Critical path delay"), ("9.736 ns", "14.391 ns에서 단축")],
         tags=["Verilog", "RISC-V", "Basys3"]),
    dict(file="uart_fifo_uvm", accent="#7C3AED", category="VERIFICATION",
         title="UART & FIFO", subtitle="통신 IP 설계 및 UVM 기반 검증",
         stats=[("8-N-1", "UART 컨트롤러"), ("UVM", "테스트벤치 검증")],
         tags=["SystemVerilog", "UVM", "FIFO"]),
    dict(file="axi_soc", accent="#059669", category="SoC",
         title="AXI 기반 SoC", subtitle="MicroBlaze + 직접 설계한 Custom IP",
         stats=[("5종", "Timer·UART·SPI·I2C·GPIO"), ("AXI4-Lite", "버스 인터페이스")],
         tags=["AXI", "Vivado", "Vitis", "C"]),
    dict(file="ov7670_vga", accent="#EA580C", category="VIDEO",
         title="OV7670 Camera & VGA", subtitle="카메라 영상 입력 → VGA 출력",
         stats=[("SCCB", "FSM 기반 카메라 설정"), ("Gray/Binary", "스위치 제어 필터")],
         tags=["Verilog", "SCCB", "VGA"]),
    dict(file="workout_check", accent="#DB2777", category="EDGE AI",
         title="운동 자세 체크 시스템", subtitle="체형 기반 운동 추천 및 자세 판별",
         stats=[("30→10", "판단 윈도우 (프레임)"), ("LSTM", "Mediapipe 자세 판별")],
         tags=["Python", "LSTM", "Jetson Orin Nano"]),
]


def text_w(s, size):
    # Rough width estimate: Hangul is ~1em, ASCII ~0.6em
    return sum(size * (1.0 if ord(c) > 0x2E80 else 0.6) for c in s)


def card(c):
    a = c["accent"]
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
    p.append(f'<defs><clipPath id="r"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>')
    p.append(f'<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="#FFFFFF"/>'
             f'<rect width="{W}" height="6" fill="{a}"/></g>')
    p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#E5E7EB"/>')
    p.append(f'<text x="24" y="38" font-size="11" font-weight="700" letter-spacing="1.5" fill="{a}">{escape(c["category"])}</text>')
    p.append(f'<text x="24" y="66" font-size="22" font-weight="800" fill="#111827">{escape(c["title"])}</text>')
    p.append(f'<text x="24" y="89" font-size="13" fill="#6B7280">{escape(c["subtitle"])}</text>')

    bw, by, bh = (W - 48 - 12) / 2, 104, 68
    for i, (val, lab) in enumerate(c["stats"]):
        bx = 24 + i * (bw + 12)
        p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{a}" fill-opacity="0.08"/>')
        p.append(f'<text x="{bx+14}" y="{by+32}" font-size="22" font-weight="800" fill="{a}">{escape(val)}</text>')
        p.append(f'<text x="{bx+14}" y="{by+53}" font-size="11" fill="#4B5563">{escape(lab)}</text>')

    tx, ty = 24, 190
    for t in c["tags"]:
        tw = text_w(t, 11) + 20
        p.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="24" rx="12" fill="#F3F4F6"/>')
        p.append(f'<text x="{tx+tw/2}" y="{ty+16}" font-size="11" font-weight="600" fill="#374151" text-anchor="middle">{escape(t)}</text>')
        tx += tw + 6

    p.append('</svg>')
    return "\n".join(p)


if __name__ == "__main__":
    for c in CARDS:
        (OUT / f'{c["file"]}.svg').write_text(card(c), encoding="utf-8")
        print("wrote", c["file"] + ".svg")
