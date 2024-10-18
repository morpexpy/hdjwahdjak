from math import pi
import flet as ft
import random as rd
import time

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.adaptive = True
    colors = {
        1: "#9966CC",  # Аметист
        2: "#FF6347",  # Томато
        3: "#00FF00",  # Лайм
        4: "#0000FF",  # Синий
        5: "#00FFFF",  # Циан
        6: "#FF007F",  # Малиновый
        7: "#FFA500",  # Оранжевый
        8: "#FFD700",  # Золотой
        9: "#E6E6FA",  # Лаванда
        10: "#98FB98", # Салатовый
        11: "#4B0082", # Индиго
        12: "#FF7F50"  # Коралл
    }

    page.title = "Thirsty Bombucks Bot"
    global click_count

    otvet_text = ft.Text()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"

    size = ["2x3", "3x6", "4x9", "5x12"] 

    user_text = ft.TextField(value=size[0], width=80, read_only=True)

    def minus(e):
        if size.index(user_text.value) >= 1:
            user_text.value = size[size.index(user_text.value) - 1]
            page.update()

    def plus(e):
        if size.index(user_text.value) <= 2:
            user_text.value = size[size.index(user_text.value) + 1]
            page.update()

    def animate(e):
        # Очищаем управление на странице
        page.controls.clear()
        
        page.add(ft.Text(value="𝘼𝙣𝙖𝙡𝙮𝙯𝙞𝙣𝙜 𝙂𝙖𝙢𝙚...",size=30))
        time.sleep(1.5)
        page.controls.clear()



        page.add(
        ft.Lottie(
            src='anim.json',
            repeat=True,
            reverse=False,
            animate=True
        )
        
        )
        time.sleep(4.5)
        page.controls.clear()

        # page.add(ft.Text(value="𝙍𝙚𝙖𝙙𝙮 ✅",size=30))
        # time.sleep(0.5)
        # page.controls.clear()
        page.add((ft.Row([ft.Text(value="𝙍𝙚𝙖𝙙𝙮 ",size=30),
        ft.Lottie(src="ready_anim.json",repeat=True,animate=True,reverse=True,width=70,height=70)],alignment=ft.MainAxisAlignment.CENTER)
        )
        )
        page.update()
        time.sleep(2)
        page.controls.clear()


        size_field = user_text.value.split("x")

        for i in range(int(size_field[1])):
            mas = []
            cnt_win = rd.randint(1, int(size_field[0]))
            time.sleep(1)
            for b in range(1, int(size_field[0]) + 1):
                if cnt_win == b:
                    mas.append(ft.Container(
                        width=50,
                        height=50,
                        bgcolor="green",
                        content=ft.Text(value=str(b), color="white", text_align=ft.TextAlign.CENTER, size=24)
                    ))
                else:
                    mas.append(ft.Container(
                        width=50,
                        height=50,
                        bgcolor="red",
                        content=ft.Text(value=str(b), color="white", text_align=ft.TextAlign.CENTER, size=24)
                    ))

            page.add(ft.Row(mas, alignment=ft.MainAxisAlignment.CENTER))

        # Добавляем кнопку restart
        page.add(ft.TextButton(text="Restart", on_click=restart_game))

        page.update()

    def restart_game(e):
        # Возвращаемся к исходному состоянию приложения
        page.controls.clear()
        page.add(
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus, hover_color="#0000FF"),
                    user_text,
                    ft.IconButton(ft.icons.ADD, on_click=plus, hover_color="#0000FF")
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ft.TextButton(text="START", on_click=animate)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30

    # Добавляем начальные элементы управления
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus, hover_color="#0000FF"),
                user_text,
                ft.IconButton(ft.icons.ADD, on_click=plus, hover_color="#0000FF")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.TextButton(text="START", on_click=animate)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main,view = ft.AppView.WEB_BROWSER,port = 8000)
