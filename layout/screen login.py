import flet as f


def main(page: f.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    isLogin = f.Text(
        value="login",
        weight="bold",
        color="white",
        size=20,
        offset=f.transform.Offset(0, 0),
        animate_offset=f.animation.Animation(duration=300)
    )

    def ganti(e):
        ctx.bgcolor = "blue" if isLogin.value == "Login" else "red"
        ctx.height = 500 if isLogin.value == "Login" else 150
        ctx.width = 300 if isLogin.value == "Login" else 100
        ctx.border_radius = 0 if isLogin.value == "Login" else 100

        print(isLogin.value)

        isLogin.value = "Register" if isLogin.value == "Login" else "Login"
        isLogin.offset = f.transform.Offset(5, 0) if isLogin.value == "Login" else f.transform.Offset(0, 0)

        register_btn.value = "Register" if isLogin.value == "Login" else "Login"
        register_btn.value = f.transform.Offset(0, 0) if isLogin.value == "Login" else f.transform.Offset(5, 0)

        txt_box_register.visible = True if isLogin.value == "Register" else False

        page.update()

    txt_box_register = f.Container(
        content=f.Column([
            f.TextField(
                label="Username",
                border_color="white",
                color="white"
            ),
            f.TextField(
                label="Password",
                border_color="white",
                color="white"
            ),
            f.ElevatedButton(
                text="Login",
                width=page.window_width,
                on_click=ganti
            )
        ])
    )

    txt_box_register.visible = False

    register_btn = f.ElevatedButton(
        text="Register",
        on_click=ganti,
        offset=f.transform.Offset(0, 0),
        animate_offset=f.animation.Animation(duration=300)
    )

    ctx = f.Container(
        bgcolor="red",
        border_radius=100,
        padding=20,
        width=200,
        height=150,
        alignment=f.alignment.center,
        animate=f.animation.Animation(300, "easeInOut"),
        content=f.Column([
            isLogin,
            txt_box_register,
            register_btn
        ])
    )

    page.add(
        ctx
    )


f.app(target=main)
