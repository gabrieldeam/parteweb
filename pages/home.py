# pages/home.py
import flet as ft

def view_home(page: ft.Page):
    def go_login(e):
        page.go("/login")

    def go_sign_up(e):
        page.go("/sign-up")

    def go_forgot_password(e):
        page.go("/forgot-password")

    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Home Page")),
            ft.Column(
                [
                    ft.Text("Home Page", size=40),
                    ft.Row(
                        [
                            ft.ElevatedButton("Login", on_click=go_login),
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
