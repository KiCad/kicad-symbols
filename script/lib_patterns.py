import fnmatch

PATTERNS = {

    ###
    # These patterns are used to reorganize the KiCad libraries
    # Filters are not case sensitive
    #

    '74xgxx' : 'Logic_74xGxx',
    '74xx' : 'Logic_74xx',

    'battery_management' : 'Battery_Management',

    'cmos4000' : 'Logic_CMOS_4000',
    'cmos_ieee' : 'Logic_CMOS_IEEE',

    'conn' : 'Connector',

    # adc-dac library
    'adc-dac:mcp4801*' : 'Analog_DAC',
    'adc-dac:mcp355*' : 'Analog_ADC',
    'adc-dac:AD390*' : 'Analog_DAC',
    'adc-dac:AD55*' : 'Analog_DAC',
    'adc-dac:AD56*' : 'Analog_DAC',
    'adc-dac:AD722*' : 'Analog_DAC',
    'adc-dac:AD73*' : 'Analog_DAC',
    'adc-dac:AD7533*' : 'Analog_DAC',
    'adc-dac:AD7722*' : 'Analog_ADC',
    'adc-dac:AD775*' : 'Analog_DAC',
    'adc-dac:AD7819*' : 'Analog_ADC',
    'adc-dac:ADS112*' : 'Analog_ADC',
    'adc-dac:ADS123*' : 'Analog_ADC',
    'adc-dac:ADS124*' : 'Analog_ADC',
    'adc-dac:ADS125*' : 'Analog_ADC',
    'adc-dac:ADS128*' : 'Analog_ADC',
    'adc-dac:ADS129*' : 'Analog_ADC',
    'adc-dac:ADS7843*' : 'Driver_Display',
    'adc-dac:LTC186*' : 'Analog_ADC',
    'adc-dac:LTC1664*' : 'Analog_DAC',
    'adc-dac:MAX11*' : 'Analog_ADC',
    'adc-dac:MAX12*' : 'Analog_ADC',
    'adc-dac:MCP342*' : 'Analog_ADC',
    'adc-dac:MCP320*' : 'Analog_ADC',
    'adc-dac:MCP355*' : 'Analog_ADC',
    'adc-dac:MCP49*' : 'Analog_DAC',
    'adc-dac:UVC3*' : 'Analog_MultiFunction',
    'adc-dac:XPT*' : 'Driver_Display',

    # allegro
    'allegro' : 'Sensor_Current',

    # atmel library
    'atmel:AT*MEGA*' : 'MCU_Atmel_AVR',
    'atmel:AT*TINY*' : 'MCU_Atmel_AVR',
    'atmel:AT89*' : 'Memory_Flash',
    'atmel:AT90*' : 'Memory_Flash',
    'atmel:SAM*' : 'MCU_Atmel_ARM',
    'atmel:AT42*' : 'Sensor_Touch',

    # audio library
    'audio:LM18*' : 'Amplifier_Audio',
    'audio:LM38*' : 'Amplifier_Audio',
    'audio:tda*' : 'Amplifier_Audio',

    'contrib' : 'Interface_Telecom',

    # bosch library
    'bosch:BMF*' : 'Sensor_Motion',

    # DC-DC library
    'dc-dc:ADP*' : 'Regulator_Switching',
    'dc-dc:APE*' : 'Regulator_Switching',
    'dc-dc:BD9*' : 'Regulator_Switching',
    'dc-dc:CRE*' : 'Regulator_Switching',
    'dc-dc:CRE*' : 'Regulator_Switching',
    'dc-dc:GL2*' : 'Regulator_Switching',
    'dc-dc:ICL*' : 'Regulator_SwitchedCapacitor',
    'dc-dc:IS3*' : 'Driver_LED',
    'dc-dc:ISL*' : 'Regulator_Switching',
    'dc-dc:L59*' : 'Regulator_Switching',
    'dc-dc:LM25*' : 'Regulator_Switching',
    'dc-dc:LM26*' : 'Regulator_Switching',
    'dc-dc:LM2731*' : 'Regulator_Switching',
    'dc-dc:LM2733*' : 'Regulator_Switching',
    'dc-dc:LM2734*' : 'Regulator_Switching',
    'dc-dc:LM2735*' : 'Regulator_Switching',
    'dc-dc:LM27761*' : 'Regulator_SwitchedCapacitor',
    'dc-dc:LM3670*' : 'Regulator_Switching',
    'dc-dc:LM50*' : 'Regulator_Switching',
    'dc-dc:LM51*' : 'Regulator_Switching',
    'dc-dc:LMR*' : 'Regulator_Switching',
    'dc-dc:LT1054*' : 'Regulator_SwitchedCapacitor',
    'dc-dc:LTC1044*' : 'Regulator_SwitchedCapacitor',
    'dc-dc:LTC660*' : 'Regulator_SwitchedCapacitor',
    'dc-dc:LT1073*' : 'Regulator_Switching',
    'dc-dc:LT1108*' : 'Regulator_Switching',
    'dc-dc:LT137*' : 'Regulator_Switching',
    'dc-dc:LT194*' : 'Regulator_Switching',
    'dc-dc:LT343*' : 'Regulator_Switching',
    'dc-dc:LT346*' : 'Driver_LED',
    'dc-dc:LT347*' : 'Regulator_Switching',
    'dc-dc:LT3755*' : 'Driver_LED',
    'dc-dc:MAX150*' : 'Regulator_Switching',
    'dc-dc:MAX503*' : 'Regulator_Switching',
    'dc-dc:MCP163*' : 'Regulator_Switching',
    'dc-dc:MCP1640*' : 'Regulator_Switching',
    'dc-dc:MCP165*' : 'Regulator_Switching',
    'dc-dc:NMA*' : 'Regulator_Switching',
    'dc-dc:NXE*' : 'Regulator_Switching',
    'dc-dc:PAM*' : 'Regulator_Switching',
    'dc-dc:TEN20*' : 'Converter_DC-DC',
    'dc-dc:TMR_*' : 'Regulator_Switching',
    'dc-dc:TPS543*' : 'Regulator_Switching',
    'dc-dc:TPS560*' : 'Regulator_Switching',
    'dc-dc:TPS605*' : 'Regulator_ChargePump',
    'dc-dc:TPS612*' : 'Regulator_Switching',
    'dc-dc:TPS621*' : 'Regulator_Switching',
    'dc-dc:TPS622*' : 'Regulator_Switching',
    'dc-dc:TSR_*' : 'Regulator_Switching',



    'digital_audio' : 'Audio',

    'driver_gate' : 'Driver_Gate',

    'display' : 'Display',

    'ESD_Protection' : 'Power_Protection',

    'ftdi' : 'Interface_USB',

    'graphic_symbols' : 'Graphics',

    # intel library
    'intel:16*' : 'Interface_UART',

    # interface library
    'interface:ADM*' : 'Interface_UART',
    'interface:CH376T' : 'Memory_Controller',
    'interface:FUSB*' : 'Interface_USB',
    'interface:GD*' : 'Interface_UART',
    'interface:LT1080' : 'Interface_UART',
    'interface:LTC2875*' : 'Interface_CAN_LIN',
    'interface:ltc2983' : 'Sensor_Temperature',
    'interface:ltc2990' : 'Sensor_MultiFunction',
    'interface:max134*' : 'Interface_UART',
    'interface:max2*' : 'Interface_UART',
    'interface:max30*' : 'Interface_UART',
    'interface:MAX318*' : 'Sensor_Temperature',
    'interface:max32*' : 'Interface_UART',
    'interface:mcp25*' : 'Interface_CAN_LIN',
    'interface:mcp4*' : 'Digital_Potentiometer',
    'interface:SN65*' : 'Interface_CAN_LIN',
    'interface:sp34*' : 'Interface_UART',
    'Interface_tca94*' : 'Interface_I2C',
    'interface:tja1*' : 'Interface_CAN_LIN',
    'interface:xtr*' : 'Interface_Current_Loop',

    # intersil library
    'intersil:EL7*' : 'Driver_Gate',
    'intersil:HIP*' : 'Driver_Gate',

    # IR
    'ir:IR*21*' : 'Driver_Gate',
    'ir:IRS20*' : 'Amplifier_Audio',
    'ir:AUIPS*' : 'Sensor_Current',

    'LEM' : 'Sensor_Current',

    # maxim
    'maxim:DS12*' : 'Digital_Potentiometer',
    'maxim:DS18*' : 'Sensor_Temperature',
    'maxim:DS28*' : 'Sensor_Temperature',
    'maxim:MAX12*' : 'Analog_ADC',
    'maxim:max318*' : 'Sensor_Temperature',

    # memory
    'memory:2130' : 'Memory_VRAM',
    'memory:24A*' : 'Memory_EEPROM',
    'memory:24LC*' : 'Memory_EEPROM',
    'memory:25LC*' : 'Memory_EEPROM',
    'memory:dram*' : 'Memory_VRAM',
    'memory:fm*' : 'Memory_NVRAM',
    'memory:hm6*' : 'Memory_VRAM',
    'memory:mt48*' : 'Memory_VRAM',
    'memory:sst*' : 'Memory_Flash',
    'memory:ram*' : 'Memory_VRAM',
    'memory:mb8*' : 'Memory_NVRAM',
    'memory:m29*' : 'Memory_Flash',
    'memory:mr2*' : 'Memory_NVRAM',
    'memory:at24*' : 'Memory_EEPROM',
    'memory:27C*' : 'Memory_EEPROM',
    'memory:idt*' : 'Memory_VRAM',
    'memory:m25*' : 'Memory_Flash',
    'memory:m29*' : 'Memory_flash',
    'memory:at45*' : 'Memory_flash',
    'memory:93*' : 'Memory_EEPROM',
    'memory:am29*' : 'Memory_Flash',

    # microchip
    'microchip:enc*' : 'Interface_Ethernet',
    'microchip:KSZ*' : 'Interface_Ethernet',
    'microchip:LAN*' : 'Interface_Ethernet',
    'microchip:mcp2050*' : 'Interface_CAN_LIN',
    'microchip:mcp2515*' : 'Interface_CAN_LIN',
    'microchip:mic*' : 'Driver_Gate',
    'microchip:usb*' : 'Interface_USB',

    # microchip processors, etc
    'microchip_dspic33dsc' : 'DSP_Microchip_dsPIC33',
    'microchip_pic10mcu' : 'MCU_Microchip_PIC10',
    'microchip_pic12mcu' : 'MCU_Microchip_PIC12',
    'microchip_pic16mcu' : 'MCU_Microchip_PIC16',
    'microchip_pic18mcu' : 'MCU_Microchip_PIC18',
    'microchip_pic24mcu' : 'MCU_Microchip_PIC24',
    'microchip_pic32mcu' : 'MCU_Microchip_PIC32',

    # motor_drivers library
    'motor_drivers:STK*' : 'Driver_Motor',
    'motor_drivers:STSPIN*' : 'Driver_Motor',
    'motor_drivers:TMC*' : 'Driver_Motor',
    'motor_drivers:SLA*' : 'Driver_Motor',
    'motor_drivers:l29*' : 'Driver_Motor',
    'motor_drivers:drv*' : 'Driver_Motor',
    'motor_drivers:A495*' : 'Driver_Motor',

    'motors' : 'motor',

    # motorola
    'motorola:MC13192' : 'Interface_ZigBee',

    "msp430" : "MCU_Texas_MSP430",

    'nordicsemi' : 'Interface_Bluetooth',

    # nxp library
    'nxp:pca9*' : 'Driver_LED',

    'nxp_armmcu' : 'MCU_NXP_LPC',
    'nxp_s08' : 'MCU_NXP_S08',
    'nxp_kinetis' : 'MCU_NXP_Kinetis',

    # onsemi
    'onsemi:CM12*' : 'Power_Protection',
    'onsemi:NUP*' : 'Power_Protection',
    'onsemi:NPC*' : 'Power_Pistribution',

    # philips
    'philips:p8*' : 'Interface_I2C',
    'philips:pca8*' : 'Interface_CAN_LIN',
    'philips:pca9*' : 'Interface_I2C',

    'power' : 'Power',

    # power Management
    'power_management:FAN7842' : 'Driver_Gate',
    'power_management:LM50*' : 'Power_Distribution',
    'power_management:LT1641*' : 'Power_Distribution',
    'power_management:LTC435*' : 'Power_Distribution',
    'power_management:LTC4364*' : 'Power_Distribution',
    'power_management:LTC4365*' : 'Power_Distribution',
    'power_management:MCP100*' : 'Power_Supervisor',
    'power_management:TCM8*' : 'Power_Supervisor',
    'power_management:MCP10*' : 'Power_Supervisor',
    'power_management:LTC444*' : 'Driver_Gate',
    'power_management:PM8*' : 'Driver_Gate',
    'power_management:MIC8*' : 'Power_Supervisor',
    'power_management:MIC2587*' : 'Power_Distribution',
    'power_management:MIC2026*' : 'Power_Distribution',

    # power int

    # references
    'references' : 'Reference_Voltage',

    # Relays
    'relays' : 'Relay',

    # rfcom library
    'rfcom:B*' : 'Interface_Bluetooth',
    'rfcom:CC1*' : 'Interface_RF',
    'rfcom:CC2*' : 'Interface_ZigBee',
    'rfcom:DCT*' : 'Interface_RF',
    'rfcom:HF-*' : 'Interface_WiFi',
    'rfcom:MM*' : 'Interface_RF',
    'rfcom:NRF*' : 'Interface_RF',
    'rfcom:RN*' : 'Interface_Bluetooth',
    'rfcom:RXM*' : 'Interface_GPS',
    'rfcom:XBee*' : 'Interface_ZigBee',

    'RFSolutions' : 'Interface_RF',

    # sensors library
    'sensors:40pc*' : 'Sensor_Pressure',
    'sensors:a110*' : 'Sensor_Magnetic',
    'sensors:a130*' : 'Sensor_Magnetic',
    'sensors:ad8148' : 'Sensor_Current',
    'sensors:AS50*' : 'Sensor_Magnetic',
    'sensors:BD*' : 'Sensor_Temperature',
    'sensors:BMP*' : 'Sensor_Pressure',
    'sensors:Flir*' : 'Sensor_Photo',
    'sensors:INA*' : 'Sensor_Current',
    'sensors:KT*' : 'Sensor_Temperature',
    'sensors:L3*' : 'Sensor_Motion',
    'sensors:LG*' : 'Sensor_Motion',
    'sensors:LA*' : 'Sensor_Current',
    'sensors:LIS*' : 'Sensor_Motion',
    'sensors:LM35*' : 'Sensor_Temperature',
    'sensors:LM73*' : 'Sensor_Temperature',
    'sensors:LMT8*' : 'Sensor_Temperature',
    'sensors:LPS*' : 'Sensor_Pressure',
    'sensors:LSM*' : 'Sensor_Motion',
    'sensors:LV*' : 'Sensor_Voltage',
    'sensors:MCP950*' : 'Sensor_Temperature',
    'sensors:MCP970*' : 'Sensor_Temperature',
    'sensors:MCP980*' : 'Sensor_Temperature',
    'sensors:MP45D*' : 'Sensor_Audio',
    'sensors:MPU-*' : 'Sensor_Motion',
    'sensors:MPX*' : 'Sensor_Pressure',
    'sensors:ZXC*' : 'Sensor_Current',
    'sensors:PT1*' : 'Sensor_Temperature',
    'sensors:tmp*' : 'Sensor_Temperature',
    'sensors:mma*' : 'Sensor_Motion',
    'sensors:sht1*' : 'Sensor_MultiFunction',
    'sensors:tlv*' : 'Sensor_Magnetic',
    'sensors:dht*' : 'Sensor_MultiFunction',
    'sensors:ad84*' : 'Sensor_Current',
    'sensors:c12*' : 'Sensor_Photo',
    'sensors:mpl11*' : 'Sensor_Pressure',
    'sensors:CCS811' : 'Sensors_Gas',
    'sensors:DS16*' : 'Sensor_Temperature',
    'sensors:MAX3182*' : 'Sensor_Temperature',
    'sensors:TSIC*' : 'Sensor_Temperature',

    # silabs
    'silabs:cp210*' : 'Interface_USB',

    'stm32' : 'MCU_ST_STM32',

    'stm8' : 'MCU_ST_STM8',

    # supertex
    'supertex:CL220*' : 'Driver_LED',
    'supertex:HV99*' : 'Driver_LED',
    'supertex:LR8*' : 'Regulator_Linear',

    'switches' : 'Switch',

    # texas library
    'texas:TLC5973' : 'Driver_LED',
    'texas:TPL0*' : 'Digital_Potentiometer',
    'texas:TUSB*' : 'Interface_USB',
    'texas:TS5*' : 'Analog_Switch',

    'transistors' : 'Transistor',

    'ttl_ieee' : 'Logic_TTL_IEEE',

    'valves' : 'Valve',

    'wiznet' : 'Interface_Ethernet',

    'Worldsemi' : 'LED',

    'Xicor' : 'Digital_Potentiometer',

    'zetex' : 'Driver_Gate',
}

def get_lib_name(pattern):
    return pattern.split(':')[0].lower()

def get_part_filter(pattern):

    s = pattern.split(':')

    # Match all the things!!
    if len(s) < 2:
        return '*'

    return s[1].lower()

def get_output_lib(pattern):
    return PATTERNS[pattern]

def is_entire_lib(pattern):

    """
    Determine if a library pattern designates the entire library
    """

    return get_part_filter(pattern) == '*'


def get_entire_lib_match(lib_name):

    """
    If the library is to be moved entirely,
    return the destination library.
    Otherwise, return None
    """

    lib_name = lib_name.lower()

    for pattern in PATTERNS:
        if not is_entire_lib(pattern):
            continue

        if get_lib_name(pattern) == lib_name:
            return get_output_lib(pattern)

    return None


def get_matches(lib_name, cmp_name):

    lib_name = lib_name.lower()
    cmp_name = cmp_name.lower()

    """
    Return any matches for a lib_name:cmp_name pair
    """

    matches = []

    for pattern in PATTERNS:
        if is_entire_lib(pattern):
            continue

        if not get_lib_name(pattern) == lib_name:
            continue

        part_filter = get_part_filter(pattern)

        # An exact match overrides all other filters
        if part_filter == cmp_name:
            return [part_filter]

        if fnmatch.fnmatch(cmp_name, part_filter):
            matches.append(get_output_lib(pattern))


    return matches