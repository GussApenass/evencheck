import aiohttp
import aiofiles
import asyncio
import os

URL = "https://raw.githubusercontent.com/kleeedolinux/kleeedolinux/refs/heads/main/output.json"
LOCAL_FILE = "is_par.json"


async def check_number(number: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            async with aiofiles.open(LOCAL_FILE, "w", encoding="utf-8") as f:
                async for chunk in response.content:
                    await f.write(chunk.decode())

    async with aiofiles.open(LOCAL_FILE, "r", encoding="utf-8") as f:
        current_number = None
        current_even = None

        async for line in f:
            line = line.strip()

            if '"number"' in line:
                try:
                    current_number = int(
                        line.split(":")[1].replace(",", "").strip()
                    )
                except:
                    current_number = None

            if '"even"' in line:
                if "true" in line:
                    current_even = True
                elif "false" in line:
                    current_even = False

            if "}" in line:
                if current_number == number:
                    result = current_even

                    try:
                        os.remove(LOCAL_FILE)
                    except:
                        pass

                    return result

                current_number = None
                current_even = None

    try:
        os.remove(LOCAL_FILE)
    except:
        pass

    return None


def IsEven(number: int):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop is None:
        return asyncio.run(check_number(number))

    return loop.run_until_complete(check_number(number))