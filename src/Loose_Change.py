def loose_change(cents):
    cents = int(cents)
    monedas = {
        "Pennies": 0,
        "Nickels": 0,
        "Dimes": 0,
        "Quarters": 0,
    }

    if cents <= 0:
        return monedas
    else:
        monedas["Quarters"] = cents // 25
        cents = cents % 25
        monedas["Dimes"] = cents // 10
        cents = cents % 10
        monedas["Nickels"] = cents // 5
        cents = cents % 5
        monedas["Pennies"] = cents // 1

    return monedas

if __name__ == "__main__":
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(1) == {'Nickels': 0, 'Pennies': 1, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(5) == {'Nickels': 1, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(10) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 1, 'Quarters': 0}
  

