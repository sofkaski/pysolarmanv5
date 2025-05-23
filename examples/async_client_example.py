"""A basic client demonstrating how to use the async version of pysolarmanv5."""

from pysolarmanv5 import PySolarmanV5Async
import asyncio


async def main():
    """Create new PySolarman instance, using IP address and S/N of data logger

    Only IP address and S/N of data logger are mandatory parameters. If port,
    mb_slave_id, and verbose are omitted, they will default to 8899, 1 and 0
    respectively.
    """
    modbus = PySolarmanV5Async(
        "192.168.1.121",
        1234567890,
        port=8899,
        mb_slave_id=1,
        verbose=False,
        auto_reconnect=True,
    )
    await modbus.connect()

    """Query six input registers, results as a list"""
    print(await modbus.read_input_registers(register_addr=33022, quantity=6))

    """Query six holding registers, results as list"""
    print(await modbus.read_holding_registers(register_addr=60, quantity=6))

    """Query single input register, result as an int"""
    print(await modbus.read_input_register_formatted(register_addr=33035, quantity=1))

    """Query single input register, apply scaling, result as a float"""

    print(
        await modbus.read_input_register_formatted(
            register_addr=33035, quantity=1, scale=0.1
        )
    )

    """Query two input registers, shift first register up by 16 bits, result as a signed int, """
    print(
        await modbus.read_input_register_formatted(
            register_addr=33079, quantity=2, signed=1
        )
    )

    """Query single holding register, apply bitmask and bitshift left (extract bit1 from register)"""
    print(
        await modbus.read_holding_register_formatted(
            register_addr=500, quantity=1, bitmask=0x2, bitshift=1
        )
    )

    await modbus.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
