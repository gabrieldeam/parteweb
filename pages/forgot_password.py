# pages/forgot_password.py
import flet as ft

def view_forgot_password(page: ft.Page):
    def go_home(e):
        page.go("/")

    def go_login(e):
        page.go("/login")

    def go_sign_up(e):
        page.go("/sign-up")

    return ft.View(
        "/forgot-password",
        [
            ft.AppBar(title=ft.Text("Forgot Password Page")),
            ft.Column(
                [
                    ft.Text("Forgot Password Page", size=40),
                    ft.Row(
                        [
                            ft.ElevatedButton("Home", on_click=go_home),
                            ft.ElevatedButton("Login", on_click=go_login),
                            ft.ElevatedButton("Sign-Up", on_click=go_sign_up),
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
