import pandas as pd


class Position:
    def __init__(self, direction, entry_price, stop_loss, take_profit, risk, capital):
        self.direction = direction
        self.entry_price = entry_price
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.risk = risk
        self.reward = risk * abs(take_profit - entry_price) / abs(stop_loss - entry_price)
        self.capital = capital
        self.closed = False
        self.closing_price = None
        self.closing_time = None

    def dict(self):
        return {
            'type': self.direction,
            'entry': self.entry_price,
            'tp': self.take_profit,
            'sl': self.stop_loss,
            'risk': self.risk,
            'closed': self.closed,
            'closing_time': self.closing_time
        }

    def close(self, closing_price, timestamp):
        self.closed = True
        self.closing_price = closing_price
        self.closing_time = timestamp

    def calculate_profit(self):
        if self.direction == "buy":
            if self.closing_price >= self.take_profit:
                return self.reward * self.capital
            elif self.closing_price <= self.stop_loss:
                return -self.risk * self.capital
        elif self.direction == "sell":
            if self.closing_price <= self.take_profit:
                return self.reward * self.capital
            elif self.closing_price >= self.stop_loss:
                return -self.risk * self.capital
        return 0


class Backtest:
    def __init__(self, ticks, strategy_class):
        self.ticks = ticks
        self.strategy_class = strategy_class
        self.strategy = strategy_class
        self.open_positions = []
        self.closed_positions = []
        self.capital = 1000.0

    def buy(self, entry_price, stop_loss, take_profit, risk):
        if risk * self.capital < 1:
            raise Exception("Risked amount is lower than 1")
        if take_profit <= entry_price or stop_loss >= entry_price:
            raise Exception("Invalid stop loss or take profit for buy position")
        position = Position("buy", entry_price, stop_loss, take_profit, risk, self.capital)
        self.open_positions.append(position)

    def sell(self, entry_price, stop_loss, take_profit, risk):
        if risk * self.capital < 1:
            raise Exception("Risked amount is lower than 1")
        if take_profit >= entry_price or stop_loss <= entry_price:
            raise Exception("Invalid stop loss or take profit for sell position")
        position = Position("sell", entry_price, stop_loss, take_profit, risk, self.capital)
        self.open_positions.append(position)

    def _update_open_positions(self, tick):
        for position in self.open_positions:
            if position.closed:
                continue

            close = False

            if position.direction == 'buy' and tick['Price'] >= position.take_profit:
                close = True
            elif position.direction == 'buy' and tick['Price'] <= position.stop_loss:
                close = True
            elif position.direction == 'sell' and tick['Price'] <= position.take_profit:
                close = True
            elif position.direction == 'sell' and tick['Price'] >= position.stop_loss:
                close = True

            if close:
                position.close(tick['Price'], tick['Gmt time'])
                self.capital += position.calculate_profit()
                self.closed_positions.append(position)
                self.open_positions.remove(position)

    def run(self):
        for tick in self.ticks:
            self.strategy.process_tick(tick, self.buy, self.sell)
            self._update_open_positions(tick)

        return {
            'score': self.capital,
            'open_positions': [pos.dict() for pos in self.open_positions],
            'closed_positions': [pos.dict() for pos in self.closed_positions]
        }
