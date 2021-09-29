from portfolio.models import Portfolio
from investment.models import Investment



def builder(history, name=''):
    """
    in:
        - history: a number of transactions (list of lists)
        - name: name of portfolio (string)

    example: 
        - builder([['2020-10-21 10:35', 'Buy stocks', 30, 1000, 'Vodafone Group PLC'],['2020-10-21 10:40', 'Buy stocks', 100, 3000, 'SAMSUNG'],], 'prueba')

    """

    try:
        portfolio = Portfolio.objects.get(name=name)
    except Exception as e:
        portfolio = None

    if not portfolio:
        try:
            portfolio = Portfolio.objects.create(name=name, value=0)
        except Exception as e:
            if 'unique constraint' in e.message:
                return '[!] The name of the portfolio is on use.'
            else:
                return '[!] Error: {}'.format(e)

    portfolio.save()

    for transaction in history:
        try:
            investment = Investment.objects.get(invested_by=portfolio, name=transaction[4])
            print(investment.name)
        except Exception:
            investment = None
            
        # Aumentamos o reducimos el volumen total del stock
        if investment:
            if transaction[1] == 'Sell stocks':
                investment.volume -= transaction[2]
                investment.save()
            else:
                investment.volume += transaction[2]
                investment.save()

        else:
            investment = Investment.objects.create(
                name=transaction[4],
                invested_by=portfolio,
                volume=transaction[2],
                current_price=0,
                profit=0,
            )
        if transaction[1] == 'Buy stocks':
            investment.profit += calculate_profit(portfolio, investment.current_price, transaction[2], transaction[3])
        else:
            investment.profit -= calculate_profit(portfolio, investment.current_price, transaction[2], transaction[3])
        investment.current_price = transaction[3]
        investment.save()

    calculate_value(portfolio)

    return '[*] Success !'


def calculate_value(portfolio):

    investments = Investment.objects.all().filter(invested_by=portfolio)
    for investment in investments:
        portfolio.value += investment.current_price * investment.volume
        portfolio.save()


def calculate_profit(portfolio, current_price, volume, purchase_price):
    
    total = volume * (current_price - purchase_price)
    print(str(total) + " = " + str(volume) + " * (" + str(current_price) + " - " + str(purchase_price) + ")")
    return abs(total)

        
# ------------------------------------------------------------------------------------------------------