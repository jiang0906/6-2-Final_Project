import pygame

# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()
        self.model.towers_attack()
        self.model.enemies_advance()
        self.model.condition_update()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.events["keyboard key"] = pygame.K_n
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        '''self.view.draw_hp(self.model.hp)'''
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_towers(self.model.towers)
        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)
        """(Q2) Controller request View to render something"""
        if self.model.menu is not None:
            self.view.draw_thumbnail(self.model.menu)
            self.view.draw_menu(self.model.menu)
            self.view.draw_Number(self.model.menu, self.model.selected_tower, self.model.selected_plot)
        # 顯示錢錢跟敵人來了幾波
        self.view.draw_money(self.model.money)
        self.view.draw_wave(self.model.wave)
        self.view.draw_popularity(self.model.support, self.model.notsupport)
        self.view.draw_year_month(self.model.year, self.model.month, self.model.date, self.model.max_date)
        if self.model.check_game_over() is True:
            self.view.draw_game_result(self.model)


    @property
    def quit_game(self):
        return self.events["game quit"]

