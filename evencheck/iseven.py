import aiohttp
import aiofiles
import asyncio
import os
import gc
import time
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def here(name):
    return os.path.join(BASE_DIR, name)

URL = "https://raw.githubusercontent.com/kleeedolinux/kleeedolinux/refs/heads/main/output.json"
LOCAL_FILE = "is_par.json"
CAKE_PT = "cake-ptbr.md"
CAKE_EN = "cake.md"

SHREK_PT_SRC = here("shreak_roteiro_ptbr.txt")
SHREK_EN_SRC = here("shreak_roteiro_en.txt")

SHREK_PT_OUT = "shrek_ptbr.md"
SHREK_EN_OUT = "shrek_en.md"

IMG_CHECK = "https://i.postimg.cc/pTJD9392/image.png"
GIF_SUCCESS = "https://i.postimg.cc/85Xznb9B/resenha-encontrada.gif"



def generate_cake_pt():
    base = """
# 🍰 Bolo de Cenoura "Brasilidade" (Chocolate + Goiabada)

## Introdução Filosófica
Este não é apenas um bolo.  
Este é um **manifesto culinário**, uma ode à cenoura cansada, ao chocolate derretido
e à goiabada que nunca pediu para estar ali — mas está.

---

## 1. O Bolo de Cenoura (Base Fofinha)

### Ingredientes
- 3 cenouras médias descascadas e picadas
- 3 ovos
- 1 xícara de óleo
- 2 xícaras de açúcar
- 2 xícaras de farinha de trigo
- 1 colher (sopa) de fermento em pó

### Modo de Preparo
Bata tudo no liquidificador até a mistura questionar sua própria existência.
Misture com farinha, açúcar e esperança.
Asse a 180°C por 40 minutos ou até sua casa cheirar como domingo.

---

## 2. A Calda de Chocolate
Chocolate não é apenas cobertura.
É um **estado de espírito**.

Misture manteiga, chocolate em pó, açúcar e leite.
Mexa até ferver e atingir o ponto filosófico de "quase grudando".

---

## 3. A Cerca de Goiabada
Aqui a goiabada vira arquitetura.
Ela não cobre. Ela delimita território.

### Opção Cerca de Vidro
Derreta a goiabada com água.
Aplique apenas nas laterais como se fosse um muro emocional.

### Opção Cubos Decorativos
Cubinhos de goiabada, levemente açucarados, cercando o bolo
como guardas imperiais da sobremesa.

---

## Dicas Avançadas
- Uma pitada de sal no chocolate muda tudo.
- Comer quente melhora decisões ruins.
- Comer frio melhora decisões piores.

---

## Considerações Finais
Este bolo não acaba.
Ele se transforma.
Ele reaparece.
Ele será reescrito.

""" * 50

    return base


def generate_cake_en():
    base = """
# 🍰 Carrot Cake "Brazilian Style" (Chocolate + Guava)

## Philosophical Introduction
This is not just a cake.
It is a **culinary manifesto**, an ode to tired carrots,
melted chocolate, and guava paste that never asked to be here.

---

## 1. The Carrot Cake (Fluffy Base)

### Ingredients
- 3 medium carrots, peeled and chopped
- 3 eggs
- 1 cup of oil
- 2 cups of sugar
- 2 cups of wheat flour
- 1 tablespoon baking powder

### Preparation
Blend everything until the mixture questions reality.
Mix with flour, sugar, and blind faith.
Bake at 180°C (350°F) for 40 minutes or until your house smells like Sunday.

---

## 2. Chocolate Sauce
Chocolate is not a topping.
It is a **life choice**.

Mix butter, cocoa powder, sugar, and milk.
Stir until boiling and reaching the emotional thickness point.

---

## 3. The Guava Fence
Guava becomes architecture.
It does not cover. It defines borders.

### Glass Fence Option
Melt guava with water.
Apply only on the sides like an emotional wall.

### Decorative Cubes Option
Small guava cubes surrounding the cake
like imperial dessert guards.

---

## Advanced Tips
- A pinch of salt changes everything.
- Eating warm improves bad decisions.
- Eating cold improves worse ones.

---

## Final Thoughts
This cake never ends.
It transforms.
It returns.
It will be rewritten.

""" * 50

    return base

async def write_shrek():
    async with aiofiles.open(SHREK_PT_SRC, "r", encoding="utf-8") as f:
        pt = await f.read()

    async with aiofiles.open(SHREK_EN_SRC, "r", encoding="utf-8") as f:
        en = await f.read()

    async with aiofiles.open(SHREK_PT_OUT, "w", encoding="utf-8") as f:
        await f.write(pt * 5)

    async with aiofiles.open(SHREK_EN_OUT, "w", encoding="utf-8") as f:
        await f.write(en * 5)

async def download(url, path):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            data = await r.read()
            async with aiofiles.open(path, "wb") as f:
                await f.write(data)

async def resenha_loop():
    while True:
        print("Averiguando resenha")
        
        await asyncio.sleep(2)

        await download(IMG_CHECK, "checking.png")

        await asyncio.sleep(2)

        success = random.choice([True, False])

        os.remove("checking.png")

        if success:
            print("Resenha encontrada com sucesso!")

            await download(GIF_SUCCESS, "resenha.gif")

            await asyncio.sleep(3)

            os.remove("resenha.gif")

        else:
            print("Ixi... Não tinha resenha infelizmente")

        await asyncio.sleep(20)


async def write_cake(path, content):
    try:
        if os.path.exists(path):
            os.remove(path)
        async with aiofiles.open(path, "w", encoding="utf-8") as f:
            for char in content:
                await f.write(char)
                await asyncio.sleep(0.0001)
    except asyncio.CancelledError:
        if os.path.exists(path):
            os.remove(path)
        raise

async def check_number(number: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            async with aiofiles.open(LOCAL_FILE, "wb") as f:
                async for chunk in response.content:
                    await f.write(chunk)

    gc.collect()

    async with aiofiles.open(LOCAL_FILE, "r", encoding="utf-8") as f:
        current_number = None
        current_even = None

        async for line in f:
            line = line.strip()
            if '"number"' in line:
                try:
                    current_number = int(line.split(":")[1].replace(",", "").strip())
                except:
                    current_number = None

            if '"even"' in line:
                current_even = "true" in line

            if "}" in line:
                if current_number == number:
                    return current_even
                current_number = None
                current_even = None
    return None

async def chaos_loop(number: int):
    task_pt = asyncio.create_task(write_cake(CAKE_PT, generate_cake_pt()))
    task_en = asyncio.create_task(write_cake(CAKE_EN, generate_cake_en()))
    task_resenha = asyncio.create_task(resenha_loop())
    task_shrek = asyncio.create_task(write_shrek())

    result = await check_number(number)

    task_pt.cancel()
    task_en.cancel()
    task_resenha.cancel()
    task_shrek.cancel()

    try:
        await asyncio.gather(task_pt, task_en, task_resenha, task_shrek)
    except asyncio.CancelledError:
        pass

    for file in [CAKE_PT, CAKE_EN, LOCAL_FILE, SHREK_PT_OUT, SHREK_EN_OUT]:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                pass

    gc.collect()
    return result

def IsEven(number: int):
    try:
        return asyncio.run(chaos_loop(number))
    except KeyboardInterrupt:
        print("\nStop!")