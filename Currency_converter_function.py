import sys

from Exchange_Rate_and_Balance import current_currency_dollar_uah, current_currency_uah_dollar, \
    usd_balance, uah_balance


def rate_output(currency):
    if currency == 'USD':
        currency = f'1 USD to UAH: {current_currency_dollar_uah}, USD BALANCE is {usd_balance}'
        return currency
    elif currency == 'UAH':
        currency = f'1 UAH to USD: {current_currency_uah_dollar}, UAH BALANCE is {uah_balance}'
        return currency
    else:
        print(f'Sorry, we do not exchange this {currency}.\nBye', )
        return sys.exit()


def exchange_currency_usd_uah(current_currency_dollar_uah, usd_balance, uah_balance):
    sell_dollars = int(input('How many dollars do you want to sell? '))
    trade = sell_dollars * current_currency_dollar_uah
    if trade < uah_balance:
        usd_balance = usd_balance - sell_dollars
        uah_balance = uah_balance + trade
        print(f'EXCHANGE USD {sell_dollars}'
              f'UAH {trade}, RATE {current_currency_dollar_uah}')
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE UAH {trade}, BALANCE is {uah_balance}')


def exchange_currency_uah_usd(current_currency_uah_dollar, usd_balance, uah_balance):
    sell_uah = int(input('How many dollars do you want to buy? '))
    trade = sell_uah * current_currency_uah_dollar
    if trade < usd_balance:
        usd_balance = usd_balance + sell_uah
        uah_balance = uah_balance - trade
        print(f'EXCHANGE UAH {sell_uah}'
              f'UAH {trade}, RATE {current_currency_uah_dollar}')
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE USD {usd_balance}, BALANCE is {trade}')


course = rate_output(input('What currency do you choose? USD or UAH'))
print(course)
answer = input('Would you like to use the currency exchange service? Y/N')
while answer == 'Y' or answer == 'N':
    while answer == 'Y':
        exchange_currency = (input('What currency do you want to exchange? '
                                   '\nUAH to USD or USD to UAH '))
        if exchange_currency == 'USD to UAH':
            exchange_currency_usd_uah(current_currency_dollar_uah, usd_balance, uah_balance)
            print(course)
            answer = input('Would you like to use the currency exchange service? Y/N')
        elif exchange_currency == 'UAH to USD':
            exchange_currency_uah_usd(current_currency_uah_dollar, usd_balance, uah_balance)
            print(course)
            answer = input('Would you like to use the currency exchange service? Y/N')
        else:
            print('Incorrect exchange')
    if answer == 'N':
        print('STOP \nSERVICE STOPPED')
        break
    else:
        print('Incorrect answer')
