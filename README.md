# Testing Hackerrank Problems

## Creator

**NUTTASIT TINMAS 6610110096**


## Test Results

```
----------------------------------------------------------------------
Ran 46 tests in 0.004s

OK
Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
case/alter_char/alternating_char_utils.py         6      0   100%
case/caesar_cipher/caesar_cipher_utils.py         8      0   100%
case/funny_string/funny_string_utils.py           7      0   100%
case/grid_challenge/grid_challenge_utils.py       8      0   100%
case/two_char/two_char_utils.py                  12      0   100%
test/test_alter_char.py                          43      0   100%
test/test_caesar_cipher.py                       23      0   100%
test/test_funny_string.py                        23      0   100%
test/test_grid_challenge.py                      24      0   100%
test/test_two_char.py                            21      0   100%
-----------------------------------------------------------------
TOTAL                                           175      0   100%
```
## File Structure

```
tree
.
├── case
│   ├── alter_char
│   │   └── alternating_char_utils.py
│   ├── caesar_cipher
│   │   └── caesar_cipher_utils.py
│   ├── funny_string
│   │   └── funny_string_utils.py
│   ├── grid_challenge
│   │   └── grid_challenge_utils.py
│   └── two_char
│       └── two_char_utils.py
├── README.md
└── test
    ├── test_alter_char.py
    ├── test_caesar_cipher.py
    ├── test_funny_string.py
    ├── test_grid_challenge.py
    └── test_two_char.py

8 directories, 11 files
```
## Description

The `case` directory contains implementations of different problem-solving scenarios, including algorithms for alternating characters, Caesar cipher, funny strings, grid challenges, and two characters. Each subdirectory under `case` corresponds to a specific problem.

The `test` directory contains test scripts for each implemented algorithm. These tests ensure that the implementations are correct and functioning as expected.

## Installation

**Windows:**

    pip install coverage nose2

**Linux:**

    pip install coverage nose2

## Run Testing

**- Change to project directory**


**Linux:**

    python3 -m unittest -v tests/test_name.py

**OSX:**

    python -m unittest -v tests/test_name.py

**Windows:**

    python -m unittest -v tests/test_name.py

## Run nose2

 

    nose2 -v --with-coverage

or

    nose2 -v --with-coverage --coverage-report html

or

    nose2 -v –with-coverage --coverage <package_name>

## Creator

**NUTTASIT TINMAS 6610110096**