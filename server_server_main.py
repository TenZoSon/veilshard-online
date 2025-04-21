# server/server_main.py

import asyncio

clients = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"New player connected from {addr}")
    clients.append(writer)
    writer.write("Welcome to Veilshard Online!\n".encode())
    await writer.drain()

    try:
        while True:
            data = await reader.readline()
            message = data.decode().strip()
            if message.lower() == "quit":
                writer.write("Goodbye!\n".encode())
                await writer.drain()
                break
            else:
                for c in clients:
                    if c != writer:
                        c.write(f"[{addr}]: {message}\n".encode())
                        await c.drain()
    except:
        pass
    print(f"{addr} disconnected.")
    clients.remove(writer)
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    async with server:
        print("Veilshard Server running on port 8888...")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

# client/client_interface.py

import asyncio

async def main():
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    print("Connected to Veilshard Server. Type 'quit' to exit.")
    asyncio.create_task(read_from_server(reader))

    while True:
        message = input("> ")
        writer.write((message + "\n").encode())
        await writer.drain()
        if message == "quit":
            break

    writer.close()
    await writer.wait_closed()

async def read_from_server(reader):
    while True:
        data = await reader.readline()
        if not data:
            break
        print(data.decode().strip())

if __name__ == "__main__":
    asyncio.run(main())

# ai/npc_memory/dialogue_engine.py

class NPC:
    def __init__(self, name, memory=None):
        self.name = name
        self.memory = memory or {}
        self.personality = "guarded"

    def speak(self, player_name):
        if "betrayed" in self.memory.get(player_name, []):
            return f"{self.name} narrows their eyes. 'You've done enough, {player_name}...'"
        elif "gifted" in self.memory.get(player_name, []):
            return f"{self.name} smiles faintly. 'You're kind. I remember.'"
        else:
            return f"{self.name} watches you silently, unsure what to say."

    def update_memory(self, player_name, flag):
        if player_name not in self.memory:
            self.memory[player_name] = []
        self.memory[player_name].append(flag)


# gm/tools/gm_terminal.py

def inject_zone(name, description, connections=None, items=None):
    print(f"[GM] Injecting new zone: {name}")
    zone_data = {
        "description": description,
        "exits": connections or {},
        "items": items or []
    }
    print(f"[ZONE CREATED] {zone_data}")
    return zone_data

def trigger_event(name, effect):
    print(f"[GM EVENT] Triggered event: {name}")
    print(f"[EFFECT]: {effect}")

// data/npcs/npc_memory_example.json
{
  "npc_id": "warden_zhyra",
  "personality": "guarded",
  "memory": {
    "TestPlayer": ["gifted", "betrayed"]
  }
}

#!/bin/bash
echo "Launching Veilshard Server..."
python3 server/server_main.py


