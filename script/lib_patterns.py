import fnmatch

PATTERNS = {

    ###
    # These patterns are used to reorganize the KiCad libraries
    # Filters are not case sensitive
    #

    # adc-dac library
    'adc-dac:mcp4801*' : 'Analog_DAC',
    'adc-dac:mcp355*' : 'Analog_ADC',

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

    'Driver_Gate' : 'Driver_Gate',

    'ftdi' : 'Interface_USB',

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
    'microchip_PIC10mcu' : 'MCU_Microchip_PIC10',
    'microchip_PIC12mcu' : 'MCU_Microchip_PIC12',
    'microchip_PIC16mcu' : 'MCU_Microchip_PIC16',
    'microchip_PIC18mcu' : 'MCU_Microchip_PIC18',
    'microchip_PIC24mcu' : 'MCU_Microchip_PIC24',
    'microchip_PIC32mcu' : 'MCU_Microchip_PIC32',

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
    'Power_Management:FAN7842' : 'Driver_Gate',
    'Power_Management:LM50*' : 'Power_Distribution',
    'Power_Management:LT1641*' : 'Power_Distribution',
    'Power_Management:LTC435*' : 'Power_Distribution',
    'Power_Management:LTC4364*' : 'Power_Distribution',
    'Power_Management:LTC4365*' : 'Power_Distribution',
    'Power_Management:MCP100*' : 'Power_Supervisor',
    'Power_Management:TCM8*' : 'Power_Supervisor',
    'Power_Management:MCP10*' : 'Power_Supervisor',
    'Power_Management:LTC444*' : 'Driver_Gate',
    'Power_Management:PM8*' : 'Driver_Gate',
    'Power_Management:MIC8*' : 'Power_Supervisor',
    'Power_Management:MIC2587*' : 'Power_Distribution',
    'Power_Management:MIC2026*' : 'Power_Distribution',

    # power int

    # rfcom library
    'rfcom:B*' : 'Interface_Bluetooth',
    'rfcom:CC1*' : 'Interface_RF',
    'rfcom:CC2*' : 'Interface_zigbee',
    'rfcom:DCT*' : 'Interface_RF',
    'rfcom:HF-*' : 'Interface_WiFi',
    'rfcom:MM*' : 'Interface_RF',
    'rfcom:NRF*' : 'Interface_RF',
    'rfcom:RN*' : 'Interface_Bluetooth',
    'rfcom:RXM*' : 'Interface_GPS',

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

    # silabs
    'silabs:cp210*' : 'Interface_USB',

    'stm32' : 'MCU_ST_STM32',

    'stm8' : 'MCU_ST_STM8',

    # supertex
    'supertex:CL220*' : 'Driver_LED',
    'supertex:HV99*' : 'Driver_LED',
    'supertex:LR8*' : 'Regulator_Linear',

    # texas library
    'texas:TLC5973' : 'Driver_LED',
    'texas:TPL0*' : 'Digital_Potentiometer',
    'texas:TUSB*' : 'Interface_USB',
    'texas:TS5*' : 'Analog_Switch',

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