# AI Test Bench

A modular, real-time machine-vision inspection framework built with Python,
OpenCV and YOLO.

## Current Features

- Live camera inspection
- YOLO object detection
- Detector-independent `Detection` objects
- Configurable inspection modules
- Pass/fail inspection results
- Operator-triggered result saving
- SQLite result storage
- Custom live overlays and bounding boxes
- FPS display

## Architecture

The application separates camera capture, AI detection, inspection logic,
rendering, reporting and persistence into independent modules.

See [Architecture](docs/architecture.md) for the full design.

## Installation

```bash
git clone https://github.com/LukeCunniffe/ai_test_bench.git
cd ai_test_bench

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
