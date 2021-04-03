class Itens:

    # itens que se usam na batalha
    @property
    def dire_hit(self):
        # Raises the critical-hit ratio of Pokémon in battle. Wears off if the Pokémon is withdrawn
        return [0, "Dire Hit"]
    @property
    def guard_spec(self):
        # An item that prevents stat reduction among party Pokémon for five turns after use.
        return [1, "Guard Spec"]
    @property
    def x_accuracy(self):
        # Raises the accuracy stat of Pokémon in battle. Wears off if the Pokémon is withdrawn.
        return [2, "X Accuracy"]
    @property
    def x_attack(self):
        # Raises the ATTACK stat of Pokémon in battle. Wears off if the Pokémon is withdrawn.
        return [3, "X Attack"]
    @property
    def x_defense(self):
        # Raises the DEFENSE stat of Pokémon in battle. Wears off if the Pokémon is withdrawn.
        return [4, "X Defense"]
    @property
    def x_special(self):
        # Raises the SP. ATK stat of Pokémon in battle. Wears off if the Pokémon is withdrawn.
        return [5, "X Special"]
    @property
    def x_speed(self):
        # Raises the SPEED stat of Pokémon in battle. Wears off if the Pokémon is withdrawn.
        return [6, "X Speed"]


    # alimentos:

    @property
    def berry_juice(self):
        # A 100% pure juice. It restores the HP of one Pokémon by 20 points.
        return [-1, "Berry Juice"]
    @property
    def elixir(self):
        # Restores the PP of all moves for one Pokémon by 10 points each.
        return [-2, "Elixir"]
    @property
    def potion(self):
        # A spray-type wound medicine. It restores the HP of one Pokémon by 20 points.
        return [-3, "Potion"]