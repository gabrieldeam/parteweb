# pages/login.py
import flet as ft

def view_login(page: ft.Page):
    def go_home(e):
        page.go("/")

    def go_sign_up(e):
        page.go("/sign-up")

    def go_forgot_password(e):
        page.go("/forgot-password")

    return ft.View(
        "/login",
        [
            ft.AppBar(title=ft.Text("Login Page")),
            ft.Column(
                [
                    ft.Text("Login Page", size=40),
                    ft.Row(
                        [
                            ft.ElevatedButton("Home", on_click=go_home),
                            ft.ElevatedButton("Sign-Up", on_click=go_sign_up),
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
