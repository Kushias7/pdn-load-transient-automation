# PDN Test Automation

Automated load transient test framework for qualifying a Power Distribution Network (PDN).

## Repository Structure

src/
    instruments.py
    load_transient_test.py
    report_generator.py

scripts/
    run_test.py

requirements.txt

## Hardware Setup

+5V PSU ----> PDN Input

Electronic Load ---> Output Rail Under Test

Oscilloscope CH1 ---> Rail Output
Oscilloscope GND ---> Board Ground

Example Wiring

     +5V PSU
        |
        |-----> PDN Board -----> Electronic Load
        |
     Oscilloscope CH1

## Example Scope Settings

Timebase: 1 ms/div  
Voltage scale: 500 mV/div  
Trigger: Rising edge on output rail

## Running Test

pip install -r requirements.txt

python scripts/run_test.py

## Generated Files

results_SN001.csv
waveform_SN001_*.txt
test_report.pdf