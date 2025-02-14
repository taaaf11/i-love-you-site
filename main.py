import flet as ft



def heart_container(from_: str, *args, **kwargs):
    return ft.Container(
        *args,
        **kwargs,
        content=ft.Column(
            [
                ft.Container(
                    ft.Text(
                        "♥",
                        # "❦",
                        color="#fa4e87",
                        size=50,
                    )
                ),
                ft.Text(
                    "I love uhh!",
                    size=20
                ),
                ft.Container(height=10, width=0),
                ft.Text(
                    f"By ♥ from {from_}",
                    size=10,
                    opacity=0.6,
                )
            ],
            tight=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#121212",
        padding=ft.padding.symmetric(vertical=20, horizontal=50),
        border_radius=20,
        height=200,
        # border=ft.border.all(1, None)
        # width=200,
        # expand=True
    )


def main(page: ft.Page):
    page.bgcolor = "#17080d"
    page.title = "I love you!"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #
    page.fonts = {
        "Comfortaa": "fonts/Comfortaa[wght].ttf"
    }
    page.theme = ft.Theme(font_family="Comfortaa")

    # page.add(
    #     ft.Stack(
    #         controls=[
    #             heart_container("Test"),
    #             ft.Container(
    #                 ft.Text("Made with ♡ by Altaaf"),
    #                 # width=20, height=20,
    #                 bottom=0,
    #                 # right=0,
    #             )
    #         ],
    #         # fit=ft.StackFit.PASS_THROUGH,
    #     )
    # )
    page.add(
        # ft.Container(heart_container("Test"), expand=True),
        # heart_container("Test", expand=True),
        heart_container(page.route.split("/")[1]),
        # ft.Container(expand=True),
        # ft.Container(expand=True),
        # ft.Container(
        #     ft.Text("Made with ♡ by Altaaf"),
        #     alignment=ft.alignment.center,
        #     # expand=True
        #     # bottom=0,
        # )
    )
    print(page.route)

    page.on_route_change = lambda _: print(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)
