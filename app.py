# app.py
import flet as ft
from pages.home import view_home
from pages.login import view_login
from pages.sign_up import view_sign_up
from pages.forgot_password import view_forgot_password

def main(page: ft.Page):
    page.title = "Projeto Multi-Página com Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Função para lidar com mudanças de rota
    def route_change(e: ft.RouteChangeEvent):
        # Limpa as views e adiciona a view correspondente à rota
        page.views.clear()
        if page.route == "/":
            page.views.append(view_home(page))
        elif page.route == "/login":
            page.views.append(view_login(page))
        elif page.route == "/sign-up":
            page.views.append(view_sign_up(page))
        elif page.route == "/forgot-password":
            page.views.append(view_forgot_password(page))
        else:
            # View padrão para rotas não reconhecidas
            page.views.append(
                ft.View(
                    "/404",
                    [
                        ft.AppBar(title=ft.Text("Página Não Encontrada")),
                        ft.Column(
                            [
                                ft.Text("404 - Página Não Encontrada", size=40),
                                ft.ElevatedButton("Voltar para Home", on_click=lambda _: page.go("/")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                )
            )
        page.update()

    # Função para lidar com pop de views
    def view_pop(e: ft.ViewPopEvent):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    # Definir handlers
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicializar com a rota atual
    page.go(page.route)

# Iniciar o app Flet no navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
