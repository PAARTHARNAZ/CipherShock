# CipherShock

CipherShock is a tool designed to showcase the avalanche effect in cryptographic algorithms. This project includes two Python scripts that demonstrate the effect using DES and AES encryption algorithms.

## Features

- **DES Avalanche Effect**: Visualize the avalanche effect using the DES encryption algorithm.
- **AES Avalanche Effect**: Visualize the avalanche effect using the AES encryption algorithm.

## Prerequisites

Ensure you have Python installed on your system. Additionally, you will need the `pycryptodome` library for cryptographic operations. Install it using the following command:

```sh
pip install pycryptodome
```

## Usage

### DES Avalanche Effect

The `DES_avalanche.py` script demonstrates the avalanche effect using the DES encryption algorithm.

#### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `DES_avalanche.py`.
3. Run the script using Python:

```sh
python DES_avalanche.py
```

### AES Avalanche Effect

The `AES_avalanche.py` script demonstrates the avalanche effect using the AES encryption algorithm.

#### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `AES_avalanche.py`.
3. Run the script using Python:

```sh
python AES_avalanche.py
```

## Understanding the Avalanche Effect

The avalanche effect is a desirable property of cryptographic algorithms, where a small change in the input (such as flipping a single bit) results in a significant change in the output. This ensures that the output is highly sensitive to changes in the input, enhancing security.

## Example Output

When you run the scripts, you will see outputs that highlight the differences in the encrypted results when minor changes are made to the plaintext or key. These differences are quantified and displayed, demonstrating the avalanche effect.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and ensure you understand the underlying cryptographic principles.

## Authors

- **[PAARTHARNAZ](https://github.com/PAARTHARNAZ)**

---

Unleashing the chaos in cryptography to secure your data.
