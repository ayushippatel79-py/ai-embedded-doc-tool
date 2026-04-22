/**
 * Initialises the light sensor GPIO pin and sets pull-up resistor.
 * Must be called before any sensor read operations.
 */
void sensor_init(uint8_t pin) {
    pinMode(pin, INPUT_PULLUP);
}

/**
 * Reads the current digital state of the light sensor.
 * Returns 1 if object detected, 0 otherwise.
 */
uint8_t sensor_read(uint8_t pin) {
    return digitalRead(pin);
}

/**
 * Applies debounce logic to sensor input over a configurable window.
 * Prevents false triggers from electrical noise or vibration.
 */
uint8_t sensor_debounce(uint8_t pin, uint16_t delay_ms) {
    uint8_t state1 = sensor_read(pin);
    delay(delay_ms);
    uint8_t state2 = sensor_read(pin);
    return (state1 == state2) ? state1 : 0;
}
