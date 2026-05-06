import pytest
from doc_generator import extract_functions, generate_markdown

SAMPLE_C = """
/**
 * Initialises the sensor pin.
 * Call before any read operation.
 */
void sensor_init(uint8_t pin) {
    pinMode(pin, INPUT_PULLUP);
}

/**
 * Reads digital state of the sensor.
 * Returns 1 if object detected.
 */
uint8_t sensor_read(uint8_t pin) {
    return digitalRead(pin);
}
"""

def test_extract_finds_two_functions():
    functions = extract_functions(SAMPLE_C)
    assert len(functions) == 2

def test_function_names_correct():
    functions = extract_functions(SAMPLE_C)
    names = [f['name'] for f in functions]
    assert 'sensor_init' in names
    assert 'sensor_read' in names

def test_markdown_contains_function_index():
    functions = extract_functions(SAMPLE_C)
    md = generate_markdown("test.c", functions)
    assert "Function Index" in md

def test_markdown_contains_function_names():
    functions = extract_functions(SAMPLE_C)
    md = generate_markdown("test.c", functions)
    assert "sensor_init" in md
    assert "sensor_read" in md
