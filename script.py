from hdwallet import BIP44HDWallet
from hdwallet.utils import generate_mnemonic
from typing import Optional


def generate_address(address_count, seed_count):
    # Generate english mnemonic words
    for i in range(address_count):
        strength = 128
        match seed_count:
            case 12:
                strength = 128
            case 18:
                strength = 192
            case 24:
                strength = 256

        MNEMONIC: str = generate_mnemonic(language="english", strength=strength)
        PASSPHRASE: Optional[str] = None

        # Initialize BIP44HDWallet
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet()


        # Get BIP44HDWallet from mnemonic
        bip44_hdwallet.from_mnemonic(
            mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
        )

        bip44_hdwallet.clean_derivation()

        print("Mnemonic:", bip44_hdwallet.mnemonic())

        PATH: str = "m/44'/242'/0'/0'"

        # Apply custom derivation path
        bip44_hdwallet.from_path(PATH)

        print(f"Address: {bip44_hdwallet.address()} \nPrivate Key: {bip44_hdwallet.private_key()} \n")
        output = f"{bip44_hdwallet.address()} : {bip44_hdwallet.private_key()} : {bip44_hdwallet.mnemonic()} \n"

        # Write each line to the file
        with open("BTC.txt", "a") as file:
            file.write(output)


def main():
    try:
        address_count = int(input("Введите количество адресов: "))
        seed_count = int(input("Введите количество слов в seed фразе (12, 18, или 24): "))

        if seed_count not in (12, 18, 24):
            print("Количество слов в seed фразе должно быть 12, 18 или 24.")
            return

        generate_address(address_count, seed_count)
        print('Результат сохранен в файл NIMIQ.txt')
    except ValueError:
        print("Ошибка: Введите целое число для количества адресов и количество слов в seed фразе.")


if __name__ == "__main__":
    main()
