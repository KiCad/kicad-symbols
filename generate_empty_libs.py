from __future__ import print_function

import os

libs = [
    # Basic Devices
    "device",
    "led",
    "motor",
    "power",
    "pspice",
    "relay",
    "switch",

    # Connectors
    "connector",

    # Virtual Symbols
    "graphical_symbol",
    "logo",
    "mechanical",

    # Simple semiconductors
    "diode",
    "esd_protection",
    "transistor",
    "thyristor",
    "valve",

    # Displays
    "display_character",
    "display_graphic",
    "display_segment",

    # Transformers
    "transformer",
    "transformer_power",
    "transformer_pulse",
    "transformer_signal",

    # Sensors
    "sensor",
    "sensor_current",
    "sensor_humidity",
    "sensor_magnetic",
    "sensor_motion",
    "sensor_multi-function",
    "sensor_photo",
    "sensor_pressure",
    "sensor_temperature",

    # Audio / Video
    "audio_adc_dac",
    "audio_codec",
    "audio_misc",
    "video",

    # Linear Devices
    "amplifier_audio",
    "amplifier_current_sense",
    "amplifier_difference",
    "amplifier_instrumentation",
    "amplifier_operational",
    "amplifier_rf",
    "amplifier_video",
    "comparator",

    # References
    "reference_current",
    "reference_voltage",

    # Power Management
    "battery",
    "battery_management",
    "power_conditioning",
    "power_distribution",
    "power_monitor",
    "power_supervisor",
    "power_module_ac-dc",
    "power_module_ac-ac",
    "power_module_dc-dc",
    "power_module_dc-ac",

    # Voltage Regulators
    "regulator_linear",
    "regulator_linear_controller",
    "regulator_switching",
    "regulator_switching_controller",
    "regulator_switching_module",

    # Mixed Signal
    "adc",
    "adc_dac",
    "analog_switch",
    "dac",
    "digital_pot",

    # Drivers
    "driver_led",
    "driver_gate",
    "driver_motor",

    # Timers
    "timer",
    "timer_oscillator",
    "timer_pll",
    "timer_rtc",

    # Logic
    "logic",
    "logic_74xx",
    "logic_cmos40xx",
    "logic_translator",

    # Isolators
    "isolator.lib",
    "isolator_analog.lib",

    # CPLD
    "cpld",
    "cpld_altera_intel",
    "cpld_xilinx",

    # FPGA
    "fpga",
    "fpga_actel",
    "fpga_altera_intel",
    "fpga_atmel",
    "fpga_xilinx",

    # MCU
    "mcu",
    "mcu_8048",
    "mcu_8051",
    "mcu_atmel_avr",
    "mcu_atmel_avr32",
    "mcu_atmel_arm",
    "mcu_cypress",
    "mcu_cypress_arm",
    "mcu_microchip_pic10",
    "mcu_microchip_pic12",
    "mcu_microchip_pic16",
    "mcu_microchip_pic18",
    "mcu_microchip_pic24",
    "mcu_microchip_pic32",
    "mcu_freescale_hc",
    "mcu_freescale_coldfire",
    "mcu_infineon_c166",
    "mcu_nxp_arm",
    "mcu_parallax",
    "mcu_renesas",
    "mcu_st_stm32",
    "mcu_st_stm8",
    "mcu_texas_msp430",

    # CPU
    "cpu",
    "cpu_intel_x86",
    "cpu_amd_x86",
    "cpu_motorola_68000",
    "cpu_motorola_powerpc",
    "cpu_zilog_z80",

    # DSP
    "dsp",
    "dsp_microchip_dspic33",
    "dsp_texas",
    "dsp_freescale",

    # SOC
    "soc",
    "soc_texas_arm",

    # Memory
    "memory",
    "memory_card",
    "memory_controller",
    "memory_eeprom",
    "memory_flash",
    "memory_nvram",
    "memory_vram",

    # Interface
    "interface",
    "interface_bluetooth",
    "interface_can_lin",
    "interface_ethernet",
    "interface_i2c",
    "interface_lvds",
    "interface_rf",
    "interface_spi",
    "interface_telecom",
    "interface_uart",
    "interface_usb",
    "interface_wifi",
    "interface_video",
    "interface_zigbee",
]

LIB_DATA = [
    "EESchema-LIBRARY Version 2.3",
    "#encoding utf-8",
    "#End Library"
]

DCM_DATA = [
    "EESchema-DOCLIB  Version 2.0",
    "#",
    "#End Doc Library"
]


def make_library(fn):

    lib_name = fn + ".lib"
    dcm_name = fn + ".dcm"

    if os.path.exists(lib_name):
        print("Skipping library {l}".format(l=fn))
        return

    print("Generating library {l}".format(l=fn))

    # Write the LIB file
    f = open(lib_name, 'w')
    for line in LIB_DATA:
        f.write(line + "\n")
    f.close()

    # Write the DCM file
    f = open(dcm_name, 'w')
    for line in DCM_DATA:
        f.write(line + "\n")
    f.close()

for lib in libs:
    make_library(lib)