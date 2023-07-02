# All-in-One Fuzzer

This repository contains Python scripts for network protocol fuzzing using Sulley and HTTP Basic fuzzing using the `http.py` script.

## Prerequisites

- Sulley library (installation instructions)
- Python 3.x

## Usage

1. Clone the repository:

```shell
git clone https://github.com/your-username/your-repo.git
```

2. Install Sulley library:

```shell
pip install sulley
```

### Fuzzing with Sulley

1. Open the `sulley_fuzzer.py` script.

2. Get user input for the target IP address and port.

3. Run the script:

```shell
python sulley_fuzzer.py
```

### HTTP Basic Fuzzing

1. Open the `http.py` script.

2. Get user input for the target IP address and port.

3. Run the script:

```shell
python http.py
```

## Configuration

### Sulley Fuzzer

- Modify the target IP address and port in the `sulley_fuzzer.py` script to specify the target.

### HTTP Basic Fuzzing

- Modify the target IP address and port in the `http.py` script to specify the target.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
