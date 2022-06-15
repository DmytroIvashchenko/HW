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


# answer = input('Would you like to use the currency exchange service? Y/N')
course = rate_output(input('What currency do you choose? USD or UAH'))
print(course)


answer = input('Would you like to use the currency exchange service? Y/N')


while answer == 'Y' or answer == 'N':
    while answer == 'Y':
        exchange = input('What currency do you want to exchange? UAH to USD or USD to UAH ')
        if exchange == 'USD to UAH':
            sell_dollars = int(input('How many dollars do you want to sell? '))
            trade = sell_dollars * current_currency_dollar_uah
            if trade < uah_balance:
                usd_balance = usd_balance - sell_dollars
                uah_balance = uah_balance + trade
                print(f'EXCHANGE USD {sell_dollars}\nUAH {trade}, RATE {current_currency_dollar_uah}')
                print(f'USD BALANCE - {usd_balance}, UAH BALANCE - {uah_balance}')
                answer = input('Would you like to use the currency exchange service? Y/N')
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE UAH {trade}, BALANCE is {uah_balance}')
                answer = input('Would you like to use the currency exchange service? Y/N')
        if exchange == 'UAH to USD':
            sell_uah = int(input('How many dollars do you want to buy? '))
            trade = sell_uah * current_currency_uah_dollar
            if trade < usd_balance:
                usd_balance = usd_balance + sell_uah
                uah_balance = uah_balance - trade
                print(f'EXCHANGE UAH {sell_uah} \nUAH {trade}, RATE {current_currency_uah_dollar}')
                print(f'USD BALANCE - {usd_balance}, UAH BALANCE - {uah_balance}')
                answer = input('Would you like to use the currency exchange service? Y/N')
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE USD {usd_balance}, BALANCE is {trade}')
                answer = input('Would you like to use the currency exchange service? Y/N')
    if answer == 'N':
        print('STOP \nSERVICE STOPPED')
    break
else:
    print('Incorrect answer')
    answer = input('Would you like to use the currency exchange service? Y/N')
