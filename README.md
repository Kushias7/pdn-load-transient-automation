# PDN Load Transient Automation

Automated test framework for validating a Power Distribution Network (PDN) used in satellite payload systems.

## Overview
This project implements a Python-based automated testing system that performs load transient testing on a PDN.

The system controls:
- Programmable Power Supply
- Electronic Load
- Oscilloscope

via PyVISA and captures transient responses for analysis.

## Test Setup

PSU (+5V) → PDN Board → Electronic Load  
Oscilloscope Channel 1 connected to output rail

## Example Scope Settings

Timebase: 1 ms/div  
Voltage scale: 500 mV/div  
Trigger: Rising edge on output rail  
Bandwidth limit: 20 MHz

## Running the Test

```bash
pip install -r requirements.txt
python scripts/run_test.py
