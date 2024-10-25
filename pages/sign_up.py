# pages/sign_up.py
import flet as ft

def view_sign_up(page: ft.Page):
    def go_home(e):
        page.go("/")

    def go_login(e):
        page.go("/login")

    def go_forgot_password(e):
        page.go("/forgot-password")

    return ft.View(
        "/sign-up",
        [
            ft.AppBar(title=ft.Text("Sign-Up Page")),
            ft.Column(
                [
                    ft.Text("Sign-Up Page", size=40),
                    ft.Row(
                        [
                            ft.ElevatedButton("Home", on_click=go_home),
                            ft.ElevatedButton("Login", on_click=go_login),
                            ft.ElevatedButton("Forgot Password", on_click=go_forgot_password),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]
    )
