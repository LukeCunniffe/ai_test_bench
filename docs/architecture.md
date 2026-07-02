# AI Test Bench Architecture

## Goal

Create an AI-powered inspection framework that can perform multiple independent inspections on a live camera feed.

---

## Design Principles

1. One class = one responsibility.
2. Inspections are independent plugins.
3. Configuration belongs in configuration files.
4. Images are processed in memory and are not stored by default.
5. Every architectural decision should be documented.

---

## Data Flow

Camera
    ↓
Detector
    ↓
Inspection Manager
    ↓
Inspection Plugins
    ↓
Inspection Results
    ↓
Database
    ↓
Dashboard (future)

---

## Core Components

Camera
- Captures frames

Detector
- Runs YOLO

Inspection Manager
- Coordinates inspections

Inspection Plugins
- Individual checks

Database
- Stores inspection history

Dashboard
- Displays results
