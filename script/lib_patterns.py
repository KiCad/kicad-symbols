import fnmatch

PATTERNS = {

    ###
    # These patterns are used to reorganize the KiCad libraries
    # Filters are not case sensitive
    #

    ###
    # The following filters are used to rename an entire library
    ###

    'microchip_pic10mcu' : 'mcu_microchip_pic10',
    'microchip_pic12mcu' : 'mcu_microchip_pic12',
    'microchip_pic16mcu' : 'mcu_microchip_pic16',
    'microchip_pic18mcu' : 'mcu_microchip_pic18',
    'microchip_pic24mcu' : 'mcu_microchip_pic24',
    'microchip_pic32mcu' : 'mcu_microchip_pic32',

    'microchip_dspic33dsc' : 'dsp_microchip_dspic33',

    'stm32' : 'mcu_st_stm32',
    'stm8' : 'mcu_st_stm8',

    'nxp_armmcu' : 'mcu_nxp_lpc',

    'power' : 'power',

    'motors' : 'motor',

    'nordicsemi' : 'interface_bluetooth',

    'RFSolutions' : 'interface_rf',

    'wiznet' : 'interface_ethernet',

    # Gate Drivers
    'zetex' : 'driver_gate',
    'driver_gate' : 'driver_gate',

    ###
    # The following filters are used to separate symbols out from various libraries
    ###

    # adc-dac library
    'adc-dac:mcp4801*' : 'analog_dac',
    'adc-dac:mcp355*' : 'analog_adc',

    # sensors library
    'sensors:40pc*' : 'sensor_pressure',
    'sensors:a110*' : 'sensor_magnetic',
    'sensors:a130*' : 'sensor_magnetic',
    'sensors:ad8148' : 'sensor_current',
    'sensors:AS50*' : 'sensor_magnetic',
    'sensors:BD*' : 'sensor_temperature',
    'sensors:BMP*' : 'sensor_pressure',
    'sensors:Flir*' : 'sensor_photo',
    'sensors:INA*' : 'sensor_current',
    'sensors:KT*' : 'sensor_temperature',
    'sensors:L3*' : 'sensor_motion',
    'sensors:LG*' : 'sensor_motion',
    'sensors:LA*' : 'sensor_current',
    'sensors:LIS*' : 'sensor_motion',
    'sensors:LM35*' : 'sensor_temperature',
    'sensors:LM73*' : 'sensor_temperature',
    'sensors:LMT8*' : 'sensor_temperature',
    'sensors:LPS*' : 'sensor_pressure',
    'sensors:LSM*' : 'sensor_motion',
    'sensors:LV*' : 'sensor_voltage',
    'sensors:MCP950*' : 'sensor_temperature',
    'sensors:MCP970*' : 'sensor_temperature',
    'sensors:MCP980*' : 'sensor_temperature',
    'sensors:MP45D*' : 'sensor_audio',
    'sensors:MPU-*' : 'sensor_motion',
    'sensors:MPX*' : 'sensor_pressure',
    'sensors:ZXC*' : 'sensor_current',
    'sensors:PT1*' : 'sensor_temperature',
    'sensors:tmp*' : 'sensor_temperature',
    'sensors:mma*' : 'sensor_motion',
    'sensors:sht1*' : 'sensor_multi_function',
    'sensors:tlv*' : 'sensor_magnetic',
    'sensors:dht*' : 'sensor_mult_function',
    'sensors:ad84*' : 'sensor_current',
    'sensors:c12*' : 'sensor_photo',
    'sensors:mpl11*' : 'sensor_pressure',

    # rfcom library
    'rfcom:B*' : 'interface_bluetooth',
    'rfcom:CC1*' : 'interface_rf',
    'rfcom:CC2*' : 'interface_zigbee',
    'rfcom:DCT*' : 'interface_rf',
    'rfcom:HF-*' : 'interface_wifi',
    'rfcom:MM*' : 'interace_rf',
    'rfcom:NRF*' : 'interface_rf',
    'rfcom:RN*' : 'interface_bluetooth',
    'rfcom:RXM*' : 'interface_gps',

    # interface library
    'interface:ADM*' : 'interface_uart',
    'interface:CH376T' : 'memory_controller',
    'interface:FUSB*' : 'interface_usb',
    'interface:GD*' : 'interface_uart',
    'interface:LT1080' : 'interface_uart',
    'interface:LTC2875*' : 'interface_can_lin',
    'interface:ltc2983' : 'sensor_temperature',
    'interface:ltc2990' : 'sensor_mult_function',
    'interface:max134*' : 'interface_uart',
    'interface:max2*' : 'interface_uart',
    'interface:max30*' : 'interface_uart',
    'interface:MAX318*' : 'sensor_temperature',
    'interface:max32*' : 'interface_uart',
    'interface:mcp25*' : 'interface_can_lin',
    'interface:mcp4*' : 'digital_potentiometer',
    'interface:SN65*' : 'interface_can_lin',
    'interface:sp34*' : 'interface_uart',
    'interface_tca94*' : 'interface_i2c',
    'interface:tja1*' : 'interface_can_lin',
    'interface:xtr*' : 'interface_current_loop',

    # intersil library
    'intersil:EL7*' : 'driver_gate',
    'intersil:HIP*' : 'driver_gate',

    # microchip
    'microchip:enc*' : 'interface_ethernet',
    'microchip:KSZ*' : 'interface_ethernet',
    'microchip:LAN*' : 'interface_ethernet',
    'microchip:mcp2050*' : 'interface_can_lin',
    'microchip:mcp2515*' : 'interface_can_lin',
    'microchip:mic*' : 'driver_gate',
    'microchip:usb*' : 'interface_usb',

    # motor_drivers library
    'motor_drivers:STK*' : 'driver_motor',
    'motor_drivers:STSPIN*' : 'driver_motor',
    'motor_drivers:TMC*' : 'driver_motor',
    'motor_drivers:SLA*' : 'driver_motor',
    'motor_drivers:l29*' : 'driver_motor',
    'motor_drivers:drv*' : 'driver_motor',
    'motor_drivers:A495*' : 'driver_motor',

    # nxp library
    'nxp:pca9*' : 'driver_led',

    # philips
    'philips:p8*' : 'interface_i2c',
    'philips:pca8*' : 'interface_can_lin',
    'philips:pca9*' : 'interface_i2c',


    # texas library
    'texas:TLC5973' : 'driver_led',
    'texas:TPL0*' : 'digital_potentiometer',
    'texas:TUSB*' : 'interface_usb',
    'texas:TS5*' : 'analog_switch',

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