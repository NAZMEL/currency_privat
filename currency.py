import requests
from config import api_link

def get_currency():
    privatbank = requests.get(api_link)
    data = privatbank.json()
    return data

def get_all_currency():
    data = get_currency()

    text = ''

    for item in data:
        text += f'💴 {item["base_ccy"]} - {item["ccy"]}💵\n'
        text += f'buying: {round(float(item["buy"]), 2)}\n'
        text += f'selling: {round(float(item["sale"]), 2)}\n\n'

    return text

def get_usd_currency():
    usd = get_currency()[0]

    text = f'💴 {usd["base_ccy"]} - {usd["ccy"]}💵\n'
    text += f'buying: {round(float(usd["buy"]), 2)}\n'
    text += f'selling: {round(float(usd["sale"]), 2)}\n\n'

    return text

def get_eur_currency():
    eur = get_currency()[1]

    text = f'💴 {eur["base_ccy"]} - {eur["ccy"]}💵\n'
    text += f'buying: {round(float(eur["buy"]), 2)}\n'
    text += f'selling: {round(float(eur["sale"]), 2)}\n\n'

    return text

def get_rur_currency():
    rur = get_currency()[2]

    text = f'💴 {rur["base_ccy"]} - {rur["ccy"]}💵\n'
    text += f'buying: {round(float(rur["buy"]), 2)}\n'
    text += f'selling: {round(float(rur["sale"]), 2)}\n\n'

    return text

def get_btc_currency():
    btc = get_currency()[3]

    text = f'💴 {btc["base_ccy"]} - {btc["ccy"]}💵\n'
    text += f'buying: {round(float(btc["buy"]), 2)}\n'
    text += f'selling: {round(float(btc["sale"]), 2)}\n\n'

    return text


def calculate(value = 0, index_option = 'buy', currency_type = 'USD'):
    if index_option == 'buy':
        if currency_type == 'USD':
            usd = get_currency()[0] 
            return value * round(float(usd["sale"]), 2)
        elif currency_type == 'EUR':
            eur = get_currency()[1]
            return value * round(float(eur["sale"]), 2)
        elif currency_type == 'RUR':
            rur = get_currency()[2]
            return value * round(float(rur["sale"]), 2)
        elif currency_type == 'BTC':
            btc = get_currency()[3]
            return value * round(float(btc["sale"]), 2)

    elif index_option == 'sell':
        if currency_type == 'USD':
            usd = get_currency()[0] 
            return value * round(float(usd["buy"]), 2)
        elif currency_type == 'EUR':
            eur = get_currency()[1]
            return value * round(float(eur["buy"]), 2)
        elif currency_type == 'RUR':
            rur = get_currency()[2]
            return value * round(float(rur["buy"]), 2)
        elif currency_type == 'BTC':
            btc = get_currency()[3]
            return value * round(float(btc["buy"]), 2)

 


if __name__ == '__main__':
    print(get_usd_currency())
