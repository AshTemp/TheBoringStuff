import random

choice = input('Use the number to select the correct language [1.English - 2.Spanish - 3.French :')
choice = int(choice)

if choice == 1:

    print('Hello and welcome to the rock, paper, scissors game! \n')

    prompt_error = ('You did not select from the allowed options!')
    game_is_active = True

    while game_is_active:
        options = ('rock', 'paper', 'scissors')

        player_choice = input('Did you throw rock, paper, or scissors? ')
        computer_choice = options[random.randint(0, 2)]

        # Players must choose a correct option!
        while player_choice not in options:
            print(prompt_error)
            player_choice = input('Did you throw rock, paper, or scissors? ')

        # What did the players select?
        print('The player\'s choice is', player_choice)
        print('The computer\'s choice is', computer_choice)

        if player_choice == computer_choice:
            print('\n~Tie Game!~\n')

        elif player_choice == 'rock':
            if computer_choice == 'paper':
                print('\n ~Computer Wins!~\n')
            elif computer_choice == 'scissors':
                print('\n ~Player Wins!~\n')

        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                print('\n ~Player Wins!~\n')
            elif computer_choice == 'rock':
                print('\n ~Computer Wins!~\n')

        elif player_choice == 'paper':
            if computer_choice == 'scissors':
                print('\n ~Computer Wins!~\n')
            elif computer_choice == 'rock':
                print('\n ~Player Wins!~\n')

        # End of game
        game_is_active = input('Would you like to keep playing? (y/n)')

        while type(game_is_active) is not bool:
            game_is_active = game_is_active.lower()
            if game_is_active == 'y' or game_is_active == 'yes' or game_is_active == 'oui' or game_is_active == 'si':
                game_is_active = True
            elif game_is_active == 'n' or game_is_active == 'no' or game_is_active == 'non':
                game_is_active = False
                print('Goodbye!')
            else:
                print(prompt_error)
                game_is_active = input('Would you like to keep playing? (y/n)')

elif choice == 2:
    print('Bienvenido al juego piedra, papel, o tijera! \n')

    prompt_error = ('No es una opción')
    game_is_active = True

    while game_is_active:
        options = ('piedra', 'papel', 'tijera')

        player_choice = input('¿Elegiste piedra, papel, tijera?')
        computer_choice = options[random.randint(0, 2)]

        # Players must choose a correct option!
        while player_choice not in options:
            print(prompt_error)
            player_choice = input('¿Elegiste piedra, papel, tijera?')

        # What did the players select?
        print('El jugador eligió', player_choice)
        print('El computador eligió', computer_choice)

        if player_choice == computer_choice:
            print('\n~¡El jego terminó en empate!~\n')

        elif player_choice == 'piedra':
            if computer_choice == 'papel':
                print('\n ~¡La computadora gana!~\n')
            elif computer_choice == 'tijera':
                print('\n ~¡El jugador gana!~\n')

        elif player_choice == 'tijera':
            if computer_choice == 'papel':
                print('\n ~¡El jugador gana!~\n')
            elif computer_choice == 'piedra':
                print('\n ~¡La computadora gana!~\n')

        elif player_choice == 'papel':
            if computer_choice == 'tijera':
                print('\n ~¡La computadora gana!!~\n')
            elif computer_choice == 'piedra':
                print('\n ~¡El jugador gana!~\n')

        # End of game
        game_is_active = input('¿Otra vez? (y/n)')

        while type(game_is_active) is not bool:
            game_is_active = game_is_active.lower()
            if game_is_active == 'y' or game_is_active == 'yes' or game_is_active == 'oui' or game_is_active == 'si':
                game_is_active = True
            elif game_is_active == 'n' or game_is_active == 'no' or game_is_active == 'non':
                game_is_active = False
                print('¡Hasta Luego!')
            else:
                print(prompt_error)
                game_is_active = input('Would you like to keep playing? (y/n)')

elif choice == 3:
    print('Bienvenue a le jeu roche, papier, ciseaux ! \n')

    prompt_error = ('N\'est pas une option!')
    game_is_active = True

    while game_is_active:
        options = ('roche', 'papier', 'ciseaux')

        player_choice = input('Avez-vous choisi roche, papier, ou ciseaux? ')
        computer_choice = options[random.randint(0, 2)]

        # Players must choose a correct option!
        while player_choice not in options:
            print(prompt_error)
            player_choice = input('Avez-vous choisi roche, papier, ou ciseaux? ')

        # What did the players select?
        print('Le joueur chosit', player_choice)
        print('L\'ordinatuer chosit', computer_choice)

        if player_choice == computer_choice:
            print('\n~Match Nul!~\n')

        elif player_choice == 'roche':
            if computer_choice == 'papier':
                print('\n ~L\'ordinateur gagne!~\n')
            elif computer_choice == 'ciseaux':
                print('\n ~Le joueur gagne!~\n')

        elif player_choice == 'ciseaux':
            if computer_choice == 'papier':
                print('\n ~Le jouer gagne!~\n')
            elif computer_choice == 'roche':
                print('\n ~L\'ordinateur gagne!~\n')

        elif player_choice == 'papier':
            if computer_choice == 'ciseaux':
                print('\n ~L\'ordinateur gagne!~\n')
            elif computer_choice == 'roche':
                print('\n ~Le jouer gagne!~\n')
        # End of game
        game_is_active = input('Voulez-vous jouer a nouveau? (y/n)')

        while type(game_is_active) is not bool:
            game_is_active = game_is_active.lower()
            if game_is_active == 'y' or game_is_active == 'yes' or game_is_active == 'oui' or game_is_active == 'si':
                game_is_active = True
            elif game_is_active == 'n' or game_is_active == 'no' or game_is_active == 'non':
                game_is_active = False
                print('Aurevoir!')
            else:
                print(prompt_error)
                game_is_active = input('Would you like to keep playing? (y/n)')
