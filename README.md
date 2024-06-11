# QUIC Protocol Implementation

This project implements the QUIC (Quick UDP Internet Connections) protocol using Python. QUIC is a new transport protocol that provides multiplexed connections between two endpoints over UDP. This implementation includes a server and a client, and it leverages several dependencies to handle various aspects of the protocol.

## Video Demo

[![QUIC Protocol Implementation Demo([http://img.youtube.com/vi/VIDEO_ID_HERE/0.jpg)](https://github.com/PrayujaTeli/Chat-Protocol/blob/60c073c175a41b7f9239dd9496083c644b84e7c4/Chat-Protocol-Demo.mp4)]

## Features

- **Client-Server Communication**: Implements basic QUIC client and server communication.
- **Security**: Utilizes TLS for encryption to secure communication.
- **Performance**: Efficient handling of connections and data transfer using asynchronous I/O.

## Prerequisites

Make sure you have Python 3.8 or higher installed on your machine.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/quic-protocol.git
    cd quic-protocol
    ```

2. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the server:**

    ```sh
    python3 main.py server
    ```

2. **Run the client:**

    ```sh
    python3 main.py client
    ```

## Project Structure

- **client.py**: Contains the client-side implementation of the QUIC protocol.
- **main.py**: Entry point for running the server and client.
- **pdu.py**: Handles Protocol Data Units (PDU) for the QUIC protocol.
- **quic_engine.py**: Core logic for the QUIC protocol implementation.
- **quic.py**: Additional support for the QUIC protocol.
- **server.py**: Contains the server-side implementation of the QUIC protocol.

## Requirements

The project relies on several Python packages, which are listed in the `requirements.txt` file:

- aioquic==1.0.0
- asyncio==3.4.3
- attrs==23.2.0
- certifi==2024.2.2
- cffi==1.16.0
- cryptography==42.0.5
- dnslib==0.9.24
- pyasn1==0.5.1
- pyasn1-modules==0.3.0
- pycparser==2.21
- pylsqpack==0.3.18
- pyOpenSSL==24.1.0
- service-identity==24.1.0

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
