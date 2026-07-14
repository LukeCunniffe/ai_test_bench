# AI Test Bench

A modular, real-time machine-vision inspection framework built with Python,
OpenCV and YOLO.

## Overview

AI Test Bench is an extensible computer-vision platform for creating automated
inspection workflows.

The project separates camera capture, object detection, inspection logic,
rendering, reporting and data storage into independent components.

## Current Features

- Live camera inspection
- YOLO object detection
- Detector-independent `Detection` objects
- Configurable inspection modules
- Pass/fail inspection results
- Operator-triggered result saving
- SQLite result storage
- Custom live overlays
- Bounding boxes and confidence labels
- Live FPS display
- Keyboard controls

## Architecture

```text
Camera
   |
   v
Detector
   |
   v
Detection Objects
   |
   +-------------------+
   |                   |
   v                   v
Inspection Manager   Overlay Renderer
   |                   |
   v                   v
Inspection Report    Live Display
   |
   v
Database
